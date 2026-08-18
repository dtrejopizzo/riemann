#!/usr/bin/env python3
"""Verifier for 107.244 - axis-restricted lower bound and dim_2(7)."""
import itertools, math, sys, pathlib, importlib.util
_l = pathlib.Path(__file__).with_name("107_146_cc_absolute_dimension_lib.py")
if not _l.exists():
    _l = pathlib.Path("/home/trabajo/Documentos/research/riemann/riemann/03-research/"
                      "phase-107-arithmetic-lefschetz-reconstruction/107_146_cc_absolute_dimension_lib.py")
_s = importlib.util.spec_from_file_location("lib", _l); _m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
ball, reach, candidates = _m.ball, _m.reach, _m.candidates
FAIL=[]
def check(n, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {extra}")
    if not ok: FAIL.append(n)

def K(n): return max(1, math.ceil(math.log(n+1)/math.log(2)-1e-12))

# --- A. axis-restricted minimum equals exactly 2k ---------------------------
def axis_min(n):
    B=set(ball(n,2)); ax=[(a,0) for a in range(1,n+1)]+[(0,b) for b in range(1,n+1)]
    for size in range(1, 2*K(n)+1):
        for F in itertools.combinations(ax, size):
            if reach(list(F), n)==B: return size
    return None
ok=True; rows=[]
for n in range(1,13):
    d=axis_min(n); rows.append((n,d,2*K(n)))
    if d!=2*K(n): ok=False
check("axis-restricted minimum = 2*ceil(log2(n+1)) for n=1..12", ok,
      str([(n,d) for n,d,_ in rows]))

# --- B. the powers-of-2 construction attains it -----------------------------
ok=True
for n in range(1,40):
    k=K(n); F=[(2**i,0) for i in range(k)]+[(0,2**i) for i in range(k)]
    if reach(F,n)!=set(ball(n,2)): ok=False
check("powers-of-2 axis construction generates B_n for n=1..39", ok)

# --- C. Lemma-1 axis filter is valid: (n,0) needs x-axis generators summing n
def hits(S,t):
    r={0}
    for s in S: r |= {v+s for v in r if v+s<=t}
    return t in r
ok=True
for n in range(1,10):
    B=set(ball(n,2)); C=candidates(n,2)
    for _ in range(1):
        for F in itertools.combinations(C, 2):
            if reach(list(F),n)==B:                     # generating => filter must pass
                X=[f[0] for f in F if f[1]==0]; Y=[f[1] for f in F if f[0]==0]
                if not (hits(X,n) and hits(Y,n)): ok=False
check("Lemma-1 axis filter is a valid necessary condition (size-2 sweep)", ok)

# --- D. exhaustive dim_2(7) = 6 ---------------------------------------------
n=7; B=set(ball(n,2)); C=candidates(n,2); found=None
for size in range(K(n), 2*K(n)):
    for F in itertools.combinations(C, size):
        X=[f[0] for f in F if f[1]==0]; Y=[f[1] for f in F if f[0]==0]
        if not (hits(X,n) and hits(Y,n)): continue
        if reach(list(F), n)==B: found=(size,F); break
    if found: break
check("exhaustive: no generating set of size < 6 exists at n=7", found is None)
k=K(7); F=[(2**i,0) for i in range(k)]+[(0,2**i) for i in range(k)]
check("dim_2(7) = 6 (upper bound attained)", reach(F,7)==set(ball(7,2)) and len(F)==6)

print()
print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
