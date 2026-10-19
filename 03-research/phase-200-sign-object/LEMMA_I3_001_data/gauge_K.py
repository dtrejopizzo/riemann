# P2_GAUGE_RADICAL_001: gauge tails Φ_φ (φ ∈ 𝒢_T, even, supp [-1/λ,1/λ], C², φ(0)=∫φ=0) and the complete line form.
# Φ_φ(x)=e^{x/2}Σ_{n≥1}φ(n e^x), supported in x≤-T.  In u=e^x: c(log n)=√n ∫ S(u)S(nu)du, S(u)=Σ_k φ(ku).
# Mellin: Φ̂(τ)=ζ(s)φ̃(s), s=1/2+iτ, φ̃(s)=∫_0^{1/λ}φ(v)v^{s-1}dv;  A=Mellin@1, B=Mellin@0.
# 𝒲_a[Φ]=(1/2π)∫m|Φ̂|² - Σ_n 2a(n)/√n c(log n) + 2AB. NUMÉRICO (float64 quadrature + mpmath ζ).
import numpy as np, mpmath as mp, sys, json
from scipy.special import digamma
mu=int(sys.argv[1]); K=int(sys.argv[2]) if len(sys.argv)>2 else 10
lam=np.sqrt(mu); T=np.log(mu)/2
# raw basis in x=λ|v|: p_k(x)=x^2(1-x^2)^3 x^{2k}, k=0..K-1; polynomial coefficient arrays (in x)
def raw(k):
    c=np.zeros(2*K+12); base=np.polynomial.polynomial.polymul([0,0,1],np.polynomial.polynomial.polypow([1,0,-1],3))
    c[2*k:2*k+len(base)]+=base; return c
R=np.array([raw(k) for k in range(K)])          # K x deg
deg=R.shape[1]
mom=np.array([sum(R[k,j]/(j+1) for j in range(deg)) for k in range(K)])/lam   # ∫_0^{1/λ}
# L2(-1/λ,1/λ) Gram of raw basis: 2/λ ∫_0^1 p_k p_l dx
Gm=np.array([[2/lam*sum(np.convolve(R[k],R[l])[j]/(j+1) for j in range(2*deg-1)) for l in range(K)] for k in range(K)])
# subspace ∫φ=0 : orthonormal basis (generalised) of {c: mom·c=0} w.r.t Gm
_,_,Vt=np.linalg.svd(mom[None,:]); Z=Vt[1:].T
Gz=Z.T@Gm@Z; e,U=np.linalg.eigh(Gz); Bc=Z@U@np.diag(e**-0.5)  # columns: gauge ON basis coefficients (in raw basis)
Mg=Bc.shape[1]
C=Bc.T@R            # Mg x deg polynomial coefficients in x of ON gauge basis
# --- S_k(u) on uniform grid u_i=iδ, i=0..N, u_N=1/λ
N=int(sys.argv[3]) if len(sys.argv)>3 else 400000
delta=1/(lam*N); i=np.arange(N+1)
S=np.zeros((Mg,N+1))
P=np.polynomial.polynomial
for n in range(1,N+1):
    m=N//n
    x=(n*i[1:m+1])/N   # λ n u
    if m<1: break
    S[:,1:m+1]+=np.array([P.polyval(x,C[k]) for k in range(Mg)])
# trapezoid weights
def corr(n):
    m=N//n
    if m<1: return np.zeros((Mg,Mg))
    a=S[:,:m+1]; b=S[:,0:n*m+1:n]
    w=np.full(m+1,delta); w[0]=w[-1]=delta/2
    X=(a*w)@b.T; return np.sqrt(n)*(X+X.T)/2
def mangoldt(n):
    for p in range(2,int(n**0.5)+1):
        if n%p==0:
            m=n
            while m%p==0: m//=p
            return (p,np.log(p)) if m==1 else (p,0.0)
    return (n,np.log(n))
NC=int(sys.argv[4]) if len(sys.argv)>4 else 20000
atoms={}
for n in range(2,NC):
    p,L=mangoldt(n)
    if L>0: atoms[n]=(p,L,corr(n))
c0=corr(1)
# --- Mellin side
mp.mp.dps=20
def phit(s,k):  # φ̃_k(s)=λ^{-s} Σ_j C[k,j]/(j+s)
    return lam**(-s)*sum(C[k,j]/(j+s) for j in range(deg) if C[k,j]!=0)
taus=np.concatenate([np.linspace(0,50,20001)[:-1],np.linspace(50,600,22001)])
wt=np.zeros(len(taus)); 
for seg in [(0,20000),(20000,len(taus))]:
    a,b=seg; h=taus[a+1]-taus[a]; wt[a:b]+=h; wt[a]-=h/2; wt[b-1]-=h/2
zeta=np.array([complex(mp.zeta(0.5+1j*t)) for t in taus])
mm=np.real(digamma(0.25+0.5j*taus))-np.log(np.pi)
Fh=np.array([[zeta[j]*phit(0.5+1j*taus[j],k) for j in range(len(taus))] for k in range(Mg)])
arch=np.real((Fh*(wt*mm))@Fh.conj().T)/np.pi
pars=np.real((Fh*wt)@Fh.conj().T)/np.pi      # should equal c0 (Parseval)
# A=Mellin@1: ζ(s)φ̃(s) → φ̃'(1) (φ̃(1)=∫φ/... =0); B=Mellin@0: ζ(0)φ̃(0)
A=np.array([float(mp.diff(lambda s: phit(s,k),1)) for k in range(Mg)])
B=np.array([-0.5*float(phit(mp.mpf(0)+0j,k).real) if False else -0.5*float(lam**0*sum(C[k,j]/j for j in range(1,deg))) for k in range(Mg)])
AB=np.outer(A,B)+np.outer(B,A)
combL=sum(2*L/np.sqrt(n)*X for n,(p,L,X) in atoms.items())
WL=arch-combL+AB
res=dict(mu=mu,Mg=Mg,N=N,NC=NC,parseval_err=float(np.abs(pars-c0).max()/np.abs(c0).max()),
  WLambda_norm=float(np.abs(np.linalg.eigvalsh(WL)).max()),arch_norm=float(np.abs(np.linalg.eigvalsh(arch)).max()),
  comb_norm=float(np.abs(np.linalg.eigvalsh(combL)).max()))
np.savez(f'gaugeK{K}_mu{mu}.npz',arch=arch,c0=c0,AB=AB,combL=combL,atoms_n=np.array(list(atoms)),
  atoms=np.array([X for (p,L,X) in atoms.values()]),C=C)
print(json.dumps(res,indent=1))
