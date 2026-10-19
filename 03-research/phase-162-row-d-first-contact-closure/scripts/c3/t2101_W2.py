import numpy as np, scipy.special as sp
import t2101_single_atom as SA
from t2101_polya import Phi, coeffs
K=34
for T in [0.4,0.45,0.5,0.54]:
  for x in [2.0,1.8,2.2]:
    A0,A1,ph,P0=SA.pieces(T,K,x); A=A0-A1
    l=np.arange(0,K,2); phi=np.sqrt((2*l+1)/(2*T))*2*T*sp.spherical_in(l,0.5*T)
    W=A+2*np.outer(phi,phi); nu,V=np.linalg.eigh(W)
    out=[]
    for F in [lambda t:Phi(t), lambda t:0.25*Phi(t)-Phi(t,2)]:
        c=coeffs(T,K,F); c/=np.linalg.norm(c); out.append('%.2e/%.3f'%(c@W@c,abs(c@V[:,0])))
    print(T,x,'nu0..2',' '.join('%.2e'%v for v in nu[:3]),'| W-Rayleigh/|<.,v0>| Phi,F1:',*out,flush=True)
