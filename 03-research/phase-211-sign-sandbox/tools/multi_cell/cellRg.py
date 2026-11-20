# R-cell compressed complete form Q = W[DF] + 2A B (comb weight c), transported constraints, ratio to gauge-quotient leakage l_g
# usage: python3 cellRg.py R Nb T J c
import sys, numpy as np, scipy.linalg as sl, scipy.special as sp
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-211-sign-sandbox/tools')
import galerkin_mp as Gm
R=int(sys.argv[1]); Nb=int(sys.argv[2]); T=float(sys.argv[3]); J=int(sys.argv[4]); cc=float(sys.argv[5]) if len(sys.argv)>5 else 1.0
ell=np.log(R); Dd=Gm.build(ell/2,Nb,dps=20,verbose=False,cache=True,errcheck=False)
f2n=lambda M: np.array([[float(M[i,j]) for j in range(Nb)] for i in range(Nb)])
Ar=f2n(Dd['Arch']); Pi=f2n(Dd['Pi']); W=Ar-cc*Pi
z=np.linspace(-ell/2,ell/2,20001); E=np.array([np.sin(k*np.pi*(z+ell/2)/ell)/np.sqrt(ell/2) for k in range(1,Nb+1)])
Tm=np.zeros((Nb,Nb))
for N in range(1,R):
    zs=z-np.log(N); ok=zs>-ell/2
    Es=np.where(ok[None,:],np.array([np.sin(k*np.pi*(zs+ell/2)/ell)/np.sqrt(ell/2) for k in range(1,Nb+1)]),0)
    Tm+=N**-0.5*np.trapz(E[:,None,:]*Es[None,:,:],z,axis=2)
Q=Tm.T@W@Tm
xw=z-T-ell/2; a_=Tm.T@np.trapz(E*np.exp(xw/2)[None,:],z,axis=1); b_=Tm.T@np.trapz(E*np.exp(-xw/2)[None,:],z,axis=1)
Qp=Q+np.outer(a_,b_)+np.outer(b_,a_)
lam=np.exp(T); xi=np.exp(-xw); wt=xi**0.5
def I(a,b): return 2*(np.sin(2*np.pi*xi*b)-np.sin(2*np.pi*xi*a))/(2*np.pi*xi)
def Il(a,b): return 2*(sp.sici(2*np.pi*xi*b)[1]-sp.sici(2*np.pi*xi*a)[1])
ns=[n for n in range(1,50) if n*np.exp(-T)<lam]
fun={'f0':2*np.ones_like(xi),'flam':2*np.cos(2*np.pi*lam*xi),
 'A':sum(I(n*np.exp(-T),min(n*np.exp(T),lam))/n for n in ns),'B':sum(Il(n*np.exp(-T),min(n*np.exp(T),lam)) for n in ns)}
C=np.array([np.trapz(E*(wt*fun[k])[None,:],z,axis=1) for k in fun]).T
Vn=sl.null_space(C.T)
# gauge tails: phi = (1-s^2)^3 s^2 P_{2i}(s), s=lam*y, i<J, combos with int phi=0 ; ghat(xi)=2 int_0^{1/lam} phi cos(2 pi xi y) dy
def gauge_L(J,XMAX=80.,NX=40001):
    if J==0: return np.eye(Nb)
    yn,yw=np.polynomial.legendre.leggauss(600); s_=(yn+1)/2; yw=yw/2; y=s_/lam; wy=yw/lam
    ph=np.array([(1-s_**2)**3*s_**2*sp.eval_legendre(2*i,s_) for i in range(J)])
    Bc=sl.null_space((ph@wy)[None,:]); ph=Bc.T@ph
    xg=np.linspace(lam,XMAX,NX); Gt=np.zeros((ph.shape[0],NX))
    for i0 in range(0,NX,4000):
        q=xg[i0:i0+4000]; Gt[:,i0:i0+4000]=2*(ph*wy[None,:])@np.cos(2*np.pi*np.outer(y,q))
    w=np.sqrt(np.gradient(xg)); Qg,rr=np.linalg.qr((Gt*w[None,:]).T)
    keep=np.abs(np.diag(rr))>1e-12*np.abs(rr[0,0]); Qg=Qg[:,keep]
    qf=Qg/w[:,None]                          # orthonormal functions q_k(xi) in L2(lam,XMAX)
    qz=np.array([np.interp(xi,xg,qf[:,k]) for k in range(qf.shape[1])])   # on window
    Cg=np.trapz(E[:,None,:]*(wt*qz)[None,:,:],z,axis=2)   # <F, xi^{1/2} q_k> = <u,q_k>
    return np.eye(Nb)-Cg@Cg.T, keep.sum()
L,rk=gauge_L(J) if J>0 else (np.eye(Nb),0)
def bottoms(Qm,Lm):
    A=Vn.T@Qm@Vn; B=Vn.T@Lm@Vn
    eB=np.linalg.eigvalsh(B)
    ev,V=sl.eigh(A,B); v=Vn@V[:,0]; 
    global diag; diag=(v@Qm@v/(v@v), v@Lm@v/(v@v), np.linalg.eigvalsh(A)[0])
    return ev[:2], eB[0]
r1,_=bottoms(Qp,np.eye(Nb)); r2,mb=bottoms(Qp,L)
print(f"R={R} T={T} Nb={Nb} J={J}(rk {rk}) c={cc}: on V: Q/|F|^2 {np.round(r1,4)}  Q/l_g {np.round(r2,4)}  [min l_g/|F|^2 on V {mb:.2e}]  l_g-units (lam/2)kappa={lam/2*r2[0]:.4f} | bottom vec: Q/|F|^2={diag[0]:.3e} l_g/|F|^2={diag[1]:.3e}; unconstr. bottom of Q {np.linalg.eigvalsh(Qp)[0]:.3e}",flush=True)
