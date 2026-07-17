#!/usr/bin/env python3
# ======================================================================================
# Phase 71 -- CAND-1 (Zeta Spectral Triples, CCM 2025-26): is the self-adjointness
# "by construction" genuinely off the Weil-positivity wall, or is it positivity in disguise?
#
# THE FORK.  Eigenvalues of H are represented by roots of
#   f(s) = Σ_k ξ_k/(s - d_k),  d_k = 2πk/L real.
# Generic real rational functions with real poles do NOT automatically have all roots real.
# A sign-definite residue pattern would give a Herglotz/Stieltjes mechanism, which would smell like
# positivity. CCM instead advertises self-adjointness by construction. So:
#   (A) if ξ is sign-definite automatically, the reality may be a hidden positivity mechanism.
#   (B) if ξ has mixed signs but the CCM finite operator still gives real spectrum, then the route is
#       genuinely off MW-1; RH content has moved from positivity to convergence.
#
# TEST (cheap, decisive):
#   1. build QW for ζ (faithful CCM), take ground eigenvector ξ; report its sign pattern.
#   2. search f(s) for COMPLEX roots (not just real) -> are there any?
#   3. PLANT an off-line zero by adding its explicit-formula contribution to QW and re-check
#      whether ξ loses sign-definiteness / f acquires complex roots.
#
# This does NOT re-run the phase-60 convergence horizon; it isolates the REALITY MECHANISM.
# ======================================================================================
import numpy as np
from scipy.integrate import quad
np.set_printoptions(precision=4, suppress=True, linewidth=140)

GAMMA=0.5772156649015329; LOG4PI=np.log(4*np.pi)

def make_q(m,n,L):
    if m==n: return lambda y: 2*(1-y/L)*np.cos(2*np.pi*n*y/L) if 0<=y<=L else 0.0
    c=1.0/(np.pi*(n-m))
    return lambda y: (np.sin(2*np.pi*m*y/L)-np.sin(2*np.pi*n*y/L))*c if 0<=y<=L else 0.0

def QW_entry(m,n,L,lam,planted=None):
    q=make_q(m,n,L); q0=q(0.0)
    W02,_=quad(lambda y: q(y)*(np.exp(y/2)+np.exp(-y/2)),0,L,limit=200)
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
        while pm<=maxn:
            arith+=lp*(pm**-0.5)*q(me*lp); pm*=p; me+=1
    val=W02-WR-arith
    # PLANT an off-line zero pair rho = 1/2+b +/- i*g0 : its explicit-formula contribution
    # to the Weil form is  +[ h(g0-ib..) ]; here we inject the archimedean-style term for a
    # zero at height g0 with real-part offset b, i.e. add  2*Re( qhat(g0 - i*b) ) style mass.
    # Concretely a zero contributes to W(F) the term  F-hat evaluated at the zero. In this
    # basis F-hat(s) = (2/sqrt L) sin(sL/2) * Qhat(s) with Qhat_{mn}(s)=Σ.. ; we use the
    # closed q-transform: inject  c * q_hat(m,n; g0, b).
    if planted is not None:
        g0,b,c=planted
        # q_hat(s) = ∫_0^L q(y) cos(s y) dy  (even test), evaluate at complex s=g0 - i b and conj
        def qhat(scomplex):
            re,_=quad(lambda y: q(y)*np.real(np.cos(scomplex*y)),0,L,limit=200)
            im,_=quad(lambda y: q(y)*np.imag(np.cos(scomplex*y)),0,L,limit=200)
            return re+1j*im
        contrib=2*np.real(qhat(g0-1j*b))   # off-line: b>0 gives a real-part-shifted contribution
        val=val+c*contrib
    return val

def build_QW(lam,N,planted=None):
    L=2.0*np.log(lam); dim=2*N+1; idx=np.arange(-N,N+1); M=np.zeros((dim,dim))
    for a in range(dim):
        for b in range(a,dim):
            v=QW_entry(idx[a],idx[b],L,lam,planted)
            M[a,b]=v; M[b,a]=v
    return M,idx,L

def complex_roots(xi,idx,L,box=55,grid=40):
    """Search f(s)=Σ ξ_k/(s-d_k) for roots in a complex box via argument-principle-free
    sampling: find sign changes of Re,Im on a grid + polish. Report any with |Im|>tol."""
    d=2*np.pi*idx/L
    def f(s): return np.sum(xi/(s-d))
    # coarse: roots are where |f| small; scan complex grid
    xs=np.linspace(1,box,300); ys=np.linspace(-6,6,grid)
    found=[]
    from scipy.optimize import fsolve
    for yr in ys:
        for xr in xs[::5]:
            s0=xr+1j*yr
            try:
                sol=fsolve(lambda v: [np.real(f(v[0]+1j*v[1])),np.imag(f(v[0]+1j*v[1]))],
                           [xr,yr],full_output=True)
                (rx,ry),info,ier,_=sol
                if ier==1 and abs(np.sum(xi/((rx+1j*ry)-d)))<1e-6 and 1<rx<box:
                    found.append(rx+1j*ry)
            except Exception: pass
    # dedup
    uniq=[]
    for z in found:
        if not any(abs(z-u)<1e-3 for u in uniq): uniq.append(z)
    return uniq

def analyze(tag,lam,N,planted=None):
    M,idx,L=build_QW(lam,N,planted)
    w,V=np.linalg.eigh(M); xi=V[:,0]; xi=(xi+xi[::-1])/2
    npos=np.sum(xi>0); nneg=np.sum(xi<0)
    sign_definite = (npos==0 or nneg==0)
    roots=complex_roots(xi,idx,L)
    cplx=[z for z in roots if abs(z.imag)>1e-4]
    print(f"[{tag}] λ={lam} N={N}  eps_min={w[0]:+.4e}")
    print(f"    ξ sign pattern: {npos} pos, {nneg} neg  -> sign-definite={sign_definite}")
    print(f"    ξ (center 11): {xi[N-5:N+6]}")
    print(f"    complex roots of f (|Im|>1e-4): {len(cplx)}  {[np.round(z,3) for z in cplx[:6]]}")
    return sign_definite,cplx

if __name__=="__main__":
    print("="*80)
    print(" E71.1 -- CAND-1 reality mechanism: is ξ sign-definite by construction?")
    print("="*80)
    lam,N=5.0,20
    print("\n### ζ (true, RH-consistent) ###")
    sd0,cx0=analyze("zeta",lam,N,planted=None)
    print("\n### ζ + PLANTED off-line zero (b=0.25, g0=17.0) ###")
    sd1,cx1=analyze("planted",lam,N,planted=(17.0,0.25,3.0))
    print("\n### ζ + PLANTED off-line zero (b=0.40, g0=17.0, stronger) ###")
    sd2,cx2=analyze("planted2",lam,N,planted=(17.0,0.40,8.0))
    print("\n"+"="*80)
    print(" READING")
    print("  If ζ: ξ sign-definite & no complex roots, but PLANTED breaks sign-definiteness")
    print("        / creates complex roots  -> reality is a POSITIVITY condition (MW-1 disguise).")
    print("  If ζ: ξ NOT sign-definite yet all roots still real -> a genuine non-positivity")
    print("        reality mechanism (CAND-1 truly off the wall).")
    print("="*80)
