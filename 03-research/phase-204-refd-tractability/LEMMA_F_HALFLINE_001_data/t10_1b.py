# exact falsifier check: rho=phi(om)+c phi(om/2), phi bump at om0=1.3 (w=0.04): predicted F''(0)=2 lam A1 (log2)^2 c(1+2c), A1=int phi^2. NUMERICO.
import math,numpy as np
lam=math.sqrt(15)
def phi(om,c0=1.3,w=0.04): t=(om-c0)/w; return np.where(np.abs(t)<1,np.exp(-1/np.maximum(1-t*t,1e-300)),0.0)
X=60; dy=1e-5; ys=np.arange(0,math.log(X),dy); s=np.exp(ys); wq=dy*s
for c in (-0.05,-0.25,-0.45,0.1):
    S0=np.zeros_like(s);S1=np.zeros_like(s);S2=np.zeros_like(s)
    for n in range(1,X+1):
        v=phi(n*s)+c*phi(n*s/2); l=math.log(n); S0+=v;S1+=l*v;S2+=l*l*v
    F2=2*lam*np.sum(wq*(S1**2+S0*S2)); A1=np.sum(wq*phi(s)**2)
    print(c,F2,2*lam*A1*math.log(2)**2*c*(1+2*c))
