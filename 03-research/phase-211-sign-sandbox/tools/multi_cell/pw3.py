# float feasibility: R=3 complete form with truncated symbol min(m,M) in piecewise-Legendre basis (pieces [0,log1.5],[log1.5,log2],[log2,log3]),
# D and comb shift exact; transported constraints; Legendre gauge family. usage: taustar n T J [c]
import sys, numpy as np, scipy.special as sp, scipy.linalg as sl
ts=float(sys.argv[1]); n=int(sys.argv[2]); T=float(sys.argv[3]); J=int(sys.argv[4]); cc=float(sys.argv[5]) if len(sys.argv)>5 else 1.0
FULL=len(sys.argv)>6
ell=np.log(3); cuts=[0,np.log(1.5),np.log(2),ell]; P=3; N=P*n
cen=[(cuts[p]+cuts[p+1])/2 for p in range(P)]; ln=[cuts[p+1]-cuts[p] for p in range(P)]
m=lambda t: np.real(sp.digamma(0.25+0.5j*t))-np.log(np.pi)
M=m(ts)
gx,gw=np.polynomial.legendre.leggauss(40)
TM=ts if not FULL else 4000.
tau=np.concatenate([(p+(gx+1)/2) for p in range(int(TM))]); wq=np.tile(gw/2,int(TM))
hv=(M-m(tau))*(tau<ts) if not FULL else (-m(tau))   # FULL: compute -(arch) directly with full symbol on [0,TM]
# phi^_{p,l}(tau) = e^{-i tau c_p} sqrt((2l+1) len)(-i)^l j_l(tau len/2)
Phi=np.zeros((N,len(tau)),complex)
for p in range(P):
    for l in range(n):
        Phi[p*n+l]=np.exp(-1j*tau*cen[p])*np.sqrt((2*l+1)*ln[p])*(-1j)**l*sp.spherical_jn(l,tau*ln[p]/2)
Gm=np.real((Phi*(wq*hv)[None,:])@Phi.conj().T)/np.pi
Arch=(M*np.eye(N)-Gm) if not FULL else -Gm
# D: identity + 2^{-1/2} S, S maps piece0 -> piece2 (same Legendre index)
S=np.zeros((N,N)); 
for l in range(n): S[2*n+l,0*n+l]=1
D=np.eye(N)+2**-0.5*S
Pi=2*np.log(2)/np.sqrt(2)*(S+S.T)/2    # 2*sum Lambda(m) m^-1/2 <tau H,H>, symmetric form matrix: <tau H,H> = H2.S H0
# polar: A(H)=int H e^{x/2}, B(H)=int H e^{-x/2}, x=y-T-ell ; moments of Legendre on pieces
yq,yw=np.polynomial.legendre.leggauss(200)
def proj(fn):
    v=np.zeros(N)
    for p in range(P):
        y=cen[p]+ln[p]/2*yq; w=ln[p]/2*yw
        for l in range(n): v[p*n+l]=np.sum(w*fn(y)*np.sqrt((2*l+1)/ln[p])*sp.eval_legendre(l,2*(y-cen[p])/ln[p]))
    return v
xw=lambda y: y-T-ell
a=D.T@proj(lambda y: np.exp(xw(y)/2)); b=D.T@proj(lambda y: np.exp(-xw(y)/2))
Q=D.T@(Arch-cc*Pi)@D+np.outer(a,b)+np.outer(b,a)
lam=np.exp(T)
def wfun(key,y):
    xi=np.exp(-xw(y)); wt=np.sqrt(xi); ns=[k for k in range(1,50) if k*np.exp(-T)<lam]
    I=lambda A,B: 2*(np.sin(2*np.pi*xi*B)-np.sin(2*np.pi*xi*A))/(2*np.pi*xi)
    Il=lambda A,B: 2*(sp.sici(2*np.pi*xi*B)[1]-sp.sici(2*np.pi*xi*A)[1])
    return {'f0':2*wt,'flam':2*np.cos(2*np.pi*lam*xi)*wt,'A':wt*sum(I(k*np.exp(-T),min(k*np.exp(T),lam))/k for k in ns),
            'B':wt*sum(Il(k*np.exp(-T),min(k*np.exp(T),lam)) for k in ns)}[key]
C=np.array([proj(lambda y,k=k: wfun(k,y)) for k in ['f0','flam','A','B']]).T
Vn=sl.null_space(C.T)
# Legendre gauge family: g_l(y)=P_{2l}(lam y) on |y|<1/lam; ghat(xi)=(2/lam)(-1)^l j_{2l}(2 pi xi/lam)
ghat=lambda xi: np.array([(2/lam)*(-1)**l*sp.spherical_jn(2*l,2*np.pi*xi/lam) for l in range(J)])
Cg=np.array([proj(lambda y,l=l: np.sqrt(np.exp(-xw(y)))*ghat(np.exp(-xw(y)))[l]) for l in range(J)]).T
x0,w0=np.polynomial.legendre.leggauss(400); xi0=lam*(x0+1)/2; w0=w0*lam/2
G=np.diag([1/(lam*(4*l+1)) for l in range(J)])-(ghat(xi0)*w0[None,:])@ghat(xi0).T
L=np.eye(N)-Cg@np.linalg.solve(G,Cg.T)
A_=Vn.T@Q@Vn; B_=Vn.T@L@Vn
ev=sl.eigh(A_,B_,eigvals_only=True)
print(f"pw3 taustar={ts}{' FULL' if FULL else ''} n={n} T={T} J={J} c={cc}: Q/|F|^2 on V {np.round(np.linalg.eigvalsh(A_)[:2],5)} min l_g {np.linalg.eigvalsh(B_)[0]:.3e} Q/l_g {np.round(ev[:3],4)} condG {np.linalg.cond(G):.1e}",flush=True)
for kap in [0.5,0.7,0.8]:
    print(f"   kappa={kap}: lam_min(Q-kappa*L on V) = {np.linalg.eigvalsh(A_-kap*B_)[0]:.3e}   M={M:.4f} (M-0.98)/2={(M-2*np.log(2)/np.sqrt(2)*cc)/2:.4f}")
