#!/usr/bin/env python3
# ======================================================================================
# Phase 71 / E71.2 -- convergence as an RH DETECTOR.
#
# E71.1 established: sp(H) is real by pure algebra (off MW-1); an off-line zero cannot appear
# as a complex eigenvalue -- it can only DEGRADE convergence sp(H_x) -> {zeros of ζ}.
#
# TEST: for true ζ vs ζ+planted-off-line, measure the convergence of the k-th real eigenvalue
# to the k-th Riemann zero γ_k as N grows at fixed λ. The discriminating question:
#   * true ζ:            error(N) -> 0            (converges)
#   * ζ + off-line zero: error(N) floors > 0 near the planted height (STALLS) ?
#
# If the planted case stalls where ζ converges, CONVERGENCE IS A LIVE RH-DETECTOR on the one
# front that is not the positivity wall. If it converges anyway, the construction is blind.
# ======================================================================================
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
np.set_printoptions(precision=4,suppress=True,linewidth=140)

GAMMA=0.5772156649015329; LOG4PI=np.log(4*np.pi)
ZEROS=np.array([14.134725,21.022040,25.010858,30.424876,32.935062,37.586178,40.918719,
                43.327073,48.005151,49.773832])

def make_q(m,n,L):
    if m==n: return lambda y: 2*(1-y/L)*np.cos(2*np.pi*n*y/L) if 0<=y<=L else 0.0
    c=1.0/(np.pi*(n-m))
    return lambda y: (np.sin(2*np.pi*m*y/L)-np.sin(2*np.pi*n*y/L))*c if 0<=y<=L else 0.0

def QW_entry(m,n,L,lam,planted=None):
    q=make_q(m,n,L); q0=q(0.0)
    W02,_=quad(lambda y:q(y)*(np.exp(y/2)+np.exp(-y/2)),0,L,limit=200)
    def wri(y):
        if y<1e-9:
            h=1e-6; return ((q(h)-q(0.0))/h+q0/2)/2.0
        return (np.exp(y/2)*q(y)-q0)/(2*np.sinh(y))
    WRa,_=quad(wri,0,L,limit=200); WRb=q0*0.5*np.log(np.tanh(L/2))
    WR=0.5*(LOG4PI+GAMMA)*q0+WRa+WRb
    arith=0.0; maxn=int(lam*lam)
    sieve=np.ones(maxn+1,bool); sieve[:2]=False
    for p in range(2,int(maxn**0.5)+1):
        if sieve[p]: sieve[p*p::p]=False
    for p in np.nonzero(sieve)[0]:
        lp=np.log(p); pm=p; me=1
        while pm<=maxn: arith+=lp*(pm**-0.5)*q(me*lp); pm*=p; me+=1
    val=W02-WR-arith
    if planted is not None:
        g0,b,c=planted
        def qhat(sc):
            re,_=quad(lambda y:q(y)*np.real(np.cos(sc*y)),0,L,limit=200)
            im,_=quad(lambda y:q(y)*np.imag(np.cos(sc*y)),0,L,limit=200)
            return re+1j*im
        val=val+c*2*np.real(qhat(g0-1j*b))
    return val

def build_QW(lam,N,planted=None):
    L=2.0*np.log(lam); dim=2*N+1; idx=np.arange(-N,N+1); M=np.zeros((dim,dim))
    for a in range(dim):
        for b in range(a,dim):
            v=QW_entry(idx[a],idx[b],L,lam,planted); M[a,b]=v; M[b,a]=v
    return M,idx,L

def roots_of_f(xi,idx,L,smax=55):
    d=2*np.pi*idx/L; o=np.argsort(d); d=d[o]; xi=xi[o]
    f=lambda s: np.sum(xi/(s-d)); r=[]
    for i in range(len(d)-1):
        a,b=d[i]+1e-7,d[i+1]-1e-7
        if a>=b: continue
        try:
            if np.isfinite(f(a)) and np.isfinite(f(b)) and f(a)*f(b)<0:
                r.append(brentq(f,a,b,xtol=1e-11))
        except Exception: pass
    r=np.array(r); return np.sort(r[(r>1)&(r<smax)])

def matched_err(roots,targets):
    """for each target zero, nearest root; returns array of errors."""
    return np.array([np.min(np.abs(roots-z)) if len(roots) else np.nan for z in targets])

def study(tag,lam,planted,Ns):
    print(f"\n### {tag}  (λ={lam}, planted={planted}) ###")
    print(f"  {'N':>4} | " + " ".join(f"γ{k+1}={z:6.2f}" for k,z in enumerate(ZEROS[:5])))
    hist=[]
    for N in Ns:
        M,idx,L=build_QW(lam,N,planted)
        w,V=np.linalg.eigh(M); xi=V[:,0]; xi=(xi+xi[::-1])/2
        r=roots_of_f(xi,idx,L)
        errs=matched_err(r,ZEROS[:5])
        hist.append(errs)
        print(f"  {N:>4} | " + " ".join(f"{e:8.4f}" for e in errs))
    return np.array(hist)

if __name__=="__main__":
    print("="*80)
    print(" E71.2 -- convergence as RH-detector: does an off-line zero STALL convergence?")
    print("="*80)
    lam=5.0; Ns=[10,20,30,40]
    h_true=study("ζ true",lam,None,Ns)
    h_off =study("ζ + off-line b=0.30 @ g0=25",lam,(25.0,0.30,5.0),Ns)
    print("\n"+"="*80)
    print(" READING: compare error at the largest N.")
    print("  true ζ  errs@Nmax:", np.round(h_true[-1],4))
    print("  planted errs@Nmax:", np.round(h_off[-1],4))
    print("  If planted errors near g0=25 (γ3=25.01) FLOOR while true -> 0: convergence is a")
    print("  LIVE detector on the non-positivity front. If both -> 0: blind.")
    print("="*80)
