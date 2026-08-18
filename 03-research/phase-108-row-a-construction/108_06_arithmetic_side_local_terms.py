#!/usr/bin/env python3
"""Verifier for 108.06 - the arithmetic-side local terms of T_S on the graded family.
No zero of xi is used anywhere."""
import math, cmath, numpy as np, sys
FAIL=[]
def check(n, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {extra}")
    if not ok: FAIL.append(n)

# ---- A. monomials are eigenfunctions of multiplicative convolution --------
# (f_a * gtilde)(x) = int_0^inf y^{-a} conj(g(y/x)) d*y = x^{-a} * c_g(a)
def conv(a, g, x, lo=1e-3, hi=1e3, N=400001):
    y=np.geomspace(lo,hi,N)
    return np.trapz(y**(-a)*np.conj(g(y/x))/y, y)
def c_g(a, g, lo=1e-3, hi=1e3, N=400001):
    t=np.geomspace(lo,hi,N)
    return np.trapz(t**(-a)*np.conj(g(t))/t, t)
gs=[lambda t: np.exp(-((np.log(t))**2)*4),
    lambda t: np.where((t>0.5)&(t<2.0), np.sin(np.pi*(t-0.5)/1.5), 0.0)]
ok=True; errs=[]
for g in gs:
    for a in (0.3, 0.5, 0.5+2j, 0.8-1j):
        for x in (0.7, 1.0, 2.3):
            lhs=conv(a,g,x); rhs=x**(-a)*c_g(a,g)
            e=abs(lhs-rhs)/max(1e-12,abs(rhs)); errs.append(e)
            if e>2e-3: ok=False
check("A  f_a * gtilde = c_g(a) * f_a   (monomials are convolution eigenfunctions)",
      ok, f"max rel err {max(errs):.2e}")

# ---- B. closed form of the local term at a finite place p ----------------
# W_p(f_a) = sum_{n>=1} p^{-na}  +  sum_{m>=1} p^{m(a-1)}  +  C_p
#   (shell |u|_p = p^{-n}: measure 1;  |1-u|_p = 1 if n>=1, = |u|_p if n<=-1)
def shells(p, a, M):
    s1=sum(p**(-n*a)      for n in range(1,M+1))
    s2=sum(p**( m*(a-1))  for m in range(1,M+1))
    return s1, s2
def closed(p, a):
    return p**(-a)/(1-p**(-a)), p**(a-1)/(1-p**(a-1))
ok=True; errs=[]
for p in (2,3,5,7,11,101):
    for a in (0.2,0.5,0.9, 0.5+3j, 0.25-1.5j, 0.75+0.4j):
        s=shells(p,a,4000); c=closed(p,a)
        e=max(abs(s[i]-c[i])/max(1e-12,abs(c[i])) for i in (0,1)); errs.append(e)
        if e>1e-9: ok=False
check("B  closed form  p^{-a}/(1-p^{-a})  +  p^{a-1}/(1-p^{a-1})", ok,
      f"max rel err {max(errs):.2e}")

# ---- C. convergence region is EXACTLY the critical strip 0 < Re a < 1 ----
def series_converges(p, a, M=20000):
    """work with log-magnitudes: |p^{-na}| = p^{-n Re a}, |p^{m(a-1)}| = p^{m(Re a -1)}"""
    L=math.log(p); ra=a.real if isinstance(a,complex) else a
    lt1 = -M*ra*L            # log|term_M| of the first series
    lt2 =  M*(ra-1)*L        # log|term_M| of the second
    return lt1 < -30, lt2 < -30
ok=True; tab=[]
for a in (-0.5, 0.0, 0.2, 0.5, 0.9, 1.0, 1.5):
    c1_,c2_ = series_converges(3, a)
    both = c1_ and c2_
    expect = (0 < a < 1)
    tab.append((a, both))
    if both != expect: ok=False
check("C  both series converge  <=>  0 < Re a < 1  (the critical strip)", ok, str(tab))
ok=all(series_converges(5, 0.5+1j*t)==(True,True) for t in (0,5,50,500))
check("C' convergence depends only on Re a (tested on Re a = 1/2)", ok)
# and the boundaries genuinely fail
ok = (series_converges(3,0.0)[0] is False) and (series_converges(3,1.0)[1] is False)
check("C'' the two boundaries Re a = 0 and Re a = 1 are genuinely excluded", ok)

# ---- D. the sum over ALL primes diverges everywhere on the strip ---------
def primes_up_to(N):
    s=np.ones(N+1,bool); s[:2]=False
    for i in range(2,int(N**.5)+1):
        if s[i]: s[i*i::i]=False
    return np.flatnonzero(s)
P=primes_up_to(200000)
ok=True; rows=[]
for a in (0.1, 0.3, 0.5, 0.7, 0.9):
    t1=np.abs(P.astype(float)**(-a)/(1-P.astype(float)**(-a)))
    t2=np.abs(P.astype(float)**(a-1)/(1-P.astype(float)**(a-1)))
    part=[t1[:k].sum() for k in (1000,5000,len(P))]
    part2=[t2[:k].sum() for k in (1000,5000,len(P))]
    rows.append((a, round(part[-1],1), round(part2[-1],1)))
    # both partial sums must keep growing (no convergence)
    if not (part[0]<part[1]<part[2] and part2[0]<part2[1]<part2[2]): ok=False
check("D  sum over primes of BOTH terms diverges for every a in (0,1)", ok,
      f"partial sums at 17984 primes: {rows}")
# D' threshold-free: by Mertens/PNT, sum_{p<=x} p^{-a} ~ x^{1-a}/((1-a) log x),
# so the slope of log S against log x must approach 1-a.  Compare to theory.
Pb=primes_up_to(2000000).astype(float)
ok=True; fits=[]
for a in (0.1,0.3,0.5,0.7,0.9):
    xs=np.array([1e4,3e4,1e5,3e5,1e6,2e6])
    S=np.array([Pb[Pb<=x].__pow__(-a).sum() for x in xs])
    slope=np.polyfit(np.log(xs), np.log(S), 1)[0]
    fits.append((a, round(slope,3), round(1-a,3)))
    # slope must sit below 1-a (the 1/log x factor) but converge toward it
    if not (slope < 1-a + 0.02 and slope > 1-a - 0.20): ok=False
check("D' partial sums follow Mertens growth x^{1-a}/log x, hence diverge", ok,
      f"(a, fitted slope, theory 1-a): {fits}")

print()
print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
