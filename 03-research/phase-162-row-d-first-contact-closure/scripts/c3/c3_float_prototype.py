import numpy as np, scipy.special as sp, sys
from numpy.polynomial.legendre import leggauss
T=0.5*np.log(5); V={2:2*np.log(2)/np.sqrt(2),3:2*np.log(3)/np.sqrt(3),4:2*np.log(2)/2}
SV=sum(V.values())
def m(t): return sp.digamma(0.25+0.5j*t).real-np.log(np.pi)
def s(t): return m(t)-sum(v*np.cos(t*np.log(n)) for n,v in V.items())
tauN=float(sys.argv[1]); K=int(sys.argv[2])
sinf=m(tauN)-SV
x,w=leggauss(40); X=[];W=[]
for lo in np.arange(0,tauN,0.5): X.append(lo+0.25*(x+1));W.append(0.25*w)
X=np.concatenate(X);W=np.concatenate(W)
J=np.array([sp.spherical_jn(l,X*T) for l in range(K)])
g=(sinf-s(X))*W
G=(J*g)@J.T
l=np.arange(K); sq=np.sqrt(2*l+1)
sign=np.array([[ (0 if (a-b)%2 else (1 if ((b-a)//2)%2==0 else -1)) for b in l] for a in l])
G=(2*T/np.pi)*np.outer(sq,sq)*sign*G
B=sinf*np.eye(K)-G
c=np.sqrt((2*l+1)/(2*T))*2*T*np.array([sp.spherical_in(k,T/2) for k in l])
print("sinf",sinf,"c*",T*tauN)
for par in (0,1):
    idx=np.arange(par,K,2); cc=c[idx]
    Q,_=np.linalg.qr(cc.reshape(-1,1),mode='complete'); P=Q[:,1:]
    ev=np.linalg.eigvalsh(P.T@B[np.ix_(idx,idx)]@P)
    print(par, ev[:4])
for par in (0,1):
    idx=np.arange(par,K,2); cc=c[idx]
    Q,_=np.linalg.qr(cc.reshape(-1,1),mode='complete'); P=Q[:,1:]
    ev,U=np.linalg.eigh(P.T@B[np.ix_(idx,idx)]@P)
    v=P@U[:,0]
    print(par, ' '.join('%d:%.1e'%(idx[j],abs(v[j])) for j in range(0,len(idx),8)))
