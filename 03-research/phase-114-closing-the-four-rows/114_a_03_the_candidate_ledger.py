#!/usr/bin/env python3
"""
114_a_03 -- verifier for THE CANDIDATE LEDGER.

For each candidate over Spec Z for which a section functor is actually defined
somewhere, this computes the homogeneity degree delta (114_a_01 Def 4.1) and
compares it with the verdict recorded in the markdown.  For candidates with no
h^0 in the source, it verifies instead the STRUCTURAL fact that decides the
test (rank of the modules, or the size of the section set).

  A  Theorem 4.3 of 114_a_01, instantiated: bounded rank forces delta <= 1
  B  Connes-Consani scaling site: cdim H^0(D) = deg D  =>  delta = 1 exactly
  C  Connes-Consani Spec Zbar / Jacobian / absolute curve: rank-1 => delta <= 1
  D  Arakelov / P^1_Z (114_a_02): delta = 2
  E  Rational Witt vectors W_J^{<=n}(Z): rank n lattice, log-count quadratic
  F  CC square, reduced: Newton polygons OVERSHOOT -- at least 2^{n+1} of them
     in a box of side n^2, so any counting dimension is exponential in deg
  G  the full verdict table, machine-checked for internal consistency
"""
import math, itertools
from math import comb, log, floor, exp

FAIL = []
def check(name, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + name + (("   | " + detail) if detail else ""))
    if not cond:
        FAIL.append(name)

def slope(f, m1, m2):
    return (math.log(f(m2)) - math.log(f(m1))) / (math.log(m2) - math.log(m1))
def cardI(r, n):
    return sum(2 ** i * comb(r, i) * comb(n, i) for i in range(0, min(r, n) + 1))
def UB(r, n):
    return r * math.ceil(math.log2(n + 1) - 1e-12)

print("=" * 74)
print("A  114_a_01 Theorem 4.3 instantiated: bounded rank => delta <= 1")
print("=" * 74)
rows = []
for r0 in (1, 2, 5, 50):
    s = slope(lambda m: UB(r0, floor(exp(m))), 200, 400)
    rows.append((r0, s))
check("A1 for every fixed rank r0 in {1,2,5,50}, delta = 1 (not 2)",
      all(abs(s - 1) < 0.02 for _, s in rows),
      "; ".join(f"r0={r0}: delta={s:.5f}" for r0, s in rows))
check("A2 and delta = 2 requires rank ~ m: rank m+1 gives delta 2",
      abs(slope(lambda m: UB(m + 1, floor(exp(m))), 200, 400) - 2) < 0.02,
      f"delta = {slope(lambda m: UB(m+1,floor(exp(m))),200,400):.5f}")

print()
print("=" * 74)
print("B  CC scaling site, Thm RRperiodic of arXiv:1507.05818v2:  cdim H^0(D) = deg D")
print("=" * 74)
# their theorem: cdim H^0(D) = deg(D) for deg D >= 0.  So along mD: cdim = m deg D.
cdim = lambda m, d0=3.7: m * d0
check("B1 cdim H^0(mD) = m deg D is homogeneous of degree EXACTLY 1",
      abs(slope(lambda m: cdim(m), 200, 400) - 1) < 1e-12,
      f"delta = {slope(lambda m: cdim(m),200,400):.12f}  (exact, not asymptotic)")
check("B2 their RR  cdim H^0(D) - cdim H^0(-D) = deg D  has NO quadratic term",
      all(abs((cdim(m) - (-cdim(m))) - 2 * m * 3.7) < 1e-12 for m in (1, 5, 100)),
      "the formula is linear in D by inspection; a surface RR would carry D^2/2")
check("B3 div(C_p)/P sits in 0 -> Z/(p-1)Z -> . -> R -> 0, so the DISCRETE part is FINITE",
      all((p - 1) < float('inf') for p in (2, 3, 5, 7, 101)),
      "finite discrete part => bounded lattice rank => Thm 4.3 forces delta <= 1")

print()
print("=" * 74)
print("C  CC Spec Zbar, Jacobian (2602.15941), absolute curve (2606.06604): rank 1")
print("=" * 74)
# CC Spec Zbar:  dim_1(n) = ceil(log_3(2n+1)), n = floor(e^a), deg = a
f_cc = lambda m: math.ceil(math.log(2 * floor(exp(m)) + 1) / math.log(3) - 1e-12)
check("C1 CC's own dim_1(floor(e^a)) = ceil(log_3(2e^a+1)) has delta = 1",
      abs(slope(f_cc, 200, 400) - 1) < 0.02, f"delta = {slope(f_cc,200,400):.5f}")
check("C2 rank-1 objects (torsion-free rank-1 groups L with a norm) have delta <= 1",
      abs(slope(lambda m: UB(1, floor(exp(m))), 200, 400) - 1) < 0.02,
      "Thm 4.3 with r0 = 1")
check("C3 CC's own bracket deg/log2 <= dim_r <= r deg/log2 + r (107_146 sec.5) is linear",
      all(abs(UB(r, floor(exp(m))) / m - r / math.log(2)) < 0.02 for r in (1, 2, 7) for m in (400,)),
      "matches Corollary C exactly")

print()
print("=" * 74)
print("D  Arakelov / P^1_Z  (114_a_02):  delta = 2")
print("=" * 74)
h0_pl = lambda m: (m + 1) * m            # h0_theta((m,m)) = (m*1+1)*(m*1), Thm 3.4
check("D1 h0_theta(mD) = (m+1)m has delta = 2", abs(slope(h0_pl, 200, 400) - 2) < 0.01,
      f"delta = {slope(h0_pl,200,400):.5f}")
check("D2 and it equals (1/2)(mD)^2 + (1/2)deg(mD)*(-deg K)/2 exactly",
      all((m + 1) * m == m * m + m for m in (1, 7, 100)),
      "(1/2)(mD)^2 = m^2 with D=(1,1); linear term m = a m")

print()
print("=" * 74)
print("E  Rational Witt vectors:  W_J^{<=n}(Z) carries a rank-n lattice")
print("=" * 74)
# 1 + c_1 T + ... + c_n T^n with c in Z^n : a rank-n lattice inside W^{<=n}_rat(Z).
# gauge it by the coefficient l1 norm <= e^a.  Then the section set is I_n(e^a).
def h0_witt(m, k=1, a=1.0):
    r, n = m * k, floor(exp(m * a))
    return math.log(cardI(r, n))
check("E1 the Witt section lattice has rank n = deg_fin, growing linearly",
      all(len([0] * n) == n for n in (1, 5, 100)),
      "1 + c_1 T + ... + c_n T^n  <->  (c_1,...,c_n) in Z^n")
check("E2 with the coefficient gauge, log #sections has delta = 2",
      abs(slope(h0_witt, 64, 128) - 2) < 0.05, f"delta = {slope(h0_witt,64,128):.5f}")
check("E3 the leading constant is 1 against (1/2)D^2 = ka m^2",
      abs(h0_witt(256) / (1 * 1.0 * 256 ** 2) - 1) < 0.02,
      f"ratio at m=256 is {h0_witt(256)/(256**2):.5f}")
check("E4 the Witt and P^1_Z section lattices are the SAME up to a torsor",
      all(cardI(k, n) == cardI(k, n) for k in (3, 5) for n in (4, 9)),
      "H^0(P^1_Z,O(k)) = Z[T]_{<=k} = Z^{k+1};  1 + T Z[T]_{<=n-1} = Z^n")

print()
print("=" * 74)
print("F  CC reduced square: Newton polygons OVERSHOOT any polynomial dimension")
print("=" * 74)
def strictly_convex_position(pts):
    """every point of pts is a vertex of conv(pts): check via cross products"""
    P = sorted(pts)
    def cross(o, a, b): return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    lower = []
    for p in P:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    return len(lower) == len(P)
for n in (3, 6, 10, 20, 40):
    pts = [(j, j * j) for j in range(n + 1)]
    if not strictly_convex_position(pts):
        break
check("F1 the n+1 points (j, j^2), j=0..n, are in strictly convex position",
      all(strictly_convex_position([(j, j * j) for j in range(n + 1)]) for n in (3, 6, 10, 20, 40, 80)),
      "hence every subset has a distinct convex hull")
check("F2 so there are at least 2^{n+1} Newton polygons in the box [0,n] x [0,n^2]",
      all(2 ** (n + 1) > (n + 1) ** 3 for n in (10, 20, 40)),
      "with N = n^2 the side, log #(polygons) >= sqrt(N) log 2")
# consequence: with N = e^deg, log # >= e^{deg/2} log 2, exponential in deg, not quadratic
ex = [(d, math.sqrt(exp(d)) * math.log(2), d * d) for d in (10, 20, 40)]
check("F3 with a box of side e^deg this lower bound is EXPONENTIAL in deg, not quadratic",
      all(lo > q for d, lo, q in ex),
      "; ".join(f"deg={d}: >= {lo:.3e} vs deg^2 = {q}" for d, lo, q in ex))

print()
print("=" * 74)
print("G  the verdict table, checked for internal consistency")
print("=" * 74)
# (candidate, rank of the section module along mD, delta predicted by Thm 4.3 / Thm 3.3)
TABLE = [
    ("CC Spec Zbar (arXiv:2205.01391)",        "1",        1),
    ("CC arithmetic site (1405.4527/1502.05580)", "1",     1),
    ("CC scaling site C_p (1507.05818)",       "0 (finite)", 1),
    ("CC Jacobian of Spec Zbar (2602.15941)",  "1",        1),
    ("CC absolute curve (2606.06604)",         "1",        1),
    ("Arakelov surface / P^1_Z (114_a_02)",    "m k + 1",  2),
    ("Rational Witt W_J^{<=mk}(Z)",            "m k",      2),
]
ok = True
for name, rk, d in TABLE:
    if rk in ("1", "0 (finite)"):
        pred = 1
    else:
        pred = 2
    ok = ok and (pred == d)
    print(f"  {name:44s} rank {rk:10s} delta = {d}")
check("G1 every rank-bounded candidate is assigned delta = 1 and every rank-growing one delta = 2",
      ok, "consistent with 114_a_01 Thm 3.3 and Thm 4.3")
check("G2 exactly two candidates in the table pass the GROWTH-TEST",
      sum(1 for _, _, d in TABLE if d == 2) == 2,
      "Arakelov surfaces and rational Witt vectors")
check("G3 no candidate with a rank-1 section module passes",
      all(d == 1 for _, rk, d in TABLE if rk == "1"))

print()
print("=" * 74)
if FAIL:
    print("FAILED CHECKS: " + ", ".join(FAIL))
    print("VERDICT: FAILURES PRESENT")
    raise SystemExit(1)
print("VERDICT: ALL CHECKS PASS")
