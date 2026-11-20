import numpy as np
from scipy.integrate import quad
from scipy.special import zeta, gamma, digamma
from scipy.linalg import null_space
from math import pi,cos,cosh,exp,sqrt,log
C=-2*pi**(-.25)*gamma(.25)*(-1.4603545088095868)
Zc=zeta(1.5)-zeta(2.)
def tau(y):
    if y<.5:return 1/sqrt(y)-1+tau(1/y)/sqrt(y)
    n=np.arange(1,int(sqrt(42/(pi*y)))+2)
    return 2*np.sum(np.exp(-pi*y*n*n))
def profile(x):
    y=exp(2*x); ds=np.arange(2,int(sqrt(42/(pi*y)))+3)
    return 2*exp(x/2)*(sum((d**(-.5)-1/d)*tau(d*d*y) for d in ds)-tau(y)*Zc)
def calc(T,ks):
    w=np.array(ks)*pi/(2*T); n=len(ks)
    def basis(i,x):return (-1)**((ks[i]-1)//2)*cos(w[i]*x)/sqrt(T)
    c=2*w*cosh(T/2)/(sqrt(T)*(w*w+.25)); B=null_space(c[None,:])
    mv=np.array([quad(lambda x:basis(i,x)*profile(x),-T,T,epsabs=1e-11,limit=150)[0] for i in range(n)])
    def fourier(i,t):
        if abs(t-w[i])<1e-7:return (-1)**((ks[i]-1)//2)*sqrt(T)
        return 2*w[i]*cos(t*T)/(sqrt(T)*(w[i]*w[i]-t*t))
    arch=np.zeros((n,n))
    # weighted Fourier integration to 10000, tail included numerically crude
    for i in range(n):
      for j in range(i,n):
        val=quad(lambda t:(digamma(.25+.5j*t).real-log(pi))*fourier(i,t)*fourier(j,t),0,1000,epsabs=1e-8,limit=1200)[0]/pi
        arch[i,j]=arch[j,i]=val
    comb=np.zeros((n,n))
    for d in range(2,int(exp(2*T))+1):
      # Lambda
      fac=[];v=d;p=2
      while p*p<=v:
        if v%p==0:
          fac.append(p)
          while v%p==0:v//=p
        p+=1
      if v>1:fac.append(v)
      if len(fac)!=1:continue
      shift=log(d);weight=2*log(fac[0])/sqrt(d)
      for i in range(n):
       for j in range(n):comb[i,j]+=weight*quad(lambda x:basis(i,x)*basis(j,x+shift),-T,T-shift,epsabs=1e-12)[0]
    Q=arch-comb; R=B.T@(Q-C*np.outer(mv,mv))@B
    ev,vec=np.linalg.eigh(R);a=B@vec[:,0]
    print('T',T,'ks',ks,'ev',ev[0],'Q',a@Q@a,'Clb',C*(mv@a)**2,'coef',a.tolist(),flush=True)
for T in [.8,1.,1.35,2.]:
 calc(T,[1,3]);calc(T,[1,3,5,7])
