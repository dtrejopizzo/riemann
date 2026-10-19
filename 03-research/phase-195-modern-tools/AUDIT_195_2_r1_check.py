import numpy as np
from scipy.special import psi
from numpy.polynomial.legendre import leggauss
T=0.6; S=[2,3]; s1=0.85
tg,tw=leggauss(200); t=T*tg; wt=T*tw; F=(1-(t/T)**2)**4
def Phi(s,d=0):  # s array
    E=np.exp(np.outer(s-0.5,t)); return (E*(F*t**d*wt)).sum(1)
def lxi(s): # xi_S'/xi_S
    r=-0.5*np.log(np.pi)+0.5*psi(s/2)
    for p in S: r=r+np.log(p)*p**(-s)/(1-p**(-s))*(-1)  # d/ds -log(1-p^-s) = -log p p^-s/(1-p^-s)
    return r
def logxi(s):
    from scipy.special import loggamma
    r=-s/2*np.log(np.pi)+loggamma(s/2)
    for p in S: r=r-np.log(1-p**(-s))
    return r
L=80; tau=np.linspace(-L,L,32001); dt=tau[1]-tau[0]
# LHS: (1/2pi) int 2 Re(xi'/xi)(1/2+it) |F^|^2
s=0.5+1j*tau; Fh=Phi(s); lhs=(1/(2*np.pi))*np.sum(2*np.real(lxi(s))*abs(Fh)**2)*dt
sg,sw=leggauss(60); sig=0.5+(s1-0.5)*(sg+1)/2; sw=sw*(s1-0.5)/2
D1=D2=0
for a,w in zip(sig,sw):
    z=a+1j*tau; P=Phi(z); dP=Phi(z,1)
    rho=np.exp(logxi(z)-logxi(1-z)); drho=rho*(lxi(z)+lxi(1-z))
    D1+=w*np.sum(abs(dP)**2)*dt; D2+=w*np.sum(abs(drho*P+rho*dP)**2)*dt
z=s1+1j*tau; P=Phi(z); dP=Phi(z,1); rho=np.exp(logxi(z)-logxi(1-z)); drho=rho*(lxi(z)+lxi(1-z))
dG=2*np.real(np.conj(P)*dP); dRG=2*np.real(np.conj(rho*P)*(drho*P+rho*dP))
rhs=(D1-D2)/np.pi+np.sum(dRG-dG)*dt/(4*np.pi)
print(lhs,rhs)
