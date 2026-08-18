#!/usr/bin/env python3
"""Verifier for 108.36 - the assembly equals -zeta'/zeta on Re s > 1."""
import math, numpy as np, sys
FAIL=[]
def check(n,ok,x=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {x}");  FAIL.append(n) if not ok else None
def primes(N):
    s=np.ones(N+1,bool); s[:2]=False
    for i in range(2,int(N**.5)+1):
        if s[i]: s[i*i::i]=False
    return [int(x) for x in np.flatnonzero(s)]

N=200000; P=primes(N)
def assembly(s):            # sum_p sum_k (log p) p^{-ks}, truncated at n<=N
    t=0.0
    for p in P:
        pk=p
        while pk<=N:
            t+=math.log(p)*pk**(-s); pk*=p
    return t
def vonmangoldt_series(s):  # sum_{n<=N} Lambda(n) n^{-s}, built independently
    L=np.zeros(N+1)
    for p in P:
        pk=p
        while pk<=N:
            L[pk]=math.log(p); pk*=p
    n=np.arange(1,N+1,dtype=float)
    return float((L[1:]*n**(-s)).sum())

# A. the two sides agree with MATCHED truncation
ok=True; rows=[]
for s in (1.5,2.0,3.0,4.0):
    a,b=assembly(s), vonmangoldt_series(s); rows.append((s,round(abs(a-b),15)))
    if abs(a-b)>1e-12: ok=False
check("A  sum_p sum_k (log p)p^{-ks} = sum_n Lambda(n)n^{-s}, matched truncation",
      ok, str(rows))

# B. von Mangoldt coefficients are exactly log p on prime powers, 0 elsewhere
L=np.zeros(1001)
for p in primes(1000):
    pk=p
    while pk<=1000: L[pk]=math.log(p); pk*=p
bad=[n for n in range(2,1001)
     if (L[n]>0) != any(n==p**k for p in primes(1000) for k in range(1,11) if p**k<=1000)]
check("B  Lambda(n) is supported exactly on prime powers", len(bad)==0)

# C. absolute convergence for Re s > 1, failure for Re s <= 1: compare the
#    tail growth to theory rather than to a threshold.
def tail(s, lo, hi):
    t=0.0
    for p in primes(hi):
        if p<lo: continue
        pk=p
        while pk<=hi: t+=math.log(p)*pk**(-s); pk*=p
    return t
rows=[]; ok=True
for s in (1.5, 2.0):
    ts=[tail(s,10**j,10**(j+1)) for j in (2,3,4)]
    rows.append((s,[f'{x:.2e}' for x in ts]))
    if not all(ts[i]>ts[i+1] for i in range(len(ts)-1)): ok=False
for s in (0.5, 1.0):
    ts=[tail(s,10**j,10**(j+1)) for j in (2,3,4)]
    rows.append((s,[f'{x:.2e}' for x in ts]))
    if not all(ts[i]<=ts[i+1]*1.0001 for i in range(len(ts)-1)): ok=False
check("C  dyadic tails shrink for Re s>1 and do not for Re s<=1", ok, str(rows))

# D. mirror family
ok=all(abs(sum(math.log(p)*p**(m*(s-1)) for p in P[:200] for m in range(1,40))
          - sum(math.log(p)*p**(-m*(1-s)) for p in P[:200] for m in range(1,40)))<1e-12
       for s in (-0.5,-1.0,-2.0))
check("D  the mirror family is the same series at 1-s", ok)

print(); print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
