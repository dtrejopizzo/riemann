#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — E6: the convergence HORIZON H(λ).  Direct attack on Link 2.
#
# Goal (mapping to RH, Link 2): characterize the convergence ξ̂_{λ,N} -> Ξ.
#   2a (N->inf, λ fixed): each zero has a λ-FLOOR; large N saturates it.
#   2b (λ->inf): the λ-floor drops and the HORIZON of resolved zeros H(λ) grows.
# CCM phenomenon: 1st zero ~1e-18 with primes<=13, but precision DEGRADES with height
# (paper: ~1e-3 for the 50th zero). => H(λ;ε) = height up to which zeros are within <ε.
#
# E6 measures H(λ;ε): for each λ, with N scaled to reach height ~110, count how many
# CONSECUTIVE zeros from the bottom are reproduced to <ε. Tabulate H(λ) vs λ. Growth of
# H(λ) = empirical content of 2b. (Test question: does H(λ)->inf by PNT, zero-independent?)
# ======================================================================================
import numpy as np, mpmath as mp
from scipy.optimize import brentq
mp.mp.dps=25

# reference zeta zeros (high precision)
print("loading reference zeta zeros...",flush=True)
ZJSON=[float(mp.im(mp.zetazero(k))) for k in range(1,60)]   # ~ up to height ~108

def q_func(m,n,L):
    if m==n: return lambda y: 2*(1-y/L)*np.cos(2*np.pi*n*y/L)
    c=1.0/(np.pi*(n-m))
    return lambda y: (np.sin(2*np.pi*m*y/L)-np.sin(2*np.pi*n*y/L))*c
def vonmangoldt_upto(X):
    Lam=np.zeros(X+1); s=np.ones(X+1,bool); s[:2]=False
    for p in range(2,int(X**0.5)+1):
        if s[p]: s[p*p::p]=False
    for p in np.nonzero(s)[0]:
        pk=p; lp=np.log(p)
        while pk<=X: Lam[pk]=lp; pk*=p
    return Lam
def build_QW_zeta(lam,N,tgrid):
    from scipy.special import digamma
    L=2.0*np.log(lam); idx=np.arange(-N,N+1); dim=2*N+1; d=2*np.pi*idx/L
    t=tgrid; sint=np.sin(t*L/2.0)
    den=t[None,:]-d[:,None]; den=np.where(np.abs(den)<1e-12,1e-12,den)
    Vhat=(2.0/np.sqrt(L))*sint[None,:]/den
    Omega=np.real(digamma(0.25+1j*t/2.0))-np.log(np.pi)
    dt=t[1]-t[0]
    arch=(1.0/(2*np.pi))*(Vhat*Omega[None,:])@Vhat.T*dt
    Lam=vonmangoldt_upto(int(lam*lam))
    arith=np.zeros((dim,dim))
    for a in range(dim):
        for b in range(a,dim):
            q=q_func(idx[a],idx[b],L); ss=0.0
            for npow in range(2,int(lam*lam)+1):
                if Lam[npow]: ss+=Lam[npow]*(npow**-0.5)*q(np.log(npow))
            arith[a,b]=ss; arith[b,a]=ss
    def vhat_c(s): return (2.0/np.sqrt(L))*np.sin(s*L/2.0)/(s-d)
    vp=vhat_c(0.5j); vm=vhat_c(-0.5j)
    W02=np.real(np.outer(vp,np.conj(vm))+np.outer(vm,np.conj(vp)))
    QW=arch-arith+W02
    return (QW+QW.T)/2, idx, L
def all_roots(xi,idx,L,hmax):
    d=2*np.pi*idx/L; o=np.argsort(d); d=d[o]; xi=xi[o]
    f=lambda s: np.sum(xi/(s-d)); r=[]
    for i in range(len(d)-1):
        a,b=d[i]+1e-7,d[i+1]-1e-7
        if a>=b or b<1 or a>hmax: continue
        try:
            if f(a)*f(b)<0: r.append(brentq(f,a,b,xtol=1e-12))
        except Exception: pass
    return np.array(sorted([x for x in r if 1<x<hmax]))

def horizon(lam, eps, Hmax=108):
    L=2*np.log(lam); N=int(Hmax*np.log(lam)/np.pi)+15
    tgrid=np.arange(-max(400,3*Hmax),max(400,3*Hmax),0.01)+1e-6
    QW,idx,Ln=build_QW_zeta(lam,N,tgrid)
    w,V=np.linalg.eigh(QW); xi=V[:,0]
    r=all_roots(xi,idx,Ln,Hmax)
    # count consecutive zeros resolved to <eps
    nres=0; lasth=0.0
    for z in ZJSON:
        if z>Hmax: break
        if len(r)==0: break
        e=np.min(np.abs(r-z))
        if e<eps: nres+=1; lasth=z
        else: break
    return N, nres, lasth, r

if __name__=="__main__":
    print("="*78)
    print(" E6: convergence horizon H(λ) = zeros resolved to <eps (Link 2b)")
    print("="*78)
    for eps in [1e-6, 1e-9]:
        print(f"\n--- eps={eps:.0e} ---")
        print("   λ    N    #zeros_resolved   horizon_height H(λ)")
        for lam in [2.5,3.0,3.7,5.0,7.0]:
            N,nres,lasth,r=horizon(lam,eps)
            print(f"  {lam:4.1f}  {N:3d}        {nres:3d}            {lasth:7.3f}")
    print("\n READING: if H(λ) GROWS with λ -> evidence of 2b (convergence). Its rate vs λ")
    print(" is the object to bound via PNT (prime-side, zero-independent) to close 2b -> RH.")
