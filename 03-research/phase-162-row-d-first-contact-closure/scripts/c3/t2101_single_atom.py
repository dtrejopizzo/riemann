# R162_2101: single atom a=log x, weight s*2*log(x)/sqrt(x), even primitive form. UNCERTIFIED float.
import sys, numpy as np, scipy.special as sp
from scipy.integrate import quad
from scipy.optimize import brentq
import t1601_nodal_rerun as B
_c={}
def pieces(T,K,x,tmax=3000.):
    key=(round(T,12),K,x)
    if key in _c: return _c[key]
    m=lambda t: sp.digamma(0.25+0.5j*t).real-np.log(np.pi)
    X,W=B.grid(tmax); J=np.array([sp.spherical_jn(l,X*T) for l in range(K)])
    l=np.arange(K); sq=np.sqrt(2*l+1)
    sign=np.array([[0 if (a-b)%2 else (1 if ((b-a)//2)%2==0 else -1) for b in l] for a in l])
    pre=(2*T/np.pi)*np.outer(sq,sq)*sign
    tail=quad(lambda t: m(t)/(2*t*t*T*T),tmax,np.inf)[0]
    A0=pre*((J*(m(X)*W))@J.T+sign*tail)
    w=2*np.log(x)/np.sqrt(x)
    A1=pre*((J*(w*np.cos(X*np.log(x))*W))@J.T) if np.log(x)<2*T else np.zeros((K,K))
    idx=np.arange(0,K,2)
    phi=(np.sqrt((2*l+1)/(2*T))*2*T*sp.spherical_in(l,0.5*T))[idx]
    P0=np.array([sp.eval_legendre(k,1e-3)*np.sqrt((2*k+1)/(2*T)) for k in l[idx]])
    r=(A0[np.ix_(idx,idx)],A1[np.ix_(idx,idx)],phi/np.linalg.norm(phi),P0); _c[key]=r; return r
def data(T,K,x,s):
    A0,A1,ph,P0=pieces(T,K,x); A=A0-s*A1
    ev,U=np.linalg.eigh(A); U=U*np.sign(P0@U); ov=U.T@ph
    Q,_=np.linalg.qr(ph.reshape(-1,1),mode='complete'); P=Q[:,1:]
    lam=np.linalg.eigvalsh(P.T@A@P)[0]
    return dict(lam=lam,mu2=ev[1],ov=ov[1])
Tg=np.round(np.arange(0.20,1.5001,0.005),4)
def Tstar(K,x,s):
    for j in range(len(Tg)-1):
        if data(Tg[j],K,x,s)['lam']>0 and data(Tg[j+1],K,x,s)['lam']<=0:
            return brentq(lambda T: data(T,K,x,s)['lam'],Tg[j],Tg[j+1],xtol=1e-13)
if __name__=='__main__':
    K=int(sys.argv[1]); x=float(sys.argv[2])
    for s in [float(v) for v in sys.argv[3:]]:
        T=Tstar(K,x,s); d=data(T,K,x,s) if T else {}
        print(x,s,T,d.get('mu2'),d.get('ov'),flush=True)
