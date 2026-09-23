import math,sys,numpy as np,core,scipy.linalg as sla
sys.path.insert(0,'..')
K=240
def qD(T,K=K):
    l,p,vec=core.lam_min(T,K,codim=4,want_vec=True)
    G2=core.assemble(T,K,order=2)          # symbol g''
    nrm=T*np.dot(vec,vec)
    return l, -float(vec@G2@vec)/nrm, p    # D symbol = -g''
print("T      mu(T)        <D F,F>/|F|^2")
for T in [0.69,0.72,0.75,0.78,0.80,0.81]:
    l,q,p=qD(T); print(f"{T:.3f} {l: .5e} {q: .6f}")
# exact A^{(a)} lmin via aud-style doubled symbol, codim-4 exact moments
from scipy.special import psi as digamma
from numpy.polynomial.legendre import leggauss
import aud_spectral as A2
def sym_a(tau,a,T):
    s=np.zeros_like(tau)
    for sg in (+1,-1): s+=np.real(digamma(0.25+sg*a/2+0.5j*tau))
    s-=2*math.log(math.pi)
    for n,l in core.contacts(T):
        s-=2*l*(n**a+n**(-a))/math.sqrt(n)*np.cos(tau*math.log(n))
    return s
def lmin_a(T,a,K=K,taumax=4000.,npan=400,ng=24):
    edges=np.concatenate([np.linspace(0,50,npan//2+1)[:-1],np.exp(np.linspace(math.log(50),math.log(taumax),npan//2+1))])
    x,w=leggauss(ng); M=np.zeros((K,K))
    for lo,hi in zip(edges[:-1],edges[1:]):
        t=0.5*(hi-lo)*x+0.5*(hi+lo); ww=0.5*(hi-lo)*w
        H=A2.basis_hat(T,K,t); M+=np.real(H@np.diag(ww*sym_a(t,a,T))@H.conj().T)
    M=0.5*(M+M.T)*2/(2*math.pi)
    C=A2.moments(T,K,[-0.5-a,-0.5+a,0.5-a,0.5+a]); Z=sla.null_space(C)
    return sla.eigh(Z.T@M@Z,Z.T@(T*np.eye(K))@Z,eigvals_only=True)[0]
def root(f,lo,hi):
    for _ in range(40):
        m=0.5*(lo+hi)
        if f(m)>0: lo=m
        else: hi=m
    return 0.5*(lo+hi)
print("\n a       T*(exact)  T*(2nd order)  2mu+a^2<D> at T*exact   lmin_a at T*(2nd)")
for a in (0.001,0.005,0.01,0.03):
    Te=root(lambda T: lmin_a(T,a),0.60,1.00)
    T2=root(lambda T: 2*core.lam_min(T,K,codim=4)[0]+a*a*qD(T)[1],0.60,1.00)
    l,q,_=qD(Te)
    print(f"{a:<7} {Te:.5f}   {T2:.5f}      {2*l+a*a*q: .3e}            {lmin_a(T2,a): .3e}")
