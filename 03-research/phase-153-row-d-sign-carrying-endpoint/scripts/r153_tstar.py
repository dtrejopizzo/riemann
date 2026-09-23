"""R153 round 2, Task 3: detection threshold T*(a) = inf{T : A_T^(a) not >= 0 on P_T^(a)}.
Reuses the auditor's mesh-free spectral sine assembly (scripts/audit/aud_spectral.py),
extended so the contact set {n : n < e^{2T}} is recomputed at every T.  DIAGNOSTIC-NUMERIC."""
import math, sys, numpy as np, scipy.linalg as sla
sys.path.insert(0, 'audit')
import aud_spectral as A
from numpy.polynomial.legendre import leggauss

LAM = {}
for n in range(2, 200):
    for p in (2,3,5,7,11,13):
        k=1; v=p
        while v<=n:
            if v==n: LAM[n]=math.log(p)
            v*=p; k+=1

def symbol(tau,a,primes,T):
    s=np.zeros_like(tau)
    for sg in (+1,-1): s+=np.real(A.digamma(0.25+sg*a/2+0.5j*tau))
    s-=2*math.log(math.pi)
    for n,lam in primes:
        cn=lam*(n**a+n**(-a)); s-=2*cn/math.sqrt(n)*np.cos(tau*math.log(n))
    return s

def lmin(T,K,a,taumax=4000.0,npan=300,ng=20):
    primes=[(n,l) for n,l in sorted(LAM.items()) if n<math.exp(2*T)-1e-13]
    edges=np.concatenate([np.linspace(0,50,npan//2+1)[:-1],
                          np.exp(np.linspace(math.log(50),math.log(taumax),npan//2+1))])
    x,w=leggauss(ng); M=np.zeros((K,K))
    for lo,hi in zip(edges[:-1],edges[1:]):
        t=0.5*(hi-lo)*x+0.5*(hi+lo); ww=0.5*(hi-lo)*w
        H=A.basis_hat(T,K,t); m=symbol(t,a,primes,T)
        M+=np.real(H@np.diag(ww*m)@H.conj().T)
    M=2*M/(2*math.pi); G=np.eye(K)*T
    C=A.moments(T,K,[-0.5-a,-0.5+a,0.5-a,0.5+a]); Z=sla.null_space(C)
    w_,_=sla.eigh(Z.T@(0.5*(M+M.T))@Z, Z.T@G@Z)
    return w_[0]

def tstar(a,K,lo=0.30,hi=1.05):
    if lmin(lo,K,a)<0: return float('nan')
    if lmin(hi,K,a)>0: return float('inf')
    for _ in range(34):
        mid=0.5*(lo+hi)
        if lmin(mid,K,a)>0: lo=mid
        else: hi=mid
    return 0.5*(lo+hi)

if __name__=="__main__":
    Ks=[int(x) for x in (sys.argv[1:] or ['100','160'])]
    print("a     " + "  ".join(f"T*(K={K})" for K in Ks) + "     T*-log2")
    for a in [0.05,0.06,0.07,0.08,0.09,0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50]:
        vals=[tstar(a,K) for K in Ks]
        print(f"{a:.2f}  " + "  ".join(f"{v:.5f}" for v in vals) + f"   {vals[-1]-math.log(2):+.5f}")
        sys.stdout.flush()
