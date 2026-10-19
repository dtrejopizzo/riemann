import numpy as np
from scipy.special import loggamma, psi
T=0.6; S=[2,3]
x,w=np.polynomial.legendre.leggauss(400); t=T*x; wt=T*w
F=(1-(t/T)**2)**4
def Phi(s,d=0):  # s array
    E=np.exp(np.outer(s-0.5,t)); return (E*(F*t**d*wt)).sum(1)
def logxi(s):
    v=-s/2*np.log(np.pi)+loggamma(s/2)
    for p in S: v=v-np.log(1-p**(-s)+0j)
    return v
def dlogxi(s):
    v=-0.5*np.log(np.pi)+0.5*psi(s/2)
    for p in S: v=v-np.log(p)*p**(-s)/(1-p**(-s))
    return v
def d(s): return (logxi(s)-logxi(1-np.conj(s))).real
def dsig_d(s): return dlogxi(s).real+dlogxi(1-np.conj(s)).real
L=150.; nt=6000; tau=np.linspace(-L,L,nt+1); dtau=tau[1]-tau[0]
s=0.5+1j*tau
LHS=np.sum(dsig_d(s)*abs(Phi(s))**2)*dtau/(2*np.pi)
# area
ns=600; sig=0.5+(np.arange(ns)+0.5)*1.5/ns; ds=1.5/ns
tau2=tau+dtau/2*0.37
A=0
for sg in sig:
    ss=sg+1j*tau2; A+=np.sum(d(ss)*abs(Phi(ss,1))**2)*dtau*ds
pts=[1.0]+[1+2j*np.pi*k/np.log(p) for p in S for k in range(-60,61)]
src=sum(abs(Phi(np.array([z]))[0])**2 for z in pts)
s2=2+1j*tau; G=abs(Phi(s2))**2; dG=2*(Phi(s2,1)*np.conj(Phi(s2))).real
B=np.sum(d(s2)*dG-G*dsig_d(s2))*dtau
RHS=(4*A-2*np.pi*src-B)/(2*np.pi)
print(LHS,RHS, 4*A/(2*np.pi), src, B/(2*np.pi))
