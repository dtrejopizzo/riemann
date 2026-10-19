#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — high-precision CCM (mpmath).  Convergence baseline for ζ (RH-true).
#
# E4 (float64) reproduced the zeros to 1e-15 but degrades at large N (machine limit).
# To measure convergence RATES reliably (Link 2a: N->inf ; 2b: lambda->inf)
# high precision is needed. Here the faithful CCM construction is repeated in mpmath, measuring
#   err_1(λ,N) = |root_1(λ,N) - γ_1|     with γ_1 = 14.134725141734693790...
# as a function of N (at fixed λ) and of λ (at fixed N). This curve is the RH-true BASELINE
# against which L_DH (RH-false) is compared in E5.
#
# Construction (identical to E4, eq 3.13-3.16 CCM 2511.22755), in mpmath:
#   QW[m,n] = W02#(F) - WR#(F) - Σ_p Wp#(F),  F=q(U_m,U_n)∘log
#   eigenvalues = roots of f(s)=Σ_k ξ_k/(s-2πk/L), ξ=eigenvector of the smallest eigenvalue.
# ======================================================================================
import mpmath as mp
mp.mp.dps = 40

GAMMA = mp.euler
LOG4PI = mp.log(4*mp.pi)

def q_func(m,n,L):
    if m==n:
        return lambda y: 2*(1-y/L)*mp.cos(2*mp.pi*n*y/L)
    c=1/(mp.pi*(n-m))
    return lambda y: (mp.sin(2*mp.pi*m*y/L)-mp.sin(2*mp.pi*n*y/L))*c

def QW_entry(m,n,L,lam):
    q=q_func(m,n,L); q0=q(mp.mpf(0))
    W02=mp.quad(lambda y: q(y)*(mp.e**(y/2)+mp.e**(-y/2)), [0,L])
    def wr_int(y):
        if y<mp.mpf('1e-12'):
            h=mp.mpf('1e-8'); qp=(q(h)-q0)/h
            return (qp+q0/2)/2
        return (mp.e**(y/2)*q(y)-q0)/(2*mp.sinh(y))
    WRa=mp.quad(wr_int,[0,L])
    WRb=q0*mp.log(mp.tanh(L/2))/2
    WR=(LOG4PI+GAMMA)*q0/2 + WRa + WRb
    arith=mp.mpf(0); maxn=int(lam*lam)
    sieve=[True]*(maxn+1)
    for i in range(2,int(maxn**0.5)+1):
        if sieve[i]:
            for j in range(i*i,maxn+1,i): sieve[j]=False
    for p in range(2,maxn+1):
        if sieve[p]:
            lp=mp.log(p); pm=p; me=1
            while pm<=maxn:
                arith+=lp*(mp.mpf(pm)**mp.mpf('-0.5'))*q(me*lp)
                pm*=p; me+=1
    return W02-WR-arith

def lowest_xi(lam,N):
    L=2*mp.log(lam); dim=2*N+1; idx=list(range(-N,N+1))
    M=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            v=QW_entry(idx[a],idx[b],L,lam); M[a,b]=v; M[b,a]=v
    E,V=mp.eigsy(M)
    # menor autovalor
    jmin=min(range(dim),key=lambda j:E[j])
    xi=[V[i,jmin] for i in range(dim)]
    return xi,idx,L,E[jmin]

def root_near(xi,idx,L,target):
    d=[2*mp.pi*k/L for k in idx]
    f=lambda s: mp.fsum([xi[i]/(s-d[i]) for i in range(len(d))])
    # bracket around target between consecutive poles
    ds=sorted(d)
    lo=max([x for x in ds if x<target], default=target-1)
    hi=min([x for x in ds if x>target], default=target+1)
    a,b=lo+mp.mpf('1e-9'),hi-mp.mpf('1e-9')
    try:
        if f(a)*f(b)<0:
            return mp.findroot(f,(a+b)/2,solver='bisect',tol=mp.mpf('1e-30'))
    except Exception: pass
    try: return mp.findroot(f,target)
    except Exception: return None

if __name__=="__main__":
    g1=mp.mpf('14.134725141734693790')
    print("="*70)
    print(" High-precision CCM: convergence of root 1 to γ_1 (RH-true ζ)")
    print(f" γ_1 = {g1}")
    print("="*70)
    print("\n Eslabon 2a: N->inf a λ=3.7 fijo (primos<=13)")
    for N in [6,8,10,14,18]:
        xi,idx,L,eps=lowest_xi(mp.mpf('3.7'),N)
        r=root_near(xi,idx,L,g1)
        err=abs(r-g1) if r is not None else None
        print(f"   N={N:2d}: raiz_1={mp.nstr(r,18)}  |err|={mp.nstr(err,4) if err else 'NA'}")
    print("\n Eslabon 2b: λ creciente a N=14 fijo")
    for lam in ['2.5','3.7','5.0','7.0']:
        xi,idx,L,eps=lowest_xi(mp.mpf(lam),14)
        r=root_near(xi,idx,L,g1)
        err=abs(r-g1) if r is not None else None
        print(f"   λ={lam} (p<={int(float(lam)**2)}): |err_1|={mp.nstr(err,4) if err else 'NA'}")
