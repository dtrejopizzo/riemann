import os; HERE=os.path.dirname(os.path.abspath(__file__))
import numpy as np, pickle
from numpy.polynomial import legendre as Lg
P=pickle.load(open(''+HERE+'/coef08.pkl','rb')); De=P['De']; kl=np.array(P['kl']); lam=P['lam']; Tv=0.8
R=pickle.load(open(''+HERE+'/res2.pkl','rb'))
Z=np.load(os.environ['NPZ']); kH=Z['kH']
y=np.linspace(0,lam,20001)
def psi(k):
    cf=np.zeros(kl[-1]+1); cf[kl]=De[k//2]*np.sqrt(kl+.5)/np.sqrt(lam); return Lg.legval(y/lam,cf)
PS={k:psi(k) for k in kH}
Kf=lambda u:1/(2*np.sinh(u/2))+1/(2*np.cosh(u/2)); Kt=lambda q:-np.log(np.tanh(q/4))+np.pi-2*np.arctan(np.exp(q/2))
def aT(Ef,xx,primes=((2,1),(3,1),(2,2))):
    dz=xx[1]-xx[0]; n=len(xx); c=np.fft.irfft(np.abs(np.fft.rfft(Ef,2*n))**2)[:n]*dz; u_=np.arange(n)*dz
    arch=-5.3721834*c[0]+np.trapz(np.r_[0,(c[0]-c[1:])*Kf(u_[1:])],u_)+c[0]*Kt(u_[-1])
    comb=sum(2*np.log(p)/np.sqrt(p**a)*np.interp(a*np.log(p),u_,c) for p,a in primes if a*np.log(p)<u_[-1])
    return arch-comb,c[0]
xx=np.linspace(-Tv,Tv,16001)
for K,r in R.items():
    b=r['b']; I=[a for a in range(len(kH)) if kH[a]<=K]
    f=sum(b[j]*(-1)**(kH[i]//2)*PS[kH[i]] for j,i in enumerate(I))   # a_k = eps_k b_k
    fi=lambda q: np.interp(q,y,f,right=0)
    Ef=np.exp(xx/2)*sum(fi(n*np.exp(xx)) for n in range(1,6))
    a,n2=aT(Ef,xx)
    near=np.trapz(f[y<1/lam]**2,y[y<1/lam])*2; tot=np.trapz(f**2,y)*2
    print(f"K={K}: |f|^2={tot:.4f} mass in |y|<1/lam {near/tot:.3f} | |Ef|^2={n2:.5f} a_T(Ef)={a:.5f} a_T/|Ef|^2={a/n2:.4f} | A(Ef)={np.trapz(Ef*np.exp(xx/2),xx):.1e} B={np.trapz(Ef*np.exp(-xx/2),xx):.1e} f(0)={f[0]:.1e} f(lam)={f[-1]:.1e}")
