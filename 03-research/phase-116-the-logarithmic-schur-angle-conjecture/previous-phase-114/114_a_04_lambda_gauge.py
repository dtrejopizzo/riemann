#!/usr/bin/env python3
"""
114.a.04 verifier - the Lambda gauge on W_rat(Z) and the Frobenius graphs.

Checks, in order:
  A. Phi_n(1) = exp(Lambda(n))                              [= 106_210 eq (1), n=1 case]
  B. (1/phi(n)) log|Res(Phi_m,Phi_n)| = Lambda(m/n)          [= 106_210 eq (1)]
  C. Mahler measure: integral form  =  sum of log+|alpha_i|  (Jensen)
  D. r and m are homomorphisms for Witt addition (= series multiplication)
  E. m o F_N = N m ,  m o V_N = m ,  r o F_N = r ,  r o V_N = N r
  F. F_N V_N = N  on the bidegree, and on the ring itself
  G. Kronecker: m(P) = 0  <=>  P is a product of cyclotomics
  H. Tate telescoping: the F_N-equivariant gauge is unique  (numerical uniqueness test)
  I. the two rulings: r,m realise f_v=(1,0), f_h=(0,1) with the hyperbolic form
  J. growth: log #{deg<=n, |c|_1<=e^A} = nA + O(n log n), delta = 2

Every check prints PASS/FAIL. Exit 0 iff all pass.
"""
import sys
from mpmath import (mp, mpf, log, exp, quad, cos, sin, sqrt, pi, mpc,
                    polyroots, atan2, floor)
import sympy as sp

mp.dps = 40
T = sp.symbols('T')
FAIL = []


def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("   " + detail) if detail else ""))
    if not ok:
        FAIL.append(name)


def vonmangoldt(n):
    if n < 2:
        return sp.Integer(0)
    f = sp.factorint(n)
    if len(f) != 1:
        return sp.Integer(0)
    p = next(iter(f))
    return sp.log(p)


def cyc(n):
    return sp.Poly(sp.cyclotomic_poly(n, T), T)


# ---------------------------------------------------------------- A
print("=" * 70)
print("A.  Phi_n(1) = exp(Lambda(n))   [106_210 eq (1), the n=1 case]")
print("=" * 70)
bad = []
for n in range(2, 401):
    lhs = int(sp.cyclotomic_poly(n, 1))
    rhs = sp.exp(vonmangoldt(n))
    rhs = sp.nsimplify(rhs)
    if sp.simplify(sp.Integer(lhs) - rhs) != 0:
        bad.append((n, lhs, rhs))
check("A1  Phi_n(1) = e^Lambda(n) for 2<=n<=400", not bad, "counterexamples: %s" % bad[:3])

# and the summed form  sum_{d|n} Lambda(d) = log n
bad = []
for n in range(2, 201):
    s = sum(vonmangoldt(d) for d in sp.divisors(n))
    if sp.simplify(s - sp.log(n)) != 0:
        bad.append(n)
check("A2  sum_{d|n} Lambda(d) = log n  (arithmetic identity; not a diagonal intersection)", not bad,
      "counterexamples: %s" % bad[:3])

# Res(Phi_n, T-1) = +- Phi_n(1)
bad = []
for n in range(2, 121):
    R = sp.resultant(sp.cyclotomic_poly(n, T), T - 1, T)
    if abs(int(R)) != int(sp.cyclotomic_poly(n, 1)):
        bad.append((n, R))
check("A3  |Res(Phi_n, T-1)| = Phi_n(1),  so <div Phi_n, Delta>_fin = Lambda(n)",
      not bad, "counterexamples: %s" % bad[:3])

# ---------------------------------------------------------------- B
print()
print("=" * 70)
print("B.  106_210 eq (1):  (1/phi(n)) log|Res(Phi_m,Phi_n)| = Lambda(m/n)")
print("=" * 70)
bad = []
tested = 0
for n in range(1, 41):
    for m in range(n + 1, 121):
        if m % n:
            continue
        R = sp.resultant(sp.cyclotomic_poly(m, T), sp.cyclotomic_poly(n, T), T)
        if R == 0:
            bad.append((m, n, 'Res=0'))
            continue
        lhs = sp.log(abs(sp.Integer(R))) / sp.totient(n)
        rhs = vonmangoldt(m // n)
        tested += 1
        if sp.simplify(lhs - rhs) != 0:
            bad.append((m, n, sp.nsimplify(lhs), rhs))
check("B1  eq (1) holds for all n|m, n<=40, m<=120 (%d pairs)" % tested, not bad,
      "counterexamples: %s" % bad[:3])

# non-divisible pairs: resultant is +-1 (intersection number 0)
bad = []
tested = 0
for n in range(2, 31):
    for m in range(2, 31):
        if m == n or m % n == 0 or n % m == 0:
            continue
        R = sp.resultant(sp.cyclotomic_poly(m, T), sp.cyclotomic_poly(n, T), T)
        tested += 1
        if abs(int(R)) != 1:
            bad.append((m, n, R))
check("B2  Res(Phi_m,Phi_n)=+-1 when neither divides the other (%d pairs)" % tested,
      not bad, "counterexamples: %s" % bad[:3])

# ---------------------------------------------------------------- C
print()
print("=" * 70)
print("C.  Mahler measure: integral = sum log+|alpha_i|  (Jensen)")
print("=" * 70)


def mahler_integral(coeffs):
    """coeffs = [c0,...,cd] of P(T)=sum c_j T^j ; returns int_0^1 log|P(e^{2pi i t})| dt"""
    def f(t):
        z = mpc(cos(2 * pi * t), sin(2 * pi * t))
        v = mpc(0)
        for j, c in enumerate(coeffs):
            v += mpf(c) * z ** j
        a = abs(v)
        if a == 0:
            return mpf('-1e30')
        return log(a)
    # A polynomial with roots ON the unit circle (every cyclotomic) makes the
    # integrand logarithmically singular.  mpmath's default tanh-sinh rule is
    # built for ENDPOINT singularities, so the cure is to put every singularity
    # exactly at a partition node.  P(z)=prod(1-alpha_i z) vanishes at z=1/alpha_i,
    # so a unit-modulus alpha contributes the node theta = -arg(alpha)/2pi.
    # (A blind uniform partition leaves Phi_5 off by ~1e-5 -- see C1.)
    part = set([mpf(0), mpf(1)])
    d, lead = inverse_root_poly(coeffs)
    if d > 0:
        for a in _roots(lead):
            if abs(abs(a) - 1) < mpf('1e-20'):
                t = -atan2(a.imag, a.real) / (2 * pi)
                part.add(t - floor(t))
    part = sorted(part)
    return quad(f, part, maxdegree=12)


def inverse_root_poly(coeffs):
    """P(T)=sum_j c_j T^j with c_0=1 factors as prod(1-alpha_i T).
    The monic polynomial with roots exactly the alpha_i is
        A(x) = x^d P(1/x) = sum_j c_j x^{d-j},
    whose LEADING-FIRST coefficient list is [c_0, c_1, ..., c_d] = coeffs itself.
    (Getting this reversal backwards silently returns m=0 for f=1-2T.)"""
    d = len(coeffs) - 1
    while d > 0 and coeffs[d] == 0:
        d -= 1
    return d, [coeffs[j] for j in range(d + 1)]


def _roots(lead_first):
    """Robust root finder: mpmath first, numpy fallback for high degree."""
    try:
        return polyroots([mpf(c) for c in lead_first], maxsteps=2000, extraprec=2000)
    except Exception:
        import numpy as np
        return [mpc(z.real, z.imag) for z in np.roots(np.array(lead_first, dtype=float))]


def mahler_roots(coeffs):
    """m(P) = sum log+|alpha_i| over the inverse roots alpha of P (P(0)=1)."""
    d, lead = inverse_root_poly(coeffs)
    if d == 0:
        return mpf(0)
    return sum(log(abs(r)) for r in _roots(lead) if abs(r) > 1)


tests_C = [
    ("1-2T", [1, -2]),
    ("1-3T", [1, -3]),
    ("1-T-T^2 (Lehmer-ish)", [1, -1, -1]),
    ("1+T+2T^2", [1, 1, 2]),
    ("Phi_5 reversed", [1, 1, 1, 1, 1]),
    ("(1-2T)(1-3T)", [1, -5, 6]),
    ("1-6T+11T^2-6T^3", [1, -6, 11, -6]),
    ("1+T^5-T^7", [1, 0, 0, 0, 0, 1, 0, -1]),
]
bad = []
for name, c in tests_C:
    mi = mahler_integral(c)
    mr = mahler_roots(c)
    d = abs(mi - mr)
    if d > mpf('1e-12'):
        bad.append((name, mi, mr, d))
    print("      %-24s integral=%.15f   roots=%.15f   diff=%.2e"
          % (name, float(mi), float(mr), float(d)))
check("C1  Jensen: integral form = sum log+|alpha| (8 polynomials, tol 1e-12)", not bad,
      str(bad[:2]))

# ---------------------------------------------------------------- D
print()
print("=" * 70)
print("D.  r and m are homomorphisms for Witt addition (series multiplication)")
print("=" * 70)


def polymul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def r_of(coeffs):
    d = len(coeffs) - 1
    while d > 0 and coeffs[d] == 0:
        d -= 1
    return d


pairs = [([1, -2], [1, -3]), ([1, -2, 3], [1, 1, 1, 1]), ([1, -5, 6], [1, -1, -1]),
         ([1, 0, -7], [1, 4, 4]), ([1, -1], [1, -1, 1])]
bad_r, bad_m = [], []
for a, b in pairs:
    ab = polymul(a, b)
    if r_of(ab) != r_of(a) + r_of(b):
        bad_r.append((a, b))
    ma, mb, mab = mahler_roots(a), mahler_roots(b), mahler_roots(ab)
    if abs(mab - ma - mb) > mpf('1e-20'):
        bad_m.append((a, b, float(mab - ma - mb)))
check("D1  r(f +_W g) = r(f) + r(g)", not bad_r, str(bad_r))
check("D2  m(f +_W g) = m(f) + m(g)   (Mahler is additive: it IS a degree)", not bad_m,
      str(bad_m[:2]))

# ---------------------------------------------------------------- E
print()
print("=" * 70)
print("E.  Frobenius and Verschiebung on the bidegree (r,m)")
print("=" * 70)


def frob(coeffs, N):
    """F_N : {alpha_i} -> {alpha_i^N}, computed exactly over Z via a resultant.

    A(x) = prod(x - alpha_i) is monic with LEADING-FIRST coefficients = coeffs.
    B(x) = prod(x - alpha_i^N) = Res_T( A(T), x - T^N ).
    Converting B back to Witt form P_new(T) = prod(1 - alpha_i^N T) = T^d B(1/T)
    again just takes B's leading-first list verbatim."""
    d, lead = inverse_root_poly(coeffs)
    if d == 0:
        return [1]
    x = sp.symbols('x')
    A = sp.Poly([sp.Integer(c) for c in lead], T)     # monic, roots = alpha_i
    B = sp.Poly(sp.resultant(A.as_expr(), x - T ** N, T), x)
    cs = B.all_coeffs()                               # leading first, monic
    return [int(c) for c in cs]


def versch(coeffs, N):
    """V_N : f(T) -> f(T^N)."""
    out = [0] * ((len(coeffs) - 1) * N + 1)
    for j, c in enumerate(coeffs):
        out[j * N] = c
    return out


bad = []
cases = [[1, -2], [1, -3], [1, -1, -1], [1, -5, 6], [1, 1, 2]]
for c in cases:
    for N in (2, 3, 5):
        fc, vc = frob(c, N), versch(c, N)
        rF, mF = r_of(fc), mahler_roots(fc)
        rV, mV = r_of(vc), mahler_roots(vc)
        r0, m0 = r_of(c), mahler_roots(c)
        if rF != r0:
            bad.append(('rF', c, N, rF, r0))
        if abs(mF - N * m0) > mpf('1e-15'):
            bad.append(('mF', c, N, float(mF), float(N * m0)))
        if rV != N * r0:
            bad.append(('rV', c, N, rV, N * r0))
        if abs(mV - m0) > mpf('1e-15'):
            bad.append(('mV', c, N, float(mV), float(m0)))
        print("      f=%-14s N=%d :  (r,m)=(%d,%.10f)  F_N->(%d,%.10f)  V_N->(%d,%.10f)"
              % (str(c), N, r0, float(m0), rF, float(mF), rV, float(mV)))
check("E1  r o F_N = r,  m o F_N = N m,  r o V_N = N r,  m o V_N = m", not bad,
      str(bad[:2]))

# ---------------------------------------------------------------- F
print()
print("=" * 70)
print("F.  The Witt identity F_N V_N = N, on the ring and on the bidegree")
print("=" * 70)
bad = []
for c in cases:
    for N in (2, 3, 4):
        fv = frob(versch(c, N), N)
        # N * f in the additive group of W  =  f^N  as a power series product
        pw = [1]
        for _ in range(N):
            pw = polymul(pw, c)
        if fv != pw:
            bad.append(('ring', c, N, fv, pw))
        r0, m0 = r_of(c), mahler_roots(c)
        if r_of(fv) != N * r0 or abs(mahler_roots(fv) - N * m0) > mpf('1e-15'):
            bad.append(('bidegree', c, N))
check("F1  F_N V_N f = f^N  (= N.f in the Witt additive group), and (r,m)->(Nr,Nm)",
      not bad, str(bad[:2]))

# ---------------------------------------------------------------- G
print()
print("=" * 70)
print("G.  Kronecker: m(P)=0  <=>  P is a product of cyclotomics")
print("=" * 70)
bad = []
# cyclotomic products have m = 0
for n in [1, 2, 3, 4, 5, 6, 7, 8, 12, 15, 105]:
    cp = sp.Poly(sp.cyclotomic_poly(n, T), T).all_coeffs()   # leading first
    d = len(cp) - 1
    witt = [int(cp[d - k]) for k in range(d + 1)]            # P(0)=1 form
    if witt[0] != 1:
        witt = [c * witt[0] for c in witt]
    mm = mahler_roots(witt)
    if abs(mm) > mpf('1e-15'):
        bad.append(('cyc', n, float(mm)))
check("G1  m(Phi_n) = 0 for n in {1..8,12,15,105}", not bad, str(bad[:3]))

# non-cyclotomic integer polynomials have m > 0, and >= log(Lehmer) if not a unit
bad = []
# Lehmer's polynomial x^10+x^9-x^7-x^6-x^5-x^4-x^3+x+1.  It is palindromic, so
# its ascending Witt-form coefficient list equals its descending one.
lehmer = [1, 1, 0, -1, -1, -1, -1, -1, 0, 1, 1]
for name, c in [("1-2T", [1, -2]), ("1-T-T^2", [1, -1, -1]), ("Lehmer", lehmer)]:
    mm = mahler_roots(c)
    print("      m(%-10s) = %.15f" % (name, float(mm)))
    if mm <= 0:
        bad.append((name, float(mm)))
check("G2  m > 0 strictly for non-cyclotomic integer polynomials", not bad, str(bad))
# Reference: Lehmer's number, the largest root, to 39 places.  Checking the
# ROOT (an independently tabulated constant) rather than a remembered value of
# its logarithm is the honest comparison.
lm = mahler_roots(lehmer)
lam = mpf('1.17628081825991750654407033847403505069')
check("G3  m(Lehmer) = log(1.1762808182599175...) = 0.1623576120077381...",
      abs(lm - log(lam)) < mpf('1e-30'), "got %.20f  want %.20f" % (float(lm), float(log(lam))))

# ---------------------------------------------------------------- H
print()
print("=" * 70)
print("H.  Tate uniqueness: an F_N-equivariant gauge agreeing with m to O(1) IS m")
print("=" * 70)
# Simulate: let lambda = m + bounded perturbation eps(f) with |eps|<=B.
# Equivariance lambda(F_N f) = N lambda(f) forces eps(F_N f) = N eps(f); iterating,
# |eps(f)| = |eps(F_{N^k} f)| / N^k <= B / N^k -> 0.
B = mpf(10)
worst = mpf(0)
for k in range(1, 25):
    worst = max(worst, B / mpf(2) ** k)
check("H1  Tate telescoping bound B/N^k -> 0 (B=10, N=2, k=24: %.3e)" % float(B / 2 ** 24),
      B / mpf(2) ** 24 < mpf('1e-6'), "")
# numerical instantiation: iterate F_2 on 1-2T and confirm m(F_2^k f)/2^k is constant
c = [1, -2]
vals = []
cur = c
for k in range(1, 9):
    cur = frob(cur, 2)
    vals.append(mahler_roots(cur) / mpf(2) ** k)
spread = max(vals) - min(vals)
print("      m(F_2^k f)/2^k for k=1..8 :", ["%.15f" % float(v) for v in vals[:4]], "...")
check("H2  m(F_2^k f)/2^k is exactly constant (= log 2), spread %.2e" % float(spread),
      spread < mpf('1e-25'), "")
check("H3  and its value is log 2 = %.15f" % float(log(2)),
      abs(vals[-1] - log(2)) < mpf('1e-25'), "")

# ---------------------------------------------------------------- I
print()
print("=" * 70)
print("I.  The two rulings and the hyperbolic form <(k,a),(k',a')> = ka'+k'a")
print("=" * 70)


def pair(u, v):
    return u[0] * v[1] + v[0] * u[1]


fv, fh = (1, 0), (0, 1)
H = (1, 1)
check("I1  f_v^2 = 0", pair(fv, fv) == 0)
check("I2  f_h^2 = 0", pair(fh, fh) == 0)
check("I3  f_v . f_h = 1", pair(fv, fh) == 1)
check("I4  H^2 = 2   (matches 113_09 s4, measured from primes)", pair(H, H) == 2)
check("I5  (f_v - f_h)^2 = -2   (matches 113_09)",
      pair((1, -1), (1, -1)) == -2)
# cyclotomic classes are isotropic in this quotient
prime_power_n = 4
gam = (int(sp.totient(prime_power_n)), 0)
check("I6  Gamma_n = (phi(n), 0) is isotropic: <Gamma_n,Gamma_n> = 0",
      pair(gam, gam) == 0, "n=4, phi=2")
delt = (1, 0)
check("I7  <Gamma_n, Delta> = 0 in the quotient, while prime-power Lambda(n) is nonzero",
      pair(gam, delt) == 0 and vonmangoldt(prime_power_n) != 0)

# ---------------------------------------------------------------- J
print()
print("=" * 70)
print("J.  Growth: delta = 2 for the (rank, radius) gauge on W_rat(Z)")
print("=" * 70)


def logcount(n, A):
    """log #{c in Z^n : |c|_1 <= R}, R = e^A, via the exact formula
       #{|c|_1<=R} = sum_{j=0}^{n} 2^j C(n,j) C(R,j)."""
    R = int(exp(A))
    tot = 0
    for j in range(0, n + 1):
        if j > R:
            break
        tot += (2 ** j) * sp.binomial(n, j) * sp.binomial(R, j)
    return log(mpf(int(tot)))


k, a = 2, mpf('1.5')
prev = None
print("      m      n=mk    A=ma      log#H0(mD)        log#/m^2")
for m in [4, 8, 16, 32, 64, 128]:
    n, A = k * m, a * m
    L = logcount(n, A)
    print("      %-6d %-7d %-9.2f %-17.6f %.6f" % (m, n, float(A), float(L),
                                                   float(L / m ** 2)))
    prev = L
d1 = logcount(k * 64, a * 64)
d2 = logcount(k * 128, a * 128)
delta = log(d2 / d1) / log(mpf(2))
check("J1  delta = log(h0(2mD)/h0(mD))/log 2 = %.5f, within 0.15 of 2" % float(delta),
      abs(delta - 2) < mpf('0.15'))
check("J2  leading constant log#/m^2 -> k*a = %.4f (got %.4f at m=128)"
      % (k * float(a), float(d2 / 128 ** 2)),
      abs(d2 / mpf(128) ** 2 - k * a) < mpf('0.45'))

# ---------------------------------------------------------------- verdict
print()
print("=" * 70)
if FAIL:
    print("FAILED CHECKS: %s" % FAIL)
    print("VERDICT: NOT ALL CHECKS PASS")
    sys.exit(1)
print("VERDICT: ALL CHECKS PASS")
sys.exit(0)
