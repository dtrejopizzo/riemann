import os; HERE=os.path.dirname(os.path.abspath(__file__))
import sys, numpy as np
exec(open(''+HERE+'/adm.py').read().split('# tail')[0])
from sympy import factorint
def levy(G,xx,mmax):
    dz=xx[1]-xx[0]; n=len(xx); c=np.fft.irfft(np.abs(np.fft.rfft(G,2*n))**2)[:n]*dz; u_=np.arange(n)*dz
    arch=-5.3721834*c[0]+np.trapz(np.r_[0,(c[0]-c[1:])*Kf(u_[1:])],u_)+c[0]*Kt(u_[-1])
    comb=0
    for m in range(2,mmax):
        fa=factorint(m)
        if len(fa)==1 and np.log(m)<u_[-1]:
            pp=list(fa)[0]; comb+=2*np.log(pp)/np.sqrt(m)*np.interp(np.log(m),u_,c)
    return arch,comb,c[0]
print('window: a_T(Ef)=',aT,' arch',arch,'comb',comb)
Lx=float(sys.argv[4]) if len(sys.argv)>4 else 5.
xx=np.linspace(-Tv-Lx,-Tv,int(4000*Lx)+1)
fi=lambda y: np.interp(y,x,f,right=0)
Psi=np.zeros_like(xx); nmax=int(lam*np.exp(Tv+Lx))+2
for nn in range(1,nmax): Psi+=fi(nn*np.exp(xx))
Psi*=np.exp(xx/2)
ar,cb,n2=levy(Psi,xx,int(np.exp(Lx))+2)
PA=np.trapz(Psi*np.exp(xx/2),xx); PB=np.trapz(Psi*np.exp(-xx/2),xx)
print(f'tail x-space: |Psi|^2={n2:.5f} arch={ar:.5f} comb={cb:.5f} W={ar-cb:.5f} A={PA:.5f} B={PB:.5f} W+2AB={ar-cb+2*PA*PB:.5f}; Psi at -T-Lx: {Psi[0]:.2e}')
