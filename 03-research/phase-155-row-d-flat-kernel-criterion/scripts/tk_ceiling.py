import numpy as np
from scipy.special import digamma
from scipy.linalg import eigh, toeplitz
T=0.5*np.log(3.0); M=24; d=2*T/M; P=2*np.pi/d
b0=2.00256170925026; b1=-0.00965443404485797
v2=2*np.log(2)/np.sqrt(2.0); a=2*T
def m(t): return np.real(digamma(0.25+0.5j*t))-np.log(np.pi)
def gh0(t):
    c1=0.5+1j*t; c2=-0.5+1j*t
    return 2*np.real(0.5*((np.exp(c1*a)-1)/c1+(np.exp(c2*a)-1)/c2))
def gh1(t):
    out=[]
    for c in (0.5+1j*t,-0.5+1j*t):
        out.append(((a*c-1)*np.exp(c*a)+1)/c**2)
    return 2*np.real(0.5*(out[0]-out[1]))
def S(t): return m(t)-v2*np.cos(t*np.log(2))+b0*gh0(t)+b1*gh1(t)
print("S(0)=",S(np.array([0.0]))[0],"sigma(0)=",m(np.array([0.0]))[0]-v2,"gh0(0)=",gh0(np.array([0.0]))[0])
from scipy.integrate import simpson
def bound(tau0,Mloc=M):
    n=1<<18
    x=np.linspace(tau0,tau0+P,n+1); Sv=S(x)
    cs=[]
    for l in range(Mloc):
        cs.append(simpson(Sv*np.exp(1j*l*d*x),x=x)/P)
    cs=np.array(cs)
    Tz=toeplitz(np.conj(cs),cs)   # T[k,j]=c_{j-k}
    w=np.linalg.eigvalsh(Tz)
    return w[0],w[-1],cs[0].real
for t0 in [0,5,10,20,30,60,100,200,500]:
    lo,hi,mean=bound(float(t0))
    print(f"tau0={t0:5d}  lambda_min={lo: .6f}  mean_S={mean: .4f}  lambda_max={hi: .4f}")
# Fejer kernel value at a few centres (n=M-1 degree), tau0=0
def fejer_val(tc):
    n=1<<18; x=np.linspace(0,P,n+1)
    th=d*(x-tc)
    K=(np.sin(M*th/2)/np.sin(th/2+1e-300))**2/M
    return simpson(S(x)*K,x=x)/simpson(K,x=x)
for tc in [0,3,6,10,20,40,68]:
    print("Fejer centre",tc,"->",fejer_val(float(tc)))
