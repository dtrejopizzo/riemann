import os; HERE=os.path.dirname(os.path.abspath(__file__))
# limit problem: F on window (-T-ell,-T), G = T F = sum_{N<R} N^{-1/2} F(x - log N) on window; Q = a_{ell/2}(G)/|F|^2
import sys; sys.path.insert(0,''+HERE+'/..')
import galerkin_mp as Gm, numpy as np, scipy.linalg as sl, scipy.special as sp
POL=int(sys.argv[4]) if len(sys.argv)>4 else 1
R=int(sys.argv[1]); Nb=int(sys.argv[2]); T=float(sys.argv[3]) if len(sys.argv)>3 else 0.8
ell=np.log(R); Dd=Gm.build(ell/2,Nb,dps=20,verbose=False,cache=False,errcheck=False)
f2n=lambda M: np.array([[float(M[i,j]) for j in range(Nb)] for i in range(Nb)])
W=f2n(Dd['Arch'])-f2n(Dd['Pi']); Ar=f2n(Dd['Arch'])
z=np.linspace(-ell/2,ell/2,20001); E=np.array([np.sin(k*np.pi*(z+ell/2)/ell)/np.sqrt(ell/2) for k in range(1,Nb+1)])
# z = x + T + ell/2 ; window x in (-T-ell,-T); (TF)(x) = sum_N N^{-1/2} F(x - log N): in z: F(z - log N)
Tm=np.zeros((Nb,Nb))
for N in range(1,R):
    zs=z-np.log(N); ok=zs>-ell/2
    Es=np.where(ok[None,:],np.array([np.sin(k*np.pi*(zs+ell/2)/ell)/np.sqrt(ell/2) for k in range(1,Nb+1)]),0)
    Tm+=N**-0.5*np.trapz(E[:,None,:]*Es[None,:,:],z,axis=2)   # Tm[i,j]=<e_i, T e_j>
Q_=Tm.T@W@Tm
xw0=z-T-ell/2; a_=Tm.T@np.trapz(E*np.exp(xw0/2)[None,:],z,axis=1); b_=Tm.T@np.trapz(E*np.exp(-xw0/2)[None,:],z,axis=1)
if POL: Q_=Q_+np.outer(a_,b_)+np.outer(b_,a_)
lam=np.exp(T); xw=z-T-ell/2; xi=np.exp(-xw); wt=xi**0.5
def I(a,b): return 2*(np.sin(2*np.pi*xi*b)-np.sin(2*np.pi*xi*a))/(2*np.pi*xi)
def Il(a,b): return 2*(sp.sici(2*np.pi*xi*b)[1]-sp.sici(2*np.pi*xi*a)[1])
fun={'f(0)':2*np.ones_like(xi),'f(lam)':2*np.cos(2*np.pi*lam*xi),
 'A':sum(I(n*np.exp(-T),min(n*np.exp(T),lam))/n for n in range(1,50) if n*np.exp(-T)<lam),
 'B':sum(Il(n*np.exp(-T),min(n*np.exp(T),lam)) for n in range(1,50) if n*np.exp(-T)<lam)}
def cmin(keys):
    if not keys: return np.linalg.eigvalsh(Q_)[:3]
    C=np.array([np.trapz(E*(wt*fun[k])[None,:],z,axis=1) for k in keys]).T
    Qn=sl.null_space(C.T); return np.linalg.eigvalsh(Qn.T@Q_@Qn)[:3]
print(f'R={R} ell={ell:.3f} Nb={Nb} T={T}: none {np.round(cmin([]),3)} | f(0) {np.round(cmin(["f(0)"]),3)} | all4 {np.round(cmin(["f(0)","f(lam)","A","B"]),3)}  -> D-units floor (lam/2)*mu = {lam/2*cmin(["f(0)","f(lam)","A","B"])[0]:.3f}',flush=True)
