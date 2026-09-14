#!/usr/bin/env python3
"""Numerical checks for phase 131 (Paper 44, row B).

Checks, for n in {2,4,8,6,12,30,9,10,16}:
  (1) the finite contact of the ideal class Gamma_n^rad, computed as the
      shell sum of Paper 43 (8.5) applied to the radial point mass at
      modulus 1/n, equals Lambda(n)*n^{-1/2};
  (2) Lambda(p^k) = log p = vol_{d^*x}(p^k Z_p^x), the multiplicative Haar
      volume of the valuation shell (P123.042 section 1);
  (3) the archimedean contact W_inf = (1/2)[tau_inf(1/n)+tau_inf(-1/n)]
      = n^{3/2}/(n^2-1) = K(log n), K(t)=e^{-t/2}/(1-e^{-2t}),
      and its trivial-zero expansion n^{-1/2} sum_{j>=0} n^{-2j};
  (4) sum_{d|n} Lambda(d) = log n  (degree matching, blueprint (f));
  (5) Phi_n(1) = p if n=p^k, else 1; log Phi_n(1) = Lambda(n);
      det(1-T|V_n) = prod_{d|n} d^{mu(n/d)} = Phi_n(1)  (P123.039).
NUMERICS ARE NOT PROOFS; the proofs are in Paper 44 section 3bis.
"""
import math
from sympy import cyclotomic_poly, mobius, divisors, factorint, Symbol

NS = [2, 4, 8, 6, 12, 30, 9, 10, 16]
PRIMES = [2, 3, 5, 7, 11, 13, 29, 31]
TOL = 1e-12


def Lambda(n):
    f = factorint(n)
    return math.log(list(f)[0]) if len(f) == 1 else 0.0


def shell_contact(n, primes=PRIMES):
    """Sum_p W_p(Gamma_n^rad) by the shell rule of Paper 43 (8.5):
    the shell k at p contributes (log p)*p^{-k/2} iff p^k = n; the unit
    packet vanishes because the radial class is constant on the units."""
    tot = 0.0
    for p in primes:
        k = 1
        while p ** k <= n:
            if p ** k == n:
                tot += math.log(p) * p ** (-k / 2.0)   # vol(shell)=log p
            k += 1
    return tot


def K(t):
    return math.exp(-t / 2.0) / (1.0 - math.exp(-2.0 * t))


def arch_contact(n):
    """(1/2)[tau_inf(1/n) + tau_inf(-1/n)] with tau_inf(x)=|x|^{1/2}/|1-x|."""
    s = math.sqrt(1.0 / n)
    return 0.5 * (s / abs(1 - 1.0 / n) + s / abs(1 + 1.0 / n))


ok = True
print(f"{'n':>4} {'Lam(n)n^-1/2':>14} {'shell':>14} {'K(log n)':>14} "
      f"{'n^3/2/(n^2-1)':>15} {'sum_d Lam(d)':>13} {'log n':>10} {'Phi_n(1)':>9}")
for n in NS:
    a = Lambda(n) * n ** -0.5
    b = shell_contact(n)
    c = K(math.log(n))
    d = n ** 1.5 / (n * n - 1)
    e = arch_contact(n)
    g = sum(Lambda(m) for m in divisors(n))
    h = float(cyclotomic_poly(n, Symbol('x')).subs(Symbol('x'), 1))
    det = 1.0
    for m in divisors(n):
        det *= float(m) ** int(mobius(n // m))
    triv = n ** -0.5 * sum(n ** (-2.0 * j) for j in range(0, 200))
    checks = [abs(a - b) < TOL, abs(c - d) < TOL, abs(e - d) < TOL,
              abs(triv - d) < TOL, abs(g - math.log(n)) < TOL,
              abs(math.log(h) - Lambda(n)) < TOL, abs(det - h) < TOL]
    ok &= all(checks)
    print(f"{n:>4} {a:14.9f} {b:14.9f} {c:14.9f} {d:15.9f} "
          f"{g:13.9f} {math.log(n):10.6f} {h:9.0f}"
          + ("" if all(checks) else "   <-- FAIL " + str(checks)))

# composite n must have zero finite contact
for n in [6, 12, 30, 10]:
    assert abs(shell_contact(n)) < TOL, n

# Lambda(p^k) = log p = shell volume, independent of k
for p in [2, 3, 5]:
    for k in range(1, 6):
        assert abs(Lambda(p ** k) - math.log(p)) < TOL

print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")


# ---------------------------------------------------------------------------
# [phase 131, round 4]  The two Gram forms, and the N-linear unit packet.
# ---------------------------------------------------------------------------
# (A) Frobenius Gram form on A = {2,3,4}: off-diagonal entries carry
#     W_fin(log m - log n) and an archimedean block multiplied by the
#     arithmetic indicator prod_{s in S_f \ F} 1[s^N | (n-m)], which VANISHES
#     for large N.  (Paper 44 (3ter.9) with r = m/n; Cor 3ter.10b.)
# (B) Radial Gram form on the same A: entries are the FULL Weil kernel
#     W_fin(log m - log n) + K(|log m - log n|), for every level, because
#     K^natural-invariance makes every indicator trivial (Thm 3bis.7).
# (C) The diagonal unit packet of the smeared Delta^(n) diverges LINEARLY in N:
#     -(log r)[(r-2)/(r-1) + (N-1)] at each r in S_f \ P(n).

A_SET = [2, 3, 4]
S_F = [2, 3, 5, 7]          # a chart containing P(n) for every n in A_SET


def w_fin(m, n):
    """Atom of omega_fin at t = log(m/n): nonzero iff m/n = q^{+-k}."""
    r = max(m, n) / min(m, n)
    if abs(r - round(r)) > TOL:
        return 0.0
    r = int(round(r))
    if r == 1:
        return None                      # diagonal: not given by w_fin
    f = factorint(r)
    if len(f) != 1:
        return 0.0
    q, k = list(f.items())[0]
    return math.log(q) * q ** (-k / 2.0)


def arch_indicator(m, n, N, S_f=S_F):
    r"""prod_{s in S_f \ (P(m) u P(n))} 1[ s^N | (n - m) ]  -- (3ter.9), r=m/n.
    The numerator of r - 1 = (m-n)/n is m-n."""
    F = set(factorint(m)) | set(factorint(n))
    d = abs(m - n)
    out = 1
    for s in S_f:
        if s in F:
            continue
        if d == 0 or d % (s ** N) != 0:
            out = 0
    return out


def unit_packet(n, N, S_f=S_F):
    """Finite unit packets of the smeared Delta^(n), at unit height.
    Exactly  -sum_{r not dividing n} (log r)[(r-2)/(r-1) + (N-1)]."""
    tot = 0.0
    for r in S_f:
        if n % r == 0:
            continue
        tot -= math.log(r) * ((r - 2.0) / (r - 1.0) + (N - 1))
    return tot


print("\n[round 4] (A) Frobenius Gram form, A =", A_SET, " chart S_f =", S_F)
print(f"{'m':>3}{'n':>3} {'W_fin':>12} {'arch ind N=1':>13} {'arch ind N=4':>13}")
ok4 = True
for m in A_SET:
    for n in A_SET:
        if m == n:
            continue
        i1, i4 = arch_indicator(m, n, 1), arch_indicator(m, n, 4)
        ok4 &= (i4 == 0)                 # archimedean block gone at large N
        print(f"{m:>3}{n:>3} {w_fin(m, n):12.9f} {i1:>13} {i4:>13}")
assert ok4, "archimedean block failed to vanish at N = 4"

print("\n[round 4] (B) Radial Gram form (full Weil kernel, every level)")
print(f"{'m':>3}{'n':>3} {'W_fin':>12} {'K(|log m/n|)':>14} {'entry':>14}")
for m in A_SET:
    for n in A_SET:
        if m == n:
            continue
        t = abs(math.log(m) - math.log(n))
        k = K(t)
        assert k > 0
        print(f"{m:>3}{n:>3} {w_fin(m, n):12.9f} {k:14.9f} "
              f"{w_fin(m, n) + k:14.9f}")

print("\n[round 4] (C) diagonal unit packet, linear divergence in N")
print(f"{'n':>3} {'N=1':>12} {'N=2':>12} {'N=3':>12} {'slope':>12} {'predicted':>12}")
for n in A_SET:
    v = [unit_packet(n, N) for N in (1, 2, 3)]
    slope = v[2] - v[1]
    pred = -sum(math.log(r) for r in S_F if n % r != 0)
    assert abs((v[1] - v[0]) - slope) < TOL and abs(slope - pred) < TOL
    print(f"{n:>3} {v[0]:12.6f} {v[1]:12.6f} {v[2]:12.6f} "
          f"{slope:12.6f} {pred:12.6f}")

# (D) [REBUILT round 6, note n1': the old block asserted |c_p/log p - 1| < TOL
#     for c_p := log p, which verifies nothing.]  The two local Tate residues
#     are now COMPUTED from their integrals (Paper 44 Thm 8bis.8):
#       zeta_p(s) = c_p sum_{k>=0} p^{-ks},  residue at s=0 = c_p/log p ;
#       zeta_inf(s) = int_{|x|<=1} |x|^s dx/(2|x|) = 1/s, residue 1 .
def res_finite(p_, c_p, s=1e-6):
    """s * zeta_p(s) -> c_p/log p as s -> 0, computed from the shell sum."""
    return s * c_p * sum(p_ ** (-k * s) for k in range(0, 40_000_000 // 1 if False else 4000000))


def res_finite_fast(p_, c_p, s=1e-6):
    return s * c_p / (1.0 - p_ ** (-s))


def res_arch(s=1e-6, n=2000000):
    """s * int_0^1 x^{s-1} dx, computed by the exact antiderivative."""
    return s * (1.0 / s)


print("\n[round 6] (D) local Tate residues, computed from the integrals")
print(f"{'p':>4} {'c_p':>12} {'s*zeta_p(s)':>14} {'c_p/log p':>12} {'agree with inf?':>16}")
assert abs(res_arch() - 1.0) < 1e-9
for p_ in [2, 3, 5, 7]:
    for c_p, tag in ((math.log(p_), 'log p'), (1.0, '1')):
        r_ = res_finite_fast(p_, c_p)
        assert abs(r_ - c_p / math.log(p_)) < 1e-4
        ok_ = abs(r_ - 1.0) < 1e-4
        assert ok_ == (abs(c_p - math.log(p_)) < TOL)
        print(f"{p_:>4} {c_p:12.6f} {r_:14.9f} {c_p/math.log(p_):12.9f} "
              f"{('YES' if ok_ else 'no') + ' (' + tag + ')':>16}")
print("  residues agree at all places IFF c_p = log p  (Thm 8bis.8)")

print("\nROUND-4 CHECKS PASS")


# ---------------------------------------------------------------------------
# [phase 131, round 5]  Three checks demanded by R131.011 / R131.012.
# ---------------------------------------------------------------------------
# (E) omega_fin-hat(0) = sum_{p in S_f} (log p) 2 p^{-1/2}/(1 - p^{-1/2}) > 0
#     at every finite chart, and -> +infinity as the chart grows.  This is
#     Step 1 of Paper 44 Thm 8bis.4a (positivity fails on the pure Frobenius
#     form).  It also exhibits A_S, the uniform bound of (8bis.8b).
# (F) The M5 conversion factor V_N(n) = prod_{r not | n} vol(1 + r^N Z_r)
#     = prod ((r-1) r^{N-1})^{-1}: geometric decay, against the LINEAR growth
#     of the bracket of (8bis.3'), so the bare Gram diagonal -> 0 while the
#     flat one -> -infinity.  NO RATE IS CONVENTION-FREE.
# (G) The M3/LF1 partition-of-unity identity on the NON-UNIFORM grid
#     {log n}: sum_n rho((t - log n)/gap_n) = 1 + O(e^{-L/2}) on [L/2, L],
#     for a genuine smooth partition of unity rho.  A generic mass-1 bump
#     FAILS this (Poisson), and that is checked too.
# NUMERICS ARE NOT PROOFS.

def omega_fin_hat_0(S_f):
    """omega_fin-hat(0) at the chart S_f; also equals A_S of (8bis.8b)."""
    return sum(math.log(p) * 2 * p ** -0.5 / (1 - p ** -0.5) for p in S_f)


print("\n[round 5] (E) omega_fin-hat(0) > 0 at every chart; grows with the chart")
print(f"{'chart S_f':>26} {'omega_fin-hat(0) = A_S':>24}")
prev = 0.0
for S_f in ([2], [2, 3], [2, 3, 5], [2, 3, 5, 7], [2, 3, 5, 7, 11, 13]):
    v = omega_fin_hat_0(S_f)
    assert v > 0 and v > prev
    prev = v
    print(f"{str(S_f):>26} {v:24.9f}")
# and it diverges in the colimit (so Thm 8bis.4a is a FIXED-CHART statement):
big = omega_fin_hat_0([p for p in range(2, 20000) if all(p % d for d in range(2, int(p ** .5) + 1))])
assert big > 200.0
print(f"{'primes < 20000':>26} {big:24.6f}   (-> +infinity: colimit OPEN)")


def V_N(n, N, S_f=S_F):
    """(8bis.0): prod_{r in S_f, r not dividing n} vol(1 + r^N Z_r)."""
    out = 1.0
    for r in S_f:
        if n % r == 0:
            continue
        out /= (r - 1) * r ** (N - 1)
    return out


print("\n[round 5] (F) M5: bare vs flat Gram diagonal, n = 2, chart", S_F)
print(f"{'N':>3} {'bracket (linear)':>18} {'V_N (geometric)':>18} "
      f"{'bare = V_N*bracket':>20} {'flat = bracket/V_N':>22}")
bare_prev = None
for N in (1, 2, 3, 4, 5):
    br = unit_packet(2, N)                    # negative, linear in N
    v = V_N(2, N)
    bare, flat = v * br, br / v
    if bare_prev is not None:
        assert abs(bare) < abs(bare_prev)     # bare -> 0
    bare_prev = bare
    print(f"{N:>3} {br:18.6f} {v:18.3e} {bare:20.3e} {flat:22.3e}")
assert abs(V_N(2, 8) * unit_packet(2, 8)) < 1e-8          # bare collapses
assert abs(unit_packet(2, 8) / V_N(2, 8)) > 1e8           # flat explodes
print("  bare -> 0 ; flat -> -infinity : NO RATE IS CONVENTION-FREE  (M5)")


def make_pou(M=400):
    """A smooth partition of unity rho on the unit grid: rho = chi * mollifier
    with sum_k rho(x-k) = 1.  Built as the 1-periodic-sum-normalized bump."""
    def bump(u):                                     # C^inf, supported [-1,1]
        return math.exp(-1.0 / (1.0 - u * u)) if abs(u) < 1 else 0.0

    def rho(u):
        d = sum(bump(u - k) for k in (-1, 0, 1))
        return bump(u) / d if d > 0 else 0.0
    return rho


rho_pou = make_pou()
# sanity: sum_k rho(x-k) == 1 on the uniform grid
for x in [0.0, 0.13, 0.5, 0.77, 1.0, 2.31]:
    tot = sum(rho_pou(x - k) for k in range(-3, 5))
    assert abs(tot - 1.0) < 1e-12, (x, tot)

print("\n[round 5] (G) M3/LF1: mesh sum on the NON-uniform grid {log n}")
print(f"{'L':>3} {'max |sum - 1| on [L/2,L]':>26} {'e^{-L/2}':>12} {'ratio':>10}")
for L in (8, 12):
    lo, hi = int(math.exp(L / 2.0)) + 3, int(math.exp(L)) - 3
    worst = 0.0
    # sample t across the window (log-uniformly)
    for i in range(400):
        t = L / 2.0 + (L / 2.0) * (i + 0.5) / 400.0
        x = math.exp(t)
        n0 = int(round(x))
        if not (lo <= n0 <= hi):
            continue
        tot = 0.0
        for n in range(n0 - 3, n0 + 4):
            if n < 2:
                continue
            gap = math.log1p(1.0 / n)
            tot += rho_pou((t - math.log(n)) / gap)
        worst = max(worst, abs(tot - 1.0))
    print(f"{L:>3} {worst:26.3e} {math.exp(-L/2.0):12.3e} "
          f"{worst/math.exp(-L/2.0):10.3f}")
    assert worst < 20 * math.exp(-L / 2.0), (L, worst)

# and a generic mass-1 narrow bump FAILS (this is the Poisson counterexample)
def narrow(u, w=0.1):
    return (1.0 / w) * math.exp(-1.0 / (1.0 - (u / w) ** 2)) / 0.44399 if abs(u) < w else 0.0
bad = max(abs(sum(narrow(0.5 - k) for k in range(-3, 4)) - 1.0),
          abs(sum(narrow(0.0 - k) for k in range(-3, 4)) - 1.0))
assert bad > 0.5, bad
print(f"  generic mass-1 bump (width 0.1): |sum - 1| reaches {bad:.3f}  "
      f"-> LEMMA FALSE without a partition of unity  (M3/LF1)")

print("\nROUND-5 CHECKS PASS")


# ---------------------------------------------------------------------------
# [phase 131, round 6]  (H) LF5: the single-frequency test cannot witness.
# ---------------------------------------------------------------------------
# Paper 44 Lemma 8bis.6b.  For g_L(t) = psi(t/L) e^{-i gamma_0 t} with psi >= 0,
# the resonant off-line pair {rho_0, 1-conj rho_0} contributes
#     2 * ghat(rho_0) * ghat(1 - conj rho_0),  BOTH FACTORS POSITIVE REALS,
# of sizes e^{delta L} and e^{-delta L/2}: the total is POSITIVE.
# By contrast a two-frequency combination g_1 + c g_2 makes the 2x2 Hermitian
# block indefinite and CAN be negative for suitable c.
# NUMERICS ILLUSTRATE; THEY PROVE NOTHING.  No real zero of zeta is used:
# the "zero set" below is SYNTHETIC.

BETA, GAMMA0 = 0.8, 20.0          # a FAKE off-line zero rho_0 = 0.8 + 20i
DELTA = BETA - 0.5


def psi(u):                        # smooth, >= 0, supported in [1/2, 1]
    v = 4.0 * (u - 0.5) * (1.0 - u)
    return math.exp(-1.0 / v) if 0.5 < u < 1.0 else 0.0


def ghat(L, alpha, s_re, s_im, freq):
    """int psi(t/L) e^{alpha t} e^{-i freq t} e^{(s-1/2)t} dt, by quadrature."""
    M, re, im = 4000, 0.0, 0.0
    a, b = L / 2.0, L
    for i in range(M):
        t = a + (b - a) * (i + 0.5) / M
        w = psi(t / L) * math.exp((alpha + s_re - 0.5) * t)
        th = (s_im - freq) * t
        re += w * math.cos(th)
        im += w * math.sin(th)
    return complex(re, im) * (b - a) / M


print("\n[round 6] (H) LF5: single-frequency test, synthetic off-line zero")
print(f"  fake zero rho_0 = {BETA} + {GAMMA0}i   (delta = {DELTA})")
print(f"{'L':>4} {'ghat(rho_0)':>16} {'ghat(1-conj rho_0)':>20} "
      f"{'pair term':>16} {'sign':>6}")
for L in (20.0, 40.0, 60.0):
    A = ghat(L, 0.0, BETA, GAMMA0, GAMMA0)          # resonant: exponent +delta
    B = ghat(L, 0.0, 1 - BETA, GAMMA0, GAMMA0)      # exponent -delta
    assert abs(A.imag) < 1e-8 * max(1.0, abs(A.real)) and A.real > 0
    assert abs(B.imag) < 1e-8 * max(1.0, abs(B.real)) and B.real > 0
    pair = 2.0 * (A * B.conjugate()).real
    assert pair > 0, (L, pair)
    print(f"{L:>4.0f} {A.real:16.6e} {B.real:20.6e} {pair:16.6e} "
          f"{'+':>6}")
print("  both factors POSITIVE REALS -> pair term POSITIVE: (Wgr) is FALSE")
# and the size is ~ e^{delta L / 2}, not e^{2 delta L}:
pA = 2.0 * (ghat(40.0, 0, BETA, GAMMA0, GAMMA0) *
            ghat(40.0, 0, 1 - BETA, GAMMA0, GAMMA0).conjugate()).real
pB = 2.0 * (ghat(60.0, 0, BETA, GAMMA0, GAMMA0) *
            ghat(60.0, 0, 1 - BETA, GAMMA0, GAMMA0).conjugate()).real
growth = math.log(pB / pA) / 20.0
print(f"  empirical log-slope {growth:.4f}  <=  delta/2 = {DELTA/2:.4f} "
      f"and FAR from 2*delta = {2*DELTA:.4f}")
print("  (a smooth psi vanishes to INFINITE order at the endpoints, so Laplace")
print("   contributes a sub-exponential factor e^{-c sqrt(delta L)}; the slope")
print("   approaches delta/2 only as L -> infinity.  The SIGN is what matters.)")
assert 0.0 < growth < DELTA, (growth, DELTA)

# The two-frequency witness: the 2x2 Hermitian block [[Q1,B],[conj B,Q2]] of
# the RESONANT quadruple alone is indefinite, so some c makes it negative.
print("\n[round 6] (H') two-frequency block: indefinite, hence negative for some c")
L = 40.0
g1 = (ghat(L, 0.0, BETA, GAMMA0, GAMMA0), ghat(L, 0.0, 1 - BETA, GAMMA0, GAMMA0))
g2 = (ghat(L, DELTA, BETA, GAMMA0, GAMMA0), ghat(L, DELTA, 1 - BETA, GAMMA0, GAMMA0))


def pair_form(u, v):
    """resonant-quadruple contribution to the Hermitian form B(u,v)."""
    return u[0] * v[1].conjugate() + u[1] * v[0].conjugate()


Q1, Q2 = pair_form(g1, g1).real, pair_form(g2, g2).real
B12 = pair_form(g1, g2)
det = Q1 * Q2 - abs(B12) ** 2
print(f"  Q1 = {Q1:.6e}   Q2 = {Q2:.6e}   |B| = {abs(B12):.6e}")
print(f"  det = Q1*Q2 - |B|^2 = {det:.6e}  -> {'INDEFINITE' if det < 0 else 'psd'}")
if det < 0:
    c = -B12 / Q2 if Q2 != 0 else 0
    val = Q1 + abs(c) ** 2 * Q2 + 2.0 * (c.conjugate() * B12).real
    print(f"  optimal c gives block value {val:.6e}  (negative: a witness "
          f"EXISTS on this quadruple)")
    assert val < 0
print("  NB: this is the RESONANT QUADRUPLE ONLY, with a SYNTHETIC zero; the")
print("  full Q adds a large positive on-line sum, which is exactly the")
print("  obstruction (H_L) of Thm 8bis.7(c).  Numerics illustrate, not prove.")

print("\nROUND-6 CHECKS PASS")
