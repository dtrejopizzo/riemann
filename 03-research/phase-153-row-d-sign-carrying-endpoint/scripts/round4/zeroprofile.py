"""Where does the Weil mass of the minimiser sit?  Also checks the explicit formula
sum_gamma |Fhat(gamma)|^2 = <A_T F,F> on P_T (RH reading; diagnostic only)."""
import math,numpy as np,core,aud_spectral as A
z=np.load('../round3/zeros600.npy')
for T in (0.45,0.55,0.60,0.65,math.log(2)):
    lam,par,vec=core.lam_min(T,240,want_vec=True); vec/=math.sqrt(T*np.dot(vec,vec))
    m=np.abs(vec@A.basis_hat(T,240,z))**2*2; S=m.sum(); cum=np.cumsum(m)/S
    k=[int(np.searchsorted(cum,f)) for f in (0.5,0.9,0.99)]
    print(f'T={T:.4f} lam={lam:.4e} sum/lam={S/lam:.4f} g1={m[0]/S:.5f} g2={m[1]/S:.5f} '
          f'g3={m[2]/S:.5f} median/90%/99% gamma={z[k[0]]:.1f}/{z[k[1]]:.1f}/{z[k[2]]:.1f}')
