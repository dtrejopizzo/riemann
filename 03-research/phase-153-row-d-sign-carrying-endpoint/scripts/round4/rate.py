"""Hellmann-Feynman / Hadamard rate for lambda(T), away from thresholds.
dlam/dT = -(1/T)(1/2pi) int tau g'(tau) |Fhat|^2 dtau   (Gamma shape + prime transport)
          - (1/T) sum_pm (pm) c_pm int t F(t) e^{pm t/2} dt   (two-Tate projection drift)
Prime transport term equals +(2 w_n log n / T) c'_F(log n).  No rank-two endpoint term
appears between thresholds (the contact set is locally constant)."""
import math,sys,numpy as np,core,scipy.linalg as sla
from numpy.polynomial.legendre import leggauss
import aud_spectral as A

def gprime(tau,T,part):
    tau=np.asarray(tau,float)
    if part=='gamma':
        z=0.25+0.5j*tau
        from core import psi2
        # d/dtau Re psi(1/4+i tau/2) = -(1/2) Im psi'(1/4+i tau/2)
        import mpmath
        return -0.5*np.imag(psi1(z))
    raise 0
def psi1(z,M=60):
    z=np.asarray(z,dtype=complex); acc=np.zeros_like(z)
    for k in range(M): acc+=1.0/(z+k)**2
    w=z+M
    return acc + (1/w+0.5/w**2+1/(6*w**3)-1/(30*w**5)+1/(42*w**7))

def weighted(T,K,vec,f):
    """(1/2pi) int f(tau) |Fhat|^2 dtau, mesh-free, same quadrature as core.assemble"""
    npan,ng,taumax=400,24,4000.0
    edges=np.concatenate([np.linspace(0,50,npan//2+1)[:-1],np.exp(np.linspace(math.log(50),math.log(taumax),npan//2+1))])
    x,w=leggauss(ng); tot=0.0
    for lo,hi in zip(edges[:-1],edges[1:]):
        t=0.5*(hi-lo)*x+0.5*(hi+lo); ww=0.5*(hi-lo)*w
        H=A.basis_hat(T,K,t); Fh=vec@H
        tot+=np.sum(ww*f(t)*np.abs(Fh)**2)
    return 2*tot/(2*math.pi)

def tmom(T,K,beta):
    """int t phi_k(t) e^{beta t} dt by complex step in beta"""
    h=1e-20
    return np.imag(core.mom(T,K,beta+1j*h))/h

def rate(T,K=240):
    lam,par,vec=core.lam_min(T,K,want_vec=True)
    nrm=math.sqrt(T*np.dot(vec,vec)); vec=vec/nrm
    tG=-(1/T)*weighted(T,K,vec,lambda tt: tt*(-0.5*np.imag(psi1(0.25+0.5j*tt))))
    terms={'Gamma':tG}
    for n,l in core.contacts(T):
        L=math.log(n); wn=l/math.sqrt(n)
        terms[f'transport n={n}']=-(1/T)*weighted(T,K,vec,lambda tt,L=L,wn=wn: tt*2*wn*L*np.sin(tt*L))
    M=core.assemble(T,K); r=M@vec-lam*T*vec
    P=np.array([core.mom(T,K,0.5),core.mom(T,K,-0.5)]).T
    c,_,_,_=np.linalg.lstsq(P,r,rcond=None)
    tc=-(1/T)*(c[0]*np.dot(vec,tmom(T,K,0.5))-c[1]*np.dot(vec,tmom(T,K,-0.5)))
    terms['Tate drift']=tc
    return lam,par,terms

if __name__=="__main__":
    for T in (0.60,0.65,0.69,math.log(2)):
        lam,par,tm=rate(T)
        s=sum(tm.values()); h=1e-4
        fd=(core.lam_min(T+h,240)[0]-core.lam_min(T-h,240)[0])/(2*h)
        print(f"T={T:.4f} lam={lam:.6e} ({par})")
        for k,v in tm.items(): print(f"    {k:<16} {v: .6e}")
        print(f"    SUM              {s: .6e}   finite-diff {fd: .6e}   c_HF={-s/lam:.3f}  c_FD={-fd/lam:.3f}")
        sys.stdout.flush()
