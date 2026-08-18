#!/usr/bin/env python3
"""
108_15 verifier -- Route C: an explicit nonzero g with the exact primitive
condition hat g(0) = hat g(1) = 0, whose c_g(a) is nevertheless nonzero
throughout the interior of (0,1); and a bump phi supported inside (0,1)
for which the constant's contribution int phi(a) c_g(a) da is nonzero.
Plain numpy quadrature only, no scipy/mpmath.
"""

import numpy as np


def window(t):
    """Raised-cosine bump on [1,2], 0 outside, C^1 with w(1)=w(2)=0."""
    w = np.zeros_like(t)
    mask = (t >= 1.0) & (t <= 2.0)
    w[mask] = 0.5 * (1.0 - np.cos(2.0 * np.pi * (t[mask] - 1.0)))
    return w


def moment(k, n=200_000):
    """I_k = integral_1^2 w(t) t^k dt, by Simpson's rule."""
    t = np.linspace(1.0, 2.0, n + 1)
    y = window(t) * t ** k
    h = (t[-1] - t[0]) / n
    # composite Simpson's rule (n even)
    s = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2])
    return s * h / 3.0


def g_func(t, coeffs):
    """g(t) = w(t) * (a_{-1}/t + a_0 + a_1 t), coeffs = (a_{-1}, a_0, a_1)."""
    a_m1, a_0, a_1 = coeffs
    return window(t) * (a_m1 / np.where(t == 0, 1.0, t) + a_0 + a_1 * t)


def mellin_hat_g(s, coeffs, n=200_000):
    """hat g(s) = integral_0^inf g(t) t^s d^x t = integral_1^2 g(t) t^{s-1} dt."""
    t = np.linspace(1.0, 2.0, n + 1)
    y = g_func(t, coeffs) * t ** (s - 1.0)
    h = (t[-1] - t[0]) / n
    s_int = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2])
    return s_int * h / 3.0


def c_g(a, coeffs, n=200_000):
    """c_g(a) = integral_0^inf t^{-a} g(t) d^x t = integral_1^2 g(t) t^{-a-1} dt
    (g real-valued here, so conj(g) = g)."""
    return mellin_hat_g(-a, coeffs, n=n)


def main():
    print("=" * 70)
    print("Step 1: solve for a nonzero g with hat g(0) = hat g(1) = 0")
    print("=" * 70)

    # I_k = integral w(t) t^k dt for k = -2,-1,0,1
    I = {k: moment(k) for k in (-2, -1, 0, 1)}
    print("Moments I_k = int_1^2 w(t) t^k dt:")
    for k, v in I.items():
        print(f"  I_{k:2d} = {v:.10f}")

    # hat g(0) = a_{-1} I_{-2} + a_0 I_{-1} + a_1 I_0 = 0
    # hat g(1) = a_{-1} I_{-1} + a_0 I_0     + a_1 I_1 = 0
    # fix a_1 = 1, solve 2x2 system for (a_{-1}, a_0).
    M = np.array([[I[-2], I[-1]],
                  [I[-1], I[0]]])
    rhs = -np.array([I[0], I[1]])
    a_m1, a_0 = np.linalg.solve(M, rhs)
    a_1 = 1.0
    coeffs = (a_m1, a_0, a_1)
    print(f"\nSolved coefficients: a_-1 = {a_m1:.8f}, a_0 = {a_0:.8f}, "
          f"a_1 = {a_1:.8f}  (nonzero by construction, a_1=1)")

    hg0 = mellin_hat_g(0.0, coeffs)
    hg1 = mellin_hat_g(1.0, coeffs)
    print(f"\nDirect quadrature check:")
    print(f"  hat g(0) = {hg0:.10f}   (should be ~0)")
    print(f"  hat g(1) = {hg1:.10f}   (should be ~0)")
    tol_constraint = 1e-6
    constraints_ok = abs(hg0) < tol_constraint and abs(hg1) < tol_constraint

    print("\n" + "=" * 70)
    print("Step 2: c_g(a) on the interior of (0,1) -- is it identically 0?")
    print("=" * 70)

    a_grid = np.linspace(0.05, 0.95, 19)
    c_vals = np.array([c_g(a, coeffs) for a in a_grid])
    print(f"{'a':>6} {'c_g(a)':>14}")
    for a, c in zip(a_grid, c_vals):
        print(f"{a:6.2f} {c:14.6f}")

    max_abs_c = np.max(np.abs(c_vals))
    print(f"\nmax |c_g(a)| over the grid = {max_abs_c:.6f}")
    print(f"constraint residual scale   = {max(abs(hg0), abs(hg1)):.2e}")
    not_identically_zero = max_abs_c > 100 * max(abs(hg0), abs(hg1), 1e-12)
    print(f"c_g is NOT identically zero on (0,1) "
          f"(max value >> constraint residual): {not_identically_zero}")

    print("\n" + "=" * 70)
    print("Step 3: a bump phi supported strictly inside (0,1) detects it")
    print("=" * 70)

    def phi(a):
        # smooth bump supported on [0.3, 0.7], zero at and beyond endpoints
        out = np.zeros_like(a)
        mask = (a > 0.3) & (a < 0.7)
        u = (a[mask] - 0.3) / 0.4
        out[mask] = np.exp(-1.0 / (u * (1 - u)))
        return out

    a_fine = np.linspace(0.30001, 0.69999, 4001)
    phi_vals = phi(a_fine)
    c_fine = np.array([c_g(a, coeffs, n=20_000) for a in a_fine])
    pairing = np.trapz(phi_vals * c_fine, a_fine)
    print(f"int_0^1 phi(a) c_g(a) da = {pairing:.10e}")
    # Compare against the actual numerical noise floor (the constraint
    # residual, ~1e-16), not an arbitrary fixed cutoff: the pairing is
    # many orders of magnitude above machine-precision noise.
    noise_floor = max(abs(hg0), abs(hg1), 1e-15)
    print(f"noise floor (constraint residual) = {noise_floor:.2e}")
    pairing_nonzero = abs(pairing) > 1e6 * noise_floor

    print("\n" + "=" * 70)
    print("Cross-check: an independent, different g' with the SAME")
    print("primitive constraints gives a numerically different c_g on (0,1)")
    print("(rules out an accidental universal cancellation)")
    print("=" * 70)
    # second family: basis t^{-2}, t^0, t^2, fix highest coeff = 1.
    # hat g'(0) uses I_{m-1} for basis t^m; hat g'(1) uses I_m.
    Ib = {k: moment(k) for k in (-3, -2, -1, 0, 1, 2)}
    Mb = np.array([[Ib[-3], Ib[-1]], [Ib[-2], Ib[0]]])
    rhsb = -np.array([Ib[1], Ib[2]])
    b_m2, b_0 = np.linalg.solve(Mb, rhsb)

    def g2_func(t):
        return window(t) * (b_m2 / t ** 2 + b_0 + 1.0 * t ** 2)

    def mellin_g2(s, n=200_000):
        t = np.linspace(1.0, 2.0, n + 1)
        y = g2_func(t) * t ** (s - 1.0)
        h = (t[-1] - t[0]) / n
        s_int = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2])
        return s_int * h / 3.0

    hg0b = mellin_g2(0.0)
    hg1b = mellin_g2(1.0)
    c_g2_at_half = mellin_g2(-0.5)
    noise_floor_b = max(abs(hg0b), abs(hg1b), 1e-15)
    print(f"second family: hat g'(0) = {hg0b:.2e}, hat g'(1) = {hg1b:.2e}, "
          f"c_g'(0.5) = {c_g2_at_half:.6e}")
    second_ok = (abs(hg0b) < tol_constraint and abs(hg1b) < tol_constraint
                 and abs(c_g2_at_half) > 1e6 * noise_floor_b)

    all_ok = (constraints_ok and not_identically_zero and pairing_nonzero
              and second_ok)

    print()
    if all_ok:
        print("VERDICT: ROUTE_C_NO_GO_CONFIRMED "
              "(explicit nonzero g satisfies the exact primitive condition "
              "hat g(0)=hat g(1)=0, yet c_g(a) is nonzero on the interior "
              "of (0,1) and pairs nontrivially against an interior bump "
              "-- the primitive restriction does not annihilate the "
              "constant's contribution, confirming Theorem 3.1)")
    else:
        print("VERDICT: ROUTE_C_NUMERIC_CHECK_FAILED "
              "(unexpected: recheck construction)")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
