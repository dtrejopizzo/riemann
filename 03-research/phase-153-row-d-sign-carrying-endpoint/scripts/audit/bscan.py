import math,numpy as np,scipy.linalg as sla
from scipy.special import psi as digamma
from numpy.polynomial.legendre import leggauss
from aud_spectral import basis_hat, moments
def lam(T,K,b,drop_arch=False,w2on=True,w3=None,taumax=4000.,npan=400,ng=24):
    edges=np.concatenate([np.linspace(0,50,npan//2+1)[:-1],
        np.exp(np.linspace(math.log(50),math.log(taumax),npan//2+1))])
    x,w=leggauss(ng); M=np.zeros((K,K))
    W3=math.log(3)/math.sqrt(3) if w3 is None else w3
    W2=math.log(2)/math.sqrt(2)
    for lo,hi in zip(edges[:-1],edges[1:]):
        t=0.5*(hi-lo)*x+0.5*(hi+lo); ww=0.5*(hi-lo)*w
        H=basis_hat(T,K,t)
        m=np.zeros_like(t) if drop_arch else np.real(digamma(0.25+0.5j*t))-math.log(math.pi)
        if w2on: m-=2*W2*np.cos(t*math.log(2))
        if b is not None: m-=2*W3*np.cos(t*b)
        M+=np.real(H@np.diag(ww*m)@H.conj().T)
    M=2*M/(2*math.pi); G=np.eye(K)*T
    C=moments(T,K,[-0.5,0.5]); Z=sla.null_space(C)
    return sla.eigh(Z.T@(0.5*(M+M.T))@Z,Z.T@G@Z,eigvals_only=True)[0]
if __name__=="__main__":
    T=math.log(2)
    for K in (120,200):
        print("K=",K,"  arch-only lam_min(G-m0|P_T) =",f"{lam(T,K,None,w2on=False): .6e}")
        for b in [0.9,1.0,1.05,1.08,1.09,1.095,1.0986123,1.10,1.105,1.12,1.2,1.3,1.38]:
            print(f"   b={b:.7f} lam={lam(T,K,b): .6e}"+("  <-log3" if abs(b-math.log(3))<1e-6 else ""))
