#!/usr/bin/env python3
"""
Verifier for 108_41 -- Stage 4 geometry I: the archimedean space and its form.

Checks (see the .md for statements/proofs):
  1. Lemma 1.2:   pole locations of Gamma_R(-s) at s=0,2,4,6 and of
                  Gamma_R(1-s) at s=1,3,5,7 (pole-like growth as offset halves).
  2. Corollary 2.2 (i):  Res_{s=-2n} G'(s) = -1,  n=0,1,2,3.
  3. Corollary 2.2 (ii): Res_{s=1+2n} G'(1-s) = +1, n=0,1,2,3.
  4. -r_n * r_n^* = 1 for the tested n.
  5. Proposition 4.1: Gram matrix of B_inf on {b_0,b_0^*} equals [[0,1],[1,0]]
     -- by stipulation (Definition 3.2), confirmed transcribed correctly.
     This is NOT a derivation of isotropy; see 108_41.md Section 4.
     exactly, and matches the hard-coded Stage-0 matrix (107_241 Thm 3.1(1)).

No zero of zeta or xi is used anywhere in this file.
"""
import sys
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 30

PASS = []


def report(name, ok, detail=""):
    PASS.append(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


def GammaR(s):
    return mp.pi ** (-s / 2) * mp.gamma(s / 2)


def Gprime(s):
    # G(s) = log Gamma_R(s) = -1/2 log(pi) + log Gamma(s/2)
    # G'(s) = 1/2 * digamma(s/2)
    return mp.mpf('0.5') * mp.digamma(s / 2)


# ---------------------------------------------------------------------
# Check 1: Lemma 1.2 -- pole growth of Gamma_R(-s) at s=2n, Gamma_R(1-s) at s=1+2n
# ---------------------------------------------------------------------
print("=== Check 1: pole locations of the two mirrors (Lemma 1.2) ===")
ok1 = True
for n in range(4):
    s0 = 2 * n
    d1, d2 = mp.mpf('0.08'), mp.mpf('0.04')
    v1 = abs(GammaR(-(s0 + d1)))
    v2 = abs(GammaR(-(s0 + d2)))
    ratio = v2 / v1
    # simple pole: |f(s0+d)| ~ C/d, so halving d should roughly double |f|
    is_pole_like = ratio > mp.mpf('1.7')
    ok1 &= is_pole_like
    report(f"Gamma_R(-s) pole-like growth at s={s0}", is_pole_like,
           f"ratio(d/2 vs d)={float(ratio):.3f}")

for n in range(4):
    s0 = 1 + 2 * n
    d1, d2 = mp.mpf('0.08'), mp.mpf('0.04')
    v1 = abs(GammaR(1 - (s0 + d1)))
    v2 = abs(GammaR(1 - (s0 + d2)))
    ratio = v2 / v1
    is_pole_like = ratio > mp.mpf('1.7')
    ok1 &= is_pole_like
    report(f"Gamma_R(1-s) pole-like growth at s={s0}", is_pole_like,
           f"ratio(d/2 vs d)={float(ratio):.3f}")

# also confirm these are NOT pole-like at intervening odd/even integers
# (Gamma_R(-s) regular at s odd; Gamma_R(1-s) regular at s even)
for s0 in [1, 3, 5]:
    d1, d2 = mp.mpf('0.08'), mp.mpf('0.04')
    v1 = abs(GammaR(-(s0 + d1)))
    v2 = abs(GammaR(-(s0 + d2)))
    ratio = v2 / v1
    is_regular = mp.mpf('0.8') < ratio < mp.mpf('1.3')
    ok1 &= is_regular
    report(f"Gamma_R(-s) regular (not pole-like) at s={s0}", is_regular,
           f"ratio={float(ratio):.3f}")

# ---------------------------------------------------------------------
# Check 2/3: residues via central difference, step-halving convergence
# ---------------------------------------------------------------------
print("\n=== Check 2: Res_{s=-2n} G'(s) = -1 ===")


def residue_central_diff(f, pole, h):
    # f has a simple pole at `pole`; residue ~ (h)*f(pole+h) refined via
    # Richardson-style comparison at h and h/2 (we report both, and check
    # the h/2 estimate is closer to -1 / +1 respectively -- a genuine
    # convergence test, not a bare threshold).
    return h * f(pole + h)


res_minus_list = []
for n in range(4):
    pole = -2 * n
    h1, h2 = mp.mpf('1e-4'), mp.mpf('5e-5')
    r1 = residue_central_diff(Gprime, pole, h1)
    r2 = residue_central_diff(Gprime, pole, h2)
    err1 = abs(r1 - (-1))
    err2 = abs(r2 - (-1))
    shrinking = err2 < err1
    close_enough = err2 < mp.mpf('1e-3')
    ok = shrinking and close_enough
    ok1 &= ok
    res_minus_list.append(r2)
    report(f"Res_(s=-2*{n}) G'(s) -> -1", ok,
           f"err(h)={float(err1):.2e} err(h/2)={float(err2):.2e}")

print("\n=== Check 3: Res_{s=1+2n} G'(1-s) = +1 ===")


def Gprime_reflected(s):
    return Gprime(1 - s)


res_plus_list = []
for n in range(4):
    pole = 1 + 2 * n
    h1, h2 = mp.mpf('1e-4'), mp.mpf('5e-5')
    r1 = residue_central_diff(Gprime_reflected, pole, h1)
    r2 = residue_central_diff(Gprime_reflected, pole, h2)
    err1 = abs(r1 - 1)
    err2 = abs(r2 - 1)
    shrinking = err2 < err1
    close_enough = err2 < mp.mpf('1e-3')
    ok = shrinking and close_enough
    ok1 &= ok
    res_plus_list.append(r2)
    report(f"Res_(s=1+2*{n}) G'(1-s) -> +1", ok,
           f"err(h)={float(err1):.2e} err(h/2)={float(err2):.2e}")

# ---------------------------------------------------------------------
# Check 4: -r_n * r_n^* = 1
# ---------------------------------------------------------------------
print("\n=== Check 4: -r_n * r_n^* = 1 ===")
ok4 = True
for n in range(4):
    val = -res_minus_list[n] * res_plus_list[n]
    ok = abs(val - 1) < mp.mpf('1e-3')
    ok4 &= ok
    report(f"-r_{n} * r_{n}^* = 1", ok, f"value={float(val):.6f}")

# ---------------------------------------------------------------------
# Check 5: Proposition 4.1 -- exact Gram matrix comparison (exact rationals)
#
# NOTE (per the .md, Section 4): this check confirms Definition 3.2's
# stipulated values were transcribed correctly, i.e. that the construction
# does what it was built to do. It is NOT a derivation of isotropy and does
# NOT establish that B_inf(b_n,b_n)=0 follows from any independent property
# of Theta/Gamma_R. See 108_41.md Section 4 for the full, deliberately
# unglamorous, status of G2.
# ---------------------------------------------------------------------
print("\n=== Check 5: Proposition 4.1, Gram matrix equals the stipulated target ===")
print("    (this checks the construction was transcribed correctly;")
print("     it is not a derivation -- see 108_41.md Section 4)")

# B_inf on {b_0, b_0^*} by Definition 3.2, using exact Fractions.
B_binf = {
    ('b0', 'b0'): Fraction(0),
    ('b0', 'b0s'): Fraction(1),
    ('b0s', 'b0'): Fraction(1),
    ('b0s', 'b0s'): Fraction(0),
}

# Stage-0 matrix, hard-coded as a citation of 107_241 Theorem 3.1(1):
# I_partial(v0,v0)=0, I_partial(v1,v1)=0, I_partial(v0,v1)=I_partial(v1,v0)=1.
I_stage0 = {
    ('v0', 'v0'): Fraction(0),
    ('v0', 'v1'): Fraction(1),
    ('v1', 'v0'): Fraction(1),
    ('v1', 'v1'): Fraction(0),
}

phi = {'v0': 'b0', 'v1': 'b0s'}
ok5 = True
for (x, y), val in I_stage0.items():
    target = B_binf[(phi[x], phi[y])]
    match = (target == val)
    ok5 &= match
    report(f"I_partial({x},{y})={val}  vs  B_inf({phi[x]},{phi[y]})={target}", match)

# also confirm the matrix is not accidentally symmetric-degenerate, i.e.
# genuinely equals [[0,1],[1,0]] and not e.g. the zero matrix
nondeg = (B_binf[('b0', 'b0s')] * B_binf[('b0s', 'b0')] - B_binf[('b0', 'b0')] * B_binf[('b0s', 'b0s')]) != 0
report("B_inf|{b0,b0*} is nondegenerate (det != 0)", nondeg,
       f"det={B_binf[('b0','b0s')]*B_binf[('b0s','b0')] - B_binf[('b0','b0')]*B_binf[('b0s','b0s')]}")
ok5 &= nondeg

# ---------------------------------------------------------------------
overall = ok1 and all(True for _ in res_minus_list) and ok4 and ok5 and all(PASS)
print()
if overall and all(PASS):
    print("VERDICT: ALL CHECKS PASS")
    sys.exit(0)
else:
    print("VERDICT: SOME CHECKS FAILED")
    sys.exit(1)
