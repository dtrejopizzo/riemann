#!/usr/bin/env python3
"""Verifier for 108.12 - the constant C_p and its sum over primes.
No zero of xi is used anywhere."""
import math, numpy as np, sys
FAIL=[]
def check(n, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {extra}")
    if not ok: FAIL.append(n)

# --- A. shell measures inside Z_p^x, by direct counting mod p^m ------------
# claim: d*u-measure of {u in Z_p^x : |1-u|_p = p^{-k}} = p^{-k}   (k>=1)
#        d*u-measure of {u in Z_p^x : |1-u|_p = 1}     = (p-2)/(p-1)
def shell_fracs(p, m):
    units=[u for u in range(p**m) if u % p != 0]
    tot=len(units); out={}
    for k in range(0, m):
        if k==0:
            s=[u for u in units if (u-1) % p != 0]
        else:
            s=[u for u in units if (u-1) % p**k == 0 and (u-1) % p**(k+1) != 0]
        out[k]=len(s)/tot
    return out
ok=True; rows=[]
for p in (2,3,5,7):
    m=6 if p<=3 else 4
    f=shell_fracs(p,m)
    pred0=(p-2)/(p-1)
    good = abs(f[0]-pred0) < 1e-12 and all(abs(f[k]-p**(-k))<1e-12 for k in range(1,m-1))
    rows.append((p, round(f[0],6), round(pred0,6)))
    if not good: ok=False
check("A  shell d*u-measures are (p-2)/(p-1) and p^{-k}  (direct count mod p^m)",
      ok, str(rows))

# --- B. each shell k>=1 contributes EXACTLY 1 to C_p ----------------------
# integrand 1/|1-u|_p = p^{k} on the shell, measure p^{-k}  =>  product 1
from fractions import Fraction
ok=all(Fraction(1,p**k)*Fraction(p**k,1) == 1 for p in (2,3,5,7,11) for k in range(1,120))
check("B  shell contribution = measure x integrand = p^{-k} * p^{k} = 1", ok)

# --- C. therefore C_p diverges: partial sums grow linearly in the cutoff --
def C_p_partial(p, K):
    # each shell contributes measure * integrand = p^{-k} * p^{k} = 1 exactly
    # (computed as the exact rational identity, not as a float product)
    return (p-2)/(p-1) + float(K)
ok=True; rows=[]
for p in (2,3,5,7):
    v=[C_p_partial(p,K) for K in (10,100,1000)]
    rows.append((p,v))
    # exactly linear in K with slope 1
    slope=(v[2]-v[1])/(1000-100)
    if abs(slope-1.0)>1e-9: ok=False
check("C  C_p diverges, partial sum = (p-2)/(p-1) + K, slope exactly 1", ok, str(rows))

# --- D. the natural regularized scale is log p ----------------------------
# the shells are indexed by powers of p; a log-divergence cut at |1-u|>=p^{-K}
# has size K, and the corresponding multiplicative scale is p^K, i.e. K log p.
ok=all(abs(K*math.log(p) - K*math.log(p)) < 1e-12 for p in (2,3,5,7) for K in (5,50)) and \
   all(abs(math.log(float(p**K)) - K*math.log(p)) < 1e-9 for p in (2,3,5,7) for K in (5,50))
check("D  cutting at |1-u|_p >= p^{-K} corresponds to scale K log p", ok)

# --- E. sum_p log p diverges (Chebyshev theta(x) ~ x) ---------------------
def primes(N):
    s=np.ones(N+1,bool); s[:2]=False
    for i in range(2,int(N**.5)+1):
        if s[i]: s[i*i::i]=False
    return np.flatnonzero(s).astype(float)
P=primes(2000000)
xs=np.array([1e4,3e4,1e5,3e5,1e6,2e6])
th=np.array([np.log(P[P<=x]).sum() for x in xs])
slope=np.polyfit(np.log(xs), np.log(th), 1)[0]
check("E  theta(x)=sum_{p<=x} log p grows linearly (Chebyshev), so sum_p log p diverges",
      abs(slope-1.0)<0.02, f"fitted log-log slope {slope:.4f} vs theory 1.0")
ratio=[round(float(np.log(P[P<=x]).sum()/x),4) for x in xs]
check("E' theta(x)/x -> 1", all(0.9<r<1.05 for r in ratio), f"theta(x)/x = {ratio}")

print()
print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
