# R162_1803 convergence test for (C2): does the non-monotone ripple of psi/cosh shrink with K? UNCERTIFIED.
import numpy as np,scipy.special as sp,sys
from t1803_rcb_numerics import build
def ratio(T,K,model,s,par=0,N=8001):
    A,vec,l=build(T,K,model,s); idx=np.arange(par,K,2); ev,U=np.linalg.eigh(A[np.ix_(idx,idx)])
    tt=np.linspace(0,T,N)[1:]
    Pl=np.array([sp.eval_legendre(k,tt/T)*np.sqrt((2*k+1)/(2*T)) for k in l])
    co=np.zeros(K); co[idx]=U[:,0]; f=co@Pl; f*=np.sign(f[0]); f/=np.abs(f).max()
    return tt,f/(np.cosh(tt/2) if par==0 else np.sinh(tt/2)),ev[0]
model=sys.argv[1]; s=float(sys.argv[2]); par=int(sys.argv[3])
for T in [float(x) for x in sys.argv[4].split(',')]:
    prev=None
    for K in (26,34,46,60,76):
        tt,r,mu=ratio(T,K,model,s,par); d=np.diff(r); sg=np.sign(r[-1]-r[0])
        viol=np.clip(-d*sg,0,None); cum=viol.sum()/np.ptp(r)  # total variation against trend
        inner=tt<0.9*T; cumi=np.clip(-d[inner[1:]]*sg,0,None).sum()/np.ptp(r)
        dif=np.abs(r-prev).max()/np.ptp(r) if prev is not None else np.nan
        print(f"| {model} | {s} | {par} | {T:.4f} | {K} | {mu:.3e} | {cum:.2e} | {cumi:.2e} | {dif:.1e} |"); prev=r
    sys.stdout.flush()
