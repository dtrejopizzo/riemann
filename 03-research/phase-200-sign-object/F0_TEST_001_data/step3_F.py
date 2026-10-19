# F0_TEST_001 step 3: F(eps)=||Z^(eps) r*||^2_(T,inf), Theorem D consistency, F''(0), convexity, Lemma-F bound. NUMERICO.
# rho(om)=r*(lam*om) x1e35: caustic layer [1,2] on a sqrt-grid (rho_sigma.json), [2,60] (rho.json), [60,240] (rho_60_240.json),
# all computed at 256 bits from f* (400 bits).  Quadratic quantities below are in units of 1e-70.
#   s = w/lam = e^{y'}, y = T + y';  S_eps(s)=sum_n n^eps rho(n s);  F(eps)=lam*int_1^inf S_eps^2 ds
#   Psi(y)=(lam s)^{1/2} S_0(s);  A=lam*int S_0 ds;  B=int S_0 ds/s
#   Arch[Psi]=b_inf c(0)+2 int_0^inf (c(0)-c(v)) nu(v) dv,  nu=e^{-v/2}/(1-e^{-2v}),  b_inf=psi(1/4)-log pi.
import json,sys,math,os
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import digamma
lam=math.sqrt(15)
binf=float(digamma(0.25))-math.log(math.pi)
def load(f):
    R=json.load(open(f)); return R
Rs=load('rho_sigma.json'); rs=np.array([float(x) for x in Rs['rho']])*1e35; sg=Rs['dsig']*np.arange(len(rs))
spS=CubicSpline(sg,rs)
R1=load('rho.json'); r1=np.array([float(x) for x in R1['rho']])*1e35; o1=R1['omega0']+R1['dom']*np.arange(len(r1))
sp1=CubicSpline(o1,r1)
OMX=60.0; sp2=None
if os.path.exists('rho_60_240.json'):
    R2=load('rho_60_240.json'); r2=np.array([float(x) for x in R2['rho']])*1e35; o2=R2['omega0']+R2['dom']*np.arange(len(r2))
    sp2=CubicSpline(o2,r2); OMX=float(o2[-1])
def rho(x):
    out=np.zeros_like(x)
    m=x<2; out[m]=spS(np.sqrt(np.maximum(x[m]-1,0)))
    m=(x>=2)&(x<=60); out[m]=sp1(x[m])
    if sp2 is not None:
        m=(x>60)&(x<=OMX); out[m]=sp2(x[m])
    return out
def run(X, eps_list, dy=1.5e-5, npair=8, rhof=None):
    rhof=rhof or rho
    ys=np.arange(0,math.log(X)+dy/2,dy); s=np.exp(ys); nmax=int(X)
    wq=np.full(len(s),dy); wq[0]=wq[-1]=dy/2; wq=wq*s
    S=np.zeros((4,len(s))); Se={e:np.zeros(len(s)) for e in eps_list}; rows=[]
    for n in range(1,nmax+1):
        a=n*s; k=np.searchsorted(a,X,side='right')
        if k==0: break
        rn=np.zeros(len(s)); rn[:k]=rhof(a[:k]); l=math.log(n)
        for j in range(4): S[j]+=l**j*rn
        for e in eps_list: Se[e]+=n**e*rn
        if n<=npair: rows.append(rn)
    S0,S1,S2,S3=S
    F0=lam*np.sum(wq*S0*S0); F1=2*lam*np.sum(wq*S0*S1); F2=2*lam*np.sum(wq*(S1*S1+S0*S2)); F3=2*lam*np.sum(wq*(3*S1*S2+S0*S3))
    Fe={e:lam*np.sum(wq*Se[e]**2) for e in eps_list}
    A=lam*np.sum(wq*S0); B=np.sum(wq*S0/s)
    Psi=np.sqrt(lam*s)*S0; n_=len(Psi); m=1<<int(math.ceil(math.log2(2*n_)))
    fp=np.fft.rfft(Psi,m); c=np.fft.irfft(fp*np.conj(fp),m)[:n_]*dy; c0=np.sum(Psi*Psi)*dy
    v=np.arange(n_)*dy; nu=np.zeros(n_); nu[1:]=np.exp(-v[1:]/2)/(-np.expm1(-2*v[1:]))
    integ=(c0-c)*nu; integ[0]=0.0
    V=v[-1]; tailnu=sum(math.exp(-(0.5+2*k)*V)/(0.5+2*k) for k in range(200))
    lev=2*(np.sum(integ)-integ[-1]/2)*dy+2*c0*tailnu
    arch=binf*c0+lev
    H=np.array([[lam*np.sum(wq*a*b) for b in rows] for a in rows])
    return dict(X=X,F2a=2*lam*np.sum(wq*S1*S1),F2b=2*lam*np.sum(wq*S0*S2),F0=F0,F1=F1,F2=F2,F3=F3,Fe=Fe,A=A,B=B,twoAB=2*A*B,arch=arch,lev=lev,c0=c0,W_ext=arch+2*A*B-F1,H=H)
if __name__=='__main__':
    eps=[round(-0.05+0.005*k,4) for k in range(61)]
    Xs=[float(x) for x in sys.argv[1:]] or [15,30,60]
    dy=float(os.environ.get('DY','1.5e-5'))
    res={}
    for X in Xs:
        o=run(X,eps,dy=dy); res[X]=o
        print(f"X={X:6.1f} F0={o['F0']:.6f} F'={o['F1']:.6f} F''={o['F2']:.6f} F'''={o['F3']:.4f} A={o['A']:.5f} B={o['B']:.5f} 2AB={o['twoAB']:.6f} arch={o['arch']:.6f} W_ext={o['W_ext']:.6f}",flush=True)
    tag=os.environ.get('TAG','')
    json.dump({str(k):{kk:(vv.tolist() if isinstance(vv,np.ndarray) else ({str(a):b for a,b in vv.items()} if isinstance(vv,dict) else vv)) for kk,vv in v.items()} for k,v in res.items()},open(f'step3_F{tag}.json','w'),indent=1)
