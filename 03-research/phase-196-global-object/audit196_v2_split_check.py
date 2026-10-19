import numpy as np
from scipy.integrate import quad
T=0.6
def bump(t): return np.exp(-1/(1-(t/T)**2)) if abs(t)<T else 0.0
base=[lambda t,k=k: bump(t)*t**k for k in range(3)]
M=np.array([[quad(lambda t:b(t)*np.exp(s*t/2),-T,T)[0] for b in base] for s in (1,-1)])
# choose coefficients c with M c=0, c0=1
c=np.linalg.solve(M[:,1:],-M[:,0]); c=np.r_[1,c]
F=lambda t: sum(ci*b(t) for ci,b in zip(c,base))
print("A,B",[quad(lambda t:F(t)*np.exp(s*t/2),-T,T)[0] for s in (1,-1)])
f=lambda x: abs(x)**-.5*F(np.log(abs(x))) if 0<abs(x) and abs(np.log(abs(x)))<T else 0.0
X=np.exp(T)
def cF(u): return quad(lambda t:F(t)*F(t-u),-T,T,limit=200)[0]
def R(n,a):
    g=lambda x: np.sqrt(n)*f(n*x)*f(x-a)
    pts=[s*X/n for s in (-1,1)]+[s*np.exp(-T)/n for s in(-1,1)]+[a+s*X for s in(-1,1)]+[a+s*np.exp(-T) for s in(-1,1)]
    lo,hi=-X/n,X/n; return quad(g,lo,hi,points=[p for p in pts if lo<p<hi],limit=400)[0]
def fh(xi,n=1):
    g=lambda x: np.sqrt(n)*f(n*x)*np.cos(2*np.pi*x*xi)   # f even, real
    return 2*quad(g,np.exp(-T)/n,X/n,limit=400)[0]
for n in (2,3):
    amax=int(np.floor(X*(1+1/n)))
    poisson=sum(R(n,a) for a in range(-amax,amax+1))
    fourier=fh(0,n)*fh(0)+2*sum(fh(j,n)*fh(j) for j in range(1,80))
    print(n,"R0",R(n,0),"2cF",2*cF(np.log(n)),"Aff_n",poisson-R(n,0),"Sha(x)",poisson,"Sha(xi)",fourier)
