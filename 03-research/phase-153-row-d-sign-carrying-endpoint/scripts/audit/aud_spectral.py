"""HOSTILE AUDIT R153: independent Galerkin for the Xi_a Weil form.
Spectral sine basis on (-T,T); archimedean channel evaluated as a FOURIER
MULTIPLIER directly from Prop 12.6's symbol (NOT via Theorem A's conjugation);
prime channel with c_n = Lambda(n)(n^a+n^{-a}).  Independent of rowd_assembly.
q(F) = (1/2pi) int [ sum_pm Re psi(1/4 pm a/2 + i tau/2) - 2 log pi
                     - sum_n 2 c_n n^{-1/2} cos(tau log n) ] |Fhat(tau)|^2 dtau
(For a = 0 this is A_T's form, halved-doubled: a=0 gives 2*A_T.)
"""
import math, numpy as np, scipy.linalg as sla
from scipy.special import psi as digamma
from numpy.polynomial.legendre import leggauss

def basis_hat(T,K,tau):
    # phi_k(t)=sin(k pi (t+T)/(2T)); hat phi_k(tau)=int phi_k e^{-i tau t} dt
    L=2*T; b=np.array([k*math.pi/L for k in range(1,K+1)])
    tau=np.asarray(tau)
    den=(b[:,None]**2-tau[None,:]**2)
    # handle near-singularity: limit value
    sgn=np.array([(-1)**k for k in range(1,K+1)])[:,None]
    num=b[:,None]*(1-sgn*np.exp(-1j*tau[None,:]*L))
    out=np.where(np.abs(den)<1e-9, 0.0+0.0j, num/np.where(np.abs(den)<1e-9,1.0,den))
    # exact limit at tau=b_k: num/den -> derivative
    for i in range(K):
        m=np.abs(den[i])<1e-9
        if m.any():
            t0=tau[m]; out[i,m]=(-1j*L*(-1)**(i+1)*np.exp(-1j*t0*L)*b[i])/(2*b[i])
    return np.exp(1j*tau[None,:]*T)*out

def moments(T,K,betas):
    L=2*T; rows=[]
    for be in betas:
        r=[]
        for k in range(1,K+1):
            b=k*math.pi/L
            r.append(math.exp(-be*T)*b*(1-((-1)**k)*math.exp(be*L))/(be**2+b**2))
        rows.append(r)
    return np.array(rows)

def symbol(tau,a,primes,T):
    s=np.zeros_like(tau)
    for sg in (+1,-1):
        z=0.25+sg*a/2+0.5j*tau
        s+=np.real(digamma(z))
    s-=2*math.log(math.pi)
    for n,lam in primes:
        cn=lam*(n**a+n**(-a))
        s-=2*cn/math.sqrt(n)*np.cos(tau*math.log(n))
    return s

def form(T,K,a,taumax=4000.0,npan=400,ng=24):
    lam={2:math.log(2),3:math.log(3)}
    primes=[(n,l) for n,l in lam.items() if n<math.exp(2*T)-1e-13]
    # graded panels on [0,taumax]
    edges=np.concatenate([np.linspace(0,50,npan//2+1)[:-1],
                          np.exp(np.linspace(math.log(50),math.log(taumax),npan//2+1))])
    x,w=leggauss(ng)
    M=np.zeros((K,K))
    for lo,hi in zip(edges[:-1],edges[1:]):
        t=0.5*(hi-lo)*x+0.5*(hi+lo); ww=0.5*(hi-lo)*w
        H=basis_hat(T,K,t)              # K x ng
        m=symbol(t,a,primes,T)
        W=(ww*m)
        M+=np.real(H@np.diag(W)@H.conj().T)
    M=2*M/(2*math.pi)                   # two halves (+-tau), 1/2pi
    G=np.zeros((K,K))
    for k in range(K): G[k,k]=T          # int sin^2 = L/2 = T
    return 0.5*(M+M.T),G,primes

def lmin(T,K,a):
    M,G,_=form(T,K,a)
    if a==0: bet=[-0.5,0.5]
    else: bet=[-0.5-a,-0.5+a,0.5-a,0.5+a]
    C=moments(T,K,bet)
    Z=sla.null_space(C)
    w,V=sla.eigh(Z.T@M@Z,Z.T@G@Z)
    return w[0],Z@V[:,0]

if __name__=="__main__":
    for T,lab in [(math.log(2),'log2'),(0.5*math.log(3),'half-log3')]:
        for K in (40,80,160,240):
            row=[]
            for a in (0.0,0.1,0.3,0.45,0.49):
                l,_=lmin(T,K,a)
                row.append(f"a={a}: {l: .5e}")
            print(lab,"K=",K," ".join(row))
        print()
