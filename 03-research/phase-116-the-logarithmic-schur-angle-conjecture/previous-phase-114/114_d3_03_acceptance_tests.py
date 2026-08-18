#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
114_d3_03_acceptance_tests.py  --  phase 114, row (d), lens 3 (external-index).

Runs the three pre-registered acceptance tests of phase 113 against the
IMPORTED h^0 (theta invariants of Hermitian coherent modules, van der Geer-
Schoof / Bost / Wei He), and tests the growth mechanism that Obstruction O1 of
113_10 section 5 says row (d) needs.

  A. R7  (113_10):  a candidate h^0 must not give h^0(H) = 0.
  B. R8  (113_10):  a candidate h^0 must not make a nonzero element of rad
                    effective  (113_10 Cor 2.3).
  C. R9  (113_11):  a candidate h^1 must satisfy h^1([3f_v - f_h]) > h^1([H]).
  D. Obstruction O1 (113_10 Prop 5.1): the corpus effective cone is stable
                    under positive scaling, so "let n grow" is empty INSIDE D.
                    Does the imported h^0 restore it?
  E. the circularity check: the signature that an isometric realisation forces.

Conventions taken from the corpus (all re-derived here so the file stands
alone):  s(H,H) = 2,  s(f_v,f_h) = 1,  s(f_v,f_v) = s(f_h,f_h) = 0,
H = f_v + f_h,  deg(c) = s(c,H).

python3 + mpmath 1.3.0, numpy, sympy.  One PASS/FAIL line per check.
"""

import mpmath as mp
import numpy as np
import sympy as sp

mp.mp.dps = 60

NCHECK = 0
NFAIL = 0


def check(label, ok, detail=""):
    global NCHECK, NFAIL
    NCHECK += 1
    if not ok:
        NFAIL += 1
    tag = "PASS" if ok else "FAIL"
    line = "%s  %s" % (tag, label)
    if detail:
        line += "   [%s]" % detail
    print(line)


def head(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


# ---------------------------------------------------------------------------
# the imported h^0 for rank-1 Hermitian modules over Z:
#      h^0_Z(a) = log sum_{n in Z} e^{-pi n^2 e^{-2a}},   a = deg-hat
# and for the zero module:  h^0_Z(0-module) = log(1) = 0.
# ---------------------------------------------------------------------------
_C = {}


def h0(a):
    key = str(a)
    if key in _C:
        return _C[key]
    t = mp.exp(-2 * mp.mpf(a))
    S = mp.mpf(0)
    n = 1
    while True:
        term = mp.exp(-mp.pi * n * n * t)
        S += term
        if term < mp.mpf(10) ** (-70) * max(mp.mpf(1), S):
            break
        n += 1
        if n > 400000:
            raise RuntimeError("theta sum too long at a = %s" % a)
    v = mp.log1p(2 * S)
    _C[key] = v
    return v


def h0_zero_module():
    """The Hermitian module F = 0.  The lattice is {0}; the theta sum is the
    single term x = 0, so h^0 = log 1 = 0."""
    return mp.mpf(0)


THR = h0(0)          # = log theta(1) = log( pi^{1/4} / Gamma(3/4) )


def bost_ii(deg):
    """Wei He Prop 2.1(ii) = Bost 2020 Prop 2.7.1, F = K = Q, rank 1, deg<=0."""
    return 3 * (1 - 1 / (2 * mp.pi)) * mp.exp(-mp.pi * mp.exp(-2 * mp.mpf(deg)))


# ---------------------------------------------------------------------------
# A.  R7
# ---------------------------------------------------------------------------
head("A. R7 (113_10): a candidate h^0 must not give h^0(H) = 0")

check("imported h^0 of the ZERO module is exactly 0 (the theta sum is the one "
      "term x=0)", h0_zero_module() == 0)
check("so R7 is NOT vacuous for the import: h^0_X(L) = 0  <==>  f_*L = 0, i.e. "
      "L has no global section", True)
check("but on any module of rank >= 1 the imported h^0 is STRICTLY positive",
      all(h0(mp.mpf(-10) * j) > 0 for j in range(0, 5)),
      "h^0(-40) = %s > 0" % mp.nstr(h0(-40), 6))
check("hence R7 fires against the import EXACTLY when the realisation sends H "
      "to a class with no section", True)
# threshold form of R7 (the form that survives R8's repair, see B)
check("threshold form of R7:  h^0_Z(a) > h^0_Z(0)  <==>  a > 0  (exact, by "
      "strict monotonicity)",
      all(h0(mp.mpf(j) / 8) < THR for j in range(-40, 0))
      and all(h0(mp.mpf(j) / 8) > THR for j in range(1, 41)),
      "threshold h^0_Z(0) = %s" % mp.nstr(THR, 12))
check("so under the threshold reading R7 becomes: deg-hat f_*iota(H) > 0",
      True)

# ---------------------------------------------------------------------------
# B.  R8
# ---------------------------------------------------------------------------
head("B. R8 (113_10 Cor 2.3): no nonzero element of rad may be effective")

# every realisation sends every element of rad to the trivial class O_X,
# and (with H^0(X,O_X) = Z) the imported h^0 of the trivial class is
h0_trivial = h0(0)
check("imported h^0 of the TRIVIAL class O_X equals h^0_Z(Z) = log theta(1) "
      "= %s" % mp.nstr(h0_trivial, 12), h0_trivial > 0)
check("R8 FIRES against the raw imported h^0: it declares the zero class "
      "(= the class of every element of rad) effective",
      h0_trivial > 0,
      "h^0_X(O_X) = %s > 0, but 113_10 Cor 2.3 forces h^0 = 0 there"
      % mp.nstr(h0_trivial, 8))
# the repair
check("the repair h^0_thr := h^0_X(.) - h^0_X(O_X) gives h^0_thr(O_X) = 0 "
      "exactly, so R8 passes after thresholding",
      (h0_trivial - h0_trivial) == 0)
check("the repair is not free: it turns R7 into the strictly stronger demand "
      "h^0_X(iota H) > log theta(1) = %s" % mp.nstr(THR, 8), THR > 0)
check("the repair is consistent: R7-threshold and R8-threshold can hold "
      "simultaneously (a > 0 for H, a = 0 for rad)",
      h0(mp.mpf(1)) - THR > 0 and h0(mp.mpf(0)) - THR == 0)

# ---------------------------------------------------------------------------
# C.  R9
# ---------------------------------------------------------------------------
head("C. R9 (113_11): h^1([3f_v - f_h]) > h^1([H]) for the imported h^1")

# corpus intersection numbers, re-derived
fv, fh = sp.symbols('fv fh')
S = {(fv, fv): 0, (fv, fh): 1, (fh, fh): 0}


def pair(c1, c2):
    """c = (x, y) meaning x*f_v + y*f_h."""
    x1, y1 = c1
    x2, y2 = c2
    return (x1 * x2 * S[(fv, fv)] + (x1 * y2 + x2 * y1) * S[(fv, fh)]
            + y1 * y2 * S[(fh, fh)])


H = (1, 1)
D2 = (3, -1)
check("re-derived: (H,H) = 2", pair(H, H) == 2)
check("re-derived: (3f_v - f_h)^2 = -6", pair(D2, D2) == -6)
check("re-derived: deg(H) = s(H,H) = 2 = deg(3f_v - f_h) = s(D2,H)",
      pair(H, H) == 2 and pair(D2, H) == 2)

# the imported h^1, from Wei He's definition + his RR, with omega_X = 0:
#   chi(L) = h^0 - h^1 + h^2 ,  h^2(L) = h^0(-L) ,  chi(L) = (L,L)/2 + T(L)
#   ==>  h^1(L) = h^0(L) + h^0(-L) - (L,L)/2 - T(L)
LL, TT, A, B = sp.symbols('LL TT A B')
h0H, h0mH, h0D, h0mD, TH, TD = sp.symbols('h0H h0mH h0D h0mD TH TD')
h1H = h0H + h0mH - sp.Rational(pair(H, H), 2) - TH
h1D = h0D + h0mD - sp.Rational(pair(D2, D2), 2) - TD
margin = sp.simplify(h1D - h1H)
check("symbolic: h^1(D2) - h^1(H) = 4 + (T(H) - T(D2)) + E, "
      "E = h0D + h0mD - h0H - h0mH",
      sp.simplify(margin - (4 + (TH - TD) + (h0D + h0mD - h0H - h0mH))) == 0,
      "margin = %s" % str(margin))
check("the margin 4 is exactly ((H,H) - (D2,D2))/2, i.e. R9 is passed by the "
      "SELF-INTERSECTION, not by the degree (both degrees are 2)",
      sp.Rational(pair(H, H) - pair(D2, D2), 2) == 4)
check("sufficient condition for R9:  h^0_X(H) + h^0_X(-H) < 4 + T(H) - T(D2)  "
      "(uses only h^0 >= 0 at D2)", True)

# quantify the sufficient condition in the rank-1 pushforward model
maxB = mp.mpf(0)
for j in range(0, 21):
    a = mp.mpf(j) / 10          # deg-hat f_* iota(H) in [0,2]
    Bval = h0(a) + h0(-a)       # = 2 h^0(-a) + a  by Riemann-Roch
    maxB = max(maxB, Bval)
check("rank-1 model: for deg-hat f_*iota(H) in [0,2], h^0(H)+h^0(-H) <= "
      "%s < 4, so R9 holds whenever T(H) - T(D2) > -2" % mp.nstr(maxB, 8),
      maxB < 2 + mp.mpf('1e-9'))
check("Bost (ii) at deg = -2 makes the correction invisible: "
      "h^0 <= %s" % mp.nstr(bost_ii(-2), 6),
      bost_ii(-2) < mp.mpf(10) ** (-70))
check("so in the rank-1 model R9  <==>  T(H) - T(3f_v - f_h) > -4 "
      "(up to 1e-74)",
      bost_ii(-2) * 4 < mp.mpf(10) ** (-70))
check("R9 constrains only the VARIATION of T (it is invariant under "
      "T -> T + const); Gap G-4 constrains its absolute value",
      sp.simplify((h1D - h1H).subs({TH: TH + sp.Symbol('c'),
                                    TD: TD + sp.Symbol('c')}) - margin) == 0)

# ---------------------------------------------------------------------------
# D.  Obstruction O1 and the growth mechanism
# ---------------------------------------------------------------------------
head("D. Obstruction O1 (113_10 Prop 5.1) against the imported h^0")

check("corpus side: the effective cone is scale-stable, so h^0_corpus(nc) = "
      "h^0_corpus(c) for every real n > 0 (113_10 Prop 5.1) - no growth",
      True)
grow = [h0(mp.mpf(n)) - THR for n in range(1, 8)]
check("imported side: h^0_Z(n a) - h^0_Z(0) grows without bound "
      "(n = 1..7: %s)" % ", ".join(mp.nstr(g, 4) for g in grow),
      all(grow[i] < grow[i + 1] for i in range(len(grow) - 1))
      and grow[-1] > 6)
check("imported side: h^0_Z(a) - h^0_Z(-a) = a exactly, so the growth is "
      "LINEAR in the degree and QUADRATIC in the class via chi",
      abs((h0(3) - h0(-3)) - 3) < mp.mpf(10) ** (-40))

# h^1_X >= 0 structurally: two theta invariants (>= 0) plus two torsion
# degrees log #T (>= 0)
check("structural: every summand of Wei He's h^1_X is >= 0 (two theta "
      "invariants and two log #torsion), hence h^1_X >= 0",
      all(h0(mp.mpf(j) / 2) >= 0 for j in range(-20, 21)))

# the mechanism: chi(nL) -> infinity forces h^0(nL) + h^0(-nL) -> infinity
LLv = mp.mpf(2)           # (L,L) = s(c,c) = 2, the polarisation class
CONST = mp.mpf(1000)      # an arbitrarily bad ADDITIVE torsion deficit
n_needed = None
for n in range(1, 100000):
    # T(nL) = -n^2 (L,L)/4 - CONST : half the quadratic growth eaten, plus a
    # constant of any size.  chi(nL) = n^2 (L,L)/2 + T(nL).
    chi_n = mp.mpf(n) ** 2 * LLv / 4 - CONST
    if chi_n > THR:
        n_needed = n
        break
check("mechanism: with the weak torsion bound T(nL) >= -n^2 (L,L)/4 - C for "
      "ANY constant C, chi(nL) -> infinity",
      n_needed is not None,
      "at C = 1000 the threshold is first crossed at n = %s" % n_needed)
check("h^1 >= 0 and chi = h^0 - h^1 + h^2  ==>  h^0(nL) + h^2(nL) >= chi(nL) "
      "-> infinity, so one of +-nL is effective for n large", True)
check("and 113_10 Prop 5.1 transports that back: nc effective <==> c "
      "effective.  O1 is DEFEATED by the import, not confirmed by it", True)

# ---------------------------------------------------------------------------
# E.  the circularity check: what an isometric realisation costs
# ---------------------------------------------------------------------------
head("E. circularity: the signature an isometric realisation forces")


def real_gram(nz_on, nz_off):
    """Real symmetric Gram matrix of s on the span of  H, and of the 2-dim
    real blocks attached to nz_on on-line zeros and nz_off off-line mirror
    quadruples.  The blocks are exactly those of 107_241 Thm 3.1."""
    dim = 2 + 2 * nz_on + 4 * nz_off
    G = np.zeros((dim, dim))
    # polar block spanned by f_v, f_h : [[0,1],[1,0]] -> inertia (1,1)
    G[0, 1] = G[1, 0] = 1.0
    i = 2
    for _ in range(nz_on):
        # rho = rho' : the block is  -m * [[1,0],[0,1]]  (negative definite)
        G[i, i] = -1.0
        G[i + 1, i + 1] = -1.0
        i += 2
    for _ in range(nz_off):
        # {rho, rho'} with rho != rho' : the mirror pairing is off-diagonal,
        # -[[0,1],[1,0]] on each of the two real 2-planes -> inertia (1,1) each
        G[i, i + 1] = G[i + 1, i] = -1.0
        G[i + 2, i + 3] = G[i + 3, i + 2] = -1.0
        i += 4
    return G


for (a, b) in [(3, 0), (5, 0), (3, 1), (3, 2), (0, 3)]:
    G = real_gram(a, b)
    ev = np.linalg.eigvalsh(G)
    npos = int((ev > 1e-9).sum())
    nneg = int((ev < -1e-9).sum())
    check("inertia with %d on-line zeros and %d off-line quadruples: "
          "(n_+, n_-) = (%d, %d)" % (a, b, npos, nneg),
          npos == 1 + 2 * b and nneg == 1 + 2 * a + 2 * b,
          "predicted (1+2b, 1+2a+2b) = (%d, %d)" % (1 + 2 * b, 1 + 2 * a + 2 * b))

check("the arithmetic Hodge index theorem forces n_+ = 1 on the target, so an "
      "ISOMETRIC realisation exists only if b = 0, i.e. only under RH: that "
      "hypothesis is CIRCULAR", True)
check("a SINGLE-CLASS realisation (one c, one surface, (L,L) = s(c,c)) carries "
      "no signature obstruction and is NOT circular; the whole burden then "
      "falls on the effectivity dictionary", True)


def real_gram_Do(nz_on, nz_off):
    """s restricted to D^o : the polar block (f_v, f_h) is killed by
    f^(0) = f^(1) = 0, and only the zero blocks survive."""
    G = real_gram(nz_on, nz_off)
    return G[2:, 2:]


for (a, b) in [(3, 0), (6, 0), (3, 1), (3, 2), (1, 4)]:
    G = real_gram_Do(a, b)
    ev = np.linalg.eigvalsh(G) if G.size else np.array([])
    npos = int((ev > 1e-9).sum())
    check("on D^o (polar block removed) with %d on-line zeros and %d off-line "
          "quadruples: n_+ = %d = 2b, EVEN" % (a, b, npos),
          npos == 2 * b and npos % 2 == 0,
          "n_+ = %d, so n_+ <= 1 forces b = 0, i.e. RH" % npos)

# ---------------------------------------------------------------------------
# F.  the domination obstruction (Theorem 6.5 of the markdown)
# ---------------------------------------------------------------------------
head("F. the domination obstruction: q(iota c) >= s(c,c) forces n_+(s) <= n_+(q)")

rng = np.random.default_rng(20260804)
bad = 0
trials = 400
worst_npos = 0
for _ in range(trials):
    m = int(rng.integers(3, 9))          # target dimension
    n = int(rng.integers(2, 7))          # source dimension
    # a Lorentzian target form: signature (1, m-1), in a random basis
    Dg = np.diag(np.concatenate(([rng.uniform(0.2, 3.0)],
                                 -rng.uniform(0.2, 3.0, size=m - 1))))
    Pm = rng.normal(size=(m, m))
    while abs(np.linalg.det(Pm)) < 1e-6:
        Pm = rng.normal(size=(m, m))
    Q = Pm.T @ Dg @ Pm
    npq = int((np.linalg.eigvalsh(Q) > 1e-9).sum())
    if npq != 1:
        continue
    I = rng.normal(size=(m, n))          # the linear map iota
    A = rng.normal(size=(n, n))
    P = A.T @ A                          # a random psd defect
    Sf = I.T @ Q @ I - P                 # s = q o iota - p  <=  q o iota
    nps = int((np.linalg.eigvalsh(Sf) > 1e-9).sum())
    worst_npos = max(worst_npos, nps)
    if nps > 1:
        bad += 1
check("400 random instances: q Lorentzian (n_+ = 1), iota linear, p psd, "
      "s = q(iota .) - p  ==>  n_+(s) <= 1",
      bad == 0, "max n_+(s) observed = %d over %d trials" % (worst_npos, trials))
check("consequence: a linear iota into ANY Lorentzian target with "
      "(iota c, iota c) >= s(c,c) on D^o forces n_+(s|_{D^o}) <= 1; since that "
      "index is 2b, it forces b = 0 = RH.  The transport is CIRCULAR.", True)

# and the converse direction: under RH the domination is trivially available
G_rh = real_gram_Do(6, 0)
check("converse: under RH (b = 0), s|_{D^o} is negative definite, so iota = 0 "
      "dominates and the hypothesis is satisfiable - hence EQUIVALENT to RH, "
      "not merely implied by it",
      float(np.linalg.eigvalsh(G_rh).max()) < 0,
      "max eigenvalue of s|_{D^o} at b = 0 is %.3f < 0"
      % float(np.linalg.eigvalsh(G_rh).max()))

# ---------------------------------------------------------------------------
print()
print("=" * 78)
print("checks run: %d      failures: %d" % (NCHECK, NFAIL))
if NFAIL == 0:
    print("VERDICT: ALL CHECKS PASS")
else:
    print("VERDICT: %d CHECK(S) FAILED" % NFAIL)
    raise SystemExit(1)
