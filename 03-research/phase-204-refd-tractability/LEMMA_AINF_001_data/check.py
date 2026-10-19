import numpy as np, mpmath as mp
from numpy.polynomial.legendre import leggauss, Legendre
mp.mp.dps=30
C0=mp.digamma(0.25)-mp.log(mp.pi)
m=lambda t: mp.re(mp.digamma(0.25+0.5j*t))-mp.log(mp.pi)
t0=mp.findroot(m,6.29); print("C0",C0,"t0",t0,"m(6.28)",m(6.28),"m(3)",m(3))
phi1=lambda x: mp.nsum(lambda k: 4*(k+.25)/((x+4*(k+.25)**2)**2),[0,mp.inf])
print("B=phi'(t0^2)",phi1(t0**2))
t0=float(t0)
K=lambda u: 2*np.exp(1.5*u)/np.expm1(2*u)
def nminus(T,N=48):
    xg,wg=leggauss(120)
    # orthonormal Legendre on (-T,T)
    def basis(x): return np.array([Legendre.basis(n)(x/T)*np.sqrt((2*n+1)/(2*T)) for n in range(N)])
    kap=float(mp.log(mp.coth(T/2))+mp.pi-2*mp.atan(mp.e**T))
    # u-quadrature on (0,2T): substitution u=2T*s^2 to tame 1/u
    sg,sw=leggauss(400); s=(sg+1)/2; ws=sw/2
    u=2*T*s**2; du=4*T*s*ws
    M=np.zeros((N,N))
    for ui,dui in zip(u,du):
        a,b=-T,T-ui; x=(b-a)/2*xg+(a+b)/2; w=wg*(b-a)/2
        Bx=basis(x); Bxu=basis(x+ui)
        C=(Bxu*w)@Bx.T; C=(C+C.T)/2
        M+=(np.eye(N)-C)*K(ui)*dui
    M+= (C0f+kap)*np.eye(N)
    ev=[n%2==0 for n in range(N)]
    E=np.array(ev); Me=M[np.ix_(E,E)]; Mo=M[np.ix_(~E,~E)]
    return [(np.linalg.eigvalsh(X)<0).sum() for X in (M,Me,Mo)]
C0f=float(C0)
for T in [0.5*np.log(3),1,0.5*np.log(15),2,3]:
    Ntot=int(np.ceil(2*T*t0/np.pi))-1
    print(f"T={T:.4f} 2Tt0/pi={2*T*t0/np.pi:.3f} N={Ntot} Nev={(Ntot+1)//2} Nodd={Ntot//2} galerkin(n-,ev,odd)={nminus(T)}")
