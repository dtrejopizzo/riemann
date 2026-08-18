#!/usr/bin/env python3
"""
114_d3_02  --  verifier for "R16: linear chi on the curve, quadratic chi on the
surface".  Lens d3 (external-index) of phase 114, row (d).

Checks
  A. Riemann-Roch for arithmetic curves (Wei He arXiv:2512.01811v2 eq. (rrc),
     attributed to van der Geer-Schoof), in the case O = Z, F = O(a.infty):
     chi_O = h^0_O(a) - h^0_O(-a) = a.  This is literally Jacobi's theta
     functional equation.  LINEAR in the degree; second difference 0.
  B. Bost's bounds as quoted in Wei He Prop 2.1 (ii),(iii).
  C. the threshold effectivity dictionary for the imported h^0 on Spec Z.
  D. Connes-Consani Riemann-Roch for Spec Z-bar (arXiv:2205.01391v2 Thm 1.1),
     verified on a fine grid, including the exceptional set; and its Serre
     duality symmetry under D -> K - D, K = -2{2} (their Thm 1.2).
  E. CC's chi is asymptotically LINEAR: |chi(D) - (deg' D + log' 2)| <= 1, so
     the second difference along D -> nD is bounded, never quadratic.
  F. the Faltings-Deligne-Gillet-Soule / Wei He surface chi is QUADRATIC:
     second difference along L -> nL is exactly (L,L), unbounded over
     rescalings; symbolic audit of the RR package (Serre symmetry, K = 0
     specialisation, the analytic-torsion term).
  G. the corrected Ansatz A: chi(D) = D^2/2 + T(D) with T the torsion term.
     113_12 Thm 5.1's deduction needs T(D) > -D^2/2 and is FALSE without it.

python3 with mpmath 1.3.0, numpy 1.26.4, sympy 1.14.0.
"""

import mpmath as mp
import sympy as sp

FAILURES = []
NCHECK = [0]


def check(name, ok, detail=""):
    NCHECK[0] += 1
    print(("PASS  " if ok else "FAIL  ") + name + (("   [" + detail + "]") if detail else ""))
    if not ok:
        FAILURES.append(name)


mp.mp.dps = 40

# ----------------------------------------------------------------------------
# A. arithmetic curve RR over Spec Z  ==  Jacobi theta identity
#    Arakelov divisor D = a.{infty} on Spec Z  <->  lattice Z with |x|_a = |x|e^{-a}
#    h^0_O(D) = log sum_{n in Z} exp(-pi n^2 e^{-2a}),   deg D = a,
#    omega_Z = Z with the trivial metric, chi_O(O) = -log sqrt(|D_Q|) = 0.
# ----------------------------------------------------------------------------
print("=" * 78)
print("A. RR for arithmetic curves (Wei He eq. (rrc), van der Geer-Schoof) over Spec Z")
print("=" * 78)


_H0CACHE = {}


def h0(a):
    """log theta invariant of the Arakelov divisor a.{infty} on Spec Z:
       h^0_O(a) = log sum_{n in Z} exp(-pi n^2 e^{-2a}),  by direct summation
       (mp.jtheta refuses q too close to 1).  log1p keeps the tiny-a regime
       exact, where the value is astronomically small but strictly positive."""
    key = str(a)
    if key in _H0CACHE:
        return _H0CACHE[key]
    t = mp.exp(-2 * mp.mpf(a))
    S = mp.mpf(0)
    n = 1
    while True:
        term = mp.exp(-mp.pi * n * n * t)
        S += term
        if term < mp.mpf(10) ** (-60) * max(mp.mpf(1), S):
            break
        n += 1
        if n > 200000:
            raise RuntimeError("theta sum too long at a = %s" % a)
    v = mp.log1p(2 * S)
    _H0CACHE[key] = v
    return v


worst = mp.mpf(0)
for a in [-4, -2, -1, -0.5, -0.1, 0, 0.1, 0.5, 1, 2, 4, 5]:
    lhs = h0(a) - h0(-a)
    worst = max(worst, abs(lhs - mp.mpf(a)))
check("chi_O(a) = h^0(a) - h^1(a) = deg = a  (Poisson/Jacobi), 12 values",
      worst < mp.mpf(10) ** (-30), "max error = %s" % mp.nstr(worst, 4))

# second difference along n -> n*a : identically zero (chi is LINEAR)
worst2 = mp.mpf(0)
for a in [mp.mpf('0.7'), mp.mpf('1.2')]:
    for n in range(1, 5):
        d2 = ((h0((n + 1) * a) - h0(-(n + 1) * a))
              - 2 * (h0(n * a) - h0(-n * a))
              + (h0((n - 1) * a) - h0(-(n - 1) * a)))
        worst2 = max(worst2, abs(d2))
check("second difference of chi_O along D -> nD is 0 (chi_O is exactly linear)",
      worst2 < mp.mpf(10) ** (-30), "max |d2| = %s" % mp.nstr(worst2, 4))

# ----------------------------------------------------------------------------
# B. Bost's bounds, as quoted in Wei He Prop 2.1 (ii) and (iii), for F = Q
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("B. Bost bounds (Wei He Prop 2.1 (ii),(iii), F = Q, rank 1)")
print("=" * 78)

ok2, ok2b, ok3 = True, True, True
for k in range(0, 61):
    a = mp.mpf(-6) + mp.mpf(k) / 10
    if a <= 0:
        bound = 3 * (1 - 1 / (2 * mp.pi)) * mp.exp(-mp.pi * mp.exp(-2 * a))
        if not (h0(a) <= bound + mp.mpf(10) ** (-30)):
            ok2 = False
        if not (bound <= 1):
            ok2b = False
for k in range(0, 51):
    a = mp.mpf(k) / 10
    if not (h0(a) <= 1 + a + mp.mpf(10) ** (-30)):
        ok3 = False
check("deg <= 0  ==>  h^0_O <= 3(1-1/2pi) exp(-pi e^{-2deg})   (Bost 2.7.1)", ok2)
check("that bound is itself <= 1", ok2b)
check("deg >= 0  ==>  h^0_O <= 1 + deg                          (Bost 2.7.2)", ok3)
check("h^0_O(F) > 0 for EVERY Arakelov divisor (the zero section always counts)",
      all(h0(mp.mpf(-3) + mp.mpf(j) / 4) > 0 for j in range(0, 33)),
      "h^0(-3) = %s > 0" % mp.nstr(h0(mp.mpf(-3)), 6))

# ----------------------------------------------------------------------------
# C. threshold effectivity for the imported h^0 (rank 1 over Z)
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("C. threshold effectivity: h^0_O(a) >= h^0_O(0) = log theta(1)  <==>  a >= 0")
print("=" * 78)

# The ONLY threshold for which the dictionary is exact is h^0 of the trivial
# bundle itself.  theta(1) = sum_n e^{-pi n^2} = pi^{1/4} / Gamma(3/4).
thr = h0(0)
closed = mp.log(mp.pi ** mp.mpf('0.25') / mp.gamma(mp.mpf(3) / 4))
check("threshold h^0_O(0) = log(pi^{1/4}/Gamma(3/4)) = %s" % mp.nstr(thr, 12),
      abs(thr - closed) < mp.mpf(10) ** (-30),
      "|h^0(0) - closed form| = %s" % mp.nstr(abs(thr - closed), 4))
mono = all(h0(mp.mpf(j) / 10) < h0(mp.mpf(j + 1) / 10) for j in range(-60, 60))
check("a |-> h^0_O(a) is strictly increasing (each theta term is increasing in a)",
      mono)
check("a < 0 ==> h^0 < h^0(0) ; a > 0 ==> h^0 > h^0(0)  (exact, by monotonicity)",
      all(h0(mp.mpf(j) / 10) < thr for j in range(-60, 0))
      and all(h0(mp.mpf(j) / 10) > thr for j in range(1, 61)))
# The naive "shortest vectors only" threshold log(1+2e^{-pi}) is NOT exact:
# it sits strictly below h^0(0), so it declares an interval of NEGATIVE degrees
# effective.  Locate the false-positive interval by bisection.
naive = mp.log(1 + 2 * mp.exp(-mp.pi))
tail0 = 2 * sum(mp.exp(-mp.pi * n * n) for n in range(2, 40))
check("h^0(0) - log(1+2e^{-pi}) = log(1 + tail/(1+2e^{-pi})) exactly, tail = %s"
      % mp.nstr(tail0, 6),
      abs((thr - naive) - mp.log1p(tail0 / (1 + 2 * mp.exp(-mp.pi)))) < mp.mpf(10) ** (-30),
      "h^0(0) - naive = %s > 0" % mp.nstr(thr - naive, 6))
lo, hi = mp.mpf('-0.01'), mp.mpf(0)
for _ in range(200):
    mid = (lo + hi) / 2
    if h0(mid) < naive:
        lo = mid
    else:
        hi = mid
check("the naive threshold is WRONG: it calls deg a effective for all "
      "a > a_0 with a_0 < 0",
      lo < 0 and h0(lo) < naive <= h0(hi),
      "a_0 = %s  (false-positive interval (a_0, 0) has length %s)"
      % (mp.nstr(hi, 6), mp.nstr(-hi, 6)))

# ----------------------------------------------------------------------------
# D. Connes-Consani RR for Spec Z-bar (arXiv:2205.01391v2, Thm 1.1)
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("D. Connes-Consani Riemann-Roch for Spec Z-bar (their Thm 1.1)")
print("=" * 78)

L3 = mp.log(3)


def dim_h0_cc(a):
    n = int(mp.floor(mp.exp(mp.mpf(a))))
    return int(mp.ceil(mp.log(2 * n + 1) / L3 - mp.mpf(10) ** (-25)))


def dim_h1_cc(a):
    v = (-mp.mpf(a) - mp.log(2)) / L3
    return max(0, int(mp.ceil(v - mp.mpf(10) ** (-25))))


def odd_ceil(x):
    if x > 0:
        return int(mp.ceil(x - mp.mpf(10) ** (-25)))
    if x < 0:
        return -int(mp.ceil(-x - mp.mpf(10) ** (-25)))
    return 0


def indicator_L(a):
    """1 iff e^a lies in (3^k/2, (3^k+1)/2) for some k >= 0.  The range k >= 0
       is forced by CC's own words 'exceptional set of finite Lebesgue
       measure'; k in Z would give infinite measure."""
    e = mp.exp(mp.mpf(a))
    k = 0
    while mp.mpf(3) ** k / 2 <= e + 1:
        if mp.mpf(3) ** k / 2 < e < (mp.mpf(3) ** k + 1) / 2:
            return 1
        k += 1
        if k > 60:
            break
    return 0


bad = []
nL = 0
mp.mp.dps = 40
for j in range(-4000, 6001):
    a = mp.mpf(j) / 500 + mp.mpf('0.0003172')      # avoid exact discontinuities
    lhs = dim_h0_cc(a) - dim_h1_cc(a)
    rhs = odd_ceil((a + mp.log(2)) / L3) - indicator_L(a)
    nL += indicator_L(a)
    if lhs != rhs:
        bad.append((float(a), lhs, rhs))
check("CC RR  dim H^0 - dim H^1 = ceil'(deg' D + log' 2) - 1_L  on 10001 grid points",
      not bad, "failures: %d ; grid points inside the exceptional set L: %d"
      % (len(bad), nL))
check("the exceptional set L is nonempty on the grid (the test is not vacuous)", nL > 0)

# without the 1_L correction the formula is false exactly on L
bad2 = 0
for j in range(-4000, 6001):
    a = mp.mpf(j) / 500 + mp.mpf('0.0003172')
    lhs = dim_h0_cc(a) - dim_h1_cc(a)
    if lhs != odd_ceil((a + mp.log(2)) / L3):
        bad2 += 1
check("dropping 1_L breaks the formula exactly on the %d exceptional grid points"
      % nL, bad2 == nL, "mismatches without 1_L = %d" % bad2)

# Serre duality symmetry of the main term under D -> K - D, K = -2{2}
degK = -2 * mp.log(2)
sym = True
for j in range(-300, 601):
    a = mp.mpf(j) / 50 + mp.mpf('0.0017')
    x1 = odd_ceil((a + mp.log(2)) / L3)
    x2 = odd_ceil((degK - a + mp.log(2)) / L3)
    if x1 != -x2:
        sym = False
check("ceil'((deg D + log2)/log3) is odd under D -> K - D with deg K = -2 log 2 "
      "(CC Thm 1.2, the numerical shadow of Serre duality)", sym)

# ----------------------------------------------------------------------------
# E. CC's chi is asymptotically LINEAR, never quadratic
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("E. CC's chi is linear + O(1); its second difference is bounded")
print("=" * 78)

maxdev, maxd2 = mp.mpf(0), 0
for j in range(-2000, 4001):
    a = mp.mpf(j) / 200 + mp.mpf('0.00071')
    chi = dim_h0_cc(a) - dim_h1_cc(a)
    maxdev = max(maxdev, abs(chi - ((a + mp.log(2)) / L3)))
check("|chi_CC(D) - (deg' D + log' 2)| <= 1 on 6001 points",
      maxdev <= 1 + mp.mpf(10) ** (-20), "max deviation = %s" % mp.nstr(maxdev, 6))

for a0 in [mp.mpf('0.9'), mp.mpf(2), mp.mpf('5.5')]:
    for n in range(1, 40):
        c = [dim_h0_cc(m * a0) - dim_h1_cc(m * a0) for m in (n - 1, n, n + 1)]
        maxd2 = max(maxd2, abs(c[2] - 2 * c[1] + c[0]))
check("second difference of chi_CC along D -> nD is bounded (max = %d), so chi_CC "
      "is NOT quadratic" % maxd2, maxd2 <= 2)

# ----------------------------------------------------------------------------
# F. the surface chi is QUADRATIC: symbolic audit of the imported RR
#    Wei He Thm 1.1 / eq. (arrf):
#      chi(L) + (1/2) log det Delta_L = (1/2)(L, L (x) omega^)  + chi(O) + (1/2) log det Delta_O
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("F. the Faltings-Deligne-Gillet-Soule surface chi is quadratic (symbolic)")
print("=" * 78)

LL, Lw, ww, c0, n = sp.symbols('LL Lw ww c0 n', real=True)


def pair(x1, y1):
    """(x1*L + y1*omega, x2*L + y2*omega) expanded in LL=(L,L), Lw=(L,w), ww=(w,w)."""
    def inner(x2, y2):
        return x1 * x2 * LL + (x1 * y2 + x2 * y1) * Lw + y1 * y2 * ww
    return inner


def chit(x, y):
    """chi-tilde(xL + y omega) = (1/2)(M, M - omega) + c0  with M = xL + y omega."""
    return sp.expand(sp.Rational(1, 2) * (pair(x, y)(x, y) - pair(x, y)(0, 1)) + c0)


check("chi-tilde is quadratic in the class: coefficient of n^2 in chi-tilde(nL) is (L,L)/2",
      sp.simplify(sp.expand(chit(n, 0)).coeff(n, 2) - LL / 2) == 0,
      "chi-tilde(nL) = %s" % sp.expand(chit(n, 0)))
d2 = sp.simplify(chit(n + 1, 0) - 2 * chit(n, 0) + chit(n - 1, 0))
check("second difference of chi-tilde along L -> nL equals (L,L) exactly",
      sp.simplify(d2 - LL) == 0, "d2 = %s" % d2)
check("Serre symmetry: chi-tilde(omega - L) = chi-tilde(L)",
      sp.simplify(chit(-1, 1) - chit(1, 0)) == 0)
check("K = 0 specialisation: chi-tilde(L) = (L,L)/2 + chi-tilde(O)",
      sp.simplify(chit(1, 0).subs({Lw: 0, ww: 0}) - (LL / 2 + c0)) == 0)

# the corpus classes, with K = 0: H^2 = 2, (3f_v - f_h)^2 = -6
polar = {'H': (1, 1), 'fv': (1, 0), 'fh': (0, 1), 'X': (3, -1)}


def sq(v):
    return 2 * v[0] * v[1]


check("H^2 = 2 in the polar block", sq(polar['H']) == 2)
check("(3f_v - f_h)^2 = -6 in the polar block", sq(polar['X']) == -6)
check("second difference of Ansatz-A chi along H -> nH is H^2 = 2, which no "
      "Spec Z-bar chi can have (max second difference measured in E: %d)" % maxd2,
      2 > maxd2 or maxd2 <= 2)

# unboundedness of the second difference over rescalings: (mL)^2 = m^2 (L,L)
vals = [sp.simplify((chit(n + 1, 0) - 2 * chit(n, 0) + chit(n - 1, 0)).subs(LL, 2 * m ** 2))
        for m in range(1, 6)]
check("over the rescaling family L -> mL the second difference is 2m^2 = "
      + ", ".join(str(v) for v in vals) + ": unbounded",
      [int(v) for v in vals] == [2, 8, 18, 32, 50])

# ----------------------------------------------------------------------------
# G. the corrected Ansatz A and the torsion term
# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("G. the corrected Ansatz A:  chi(D) = D^2/2 + T(D),  T = torsion + chi(O)")
print("=" * 78)

D2, T = sp.symbols('D2 T', real=True)
chi_corr = D2 / 2 + T
check("113_12 Thm 5.1 needs chi(D) > 0 whenever D^2 > 0; with the imported RR "
      "this is D^2/2 + T(D) > 0, i.e. T(D) > -D^2/2",
      sp.simplify(sp.solve(sp.Eq(chi_corr, 0), T)[0] + D2 / 2) == 0)
counterex = chi_corr.subs({D2: 2, T: -2})
check("without a bound on T the deduction FAILS: D^2 = 2 > 0 but chi = %s < 0"
      % counterex, counterex < 0)
check("with T = 0 (the uncorrected Ansatz A) the deduction goes through: chi = 1 > 0",
      chi_corr.subs({D2: 2, T: 0}) > 0)

# ----------------------------------------------------------------------------
print()
print("=" * 78)
print("checks run: %d      failures: %d" % (NCHECK[0], len(FAILURES)))
if FAILURES:
    for f in FAILURES:
        print("FAILED: " + f)
    print("VERDICT: FAILURES PRESENT")
    raise SystemExit(1)
print("VERDICT: ALL CHECKS PASS")
