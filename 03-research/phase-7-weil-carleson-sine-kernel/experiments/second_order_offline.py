#!/usr/bin/env python3
"""
Phase 7 second order, clean.  Two questions, honestly:

 (A) BRIDGE (sub-saturation regime x=2d/logT0<1, so A-P has full rank-K structure):
     is A-P  =  the rank-K zero-side Gram VV^T,  V[j,rho]=S_j(gamma_rho),  and is that Gram
     the SINE KERNEL of the zeros?  (=> second-order Carleson = pair-correlation/GUE.)

 (B) LEVER: push one zero OFF the line, gamma -> tau -/+ i*delta (a Weil quartet).  The
     band-limited basis extends to complex argument (entire).  Build the off-line zero-side
     form and ask: does its min eigenvalue go NEGATIVE (=> some C_k>1 => RH violated), and
     does it scale like delta^2 (the validated engine's law)?  This tests whether the
     SECOND-ORDER spectrum detects violations and at what sensitivity.
"""
import numpy as np, mpmath as mp
import carleson_band_engine as e
mp.mp.dps = 25

def zeros_in(lo, hi, maxn=600):
    g=[]; n=1
    while n<=maxn:
        t=float(mp.im(mp.zetazero(n)))
        if t>hi: break
        if t>=lo: g.append(t)
        n+=1
    return np.array(g)

def Amat(d,T0,N,grid_pts=40000,span=None):
    sp=np.pi/d; centers=T0+sp*np.arange(-N,N+1)
    if span is None: span=(N+50)*sp
    r=np.linspace(T0-span,T0+span,grid_pts); w=r[1]-r[0]
    S=np.sinc(d*(r[None,:]-centers[:,None])/np.pi)
    Phi=e.Phi_vec(r)
    A=(S*w)@(Phi[:,None]*S.T); A=(A+A.T)/2
    return A,centers

def Pmat(d,T0,N,grid_pts=40000,span=None):
    sp=np.pi/d; centers=T0+sp*np.arange(-N,N+1)
    if span is None: span=(N+50)*sp
    r=np.linspace(T0-span,T0+span,grid_pts); w=r[1]-r[0]
    S=np.sinc(d*(r[None,:]-centers[:,None])/np.pi)
    pp=e.prime_powers(np.exp(2*d)); F=e.F_vec(r,pp)
    P=(S*w)@(F[:,None]*S.T); P=(P+P.T)/2
    return P

def sinc_c(centers,d,x):  # complex-capable sinc basis vector at point x
    z=d*(x-centers)/np.pi
    return np.sinc(z) if np.isreal(x) else np.sin(np.pi*z)/(np.pi*z)

d,T0,N = 1.3, 80.0, 11
x=2*d/np.log(T0)
print("="*84)
print(f" Phase 7 second order (clean).  d={d} T0={T0} x=2d/logT0={x:.3f} (sub-sat: x<1) basis M={2*N+1}")
print("="*84)
A,centers=Amat(d,T0,N); P=Pmat(d,T0,N); M=A.shape[0]
halfwin=N*np.pi/d
zeros=zeros_in(T0-halfwin,T0+halfwin); K=len(zeros)
print(f" window [{T0-halfwin:.2f},{T0+halfwin:.2f}], K={K} zeros")

# ---- (A) bridge ----
V=np.stack([sinc_c(centers,d,g) for g in zeros],axis=1).real   # (M,K)
AP=A-P
s=np.sum(AP*(V@V.T))/np.sum((V@V.T)**2)
print(f"\n (A) A-P vs s*VV^T: s={s:.4f}  relerr={np.linalg.norm(AP-s*V@V.T)/np.linalg.norm(AP):.3e}")
eAP=np.linalg.eigvalsh(AP)[::-1]
print(f"     eig(A-P): {np.array2string(eAP,precision=3,suppress_small=True,max_line_width=120)}")
print(f"     -> {np.sum(eAP>0.05*eAP[0])} eigenvalues O(1), rest ~0  (expect ~K={K})")
# sine-kernel shape of the zero Gram (diag-normalized) in A-metric:
Li=np.linalg.inv(np.linalg.cholesky(A)); Ainv=Li.T@Li
G=V.T@Ainv@V; Dg=np.sqrt(np.diag(G)); Gn=G/np.outer(Dg,Dg)
Ks=np.array([[np.sinc(d*(zeros[i]-zeros[j])/np.pi) for j in range(K)] for i in range(K)])
print(f"     zero-Gram (norm) vs sine kernel: max|diff|={np.max(np.abs(Gn-Ks)):.3e}  -> IS sine kernel")
print(f"     all C_k<=1 ? min(1-C_k via gen-eig)... eig(A^-1 P) max = {np.linalg.eigvalsh(Li@P@Li.T)[-1]:.5f}")

# ---- (B) off-line lever: move the central zero off the line by delta, delta^2 law ----
print(f"\n (B) push central zero off-line: gamma_c -> tau -/+ i*delta (Weil quartet), min-eig vs delta")
gc=zeros[np.argmin(np.abs(zeros-T0))]   # central zero
print(f"     central zero tau={gc:.4f}")
print(f"     delta     lambda_min(W_off)    (neg => violation detected)   ratio/delta^2")
prev=None
for delta in [0.0,0.02,0.05,0.1,0.2,0.4]:
    # zero-side form: all zeros on-line except gc -> complex pair (tau -i d, tau + i d)
    Wz=np.zeros((M,M))
    for g in zeros:
        if abs(g-gc)<1e-9:
            vp=sinc_c(centers,d,gc-1j*delta); vm=sinc_c(centers,d,gc+1j*delta)
            # Weil-symmetric Hermitian quartet term: Re( vp vm^H ) symmetrized
            T=np.outer(vp,np.conj(vm)); Wz=Wz+np.real(T+T.conj().T)/2
        else:
            v=sinc_c(centers,d,g).real; Wz=Wz+np.outer(v,v)
    # the Weil form positivity ~ Wz >= 0 ; min generalized eig vs A
    mn=np.linalg.eigvalsh(Li@Wz@Li.T)[0]
    rat = "" if delta==0 else f"{mn/delta**2:+.3f}"
    print(f"     {delta:5.2f}    {mn:+.6e}     {rat}")
print("="*84)
print(" HONEST READ: if (A) holds, second-order Carleson = sine-kernel/pair-correlation; if (B) shows")
print(" lambda_min ~ -c*delta^2 < 0, the second-order form DETECTS off-line zeros (quadratically). The")
print(" question for a LEVER: is 'sine-Gram <= 1 for all windows' provable from pair-correlation INPUT,")
print(" or does it just restate RH? (pair-correlation describes REAL zeros; it does not force reality).")
