#!/usr/bin/env python3
"""
114_a_01 -- verifier for THE GROWTH DICHOTOMY.

Checks, in order:
  A  fidelity of the implementation of the Connes-Consani absolute dimension
     (CC, arXiv:2205.01391v2 Sec.3) against their closed formula in rank 1
  B  exact rank-2 and rank-3 minima against 107_146 Sec.7
  C  Theorem 2.1 (entropy lower bound) and Theorem 2.2 (digit upper bound)
     on every exactly computed value
  D  the cardinality formula for the l1 ball
  E  Proposition 2.3   dim_r(1) = r
  F  Theorem 2.4, the two-sided bound, on a grid
  G  Theorem 3.2, the growth dichotomy: surface regime is Theta(m^2),
     both curve regimes are Theta(m)
  H  Theorem 4.1, the homogeneity degree: 2 on the surface, 1 on the curves
  I  negative controls
One PASS/FAIL line per check.
"""
import itertools, math
from math import comb, floor, log

FAIL = []
def check(name, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + name + (("   | " + detail) if detail else ""))
    if not cond:
        FAIL.append(name)

# ---------------------------------------------------------------- primitives
def ball(r, n):
    if r == 0:
        return [()]
    out = []
    for v in range(-n, n + 1):
        for rest in ball(r - 1, n - abs(v)):
            out.append((v,) + rest)
    return out

def l1(v):
    return sum(abs(x) for x in v)

def reachable(F, n, r):
    """all mass-admissible S_pm-combinations of F inside the l1 ball of radius n"""
    reach = {tuple([0] * r)}
    d = len(F)
    for mask in range(1 << d):
        S = [F[i] for i in range(d) if mask >> i & 1]
        if sum(l1(f) for f in S) > n:
            continue
        for eps in itertools.product((1, -1), repeat=len(S)):
            w = [0] * r
            for e, f in zip(eps, S):
                for i in range(r):
                    w[i] += e * f[i]
            reach.add(tuple(w))
    return reach

def dim_exact(r, n, cap=8):
    """CC absolute dimension: minimal cardinality of a linearly generating set"""
    I = set(ball(r, n))
    seen, pool = set(), []
    for v in sorted(I):
        if l1(v) == 0:
            continue
        if tuple(-x for x in v) in seen:      # F and -F generate the same
            continue
        seen.add(v)
        pool.append(v)
    for d in range(0, cap + 1):
        for F in itertools.combinations(pool, d):
            if I <= reachable(F, n, r):
                return d
    return None

def card(r, n):
    return sum(2 ** i * comb(r, i) * comb(n, i) for i in range(0, min(r, n) + 1))

def LB(r, n):                                  # Theorem 2.1
    return log(card(r, n)) / log(3)

def LBbox(r, n):                               # Theorem 2.4, left side
    return r * log(2 * (n // r) + 1) / log(3)

def UB(r, n):                                  # Theorem 2.2
    return r * math.ceil(math.log2(n + 1) - 1e-12)

print("=" * 72)
print("A  fidelity: rank one reproduces Connes-Consani  dim = ceil(log_3(2n+1))")
print("=" * 72)
bad = []
for n in range(1, 25):
    d = dim_exact(1, n, cap=5)
    cc = math.ceil(log(2 * n + 1) / log(3) - 1e-12)
    if d != cc:
        bad.append((n, d, cc))
check("A1 exhaustive dim_1(n) = ceil(log_3(2n+1)) for n=1..24", bad == [],
      f"{24 - len(bad)}/24 agree")
jumps = [n for n in range(1, 25) if dim_exact(1, n, 5) != dim_exact(1, n - 1, 5)]
want_j = [(3 ** (k - 1) + 1) // 2 for k in (1, 2, 3, 4)]
check("A2 dim_1 jumps exactly at n = (3^{k-1}+1)/2 = 1,2,5,14", jumps == want_j,
      f"observed {jumps}, predicted {want_j}")

print()
print("=" * 72)
print("B  exact higher-rank minima against 107_146 section 7")
print("=" * 72)
TABLE = {(2, 1): 2, (2, 2): 4, (2, 3): 4, (2, 4): 6, (3, 1): 3, (3, 2): 6}
exact = {}
for (r, n), want in TABLE.items():
    got = dim_exact(r, n, cap=8)
    exact[(r, n)] = got
    check(f"B  dim_{r}({n}) = {want}", got == want, f"computed {got}")
for n in (1, 4, 13):
    exact[(1, n)] = dim_exact(1, n, 5)

print()
print("=" * 72)
print("C  Theorem 2.1 (entropy) and Theorem 2.2 (digits) on every exact value")
print("=" * 72)
ok_lb = all(exact[k] >= math.ceil(LB(*k) - 1e-12) for k in exact)
ok_ub = all(exact[k] <= UB(*k) for k in exact)
check("C1 dim >= ceil(log_3 |I_r(n)|)  on all exact values", ok_lb,
      "; ".join(f"dim_{r}({n})={exact[(r,n)]}>={math.ceil(LB(r,n)-1e-12)}" for (r, n) in sorted(exact)))
check("C2 dim <= r*ceil(log_2(n+1))    on all exact values", ok_ub,
      "; ".join(f"dim_{r}({n})={exact[(r,n)]}<={UB(r,n)}" for (r, n) in sorted(exact)))

print()
print("=" * 72)
print("D  cardinality of the l1 ball")
print("=" * 72)
check("D  |I_r(n)| = sum_i 2^i C(r,i) C(n,i), r<=4, n<=6",
      all(card(r, n) == len(ball(r, n)) for r in range(1, 5) for n in range(0, 7)))

print()
print("=" * 72)
print("E  Proposition 2.3   dim_r(1) = r")
print("=" * 72)
vals = [(r, dim_exact(r, 1, cap=6)) for r in range(1, 6)]
check("E  dim_r(1) = r for r = 1..5", all(d == r for r, d in vals), str(vals))

print()
print("=" * 72)
print("F  Theorem 2.4   r*log_3(2*floor(n/r)+1) <= dim <= r*ceil(log_2(n+1))")
print("=" * 72)
grid = [(r, n) for r in range(1, 40) for n in (r, 2 * r, 10 * r, 1000, 10 ** 6) if n >= r]
check("F1 the two bracket ends are consistent (left <= right) on the grid",
      all(LBbox(r, n) <= UB(r, n) + 1e-9 for r, n in grid),
      f"{len(grid)} grid points")
check("F2 the box is inside the ball (proof of the left end)",
      all(all(l1(v) <= n for v in itertools.product(range(-(n // r), n // r + 1), repeat=r))
          for r, n in [(2, 5), (3, 7), (4, 9)]))
check("F3 the bracket contains every exact value",
      all(LBbox(r, n) - 1e-9 <= exact[(r, n)] <= UB(r, n) for (r, n) in exact),
      "; ".join(f"({r},{n}):[{LBbox(r,n):.2f},{UB(r,n)}]  dim={exact[(r,n)]}" for (r, n) in sorted(exact)))

print()
print("=" * 72)
print("G  Theorem 3.2  the growth dichotomy")
print("=" * 72)
# surface regime: D = (k,a) = (1,1);  mD = (m, m);  rank r = mk+1, radius n = e^{ma}
def surf(m, k=1, a=1.0):
    return (m * k + 1, floor(math.exp(m * a)))
mlist = [5, 10, 20, 40, 80]
sl = [(m, LBbox(*surf(m)) / m ** 2, UB(*surf(m)) / m ** 2) for m in mlist]
print("    m      LB/m^2      UB/m^2      (targets 1/ln3=0.9102, 1/ln2=1.4427)")
for m, lo, hi in sl:
    print(f"  {m:4d}   {lo:9.4f}   {hi:9.4f}")
check("G1 surface regime: LB/m^2 -> 1/ln 3 = 0.91024", abs(sl[-1][1] - 1 / log(3)) < 0.05,
      f"m=80 gives {sl[-1][1]:.5f}")
check("G2 surface regime: UB/m^2 -> 1/ln 2 = 1.44270", abs(sl[-1][2] - 1 / log(2)) < 0.05,
      f"m=80 gives {sl[-1][2]:.5f}")
all_m = [(m, LBbox(*surf(m)) / m ** 2, UB(*surf(m)) / m ** 2) for m in range(2, 121)]
check("G3a surface regime: 0.83*m^2 <= dim <= 2.25*m^2 for EVERY m >= 2 (uniform Theta)",
      all(0.83 <= lo and hi <= 2.25 for m, lo, hi in all_m),
      f"min LB/m^2 = {min(lo for _,lo,_ in all_m):.4f}, max UB/m^2 = {max(hi for _,_,hi in all_m):.4f}")
tail = [(m, lo, hi) for m, lo, hi in all_m if m >= 40]
check("G3b surface regime: the bracket tightens to [0.86,1.50]*m^2 for m >= 40",
      all(0.86 <= lo and hi <= 1.50 for m, lo, hi in tail),
      f"min LB/m^2 = {min(lo for _,lo,_ in tail):.4f}, max UB/m^2 = {max(hi for _,_,hi in tail):.4f} "
      f"(the ceiling in log_2 makes the upper end oscillate; sup is at m=43)")
# curve regime A: pure archimedean, rank 1 (this is CC's Spec Zbar)
cA = [(m, LBbox(1, floor(math.exp(m))) / m, UB(1, floor(math.exp(m))) / m) for m in mlist]
check("G4 curve regime A (rank 1, radius e^m): LB/m and UB/m both O(1)",
      all(0.5 <= lo and hi <= 2.0 for m, lo, hi in cA),
      "; ".join(f"m={m}:[{lo:.3f},{hi:.3f}]" for m, lo, hi in cA))
# curve regime B: pure rank, radius 1
check("G5 curve regime B (rank 3m+1, radius 1): dim = rank exactly, hence linear",
      all(dim_exact(r, 1, cap=6) == r for r in (1, 2, 3, 4, 5)))
check("G6 the two curve regimes are NOT quadratic: (dim/m^2) -> 0",
      cA[-1][2] / mlist[-1] < 0.05,
      f"curve A: UB/m^2 = {cA[-1][2]/mlist[-1]:.5f} at m=80")

print()
print("=" * 72)
print("H  Theorem 4.1  the homogeneity degree of h^0")
print("=" * 72)
def slope(f, m1, m2):
    return (log(f(m2)) - log(f(m1))) / (log(m2) - log(m1))
sS = slope(lambda m: UB(*surf(m)), 40, 80)
sA = slope(lambda m: UB(1, floor(math.exp(m))), 40, 80)
check("H1 surface: d log h^0 / d log m = 2", abs(sS - 2) < 0.05, f"measured {sS:.4f}")
check("H2 curve  : d log h^0 / d log m = 1", abs(sA - 1) < 0.05, f"measured {sA:.4f}")
sSl = slope(lambda m: LBbox(*surf(m)), 40, 80)
check("H3 surface, lower bracket also has slope 2", abs(sSl - 2) < 0.05, f"measured {sSl:.4f}")

print()
print("=" * 72)
print("I  negative controls")
print("=" * 72)
# I1: fixed rank can never be quadratic, whatever the radius.
#     radius e^m, so UB = r*ceil(m/ln2); evaluate the exponent without building e^m.
def UBexp(r, m):
    return r * math.ceil(m / log(2) - 1e-12)
seq = [(m, UBexp(7, m) / m ** 2) for m in (10, 10 ** 2, 10 ** 3, 10 ** 5)]
check("I1 fixed rank r=7, radius e^m: UB/m^2 <= 11/m -> 0; no fixed-rank model is a surface",
      all(v <= 11.0 / m + 1e-12 for m, v in seq) and seq[-1][1] < 1e-3,
      "; ".join(f"m={m}: {v:.3e}" for m, v in seq))
# I2: a degree-0-homogeneous h^0 (obstruction O1 inside D) has slope 0
check("I2 control: a scaling-stable h^0 has slope 0, not 2",
      abs(slope(lambda m: 7.0, 40, 80)) < 1e-12)
# I3: the entropy bound is NOT tight -- it must not be mistaken for the dimension
check("I3 the entropy bound is strictly weaker than dim at (r,n)=(2,4)",
      math.ceil(LB(2, 4) - 1e-12) < exact[(2, 4)],
      f"ceil(log_3 41) = {math.ceil(LB(2,4)-1e-12)} < dim_2(4) = {exact[(2,4)]}")
# I4: mass condition really bites -- without it dim_1(4) would be 2 as well, but
#     dim_2(2) would drop.  Check the mass condition is active:
Fbad = [(1, 0), (0, 1), (1, 1)]
check("I4 the mass condition is active: {(1,0),(0,1),(1,1)} does NOT generate I_2(2)",
      not (set(ball(2, 2)) <= reachable(Fbad, 2, 2)),
      "e.g. (2,0) needs mass 2 from (1,0)+(1,0), unavailable")

print()
print("=" * 72)
if FAIL:
    print("FAILED CHECKS: " + ", ".join(FAIL))
    print("VERDICT: FAILURES PRESENT")
    raise SystemExit(1)
print("VERDICT: ALL CHECKS PASS")
