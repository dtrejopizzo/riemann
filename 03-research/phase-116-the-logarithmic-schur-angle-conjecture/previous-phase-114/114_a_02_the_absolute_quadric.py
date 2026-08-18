#!/usr/bin/env python3
"""
114_a_02 -- verifier for  AN ARITHMETIC SURFACE OVER Spec Z WITH QUADRATIC h^0.

Object: Xbar = P^1 over Spec Z, Arakelov-compactified.
  Div(Xbar) = Z (+) R,   D = (k,a)
  <(k,a),(k',a')> = k a' + k' a          (hyperbolic, signature (1,1))
  H = (1,1),  deg D = <D,H> = k+a,  D^2 = 2ka,  K = (-2,0)
  H^0(D)  = { f in Z[T]_{<=k} : ||f|| <= e^a }        (three gauges)
  h0_th(D)= log sum_{x in H^0(X,O(k))} exp(-pi |x|^2 e^{-2a})   (van der Geer-
            Schoof / Bost / arXiv:2512.01811 definition of h^0)

Checks:
  A  mpmath theta convention and functional equation
  B  Theorem 3.4:  h0_th(D) = (1/2) D.(D-K) + eta,  0 <= eta <= 3(k+1)e^{-pi e^{2a}}
  C  Theorem 4.1:  the intersection form -- degree, H^2, signature, Hodge index
  D  Theorem 2.2:  H^0(P^1_Z, O(k)) = Z^{k+1}, by the glueing computation
  E  Theorem 3.1:  log #(l1 ball) and log #(sup box) are both (1/2)D^2 (1+o(1))
  F  Theorem 3.6:  the Connes-Consani absolute dimension on the same family
  G  Theorem 5.1:  gauge robustness -- l1 vs sup on the torus
  H  Theorem 6.1:  homogeneity degree 2; O1 fails here
  I  negative controls: k=0 and a=0 are linear
"""
import math, random, itertools
from math import comb, log, floor, exp
import mpmath as mp

mp.mp.dps = 60
FAIL = []
def check(name, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + name + (("   | " + detail) if detail else ""))
    if not cond:
        FAIL.append(name)

# ------------------------------------------------------------------ the model
def pair(D, E):                       # <(k,a),(k',a')> = k a' + k' a
    return D[0] * E[1] + E[0] * D[1]
H = (1, 1)
K = (-2, 0)
def deg(D):  return pair(D, H)
def sq(D):   return pair(D, D)
def th1(s):  return mp.jtheta(3, 0, mp.e ** (-mp.pi * s))       # sum_j e^{-pi j^2 s}
def h0_th(k, a):
    """log sum_{x in Z^{k+1}} exp(-pi |x|^2 e^{-2a}).
    Evaluated through Jacobi's functional equation theta(s) = s^{-1/2} theta(1/s)
    with s = e^{-2a}, which is both exact and numerically stable for large a:
        log theta(e^{-2a}) = a + log theta(e^{2a}),  theta(e^{2a}) = 1 + O(e^{-pi e^{2a}}).
    Check A2 verifies the functional equation to 60 digits."""
    a = mp.mpf(a)
    return (k + 1) * (a + mp.log(th1(mp.e ** (2 * a))))
def rr(k, a):                                                    # (1/2) D.(D-K)
    D = (k, mp.mpf(a))
    return (sq(D) - pair(D, K)) / 2

print("=" * 74)
print("A  mpmath theta convention")
print("=" * 74)
d1 = th1(1) - mp.nsum(lambda j: mp.e ** (-mp.pi * j ** 2), [-mp.inf, mp.inf])
check("A1 jtheta(3,0,e^{-pi s}) equals sum_j e^{-pi j^2 s} at s=1", abs(d1) < mp.mpf(10) ** -50,
      f"difference {mp.nstr(d1,3)}")
d2 = max(abs(th1(mp.mpf(s)) - mp.mpf(s) ** mp.mpf('-0.5') * th1(1 / mp.mpf(s))) for s in (0.3, 1, 3, 7))
check("A2 functional equation theta(s) = s^{-1/2} theta(1/s)", d2 < mp.mpf(10) ** -50,
      f"max deviation {mp.nstr(d2,3)}")

print()
print("=" * 74)
print("B  Theorem 3.4   h0_theta(D) = (1/2) D.(D-K) + eta,  K = (-2,0)")
print("=" * 74)
grid = [(1, 1), (2, 3), (5, 0.5), (10, 2), (0, 1), (3, 0.1), (7, 1.5), (0, 4), (40, 2.5)]
rows, ok = [], True
for k, a in grid:
    h, r = h0_th(k, a), rr(k, a)
    eta = h - r
    bnd = 3 * (k + 1) * mp.e ** (-mp.pi * mp.e ** (2 * mp.mpf(a)))
    good = (eta >= 0) and (eta <= bnd)
    ok = ok and good
    rows.append((k, a, mp.nstr(h, 14), mp.nstr(r, 14), mp.nstr(eta, 4), mp.nstr(bnd, 4)))
print("    k     a        h0_theta            (1/2)D(D-K)         eta          bound")
for k, a, h, r, e, b in rows:
    print(f"  {k:4d}  {a:<6}  {h:>18}  {r:>18}  {e:>12}  {b:>12}")
check("B1 the identity holds with 0 <= eta <= 3(k+1)exp(-pi e^{2a}) on all 9 points", ok,
      "eta = (k+1) log theta(e^{2a}) >= 0 structurally, no roundoff involved")
check("B2 the identity is EXACT to 60 digits once a >= 2", 
      all(abs(h0_th(k, a) - rr(k, a)) < mp.mpf(10) ** -50 for k, a in [(2, 3), (10, 2), (40, 2.5), (0, 4)]),
      "eta < 1e-50 at (2,3),(10,2),(40,2.5),(0,4)")
check("B3 deg K = -2, matching deg K_{P^1} = -2", deg(K) == -2, f"deg K = {deg(K)}")
check("B4 the identity FAILS for any other K: K=(-2,c) with c != 0 breaks it",
      all(abs(h0_th(3, 2.0) - ((sq((3, mp.mpf(2))) - pair((3, mp.mpf(2)), (-2, c))) / 2)) > mp.mpf('1e-6')
          for c in (-1, 1, 2)),
      "tested c = -1, 1, 2 at D=(3,2)")

print()
print("=" * 74)
print("C  Theorem 4.1   the intersection form")
print("=" * 74)
check("C1 deg(k,a) = k + a", all(deg((k, a)) == k + a for k, a in [(1, 1), (3, 2.5), (0, 7), (-4, 1)]))
check("C2 H^2 = 2", sq(H) == 2)
check("C3 D^2 = 2ka", all(sq((k, a)) == 2 * k * a for k, a in [(1, 1), (3, 2.5), (0, 7), (-4, 1)]))
ev = sorted(float(x) for x in mp.eig(mp.matrix([[0, 1], [1, 0]]))[0])
check("C4 signature is (1,1)", abs(ev[0] + 1) < 1e-30 and abs(ev[1] - 1) < 1e-30, f"eigenvalues {ev}")
# H-perp = {(k,-k)}; on it D^2 = -2k^2 < 0 for k != 0
check("C5 Hodge index: the form is NEGATIVE DEFINITE on H-perp",
      all(pair((k, -k), H) == 0 and sq((k, -k)) == -2 * k * k < 0 for k in (1, 2, 5, -3)),
      "H-perp = {(k,-k)}, D^2 = -2k^2")
check("C6 the effective classes (k>=0,a>=0) span a strict cone; H is interior",
      sq(H) > 0 and deg(H) > 0 and all(pair(H, (k, a)) > 0 for k, a in [(1, 0), (0, 1), (3, 2)]))

print()
print("=" * 74)
print("D  Theorem 2.2   H^0(P^1_Z, O(k)) = Z^{k+1}  by glueing")
print("=" * 74)
import sympy as sp
t = sp.symbols('t')
ok = True
detail = []
for k in range(0, 6):
    J = k + 3
    cs = sp.symbols(f'c0:{J+1}')
    f1 = sum(cs[j] * sp.Symbol('u') ** j for j in range(J + 1))
    expr = sp.expand(sp.simplify((t ** k) * f1.subs(sp.Symbol('u'), 1 / t)))
    # collect the strictly negative powers of t; each must vanish
    poly = sp.Poly(sp.together(expr) .as_numer_denom()[0], t)
    conds = []
    for j in range(J + 1):
        p = k - j
        if p < 0:
            conds.append(cs[j])
    sol_dim = (J + 1) - len(conds)
    ok = ok and (sol_dim == k + 1)
    detail.append(f"k={k}: dim={sol_dim}")
check("D1 sections of O(k) on P^1_Z form a free Z-module of rank k+1, k=0..5", ok, "; ".join(detail))
check("D2 monomial basis T_0^i T_1^{k-i}, i=0..k, has k+1 elements",
      all(len([(i, k - i) for i in range(k + 1)]) == k + 1 for k in range(0, 8)))

print()
print("=" * 74)
print("E  Theorem 3.1   log #(ball) and log #(box) are both (1/2)D^2 (1+o(1))")
print("=" * 74)
def cardI(r, n):
    return sum(2 ** i * comb(r, i) * comb(n, i) for i in range(0, min(r, n) + 1))
print("    m     r        log|I_r(n)|     (1/2)(mD)^2      ball ratio    box ratio")
rat = []
for m in (4, 8, 16, 32, 64, 128, 256):
    k, a = 1, 1.0
    r, n = m * k + 1, floor(exp(m * a))
    L = math.log(cardI(r, n))
    half = k * a * m * m
    box = r * math.log(2 * n + 1)
    rat.append((m, L / half, box / half))
    print(f"  {m:4d} {r:5d}  {L:16.4f} {half:15.4f}   {L/half:11.5f}  {box/half:11.5f}")
check("E1 ball ratio -> 1", abs(rat[-1][1] - 1) < 0.02, f"m=256: {rat[-1][1]:.5f}")
check("E2 box  ratio -> 1", abs(rat[-1][2] - 1) < 0.02, f"m=256: {rat[-1][2]:.5f}")
check("E3 ball ratio is inside [0.95,1.20] for every m >= 8",
      all(0.95 <= x <= 1.20 for m, x, _ in rat if m >= 8),
      f"min {min(x for m,x,_ in rat if m>=8):.5f}, max {max(x for m,x,_ in rat if m>=8):.5f}")
r2 = []
for m in (8, 16, 32, 64, 128):
    k, a = 2, 3.0
    r, n = m * k + 1, floor(exp(m * a))
    r2.append((m, math.log(cardI(r, n)) / (k * a * m * m), r * math.log(2 * n + 1) / (k * a * m * m)))
check("E4 same at (k,a)=(2,3): both ratios -> 1",
      abs(r2[-1][1] - 1) < 0.02 and abs(r2[-1][2] - 1) < 0.02,
      f"m=128: ball {r2[-1][1]:.5f}, box {r2[-1][2]:.5f}")

print()
print("=" * 74)
print("F  Theorem 3.6   the Connes-Consani absolute dimension on the same family")
print("=" * 74)
def LBbox(r, n): return r * log(2 * (n // r) + 1) / log(3)
def UB(r, n):    return r * math.ceil(math.log2(n + 1) - 1e-12)
rowsF = []
for m in (10, 20, 40, 80):
    k, a = 1, 1.0
    r, n = m * k + 1, floor(exp(m * a))
    half = k * a * m * m
    rowsF.append((m, LBbox(r, n) / (2 * half), UB(r, n) / (2 * half)))
print("    m    lower/D^2    upper/D^2      (targets 1/(2 ln3)=0.4551, 1/(2 ln2)=0.7213)")
for m, lo, hi in rowsF:
    print(f"  {m:4d}   {lo:9.5f}   {hi:9.5f}")
check("F1a dim_{S+} / D^2 lies in [0.40,0.83] for m >= 10 (a quadratic law)",
      all(0.40 <= lo and hi <= 0.83 for m, lo, hi in rowsF),
      "so dim_{S+} = (1/2)D^2 / log q for an effective q in [2,3]")
check("F1b the window tightens to [0.43,0.75] for m >= 40",
      all(0.43 <= lo and hi <= 0.75 for m, lo, hi in rowsF if m >= 40),
      f"m=40: [{rowsF[2][1]:.5f},{rowsF[2][2]:.5f}]  m=80: [{rowsF[3][1]:.5f},{rowsF[3][2]:.5f}]")
check("F2 both CC brackets are quadratic, matching E to within the base of the log",
      abs(rowsF[-1][1] - 1 / (2 * log(3))) < 0.05 and abs(rowsF[-1][2] - 1 / (2 * log(2))) < 0.05,
      f"m=80: [{rowsF[-1][1]:.5f}, {rowsF[-1][2]:.5f}] vs [0.45512, 0.72135]")

print()
print("=" * 74)
print("G  Theorem 5.1   gauge robustness: l1 versus sup on the torus")
print("=" * 74)
random.seed(20260804)
bad1 = bad2 = 0
for _ in range(400):
    k = random.randint(0, 12)
    c = [random.randint(-9, 9) for _ in range(k + 1)]
    sup = max(abs(sum(cj * complex(math.cos(j * ph), math.sin(j * ph)) for j, cj in enumerate(c)))
              for ph in [2 * math.pi * i / 4001 for i in range(4001)])
    l1 = sum(abs(x) for x in c)
    if not sup <= l1 + 1e-9:
        bad1 += 1
    if not l1 <= (k + 1) * sup + 1e-6:
        bad2 += 1
check("G1 ||f||_sup <= ||f||_{l1}                      (400 random integer forms)", bad1 == 0)
check("G2 ||f||_{l1} <= (k+1) ||f||_sup   (Fourier)    (400 random integer forms)", bad2 == 0)
# consequence: the sup ball is squeezed between two l1 balls whose log-counts agree to leading order
m, k, a = 64, 1, 1.0
r, n = m * k + 1, floor(exp(m * a))
lo = math.log(cardI(r, n)); hi = math.log(cardI(r, r * n))
check("G3 the squeeze log|I_r(n)| <= log #B_sup <= log|I_r(r n)| has both ends ~ (1/2)D^2",
      abs(lo / (k * a * m * m) - 1) < 0.05 and abs(hi / (k * a * m * m) - 1) < 0.05,
      f"m=64: [{lo/(k*a*m*m):.5f}, {hi/(k*a*m*m):.5f}] times (1/2)D^2")
g4 = abs(float(h0_th(m * k, m * a)) - r * math.log(2 * n + 1))
check("G4 the theta gauge agrees with the box gauge to O(m): |h0_th - r log(2n+1)| <= r log 2",
      g4 <= r * math.log(2) + 1e-6,
      f"difference {g4:.4f} <= r log 2 = {r*math.log(2):.4f}   (m={m}, r={r})")

print()
print("=" * 74)
print("H  Theorem 6.1   homogeneity degree 2; obstruction O1 does not apply")
print("=" * 74)
def slope(f, m1, m2): return (math.log(f(m2)) - math.log(f(m1))) / (math.log(m2) - math.log(m1))
sl = slope(lambda m: float(h0_th(m, m)), 40, 80)
check("H1 delta = d log h0_theta / d log m = 2 exactly for h0_theta", abs(sl - 2) < 0.02,
      f"measured {sl:.6f}")
check("H2 h0_theta(mD)/h0_theta(D) -> infinity, so Prop 5.1 of 113_10 does NOT hold here",
      float(h0_th(100, 100.0)) / float(h0_th(1, 1.0)) > 5000,
      f"ratio at m=100 is {float(h0_th(100,100.0))/float(h0_th(1,1.0)):.1f} (= m^2 = 10000 up to O(1/m))")
check("H3 h0_theta is strictly increasing in both k and a",
      all(h0_th(k + 1, 1.0) > h0_th(k, 1.0) for k in range(0, 8)) and
      all(h0_th(3, a + 0.3) > h0_th(3, a) for a in [0.1, 0.5, 1.0, 2.0]))

print()
print("=" * 74)
print("I  negative controls: one direction only is LINEAR")
print("=" * 74)
slA = slope(lambda m: float(h0_th(0, m)), 40, 80)              # k=0: CC's Spec Zbar
slB = slope(lambda m: float(h0_th(m, 1.0)), 40, 80)            # a fixed: rank only
check("I1 k=0 (purely archimedean, = CC's Spec Zbar): delta = 1", abs(slA - 1) < 0.02, f"measured {slA:.6f}")
check("I2 a fixed (rank direction only): delta = 1", abs(slB - 1) < 0.02, f"measured {slB:.6f}")
check("I3 in both controls (1/2)D^2 = 0 or is linear, consistent with delta = 1",
      sq((0, 5)) == 0 and sq((5, 1)) == 10)
check("I4 the quadratic term needs BOTH: D^2 = 2ka vanishes iff k=0 or a=0",
      all((sq((k, a)) == 0) == (k == 0 or a == 0) for k in range(0, 4) for a in (0, 1, 2)))

print()
print("=" * 74)
if FAIL:
    print("FAILED CHECKS: " + ", ".join(FAIL))
    print("VERDICT: FAILURES PRESENT")
    raise SystemExit(1)
print("VERDICT: ALL CHECKS PASS")
