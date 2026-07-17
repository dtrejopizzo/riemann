#!/usr/bin/env python3
"""
Phase 10 / M10.3 — the UNIFORM lower frame bound (the de Branges / Seip sampling test).

The regularized Hodge gap = lambda_min(G), G = sine-kernel Gram of the zeros (M10.2), is positive.
RH (regularized Hodge index) <=> it is bounded BELOW uniformly in T <=> zeros are a uniform RIESZ
sequence for the band-limited / de Branges space.

The zeros' density rho(T)=log(T/2pi)/(2pi) -> infinity, so the band must grow d ~ (1/2)log(T/2pi)
to keep resolving (critical sampling, K~M).  TEST: at a FIXED sampling ratio (K/M fixed), is
lambda_min(G) T-STABLE (uniform bound, encouraging) or does it DEGRADE with height?

Stable -> a uniform lower frame bound plausibly holds (Seip-type), the regularized Hodge index is
viable.  The uniform infimum is set by the worst Lehmer cluster = the cornered target (U), now as a
de Branges Riesz lower frame bound -- where two-sided sampling tools (Beurling density + a Muckenhoupt/
separation condition tied to S(T) regularity) apply, unlike the wrong-signed pair-correlation tool.
"""
import numpy as np, mpmath as mp
import sys; sys.path.insert(0,"../../phase-7/experiments")
import carleson_band_engine as e
mp.mp.dps=20

def zeros_in(lo,hi,maxn=4000):
    g=[];n=1
    while n<=maxn:
        t=float(mp.im(mp.zetazero(n)))
        if t>hi:break
        if t>=lo:g.append(t)
        n+=1
    return np.array(g)

def reg_gap(d,T0,N,grid_pts=24000):
    sp=np.pi/d; centers=T0+sp*np.arange(-N,N+1); span=(N+35)*sp
    r=np.linspace(T0-span,T0+span,grid_pts); w=r[1]-r[0]
    S=np.sinc(d*(r[None,:]-centers[:,None])/np.pi)
    Phi=e.Phi_vec(r); A=(S*w)@(Phi[:,None]*S.T); A=(A+A.T)/2
    Li=np.linalg.inv(np.linalg.cholesky(A)); Ainv=Li.T@Li
    halfwin=N*sp; zr=zeros_in(T0-halfwin,T0+halfwin); K=len(zr)
    if K<2 or K>2*N: return None
    V=np.stack([np.sinc(d*(zr[i]-centers)/np.pi) for i in range(K)],axis=1)
    G=V.T@Ainv@V; G=(G+G.T)/2; Dg=np.sqrt(np.diag(G)); Gn=G/np.outer(Dg,Dg)
    ev=np.linalg.eigvalsh(Gn)
    zs=np.sort(zr); dens=np.log(T0/(2*np.pi))/(2*np.pi); ng=np.diff(zs)*dens
    return dict(K=K, M=2*N+1, lam_min=ev[0], min_ngap=ng.min())

if __name__=="__main__":
    print("="*80)
    print(" M10.3 — uniform lower frame bound: lambda_min(G) at FIXED sampling ratio vs height T")
    print("="*80)
    # fix sampling: choose d ~ ratio * log(T/2pi)/2 so K/M ~ const (~0.8, under-critical)
    ratio=1.25
    print(f" band d = {ratio} * (1/2)log(T/2pi)  (critical-ish, K just under M); N=10")
    print("\n     T0       d     K/M       reg.gap lam_min(G)   tightest norm.gap")
    for T0 in [50.0,100.0,300.0,1000.0,3000.0]:
        d=ratio*0.5*np.log(T0/(2*np.pi))
        res=reg_gap(d,T0,N=10)
        if res is None:
            print(f"   {T0:7.0f}  {d:5.2f}   (skip)"); continue
        print(f"   {T0:7.0f}  {d:5.2f}   {res['K']}/{res['M']}      {res['lam_min']:.4f}            {res['min_ngap']:.3f}")
    print("\n"+"-"*80)
    print(" READ: if lambda_min(G) is roughly T-STABLE at fixed sampling ratio, a UNIFORM lower frame")
    print(" bound plausibly holds in this range -> the regularized Hodge index is viable; downward dips")
    print(" track the tightest pair (Lehmer).  The uniform infimum = worst Lehmer cluster = (U), now as")
    print(" a de Branges RIESZ lower frame bound.  NEW HANDLE: Seip's frame theorem ties this to a")
    print(" Muckenhoupt/Helson-Szego (A_2) condition on E ~ xi, i.e. to the REGULARITY of S(T) =")
    print(" arg zeta -- which has UNCONDITIONAL partial control (Selberg: S(T)=O(log T), moments).")
    print(" That is a two-sided tool, not the wrong-signed pair-correlation upper bound.")
    print("="*80)
