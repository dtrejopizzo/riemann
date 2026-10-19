# R162_2001 (O1901.1): two-parameter comb a = s2*w2*delta_{log2} + s3*w3*delta_{log3}, w_n = 2*Lambda(n)/sqrt(n)
# (same normalisation as t1803_rcb_numerics: s=1 reproduces the zeta weights at n=2,3; n=4,5,... absent).
# Even primitive form A^ev_T = arch - comb (Paper 47 def, tail sign fixed R162_1590). UNCERTIFIED float.
# A(T;s2,s3) = A0(T) - s2*A2(T) - s3*A3(T) (linear in s).
import numpy as np, scipy.special as sp
from scipy.integrate import quad
import t1601_nodal_rerun as B
_cache={}
def pieces(T,K,tmax=3000.):
    key=(round(T,12),K)
    if key in _cache: return _cache[key]
    m=lambda t: sp.digamma(0.25+0.5j*t).real-np.log(np.pi)
    X,W=B.grid(tmax); J=np.array([sp.spherical_jn(l,X*T) for l in range(K)])
    l=np.arange(K); sq=np.sqrt(2*l+1)
    sign=np.array([[0 if (a-b)%2 else (1 if ((b-a)//2)%2==0 else -1) for b in l] for a in l])
    pre=(2*T/np.pi)*np.outer(sq,sq)*sign
    tail=quad(lambda t: m(t)/(2*t*t*T*T),tmax,np.inf)[0]
    A0=pre*((J*(m(X)*W))@J.T+sign*tail)
    out=[A0]
    for n in (2,3):
        w=2*np.log(n)/np.sqrt(n)
        out.append(pre*((J*(w*np.cos(X*np.log(n))*W))@J.T) if np.log(n)<2*T else np.zeros((K,K)))
    idx=np.arange(0,K,2)
    phi=(np.sqrt((2*l+1)/(2*T))*2*T*sp.spherical_in(l,0.5*T))[idx]
    Pl0=np.array([np.sqrt((2*k+1)/(2*T)) for k in l[idx]])  # Legendre at t=0+ scaled: P_k(0)... use value near 0
    tt=np.array([1e-3*T]); Pl0=np.array([sp.eval_legendre(k,tt/T)[0]*np.sqrt((2*k+1)/(2*T)) for k in l[idx]])
    r=([M[np.ix_(idx,idx)] for M in out],phi/np.linalg.norm(phi),Pl0)
    _cache[key]=r; return r
def data(T,K,s2,s3):
    (A0,A2,A3),ph,P0=pieces(T,K); A=A0-s2*A2-s3*A3
    ev,U=np.linalg.eigh(A)
    U=U*np.sign(P0@U)            # eigenvectors >0 at t=0+
    ov=U.T@ph; r=ov**2
    Q,_=np.linalg.qr(ph.reshape(-1,1),mode='complete'); P=Q[:,1:]
    lam=np.linalg.eigvalsh(P.T@A@P)[0]
    g0=sum(r[k]/ev[k] for k in range(len(ev)) if k!=1)
    f0=g0+r[1]/ev[1]
    return dict(lam=lam,mu1=ev[0],mu2=ev[1],mu3=ev[2],ov=ov[1],r2=r[1],g0=g0,f0=f0,Nm=int((ev<0).sum()))
