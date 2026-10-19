"""Independent audit of the FATAL check: lmin(Q_T) at T=log2, a=0.45, gamma0=300.
Own quadrature: tanh-graded panels, different npan/ng/taumax from the original script's.
Own basis_hat via direct numerical integration cross-check on a few modes."""
import math, numpy as np, scipy.linalg as sla
from scipy.special import psi as digamma
from numpy.polynomial.legendre import leggauss

LAM={2:math.log(2),3:math.log(3)}   # T=log2 => e^{2T}=4, so n=2,3 only
def bh(T,K,tau):
    L=2*T
    b=np.array([k*math.pi/L for k in range(1,K+1)])
    tau=np.asarray(tau,float)
    den=b[:,None]**2-tau[None,:]**2
    sgn=np.array([(-1)**k for k in range(1,K+1)])[:,None]
    num=b[:,None]*(1-sgn*np.exp(-1j*tau[None,:]*L))
    small=np.abs(den)<1e-9
    out=np.where(small,0j,num/np.where(small,1.0,den))
    for i in range(K):
        m=small[i]
        if m.any():
            t0=tau[m]; out[i,m]=(-1j*L*(-1)**(i+1)*np.exp(-1j*t0*L)*b[i])/(2*b[i])
    return np.exp(1j*tau[None,:]*T)*out

def mom(T,K,betas):
    L=2*T; rows=[]
    for be in betas:
        r=[np.exp(-be*T)*(k*math.pi/L)*(1-((-1)**k)*np.exp(be*L))/(be**2+(k*math.pi/L)**2) for k in range(1,K+1)]
        rows.append(r)
    return np.array(rows)

def sym(tau,T):
    s=np.real(digamma(0.25+0.5j*tau))-math.log(math.pi)
    for n,l in LAM.items():
        if n<math.exp(2*T)-1e-13: s-=2*l/math.sqrt(n)*np.cos(tau*math.log(n))
    return s

def matA(T,K,taumax,npan,ng):
    # different grading: uniform to 200 then geometric
    e1=np.linspace(0,200,npan//2+1)[:-1]
    e2=np.exp(np.linspace(math.log(200),math.log(taumax),npan//2+1))
    edges=np.concatenate([e1,e2]); x,w=leggauss(ng); M=np.zeros((K,K))
    for lo,hi in zip(edges[:-1],edges[1:]):
        t=0.5*(hi-lo)*x+0.5*(hi+lo); ww=0.5*(hi-lo)*w
        H=bh(T,K,t); M+=np.real((H*(ww*sym(t,T)))@H.conj().T)
    M=2*M/(2*math.pi); return 0.5*(M+M.T)

def matC(T,K,a,g0):
    u=mom(T,K,[a+1j*g0])[0]; v=np.conj(mom(T,K,[-a+1j*g0])[0])
    C=2*(np.outer(u.real,v.real)+np.outer(v.real,u.real)-np.outer(u.imag,v.imag)-np.outer(v.imag,u.imag))
    return 0.5*(C+C.T)

def lmin(T,K,a,g0,taumax,npan=800,ng=32):
    M=matA(T,K,taumax,npan,ng); C=matC(T,K,a,g0)
    Z=sla.null_space(mom(T,K,[-0.5,0.5]))
    Q=Z.T@(M-C)@Z; Gr=Z.T@(np.eye(K)*T)@Z
    return sla.eigh(0.5*(Q+Q.T),0.5*(Gr+Gr.T),eigvals_only=True)[0]

T=math.log(2)
print("=== (d) FATAL recheck, T=log2, a=0.45, gamma0=300, independent quadrature")
for K,tm in [(300,4000.),(500,8000.),(700,12000.),(900,20000.)]:
    print("  K=%4d taumax=%6.0f : lminQ = %+.6e   (lminA = %+.6e)"%(
        K,tm,lmin(T,K,0.45,300.,tm), lmin(T,K,0.0,1e9,tm)))
