"""First zeros of L(s,chi), chi = Legendre symbol mod a prime q ≡ 1 (mod 4) (even, real, root number 1).
Completed Lambda(s) = (q/pi)^{s/2} Gamma(s/2) L(s,chi), real on the critical line.
Smoothed approximate functional equation (exact identity):
  Lambda(s) = sum_n chi(n) [ (q/pi)^{s/2} n^{-s} Gamma(s/2, pi n^2/q) + (q/pi)^{(1-s)/2} n^{s-1} Gamma((1-s)/2, pi n^2/q) ]
On s = 1/2+it the two terms are conjugate, so Lambda = 2 Re[ first term ].
Upper incomplete gamma for complex a, real x>0: series for x<=12, continued fraction for x>12 (vectorised numpy)."""
import numpy as np, sys, time
from math import pi, log, sqrt
from scipy.special import loggamma

def legendre_vec(N,q):
    e=(q-1)//2
    return np.array([0]+[1 if pow(n,e,q)==1 else -1 if pow(n,e,q)==q-1 else 0 for n in range(1,N+1)],dtype=np.int8)

def upper_gamma(a,x):
    """Gamma(a,x) for complex scalar a, real array x>0."""
    out=np.empty(x.shape,dtype=complex)
    small=x<=12
    xs=x[small]
    if xs.size:
        # lower gamma series: gamma(a,x)=x^a e^{-x} sum_k x^k / (a(a+1)...(a+k))
        term=np.ones_like(xs,dtype=complex)/a; s=term.copy()
        for k in range(1,400):
            term=term*xs/(a+k); s+=term
            if np.max(np.abs(term))<1e-17*np.max(np.abs(s)): break
        low=np.exp(a*np.log(xs)-xs)*s
        out[small]=np.exp(loggamma(a))-low
    big=~small
    xb=x[big]
    if xb.size:
        # Lentz continued fraction (Numerical Recipes gcf)
        b=xb+1-a; c=np.full_like(xb,1e300,dtype=complex); d=1/b; h=d.copy()
        for i in range(1,300):
            an=-i*(i-a); b=b+2
            d=an*d+b; d=np.where(np.abs(d)<1e-300,1e-300,d)
            c=b+an/c; c=np.where(np.abs(c)<1e-300,1e-300,c)
            d=1/d; delta=d*c; h*=delta
            if np.max(np.abs(delta-1))<1e-16: break
        out[big]=np.exp(-xb+a*np.log(xb))*h
    return out

class Lchi:
    def __init__(self,q,cut=28.0):
        self.q=q
        N=int(sqrt(cut*q/pi))+1
        t0=time.time()
        chi=legendre_vec(N,q)
        n=np.arange(1,N+1)
        keep=chi[1:]!=0
        self.n=n[keep].astype(float); self.chi=chi[1:][keep].astype(float)
        self.x=pi*self.n**2/q
        self.N=N; self.prep=time.time()-t0
    def Lambda(self,t):
        s=0.5+1j*t
        term=np.exp((s/2)*log(self.q/pi)-s*np.log(self.n))*upper_gamma(s/2,self.x)
        return 2*np.real(np.sum(self.chi*term))
    def zeros(self,k=10,step=0.02,tmax=60):
        zs=[]; t=step; f0=self.Lambda(t)
        while len(zs)<k and t<tmax:
            t1=t+step; f1=self.Lambda(t1)
            if f0*f1<0:
                a,b,fa=t,t1,f0
                for _ in range(40):
                    m=(a+b)/2; fm=self.Lambda(m)
                    if fa*fm<0: b=m
                    else: a,fa=m,fm
                zs.append((a+b)/2)
            t,f0=t1,f1
        return zs

if __name__=="__main__":
    q=int(sys.argv[1]); k=int(sys.argv[2]) if len(sys.argv)>2 else 10
    L=Lchi(q); print("q=%d  terms=%d  prep %.1fs"%(q,L.N,L.prep)); sys.stdout.flush()
    t0=time.time(); zs=L.zeros(k)
    print("first %d zeros of L(s,(./%d)) on Re s=1/2  (%.0fs):"%(len(zs),q,time.time()-t0))
    for i,g in enumerate(zs,1): print("  gamma_%d = %.9f"%(i,g))
    np.save('zeros_%d.npy'%q,np.array(zs))
