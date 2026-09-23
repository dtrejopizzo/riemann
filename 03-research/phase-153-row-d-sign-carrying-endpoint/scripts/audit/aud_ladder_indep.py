import numpy as np, math
from scipy.special import psi
from numpy.polynomial.legendre import leggauss
T=math.log(2); L=2*T
GV={'0.45':[0.0168,0,-0.0494,0,-0.0899,0,0.5822,0,-1,0,0.6515],
    '0.30':[0.0179,0,-0.0518,0,-0.0828,0,0.5702,0,-1,0,0.6572]}
def Fpoly(a,g):
    p=0.5+a;q=0.5-a
    w=np.zeros(9)
    for k in range(5): w[2*k]=math.comb(4,k)*(T*T)**(4-k)*(-1)**k
    H=np.zeros(9+len(g))
    for i,gi in enumerate(g):
        if gi: H[i:i+9]+=gi*w
    def der(c,n):
        for _ in range(n): c=np.array([c[i]*i for i in range(1,len(c))])
        return c
    n=len(H); d4=np.zeros(n); d2=np.zeros(n)
    t=der(H,4); d4[:len(t)]=t
    t=der(H,2); d2[:len(t)]=t
    return d4-(p*p+q*q)*d2+p*p*q*q*H
xq,wq=leggauss(200)
for astr in ('0.45','0.30'):
    a=float(astr); f=Fpoly(a,GV[astr]); fv=lambda x: np.polyval(f[::-1],x)
    def c(r):
        r=np.atleast_1d(np.asarray(r,float)); lo=-T; hi=T-r
        t=0.5*np.outer(hi-lo,xq)+0.5*(hi+lo)[:,None]; w=0.5*(hi-lo)[:,None]*wq
        return np.sum(w*fv(t)*fv(t+r[:,None]),axis=1)
    N2=float(c(0.0)[0]); m0a=2*math.log(math.pi)-psi(0.25+a/2)-psi(0.25-a/2)
    xg,wg=leggauss(50); edges=np.linspace(0,L,201)
    R=np.concatenate([0.5*(hi-lo)*xg+0.5*(hi+lo) for lo,hi in zip(edges[:-1],edges[1:])])
    W=np.concatenate([0.5*(hi-lo)*wg for lo,hi in zip(edges[:-1],edges[1:])])
    CV=c(R); WC=W*CV
    J=20000; tot=0.0
    for s in (1,-1):
        b=2*np.arange(J+1)+0.5+s*a
        for i0 in range(0,len(b),400):
            bb=b[i0:i0+400]
            tot+=float(np.sum(2*N2/bb-2*(np.exp(-np.outer(bb,R))@WC)))
    prim=sum(2*(math.log(n)*(n**a+n**(-a)))/math.sqrt(n)*float(c(math.log(n))[0]) for n in (2,3))
    q=tot-m0a*N2-prim
    A=fv(np.array([T]))[0]**2
    print(f"a={astr}: N2={N2:.12f} q(J={J})={q:.9f} q/N2={q/N2:.8f}  tail<{A/J:.2e}")
