import numpy as np, sys
from scipy.special import psi
from scipy.integrate import quad
xi0=float(sys.argv[1]); L=float(sys.argv[2]); ph=float(sys.argv[3])
X=np.linspace(1,L,1601)[1:-1]; dX=X[1]-X[0]
w=np.exp(-1/((X-1)*(L-X)))*np.cos(2*np.pi*xi0*X+ph)
wl=w*np.log(X)
rho0=w.sum()*dX; rho1=wl.sum()*dX
K=int(3*xi0)+6; V=np.log((xi0+6)); dv=1e-4
v=np.arange(0,V,dv)
U=[];UL=[]
for k in range(1,K+1):
    x=k*np.exp(v)
    C=np.zeros_like(x);CL=np.zeros_like(x)
    for i in range(0,len(x),4000):
        cs=np.cos(2*np.pi*np.outer(x[i:i+4000],X))
        C[i:i+4000]=2*cs@w*dX; CL[i:i+4000]=2*cs@wl*dX
    U.append(-np.exp(v/2)*C); UL.append(-np.exp(v/2)*(CL+v*C))
U=np.array(U);UL=np.array(UL)
P=8*len(v); F=np.fft.rfft(U,n=P,axis=1)*dv
tau=2*np.pi*np.fft.rfftfreq(P,d=dv)
Th=np.real(psi(0.25+0.5j*tau))-np.log(np.pi); dt=tau[1]-tau[0]
wts=np.full(len(tau),2.0); wts[0]=1
A=np.real((F*Th*wts)@F.conj().T)*dt/(2*np.pi); B=(U@UL.T)*dv
M=A-(B+B.T)
Fp=1/(0.5+1j*tau)
lin=np.real((F*Th*wts)@Fp.conj())*dt/(2*np.pi)
c0=-1.1082399118708237
Qpp=c0*rho0**2-2*rho0*rho1
print("xi0",xi0,"L",L,"ph",ph,"harm",M.sum(),"diag",np.trace(M),"polcross",2*rho0*lin.sum(),"Qpp",Qpp,"Q(G,G)",M.sum()+2*rho0*lin.sum()+Qpp, "edge U(V)",np.abs(U[:,-1]).max())
print("diag k:",np.round(np.diag(M)[:12],7))
