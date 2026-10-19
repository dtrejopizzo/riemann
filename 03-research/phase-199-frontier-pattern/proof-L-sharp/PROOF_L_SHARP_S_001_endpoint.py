import numpy as np
from scipy.special import exp1, psi
V=5.0; K=8; dv=2e-5
v=np.arange(0,V,dv); N=len(v)
def c(x): return 2*np.real(np.exp(2j*np.pi*x)/(1-2j*np.pi*x))
def cL(x):
    a=1-2j*np.pi*x
    return 2*np.real(np.e*exp1(a)/a)
U=[];UL=[]
for k in range(1,K+1):
    x=k*np.exp(v); w=np.exp(v/2)
    U.append(-w*c(x)); UL.append(-w*(cL(x)+v*c(x)))
U=np.array(U);UL=np.array(UL)
P=4*N; F=np.fft.rfft(U,n=P,axis=1)*dv
tau=2*np.pi*np.fft.rfftfreq(P,d=dv)
Th=np.real(psi(0.25+0.5j*tau))-np.log(np.pi)
dt=tau[1]-tau[0]
wts=np.full(len(tau),2.0); wts[0]=1.0  # even integrand: integrate over R
A=(F*Th*wts)@F.conj().T*dt/(2*np.pi)
B=(U@UL.T)*dv
M=np.real(A)-(B+B.T)
np.set_printoptions(precision=5,linewidth=200)
print(M)
for k in range(1,K+1):
    pred=(np.log(k)*(1-np.exp(-V))-(1-(1+V)*np.exp(-V)))/(2*np.pi**2*k**2)
    print(k,M[k-1,k-1],pred, M[k-1,k-1]*k**2)
print("sum diag",np.trace(M),"total",M.sum())
print("eig",np.linalg.eigvalsh(M))
from scipy.integrate import quad
from scipy.special import digamma
I=quad(lambda t: (np.real(psi(0.25+0.5j*t))-np.log(np.pi))/(0.25+t*t),-np.inf,np.inf,limit=500)[0]/(2*np.pi)
print("pol int",I, digamma(1.5)-np.log(np.pi))
# polar
rho0=1.0; rho1=np.e*exp1(1.0)
Fp=rho0/(0.5+1j*tau)  # transform of rho0 e^{v/2} on v<0 with e^{i tau v}
lin=np.real((F*Th*wts)@Fp.conj())*dt/(2*np.pi)
Qpp=rho0**2*(I+2)-2*rho0*rho1
print("Qpp",Qpp,"cross sum",lin.sum(),"Qtotal",M.sum()+2*lin.sum()+Qpp)
