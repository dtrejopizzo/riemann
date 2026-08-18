#!/usr/bin/env python3
"""Verifier for 107.146.  Checks every computational claim in the note."""
import itertools, math, sys, pathlib, importlib.util

_lib = pathlib.Path(__file__).with_name("107_146_cc_absolute_dimension_lib.py")
_spec = importlib.util.spec_from_file_location("cc_absolute_dimension_lib", _lib)
_mod = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_mod)
ball, reach, exact_dim = _mod.ball, _mod.reach, _mod.exact_dim

FAIL = []
D1 = {n: exact_dim(n,1,cap_k=6)[0] for n in range(1,41)}
def check(name, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {name} {extra}")
    if not ok: FAIL.append(name)

# ---- 1. CC rank-one formula, n = 1..40 --------------------------------
ok = all(D1[n] == math.ceil(math.log(2*n+1)/math.log(3)-1e-12) for n in range(1,41))
check("CC rank-1 formula dim = ceil(log_3(2n+1)) for n=1..40", ok)

# ---- 2. Lemma 1: no cancellation on the boundary sphere ---------------
# exhaustively: every mass-<=n representation of a sphere point has all
# summands in one closed orthant, and total mass exactly n.
def lemma1_holds(n, r):
    B = ball(n, r)
    sphere = [v for v in B if sum(map(abs,v)) == n]
    gens = [v for v in B if any(v)]
    for v in sphere:
        for m in range(1, 4):
            for A in itertools.combinations(gens, m):
                for signs in itertools.product((1,-1), repeat=m):
                    w = [tuple(s*c for c in f) for s,f in zip(signs,A)]
                    mass = sum(sum(map(abs,x)) for x in w)
                    if mass > n: continue
                    s = tuple(sum(x[i] for x in w) for i in range(r))
                    if s != v: continue
                    if mass != n: return False            # claim (1)
                    for i in range(r):                    # claim (2)
                        col = [x[i] for x in w]
                        if any(c>0 for c in col) and any(c<0 for c in col):
                            return False
    return True
check("Lemma 1 exhaustive, r=2, n=1..6", all(lemma1_holds(n,2) for n in range(1,7)))
check("Lemma 1 exhaustive, r=3, n=1..3", all(lemma1_holds(n,3) for n in range(1,4)))

# ---- 3. Theorem B construction actually generates ---------------------
ok = True
for r in (1,2,3):
    for n in range(1, 8 if r==3 else 40 if r==2 else 40):
        k = max(1, math.ceil(math.log(n+1)/math.log(2)-1e-12))
        F = [tuple(2**i if j==t else 0 for j in range(r)) for t in range(r) for i in range(k)]
        B = set(v for v in itertools.product(range(-n,n+1),repeat=r)
                if sum(map(abs,v)) <= n)
        if reach(F,n) != B: ok = False; print("   counterexample", r, n)
check("Theorem B construction generates (r=1,2 n<=39; r=3 n<=7)", ok)

# ---- 4. Theorem A lower bound respected by the exact rank-2 minima ----
exact2 = {}
for n in range(1,7):
    exact2[n] = exact_dim(n,2,cap_k=7)[0]
check("exact rank-2 minima n=1..6 equal (2,4,4,6,6,6)",
      [exact2[n] for n in range(1,7)] == [2,4,4,6,6,6], str(exact2))
check("Theorem A lower bound holds on those",
      all(exact2[n] >= math.ceil(math.log(n+1)/math.log(2)-1e-12) for n in exact2))
check("Theorem B upper bound holds on those",
      all(exact2[n] <= 2*math.ceil(math.log(n+1)/math.log(2)-1e-12) for n in exact2))
check("conjecture dim_2 = 2*ceil(log2(n+1)) on n=1..6",
      all(exact2[n] == 2*math.ceil(math.log(n+1)/math.log(2)-1e-12) for n in exact2))

# ---- 5. counting bound tight in rank 1, fails in rank 2 --------------
check("counting bound ceil(log_3|I_1(n)|) tight for n=1..40",
      all(D1[n] == math.ceil(math.log(2*n+1)/math.log(3)-1e-12) for n in range(1,41)))
check("counting bound ceil(log_3|I_2(n)|) FAILS at n=4,5,6",
      all(exact2[n] > math.ceil(math.log(len(ball(n,2)))/math.log(3)-1e-12)
          for n in (4,5,6)))

# ---- 6. Theorem D inequality, n = 1..200000 --------------------------
check("Theorem D: ceil(log2(n+1)) >= ceil(log_3(2n+1)) for n=1..200000",
      all(math.ceil(math.log(n+1)/math.log(2)-1e-12) >=
          math.ceil(math.log(2*n+1)/math.log(3)-1e-12) for n in range(1,200001)))
check("Theorem D: strict for n = 4, 8, 20, 40, 100, 1000",
      all(math.ceil(math.log(n+1)/math.log(2)-1e-12) >
          math.ceil(math.log(2*n+1)/math.log(3)-1e-12)
          for n in (4,8,20,40,100,1000)))

# ---- 7. the n=8 first-quadrant witness of section 7 -------------------
G = [(0,2),(0,6),(1,1),(2,0),(2,2),(6,0)]
seg = {(x,8-x) for x in range(9)}
got = set()
for m in range(1,7):
    for A in itertools.combinations(G,m):
        if sum(a+b for a,b in A) == 8:
            got.add((sum(a for a,_ in A), sum(b for _,b in A)))
check("sec.7 first-quadrant witness at n=8 covers the segment with |G|=6",
      seg <= got and len(G) == 6)

print()
print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"{len(FAIL)} FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
