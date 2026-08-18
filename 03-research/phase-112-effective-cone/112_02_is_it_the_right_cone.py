#!/usr/bin/env python3
"""
112.02 -- Is {f >= 0} the right cone?  (main deliverable, all three angles)

Angle (i): f>=0 <=> u_f'' = f(r)/r >= 0 <=> U_f convex (no use of I_partial).
Angle (ii): closure of {f>=0} under addition, positive scaling, salience,
            and Frobenius covariance (107_237 (4.1)).
Angle (iii): the falsifiable test.  I_partial(D_f,D_g) computed from ACTUAL
            nontrivial zeros of zeta (mp.zetazero), for many f,g >= 0 with
            DISJOINT supports (the correct classical test -- "no common
            component" -- NOT self-intersection, which is allowed to be
            negative for an irreducible effective divisor and is checked
            here only as a non-refuting consistency point).

Search includes prime-power log-offsets (log 2, log 3, log 4, log 8, log 9,
...), since that is where the explicit formula's zero sum carries
von-Mangoldt-type resonances and a sign failure, if one exists, would show
up there. Convergence of the truncated zero sum is checked by refinement
(comparing partial sums at increasing truncation and requiring the
increments to shrink), not assumed.

Run: python3 112_02_is_it_the_right_cone.py
"""

import math
import numpy as np
import mpmath as mp

mp.mp.dps = 15

results = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}" + (f"  ({detail})" if detail else ""))
    results.append(cond)


# ======================================================================
# ANGLE (i):  f >= 0  <=>  u_f'' = f(r)/r >= 0   (convexity reading)
# No use of I_partial anywhere in this section.
# ======================================================================
print("=" * 70)
print("ANGLE (i): f >= 0 <=> U_f convex (u_f''=f(r)/r), no I_partial used")
print("=" * 70)

A, B = mp.mpf('1.0'), mp.mpf('3.0')


def u_f(r, f, A=A, B=B):
    # u_f(r) = int_A^min(r,B) f(lam)(r-lam) dlam/lam   (107_237 (2.2))
    top = min(r, B)
    if top <= A:
        return mp.mpf(0)
    # split at the bump edges: mp.quad is inaccurate across non-analytic
    # points, and the second difference below amplifies any such error by
    # 1/h^2, so the split is required, not cosmetic.
    pts = sorted({A, top} | {x for x in (mp.mpf('1.3'), mp.mpf('2.3'))
                             if A < x < top})
    return mp.quad(lambda lam: f(lam) * (r - lam) / lam, pts)


def second_deriv_numeric(g, r, h=mp.mpf('1e-4')):
    return (g(r + h) - 2 * g(r) + g(r - h)) / (h ** 2)


# f1: genuinely nonnegative bump on (A,B) -> should give convex u_f
def f_pos(lam):
    lo, hi = mp.mpf('1.3'), mp.mpf('2.3')
    if lam <= lo or lam >= hi:
        return mp.mpf(0)
    t = 2 * (lam - lo) / (hi - lo) - 1
    return mp.e ** (-1 / (1 - t ** 2))


# f2: sign-changing (has a negative part) -> should give NON-convex u_f
# somewhere (a control: this must NOT always test convex, or the check
# would be vacuous)
def f_signed(lam):
    # SMOOTH sign change: a jump discontinuity makes mp.quad inaccurate, and
    # the 1/h^2 amplification of the second difference turns that inaccuracy
    # into a spurious sign.  Multiplying the smooth bump by (mid - lam) keeps
    # the function smooth while still changing sign at lam = mid.
    lo, hi = mp.mpf('1.3'), mp.mpf('2.3')
    mid = (lo + hi) / 2
    return f_pos(lam) * (mid - lam)


test_points = [mp.mpf('1.5'), mp.mpf('1.8'), mp.mpf('2.0')]

for r0 in test_points:
    d2 = second_deriv_numeric(lambda r: u_f(r, f_pos), r0)
    direct = f_pos(r0) / r0
    rel = abs(d2 - direct) / max(abs(direct), mp.mpf('1e-8'))
    check(f"u_f''(r)=f(r)/r at r={float(r0)} (f>=0 case, (2.3) of 107_237)",
          rel < mp.mpf('0.05'),
          f"numeric d2={mp.nstr(d2,6)} f(r)/r={mp.nstr(direct,6)}")

convex_flags = []
for r0 in test_points:
    d2 = second_deriv_numeric(lambda r: u_f(r, f_pos), r0)
    convex_flags.append(d2 >= -mp.mpf('1e-6'))
check("f>=0 everywhere on support => u_f convex (u_f''>=0) at all sample points",
      all(convex_flags), f"flags={convex_flags}")

# Control: with a sign-changing f, convexity FAILS somewhere -- shows the
# convexity reading is a real, non-vacuous test of the sign of f, not an
# identity that holds regardless of f's sign.
# Test "negative SOMEWHERE", scanning the region where f_signed < 0, rather
# than at one arbitrary point: u_f''(r) = f(r)/r, so a sign-changing f is only
# required to make u_f'' negative where f itself is negative.
d2_scan = [(r0, second_deriv_numeric(lambda r: u_f(r, f_signed), r0,
                                     h=mp.mpf('1e-3')))
           for r0 in (mp.mpf('1.9'), mp.mpf('2.0'), mp.mpf('2.1'))]
worst = min(v for _, v in d2_scan)
check("control: sign-changing f gives u_f''<0 somewhere (test is not vacuous)",
      worst < 0,
      "min over r in {1.9,2.0,2.1} of u_f'' = %s" % mp.nstr(worst, 6))
# and cross-check the identity u_f'' = f(r)/r directly at those points
ident = max(abs(v - f_signed(r0) / r0) for r0, v in d2_scan)
check("control: numeric u_f'' matches the analytic f(r)/r (quadrature is sound)",
      ident < mp.mpf('1e-5'),
      "max |u_f'' - f(r)/r| = %s" % mp.nstr(ident, 4))

print("\nReading: f>=0 is EXACTLY 'no subtraction needed in the DC "
      "decomposition U_f=U_{f+}-U_{f-}', i.e. D_f=int f(lam)[Psi_lam]d*lam "
      "is a nonnegative-density combination of the PRIME correspondence "
      "divisors [Psi_lam] (107_237 (1.1)-(1.3),(2.4)). This is the direct "
      "transcription of 'D=sum n_i C_i, n_i>=0, C_i prime' and uses no "
      "sign of I_partial. It is NOT shown to equal h^0(D_f)>0: no "
      "cohomology functor exists on this object (107_237 SS5 says so "
      "explicitly). See 112_02_IS_IT_THE_RIGHT_CONE.md SS1.3.")


# ======================================================================
# ANGLE (ii): closure properties of {f >= 0}
# ======================================================================
print()
print("=" * 70)
print("ANGLE (ii): closure of {f>=0} under the divisor-group operations")
print("=" * 70)


def sample_bump(mu, L, sign=1):
    def f(lam):
        t = (mp.log(lam) - mu) / L
        if abs(t) >= 1:
            return mp.mpf(0)
        return sign * mp.e ** (-1 / (1 - t ** 2))
    return f


f_a = sample_bump(mp.mpf('0.5'), mp.mpf('0.3'), 1)
f_b = sample_bump(mp.mpf('1.0'), mp.mpf('0.2'), 1)
lam_samples = [mp.mpf(x) for x in ['1.3', '1.6', '2.0', '2.4', '2.9']]

sums_nonneg = all((f_a(l) + f_b(l)) >= 0 for l in lam_samples)
check("additive closure: f,g>=0 => f+g>=0 (pointwise, sampled)", sums_nonneg)

scale_nonneg = all((mp.mpf('2.7') * f_a(l)) >= 0 for l in lam_samples)
check("positive-scaling closure: c>0, f>=0 => cf>=0 (sampled)", scale_nonneg)

# salience: f>=0 and -f>=0 => f=0
f_zero_test_vals = [f_a(l) for l in lam_samples]
salient = True
for v in f_zero_test_vals:
    if v > 0:
        # -f(l) = -v < 0 when v>0, so -f>=0 fails unless v=0
        if -v >= 0:
            salient = False
check("salience: f>=0 and -f>=0 simultaneously forces f=0 (no line in the cone)",
      salient and any(v > 0 for v in f_zero_test_vals),
      "witnessed f_a>0 somewhere, and -f_a<0 there, so no line survives")

# Frobenius covariance (107_237 (4.1)): f_{m,n}(mu) = f((n/m) mu)
def frobenius_pullback(f, m, n):
    def g(mu):
        return f((mp.mpf(n) / mp.mpf(m)) * mu)
    return g


frob_preserves_sign = True
for (m, n) in [(1, 2), (2, 1), (3, 5), (7, 2)]:
    g = frobenius_pullback(f_a, m, n)
    vals = [g(l) for l in lam_samples]
    if not all(v >= 0 for v in vals):
        frob_preserves_sign = False
check("Frobenius covariance respects the cone: f>=0 => f_{m,n}>=0 for all m,n>0 "
      "(107_237 (4.1))", frob_preserves_sign)


# ======================================================================
# ANGLE (iii): the falsifiable test
# ======================================================================
print()
print("=" * 70)
print("ANGLE (iii): I_partial(D_f,D_g) for disjoint-support f,g>=0, using "
      "actual zeta zeros")
print("=" * 70)

N_ZEROS = 120   # zero index count; height reached ~ see printed value
print(f"Computing first {N_ZEROS} nontrivial zeta zero ordinates via "
      f"mp.zetazero (rigorously located, not an RH assumption)...")
gammas = np.array([float(mp.zetazero(n).imag) for n in range(1, N_ZEROS + 1)])
print(f"done; last height = {gammas[-1]:.3f}")

NQ = 250
nodes, weights = np.polynomial.legendre.leggauss(NQ)


def phi_np(t):
    out = np.zeros_like(t)
    mask = np.abs(t) < 1.0
    out[mask] = np.exp(-1.0 / (1.0 - t[mask] ** 2))
    return out


phi_nodes = phi_np(nodes)


def fhat_scalar(s, mu, L):
    integrand = phi_nodes * np.exp(s * L * nodes)
    return L * np.exp(s * mu) * np.sum(weights * integrand)


def fhat_vec(svec, mu, L):
    expo = np.exp(np.outer(svec, L * nodes))
    integrand = expo * phi_nodes[None, :]
    return L * np.exp(svec * mu) * (integrand @ weights)


def I_partial_np(fp, gp, Nz):
    muf, Lf = fp
    mug, Lg = gp
    f0 = fhat_scalar(0.0 + 0j, muf, Lf).real
    f1 = fhat_scalar(1.0 + 0j, muf, Lf).real
    g0 = fhat_scalar(0.0 + 0j, mug, Lg).real
    g1 = fhat_scalar(1.0 + 0j, mug, Lg).real
    polar = f0 * g1 + f1 * g0
    rhos = 0.5 + 1j * gammas[:Nz]
    fr = fhat_vec(rhos, muf, Lf)
    gr = fhat_vec(rhos, mug, Lg)
    zsum = 2.0 * np.sum((fr * np.conj(gr)).real)
    return polar - zsum, polar, zsum


# --- convergence check: increments must shrink under refinement ---
print("\n--- convergence of the truncated zero sum (refinement check) ---")
fp_conv = (0.0, 0.15)
gp_conv = (math.log(2), 0.15)
depths = [30, 60, 90, 120]
totals = [I_partial_np(fp_conv, gp_conv, d)[0] for d in depths]
for d, t in zip(depths, totals):
    print(f"  Nz={d:4d}  total={t:.10f}")
incs = [abs(totals[i + 1] - totals[i]) for i in range(len(totals) - 1)]
print("  increments:", incs)
shrinking = all(incs[i + 1] < incs[i] * 0.7 for i in range(len(incs) - 1)) or \
    (incs[-1] < 1e-8)
check("convergence: increments shrink under refinement (not a truncation artifact)",
      shrinking, f"increments={incs}")

# --- control: overlapping / same support CAN go negative (not a refutation) ---
print("\n--- control: narrow self-intersection (overlapping support), "
      "expected sometimes negative -- NOT a refutation, see SS3.1 ---")
control_neg_seen = False
for L in [0.03, 0.05, 0.08]:
    tot, pol, zs = I_partial_np((0.0, L), (0.0, L), N_ZEROS)
    print(f"  L={L}: polar={pol:.6f} zerosum={zs:.6f} total={tot:.6f}")
    if tot < 0:
        control_neg_seen = True
check("control clause is non-vacuous: overlapping/self case CAN be negative "
      "(shows the test apparatus can detect negativity when present)",
      control_neg_seen)

# --- the real test: disjoint supports, prime-power centers included ---
print("\n--- the falsifiable test: disjoint-support f,g>=0 ---")
centers = {str(k): math.log(k) for k in [1, 2, 3, 4, 5, 6, 7, 8, 9, 16]}
Ls = [0.1, 0.15, 0.2, 0.3]
names = list(centers.keys())
tested = []
for L in Ls:
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = names[i], names[j]
            mu_a, mu_b = centers[a], centers[b]
            if abs(mu_a - mu_b) <= 2 * L:  # not disjoint -> skip, out of scope
                continue
            fp, gp = (mu_a, L), (mu_b, L)
            tot60, pol60, zs60 = I_partial_np(fp, gp, min(60, N_ZEROS))
            totF, polF, zsF = I_partial_np(fp, gp, N_ZEROS)
            tested.append((L, a, b, tot60, totF))

print(f"tested {len(tested)} disjoint-support pairs "
      f"(centers 1..9,16 in log r, widths {Ls}), each at two truncation depths")
neg_pairs = [t for t in tested if t[-1] < 0]
sign_flips = [t for t in tested if (t[3] < 0) != (t[4] < 0)]
worst = min(tested, key=lambda t: t[-1])
print(f"  worst (most negative) full-depth total: {worst}")
print(f"  number of disjoint pairs with total<0 at full depth: {len(neg_pairs)}")
print(f"  number of sign flips between the two truncation depths: {len(sign_flips)}")

check("ALL tested disjoint-support pairs have I_partial(D_f,D_g) >= 0 "
      "(the falsifiable claim; a single failure here refutes the cone)",
      len(neg_pairs) == 0,
      f"{len(tested)} pairs tested, {len(neg_pairs)} negative")
check("no truncation-depth sign flips among tested pairs (negativity, had "
      "it occurred, would not be a truncation artifact)",
      len(sign_flips) == 0, f"{len(sign_flips)} flips")

print()
if all(results):
    print("VERDICT: ALL CHECKS PASS")
    raise SystemExit(0)
else:
    print("VERDICT: SOME CHECKS FAILED")
    raise SystemExit(1)
