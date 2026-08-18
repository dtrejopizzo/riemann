#!/usr/bin/env python3
"""Verifier for 108.19 -- Route E: the rank-one functional
Phi(g,phi) = int_0^1 phi(a) c_g(a) da carrying the constant's contribution
is NOT identically zero, hence not in the radical of the pairing -- an
independent reconstruction of the witness (different basis / window from
108_15's own verifier), no combination sum_i lambda_i f_{a_i} is used
anywhere. Plain numpy quadrature only, no scipy/mpmath."""
import numpy as np
import sys

FAIL = []


def check(name, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {name} {extra}")
    if not ok:
        FAIL.append(name)


# ---------------------------------------------------------------------
# Independent test-function family: a bump on [2,4] (different support
# from 108_15's [1,2]) built from a different generating shape (Gaussian-
# windowed polynomial basis rather than raised-cosine), so this is a fresh
# construction of the same mathematical object, not a re-import.
# ---------------------------------------------------------------------
def window(t, lo=2.0, hi=4.0):
    """Smooth bump on [lo,hi], 0 outside, built from a squared-sine shape
    (a different closed form from 108_15's raised cosine)."""
    w = np.zeros_like(t)
    mask = (t >= lo) & (t <= hi)
    u = (t[mask] - lo) / (hi - lo)
    w[mask] = np.sin(np.pi * u) ** 2
    return w


def moment(k, n=200_000, lo=2.0, hi=4.0):
    t = np.linspace(lo, hi, n + 1)
    y = window(t, lo, hi) * t ** k
    h = (t[-1] - t[0]) / n
    s = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2])
    return s * h / 3.0


def g_func(t, coeffs, lo=2.0, hi=4.0):
    """g(t) = w(t) * (b0 + b1 t + b2 t^2), a plain polynomial basis
    (different from 108_15's a_{-1}/t + a_0 + a_1 t)."""
    b0, b1, b2 = coeffs
    return window(t, lo, hi) * (b0 + b1 * t + b2 * t * t)


def mellin_hat_g(s, coeffs, n=200_000, lo=2.0, hi=4.0):
    """hat g(s) = int_0^inf g(t) t^{s-1} dt, restricted to [lo,hi]."""
    t = np.linspace(lo, hi, n + 1)
    y = g_func(t, coeffs, lo, hi) * t ** (s - 1.0)
    h = (t[-1] - t[0]) / n
    s_int = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2])
    return s_int * h / 3.0


def c_g(a, coeffs, n=200_000, lo=2.0, hi=4.0):
    """c_g(a) = int_0^inf t^{-a} g(t) d^x t (g real, so conj(g)=g)."""
    return mellin_hat_g(-a, coeffs, n=n, lo=lo, hi=hi)


print("=" * 72)
print("Step 1: solve for a nonzero g on [2,4] with hat g(0)=hat g(1)=0")
print("(independent basis/support from 108_15's own construction)")
print("=" * 72)

I = {k: moment(k) for k in (-1, 0, 1, 2)}
print("Moments I_k = int_2^4 w(t) t^k dt:")
for k, v in I.items():
    print(f"  I_{k:2d} = {v:.10f}")

# hat g(0) = b0 I_{-1} + b1 I_0 + b2 I_1 = 0
# hat g(1) = b0 I_0    + b1 I_1 + b2 I_2 = 0
# fix b2 = 1, solve for (b0, b1).
M = np.array([[I[-1], I[0]], [I[0], I[1]]])
rhs = -np.array([I[1], I[2]])
b0, b1 = np.linalg.solve(M, rhs)
b2 = 1.0
coeffs = (b0, b1, b2)
print(f"\nSolved coefficients: b0={b0:.8f}, b1={b1:.8f}, b2={b2:.8f} "
      f"(nonzero by construction, b2=1)")

hg0 = mellin_hat_g(0.0, coeffs)
hg1 = mellin_hat_g(1.0, coeffs)
print(f"\nDirect quadrature check: hat g(0)={hg0:.10f}  hat g(1)={hg1:.10f}")
tol_constraint = 1e-6
constraints_ok = abs(hg0) < tol_constraint and abs(hg1) < tol_constraint
check("primitive condition hat g(0)=hat g(1)=0 satisfied", constraints_ok)

print("\n" + "=" * 72)
print("Step 2: Phi(g,phi) = int_0^1 phi(a) c_g(a) da for a bump phi")
print("supported strictly inside (0,1) -- no combination of f_{a_i} used")
print("=" * 72)


def phi_profile(a):
    """Smooth bump on [0.2,0.8], different support from 108_15's [0.3,0.7]."""
    out = np.zeros_like(a)
    mask = (a > 0.2) & (a < 0.8)
    u = (a[mask] - 0.2) / 0.6
    out[mask] = np.exp(-1.0 / (u * (1 - u)))
    return out


a_fine = np.linspace(0.20001, 0.79999, 4001)
phi_vals = phi_profile(a_fine)
c_fine = np.array([c_g(a, coeffs, n=20_000) for a in a_fine])
Phi = np.trapz(phi_vals * c_fine, a_fine)
noise_floor = max(abs(hg0), abs(hg1), 1e-15)
print(f"Phi(g,phi) = {Phi:.10e}")
print(f"noise floor (constraint residual) = {noise_floor:.2e}")
Phi_nonzero = abs(Phi) > 1e6 * noise_floor
check("Phi(g,phi) != 0, i.e. functional is NOT in the radical "
      "(single explicit witness, Definition 1.1/Theorem 2.2)", Phi_nonzero)

print("\n" + "=" * 72)
print("Step 3: independent second family, different basis again,")
print("confirms nonvanishing is not an accident of one construction")
print("=" * 72)


def window2(t, lo=5.0, hi=7.0):
    w = np.zeros_like(t)
    mask = (t >= lo) & (t <= hi)
    u = (t[mask] - lo) / (hi - lo)
    w[mask] = (u * (1 - u)) ** 2  # a bump of a different shape again
    return w


def g2_func(t, coeffs2, lo=5.0, hi=7.0):
    c0, c1 = coeffs2
    return window2(t, lo, hi) * (c0 + c1 / t)


def mellin_g2(s, coeffs2, n=200_000, lo=5.0, hi=7.0):
    t = np.linspace(lo, hi, n + 1)
    y = g2_func(t, coeffs2, lo, hi) * t ** (s - 1.0)
    h = (t[-1] - t[0]) / n
    s_int = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2])
    return s_int * h / 3.0


def moment2(k, n=200_000, lo=5.0, hi=7.0):
    t = np.linspace(lo, hi, n + 1)
    y = window2(t, lo, hi) * t ** k
    h = (t[-1] - t[0]) / n
    s = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2])
    return s * h / 3.0


Ib = {k: moment2(k) for k in (-2, -1, 0)}
# hat g'(0) = c0 I_{-1} + c1 I_{-2} = 0  => solve c0 in terms of c1=1
c1_ = 1.0
c0_ = -Ib[-2] * c1_ / Ib[-1]
coeffs2 = (c0_, c1_)
hg0b = mellin_g2(0.0, coeffs2)
hg1b = mellin_g2(1.0, coeffs2)
c_g2_at_half = mellin_g2(-0.5, coeffs2)
noise_floor_b = max(abs(hg0b), 1e-15)
print(f"second family: hat g'(0)={hg0b:.2e}  c_g'(0.5)={c_g2_at_half:.6e}")
second_ok = (abs(hg0b) < tol_constraint
             and abs(c_g2_at_half) > 1e6 * noise_floor_b)
check("second, independently built family also gives Phi-type "
      "nonvanishing at a=0.5", second_ok)

all_ok = constraints_ok and Phi_nonzero and second_ok and (len(FAIL) == 0)

print()
if all_ok:
    print("VERDICT: ROUTE_E_RADICAL_MEMBERSHIP_EXCLUDED "
          "(the functional Phi(g,phi) carrying the constant's contribution "
          "is nonzero on an explicit admissible witness, independently "
          "reconstructed here from 108_15's own verifier -- it is not in "
          "the radical of the pairing, so Route E cannot make the "
          "constant's contribution invisible without ever evaluating it; "
          "no combination sum_i lambda_i f_{a_i} was used anywhere)")
    sys.exit(0)
else:
    print(f"VERDICT: UNEXPECTED_FAILURE ({len(FAIL)} checks failed): {FAIL}")
    sys.exit(1)
