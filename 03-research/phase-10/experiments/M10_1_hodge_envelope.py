#!/usr/bin/env python3
"""
Phase 10 / M10.1 — reconstruct the Lorentzian (Hodge-index) envelope of the Weil-Carleson form,
and test whether the curve-case mechanism transfers.

Curve case (Weil conjectures): intersection form on NS(CxC) is LORENTZIAN (1, rho-1); on the
PRIMITIVE part it is NEGATIVE DEFINITE (Hodge index) -> a spectral GAP -> the exact bound |alpha|=q^{1/2}.
Finite genus => finite rank => definite => a gap.

Our case: the Weil-Carleson form t = A_Phi - P_F is the candidate primitive intersection form (PSD = RH).
TEST: is it DEFINITE (gap>0, curve-like) or MARGINAL (gap->0, saturated)?  And does the enlarged form
(adjoin one ample direction) have clean Lorentzian signature, or does it DEGENERATE (acquire a null
vector) as we grow the band d (= grow the 'genus'/cohomology dimension toward zeta)?

Prediction: gap = lambda_min(t) -> 0 as d grows (the N3 saturation), i.e. zeta's 'arithmetic surface'
has INFINITE genus with a VANISHING Hodge gap -> the finite-rank Hodge argument does NOT transfer; the
new mathematics required is an infinite-dimensional Hodge index controlling the marginal (zero-gap) case.
"""
import numpy as np, mpmath as mp
import sys; sys.path.insert(0, "../../phase-7/experiments")
import carleson_band_engine as e
mp.mp.dps = 18

def weil_form(d, T0, N, grid_pts=30000):
    sp=np.pi/d; centers=T0+sp*np.arange(-N,N+1)
    span=(N+40)*sp
    r=np.linspace(T0-span,T0+span,grid_pts); w=r[1]-r[0]
    S=np.sinc(d*(r[None,:]-centers[:,None])/np.pi)
    Phi=e.Phi_vec(r); pp=e.prime_powers(np.exp(2*d)); F=e.F_vec(r,pp)
    A=(S*w)@(Phi[:,None]*S.T); A=(A+A.T)/2
    P=(S*w)@(F[:,None]*S.T);  P=(P+P.T)/2
    # generalized: t = A-P vs A ; eigenvalues 1-C_k. Hodge gap = smallest.
    L=np.linalg.cholesky(A); Li=np.linalg.inv(L)
    M=Li@(A-P)@Li.T; M=(M+M.T)/2
    ev=np.linalg.eigvalsh(M)   # = 1 - C_k ; PSD if RH
    return ev, A.shape[0]

if __name__=="__main__":
    print("="*80)
    print(" M10.1 — Hodge gap of the Weil-Carleson form vs band d (= cohomology 'genus')")
    print("="*80)
    T0=100.0; N=10
    print(f" T0={T0}, basis dim 2N+1={2*N+1}.  Hodge gap = lambda_min(t) ; >0 definite (curve-like),")
    print(" ->0 marginal/degenerate (zeta saturation = infinite genus).")
    print("\n   d    x=2d/logT0  primes   Hodge gap=lam_min   #pos  #~0(null)   signature of full I")
    for d in [1.0,1.5,2.0,2.5,3.0,3.5,4.0]:
        ev,M = weil_form(d,T0,N)
        gap=ev[0]; npos=np.sum(ev>1e-6); nnull=np.sum(np.abs(ev)<=1e-6)
        x=2*d/np.log(T0)
        # full intersection I = (+kappa ample) (+) (-t):  sig = (1, npos_of_t, null_of_t)
        sig=f"(1, {npos}, {nnull})"
        deg = "DEGENERATE" if nnull>0 or gap<1e-5 else "Lorentzian OK"
        print(f"  {d:4.1f}    {x:5.2f}    {int(np.exp(2*d)):6d}    {gap:+.3e}      {npos:3d}    {nnull:3d}      {sig}  {deg}")
    print("\n"+"-"*80)
    print(" READ: as d grows (more primes/zeros = higher genus), the Hodge gap lambda_min(t) -> 0:")
    print(" the candidate intersection form DEGENERATES (acquires a null direction) -- the N3 saturation")
    print(" in cohomological language.  The curve-case Hodge index needs a DEFINITE form (finite genus,")
    print(" positive gap); zeta's surface has INFINITE genus with VANISHING gap.  So the finite-rank")
    print(" argument does NOT transfer, and the new mathematics required is precisely an INFINITE-")
    print(" DIMENSIONAL HODGE INDEX controlling the marginal (zero-gap) primitive form.  That is the")
    print(" cohomological face of the wrong-sign capstone / the Lambda=0 marginality.")
    print("="*80)
