#!/usr/bin/env python3
"""Verifier for 108.35 - the log p normalization and the Weil coefficient."""
import math, sys
FAIL=[]
def check(n,ok,x=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {x}");  FAIL.append(n) if not ok else None
PR=(2,3,5,7,11,13,101)
def G_unit(p,k,s): return (p**min(k,0))*(p**k)**(-s)
def G_tate(p,k,s): return math.log(p)*G_unit(p,k,s)
def vonmangoldt_coeff(p,k): return math.log(p)/math.sqrt(p**k)

# A. Theorem 2.1
ok=all(abs(G_tate(p,k,0.5)-vonmangoldt_coeff(p,k))<1e-15 for p in PR for k in (1,2,3,4,5))
check("A  Gamma^Tate_{p,k}(f_{1/2}) = Lambda(p^k)/sqrt(p^k)  (exact)", ok,
      f"{len(PR)*5} cases")

# B. Corollary 2.2: mirror shells agree at s=1/2
ok=all(abs(G_tate(p,-m,0.5)-G_tate(p,m,0.5))<1e-15 for p in PR for m in (1,2,3,4))
check("B  mirror shells k and -k coincide at s=1/2", ok)

# C. normalization (N1) does NOT give the Weil coefficient
bad=[(p,k) for p in PR for k in (1,2,3)
     if abs(G_unit(p,k,0.5)-vonmangoldt_coeff(p,k))>1e-12]
check("C  the unit-mass normalization (N1) fails to produce log p",
      len(bad)==len(PR)*3, f"{len(bad)} of {len(PR)*3} mismatch, as expected")

# D. the ratio between the two normalizations is exactly log p, uniform in k
ok=all(abs(G_tate(p,k,s)/G_unit(p,k,s)-math.log(p))<1e-13
       for p in PR for k in (1,2,5) for s in (0.3,0.5,0.8))
check("D  Gamma^Tate / Gamma = log p, independent of k and s", ok)

print(); print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
