#!/usr/bin/env python3
"""Verifier for 108.34 - the shell functional and its pairing formula."""
import math, sys
FAIL=[]
def check(n,ok,x=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {x}");  FAIL.append(n) if not ok else None
def G(p,k,h0): return (p**min(k,0))*h0(p**k)

# A. linearity
ok=all(abs(G(p,k,lambda x:2*x**-0.5+3*x**-0.7)
          -(2*G(p,k,lambda x:x**-0.5)+3*G(p,k,lambda x:x**-0.7)))<1e-13
       for p in (2,3,5,7) for k in (-3,-1,1,2,4))
check("A  Gamma_{p,k} is linear in h_0", ok)

# B. it is a scaled Dirac evaluation at p^k
ok=all(abs(G(p,k,lambda x,c=c: c*(1.0 if abs(x-p**k)<1e-9 else 0.0))
          - (p**min(k,0))*c) < 1e-13
       for p in (2,3) for k in (-2,1,3) for c in (1.0,-2.5))
check("B  Gamma_{p,k} = p^{min(k,0)} * delta_{p^k}", ok)

# C. pairing with the graded family, both shell families
ok=True; 
for p in (2,3,5,7,11):
    for s in (0.5, 0.3, 0.8, 0.5+2j, 0.25-1j):
        for k in (1,2,3,5,8):
            if abs(G(p,k,lambda x,s=s: x**(-s)) - p**(-k*s))>1e-11: ok=False
        for k in (-1,-2,-3,-5):
            m=-k
            if abs(G(p,k,lambda x,s=s: x**(-s)) - p**(m*(s-1)))>1e-11: ok=False
check("C  pairing: Gamma_{p,k}(f_s)=p^{-ks} (k>=1) and p^{m(s-1)} (k=-m<=-1)", ok)

# D. resumming the two shell families reproduces 108_06 Thm 3.1
ok=True
for p in (2,3,5,7):
    for s in (0.3,0.5,0.8):
        a=sum(p**(-k*s) for k in range(1,4000))
        b=sum(p**(m*(s-1)) for m in range(1,4000))
        if abs(a-p**(-s)/(1-p**(-s)))>1e-12: ok=False
        if abs(b-p**(s-1)/(1-p**(s-1)))>1e-12: ok=False
check("D  resummation gives 108_06 Thm 3.1's two closed forms", ok)

print(); print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
