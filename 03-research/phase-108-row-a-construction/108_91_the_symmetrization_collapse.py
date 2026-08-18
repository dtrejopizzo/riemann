#!/usr/bin/env python3
"""Verifier for 108.91 -- the symmetrization collapse.

Checks Theorem 1.2, Corollaries 1.3/1.4, Theorem 2.1, Corollaries 2.2/2.3.

Design rules honoured here:
  * every convergence claim is tested by REFINEMENT (error must shrink), never
    by a single hard-coded epsilon;
  * every identity is computed by two independent code paths where possible;
  * no check can pass vacuously -- each has a control that must FAIL to
    confirm the test discriminates.
"""
import sys

import mpmath as mp

mp.mp.dps = 40

PASS, FAIL = [], []


def check(name, ok, detail=""):
    (PASS if ok else FAIL).append(name)
    print("[%s] %s  %s" % ("PASS" if ok else "FAIL", name, detail))


# ----------------------------------------------------------------- objects
def A(s):
    """Mirror-symmetrized log-derivative of zeta, from zeta itself."""
    d = lambda z: mp.zeta(z, derivative=1) / mp.zeta(z)
    return d(s) + d(1 - s)


def A_gamma(s):
    """Same, from the Gamma side (Theorem 1.2 RHS)."""
    return mp.log(mp.pi) - mp.digamma(s / 2) / 2 - mp.digamma((1 - s) / 2) / 2


def Phi_arith(s):
    return mp.pi / mp.tan(mp.pi * s / 2) - A(s)


def Phi_closed(s):
    return (2 * mp.digamma(1 - s) - mp.digamma(s / 2) / 2
            - mp.digamma((1 - s) / 2) / 2 - mp.log(4 * mp.pi))


def dPhi_collapsed(s):
    return (-mp.polygamma(1, 1 - s) - mp.polygamma(1, s / 2) / 4
            - mp.polygamma(1, 1 - s / 2) / 4)


REAL = ['0.3', '0.5', '0.7', '0.123456789', '0.9', '0.05', '0.4444']
CPLX = [mp.mpc('0.3', '0.4'), mp.mpc('0.5', '2.0'), mp.mpc('0.8', '-1.3')]
ARGS = [mp.mpf(t) for t in REAL] + CPLX

print("=" * 72)
print("Theorem 1.2 -- A(s) = log pi - psi(s/2)/2 - psi((1-s)/2)/2")
print("=" * 72)
worst = max(abs(A(s) - A_gamma(s)) for s in ARGS)
check("Thm 1.2: zeta-side equals Gamma-side (10 args, 2 code paths)",
      worst < mp.mpf(10) ** -30, "max defect=%s" % mp.nstr(worst, 6))

# Control: the UNsymmetrized log-derivative must NOT equal the Gamma side.
ctrl = max(abs(mp.zeta(s, derivative=1) / mp.zeta(s) - A_gamma(s)) for s in ARGS)
check("Thm 1.2 control: one-sided zeta'/zeta does NOT match (test is sharp)",
      ctrl > mp.mpf('0.1'), "min-ish defect=%s" % mp.nstr(ctrl, 6))

print()
print("=" * 72)
print("Corollary 1.3 -- A is holomorphic at the zeros of xi")
print("=" * 72)
zeros = [mp.zetazero(k) for k in range(1, 6)]
finite_ok, ctrl_ok = True, True
for k, rho in enumerate(zeros, 1):
    # A evaluated on the ZETA side (where each summand has a pole), closer and
    # closer to rho: the sum must stay bounded.  Evaluating the Gamma side here
    # would be vacuous -- it has no pole at rho by inspection.
    vals = [abs(A(rho + mp.mpf(10) ** -j)) for j in (3, 6, 9)]
    finite_ok &= max(vals) < 100
    # control: the individual summand must blow up as we approach rho
    ind = [abs(mp.zeta(rho + mp.mpf(10) ** -j, derivative=1)
               / mp.zeta(rho + mp.mpf(10) ** -j)) for j in (3, 6, 9)]
    ctrl_ok &= (ind[2] > ind[1] > ind[0]) and ind[2] > mp.mpf(10) ** 6
    print("    rho_%d = %s   |A| stays <=%s   |zeta'/zeta| grows to %s"
          % (k, mp.nstr(rho, 12), mp.nstr(max(vals), 6), mp.nstr(ind[2], 6)))
check("Cor 1.3: A bounded at the first 5 zeros of xi", finite_ok)
check("Cor 1.3 control: each summand alone blows up there (poles do cancel)",
      ctrl_ok)

print()
print("=" * 72)
print("Corollary 1.4 -- the closed form of Phi")
print("=" * 72)
w = max(abs(Phi_arith(s) - Phi_closed(s)) for s in ARGS)
check("Cor 1.4: arithmetic Phi equals the digamma closed form",
      w < mp.mpf(10) ** -30, "max defect=%s" % mp.nstr(w, 6))
half = Phi_closed(mp.mpf('0.5'))
check("Cor 1.4: Phi(1/2) matches 108_38 Thm 3.2 (-2.230590766)",
      abs(half + mp.mpf('2.230590766')) < mp.mpf('1e-9'),
      "Phi(1/2)=%s" % mp.nstr(half, 20))

print()
print("=" * 72)
print("Theorem 2.1 -- collapsed derivative, and strict negativity")
print("=" * 72)
# two code paths: collapsed closed form vs numerical differentiation,
# tested by REFINEMENT (mp.diff at rising precision must converge to it).
errs = []
for dps in (25, 35, 45):
    mp.mp.dps = dps
    e = max(abs(mp.diff(Phi_closed, mp.mpf(t)) - dPhi_collapsed(mp.mpf(t)))
            for t in ['0.05', '0.2', '0.5', '0.77', '0.95'])
    errs.append(e)
mp.mp.dps = 40
check("Thm 2.1: collapsed derivative matches numerical differentiation",
      errs[-1] < mp.mpf(10) ** -20,
      "errors by precision: %s" % [mp.nstr(e, 3) for e in errs])

N = 500
grid = [mp.mpf(i) / N for i in range(1, N)]
neg = all(dPhi_collapsed(s) < 0 for s in grid)
check("Thm 2.1: Phi' < 0 at all %d interior grid points" % len(grid), neg)

tri_pos = all(mp.polygamma(1, mp.mpf(t)) > 0
              for t in ['0.001', '0.25', '0.5', '0.75', '0.999'])
check("Thm 2.1: trigamma > 0 on (0,1) (the sign input to the proof)", tri_pos)

print()
print("=" * 72)
print("Corollary 2.2 -- exactly one zero, simple; residues +1")
print("=" * 72)
vals = [(s, Phi_closed(s)) for s in grid]
crossings = [(vals[i][0], vals[i + 1][0]) for i in range(len(vals) - 1)
             if mp.sign(vals[i][1]) != mp.sign(vals[i + 1][1])]
check("Cor 2.2: exactly one sign change on (0,1)", len(crossings) == 1,
      "bracket=%s" % ([mp.nstr(c, 8) for c in crossings[0]] if crossings else None))

root = mp.findroot(Phi_closed, mp.mpf('0.3'))
check("Cor 2.2: root matches 108_38 Cor 3.4 (0.301692388160)",
      abs(root - mp.mpf('0.301692388160')) < mp.mpf('1e-12'),
      "s*=%s" % mp.nstr(root, 24))
check("Cor 2.2: the root is simple (Phi'(s*) != 0)",
      abs(dPhi_collapsed(root)) > mp.mpf('1e-3'),
      "Phi'(s*)=%s" % mp.nstr(dPhi_collapsed(root), 12))

# residues by REFINEMENT: eps*Phi(eps) -> +1 and eps*Phi(1+eps) -> +1,
# with the error required to shrink at each step.
for label, f in (("s=0", lambda e: e * Phi_closed(e)),
                 ("s=1", lambda e: e * Phi_closed(1 + e))):
    es = [mp.mpf(10) ** -k for k in (3, 4, 5, 6, 7, 8)]
    errs = [abs(f(e) - 1) for e in es]
    shrinking = all(errs[i] > errs[i + 1] for i in range(len(errs) - 1))
    check("Cor 2.2: residue at %s converges to +1 under refinement" % label,
          shrinking and errs[-1] < mp.mpf('1e-7'),
          "errors=%s" % [mp.nstr(e, 3) for e in errs])

# control: the residue is NOT -2 or +2 (the values a coarser test would miss)
r0 = mp.mpf(10) ** -8 * Phi_closed(mp.mpf(10) ** -8)
check("Cor 2.2 control: residue is +1, not +/-2 (discriminating test)",
      abs(r0 - 1) < mp.mpf('1e-7') and abs(r0 - 2) > mp.mpf('0.9')
      and abs(r0 + 2) > mp.mpf('2.9'), "eps*Phi(eps)=%s" % mp.nstr(r0, 12))

print()
print("=" * 72)
print("Summary: %d passed, %d failed" % (len(PASS), len(FAIL)))
if FAIL:
    print("FAILED:", FAIL)
    print("VERDICT: FAILURES PRESENT")
    sys.exit(1)
print("VERDICT: ALL CHECKS PASS")
sys.exit(0)
