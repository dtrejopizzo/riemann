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
    ns=[n for n in range(2,60) if np.log(n)<2*T and Lam(n)>0]
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
    tt=np.linspace(0,T,2001)
    Pl=np.array([sp.eval_legendre(k,tt/T)*np.sqrt((2*k+1)/(2*T)) for k in l])
    evA,UA=np.linalg.eigh(A); psi=UA[:,0]@Pl; psi*=np.sign(psi[0])
    rat=psi/np.cosh(tt/2); d=np.diff(rat)
    mono = (d<0).mean()
    idx=np.arange(0,K,2)
    Q,_=np.linalg.qr(c[idx].reshape(-1,1),mode='complete'); P=Q[:,1:]
    H=P.T@A[np.ix_(idx,idx)]@P; ev,U=np.linalg.eigh(H); co=np.zeros(K); co[idx]=P@U[:,0]
    Ks=[co@vec(a) for a in (-0.5,0.5,2.5,4.5,6.5,8.5)]
    # overlap with psi and ratio r size: ||A F - lam F|| relative
    AF=A@co; r=np.linalg.norm(AF-ev[0]*co)
    return mono, ev[0], Ks, r, abs(co@UA[:,0])
for T in [0.5,0.78,0.8047,1.0,1.2]:
    m_,lam,Ks,r,ov=run(T); print("T=%.4f frac_decr(psi/cosh)=%.3f lam=%.2e K_F(-1/2,1/2,a1..a4)="%(T,m_,lam)+" ".join("%.2e"%k for k in Ks)+" |AF-lamF|=%.2e <F,psi>=%.2e"%(r,ov))
