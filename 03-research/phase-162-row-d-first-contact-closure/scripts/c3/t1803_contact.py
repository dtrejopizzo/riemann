# R162_1803 addendum: at the first even primitive contact T_*(s) (lam_ev = bottom of A^ev on cosh^perp = 0),
# report mu2^ev(T_*) and test (R2'): sign-change point of u2 vs of psi - c*cosh (c = <psi,cosh>/|cosh|^2). UNCERTIFIED.
import numpy as np,scipy.special as sp,sys
from scipy.optimize import brentq
from t1803_rcb_numerics import build,sc
def ev_data(T,K,model,s,N=16001):
    A,vec,l=build(T,K,model,s); idx=np.arange(0,K,2); Ae=A[np.ix_(idx,idx)]; c=vec(0.5)[idx]
    Q,_=np.linalg.qr(c.reshape(-1,1),mode='complete'); P=Q[:,1:]; lam=np.linalg.eigvalsh(P.T@Ae@P)[0]
    ev,U=np.linalg.eigh(Ae)
    tt=np.linspace(0,T,N)[1:-1]; Pl=np.array([sp.eval_legendre(k,tt/T)*np.sqrt((2*k+1)/(2*T)) for k in l[idx]])
    psi=U[:,0]*np.sign(U[:,0]@Pl[:,0]); u2=U[:,1]*np.sign(U[:,1]@Pl[:,0])
    g=psi-(psi@c)/(c@c)*c
    zs=lambda f:[tt[i] for i in np.where(np.sign(f[1:])!=np.sign(f[:-1]))[0]]
    return lam,ev[0],ev[1],zs(u2@Pl),zs(g@Pl),(u2@c)/np.linalg.norm(c)
model=sys.argv[1]; a,b=float(sys.argv[3]),float(sys.argv[4])
for s in [float(x) for x in sys.argv[2].split(',')]:
    for K in (34,46):
        f=lambda T: ev_data(T,K,model,s,801)[0]
        Ts=np.linspace(a,b,40); v=[f(T) for T in Ts]; i=next((j for j in range(39) if v[j]*v[j+1]<=0),None)
        if i is None: print(f"| {model} | {s} | {K} | no contact in [{a},{b}] (lam_ev min {min(v):.2e}) |"); continue
        Tc=brentq(f,Ts[i],Ts[i+1],xtol=1e-8); lam,mu1,mu2,z2,zg,ov=ev_data(Tc,K,model,s)
        print(f"| {model} | {s} | {K} | {Tc:.6f} | {mu1:.4e} | {mu2:+.4e} | {', '.join(f'{z:.4f}' for z in z2)} | {', '.join(f'{z:.4f}' for z in zg)} | {ov:+.4f} |")
    sys.stdout.flush()
