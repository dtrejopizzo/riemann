# R162_1601: rerun of t1501 scripts with the sign*tail fix; K-convergence; deletion model a=Lambda*1_{n>=5}.
# UNCERTIFIED float.
import numpy as np, scipy.special as sp, sys
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
def Lam(n):
    for p in (2,3,5,7,11,13):
        k=n
        while k%p==0: k//=p
        if k==1 and n%p==0: return np.log(p)
    return 0.0
_X=None
def grid(tmax):
    global _X
    if _X is None:
        x,w=leggauss(30); lo=np.arange(0,tmax,0.5)
        _X=((lo[:,None]+0.25*(x+1)).ravel(),np.tile(0.25*w,len(lo)))
    return _X
def build(T,K,model,tmax=3000.):
    nmin=5 if model=='del' else 2
    ns=[n for n in range(nmin,400) if np.log(n)<2*T and Lam(n)>0]
    V={n:2*Lam(n)/np.sqrt(n) for n in ns}
    m=lambda t: sp.digamma(0.25+0.5j*t).real-np.log(np.pi)
    s=lambda t: m(t)-sum(v*np.cos(t*np.log(n)) for n,v in V.items())
    X,W=grid(tmax)
    J=np.array([sp.spherical_jn(l,X*T) for l in range(K)])
    G=(J*(s(X)*W))@J.T
    tail=quad(lambda t: m(t)/(2*t*t*T*T),tmax,np.inf)[0]
    l=np.arange(K); sq=np.sqrt(2*l+1)
    sign=np.array([[0 if (a-b)%2 else (1 if ((b-a)//2)%2==0 else -1) for b in l] for a in l])
    G=G+sign*tail
    A=(2*T/np.pi)*np.outer(sq,sq)*sign*G
    vec=lambda a: np.sqrt((2*l+1)/(2*T))*2*T*sp.spherical_in(l,a*T)
    return A,vec,l
def sc(f):
    g=f[np.abs(f)>1e-6*np.abs(f).max()]; return int(np.sum(np.sign(g[1:])!=np.sign(g[:-1])))
def analyze(T,K,model):
    A,vec,l=build(T,K,model); c=vec(0.5)
    tt=np.linspace(-T,T,4001)
    Pl=np.array([sp.eval_legendre(k,tt/T)*np.sqrt((2*k+1)/(2*T)) for k in l])
    evA,UA=np.linalg.eigh(A); out={'A':[(evA[i],sc(UA[:,i]@Pl)) for i in range(3)],'mu1':evA[0]}
    for par in (0,1):
        idx=np.arange(par,K,2)
        Q,_=np.linalg.qr(c[idx].reshape(-1,1),mode='complete'); P=Q[:,1:]
        H=P.T@A[np.ix_(idx,idx)]@P; ev,U=np.linalg.eigh(H)
        co=np.zeros(K); co[idx]=P@U[:,0]
        out[par]=dict(lam=ev[0],lam2=ev[1],S=sc(co@Pl),S2=sc(np.zeros(K)@Pl+ (lambda z:(z.__setitem__(idx,P@U[:,1]),z)[1])(np.zeros(K))@Pl),
            KF=[co@vec(a) for a in (0.5,2.5,4.5,6.5,8.5)],
            r=np.linalg.norm(A@co-ev[0]*co),ov=abs(co@UA[:,0]),
            ovmu2=abs(co@UA[:,1]))
    return out
if __name__=='__main__':
    model=sys.argv[1]; Ks=[int(k) for k in sys.argv[2].split(',')]; Ts=[float(t) for t in sys.argv[3].split(',')]
    for T in Ts:
        for K in Ks:
            o=analyze(T,K,model)
            for par in (0,1):
                d=o[par]; kf=d['KF']
                print(f"{model} T={T:.4f} K={K} par={par} lam={d['lam']:.3e} lam2={d['lam2']:.3e} S={d['S']} S2={d['S2']} "
                      f"KF(1/2,a1..a4)="+" ".join(f"{x:.3e}" for x in kf)+
                      f" r={d['r']:.2e} r/|lam|={d['r']/abs(d['lam']):.2f} <F,psi>={d['ov']:.2e} <F,psi>|mu1|/|lam|={d['ov']*abs(o['mu1'])/abs(d['lam']):.2f} |<F,u2>|={d['ovmu2']:.3f}")
            print(f"{model} T={T:.4f} K={K} A-bottom:", [(f"{a:.2e}",b) for a,b in o['A']])
        sys.stdout.flush()
