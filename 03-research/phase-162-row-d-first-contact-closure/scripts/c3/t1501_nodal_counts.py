import numpy as np, scipy.special as sp
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
def Lam(n):
    for p in (2,3,5,7):
        k=n
        while k%p==0: k//=p
        if k==1 and n%p==0: return np.log(p)
    return 0.0
def run(T,K=34,tmax=3000.):
    ns=[n for n in range(2,400) if np.log(n)<2*T and Lam(n)>0]
    V={n:2*Lam(n)/np.sqrt(n) for n in ns}
    m=lambda t: sp.digamma(0.25+0.5j*t).real-np.log(np.pi)
    s=lambda t: m(t)-sum(v*np.cos(t*np.log(n)) for n,v in V.items())
    x,w=leggauss(30); X=[];W=[]
    for lo in np.arange(0,tmax,0.5): X.append(lo+0.25*(x+1));W.append(0.25*w)
    X=np.concatenate(X);W=np.concatenate(W)
    J=np.array([sp.spherical_jn(l,X*T) for l in range(K)])
    G=(J*(s(X)*W))@J.T
    tail=quad(lambda t: m(t)/(2*t*t*T*T),tmax,np.inf)[0]
    l=np.arange(K); sq=np.sqrt(2*l+1)
    sign=np.array([[0 if (a-b)%2 else (1 if ((b-a)//2)%2==0 else -1) for b in l] for a in l])
    G=G+sign*tail  # fixed per R162_1590 (was abs(sign))
    A=(2*T/np.pi)*np.outer(sq,sq)*sign*G
    vec=lambda a: np.sqrt((2*l+1)/(2*T))*2*T*sp.spherical_in(l,a*T)
    c=vec(0.5); out={}
    for par in (0,1):
        idx=np.arange(par,K,2)
        Q,_=np.linalg.qr(c[idx].reshape(-1,1),mode='complete'); P=Q[:,1:]
        H=P.T@A[np.ix_(idx,idx)]@P; ev,U=np.linalg.eigh(H)
        row=[ev[0]]
    tt=np.linspace(-T,T,4001)
    Pl=np.array([sp.eval_legendre(k,tt/T)*np.sqrt((2*k+1)/(2*T)) for k in l])
    def sc(f):
        g=f[np.abs(f)>1e-6*np.abs(f).max()]; return int(np.sum(np.sign(g[1:])!=np.sign(g[:-1])))
    res={}
    # unconstrained full
    evA,UA=np.linalg.eigh(A); res['A']=[(evA[i],sc(UA[:,i]@Pl)) for i in range(4)]
    for par in (0,1):
        idx=np.arange(par,K,2)
        Q,_=np.linalg.qr(c[idx].reshape(-1,1),mode='complete'); P=Q[:,1:]
        H=P.T@A[np.ix_(idx,idx)]@P; ev,U=np.linalg.eigh(H)
        res[par]=[(ev[i],sc((P@U[:,i])@Pl[idx])) for i in range(4)]
    return res
for T in [0.3,0.5,0.6,0.65,0.7,0.75,0.78,0.8047,1.0,1.2]:
    o=run(T); print("T=%.4f"%T, {k:[("%.1e"%a,b) for a,b in v] for k,v in o.items()})
