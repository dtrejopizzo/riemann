import math,sys,numpy as np, mpmath as mp
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-153-row-d-sign-carrying-endpoint/scripts/round6')
import core
mp.mp.dps=25
# Levy rep check at 5 tau values with better quadrature
K=lambda u: 1/(2*mp.sinh(u/2))+1/(2*mp.cosh(u/2))
C0=mp.digamma(mp.mpf(1)/4)-mp.log(mp.pi)
m=lambda t: mp.re(mp.digamma(mp.mpf(1)/4+1j*t/2))-mp.log(mp.pi)
print("C0",mp.nstr(C0,18))
for tau in [0.3,1,2.5,6,13.7]:
    tau=mp.mpf(tau)
    pts=[0]+[k/tau for k in range(1,60)]+[60/tau,200,mp.inf] if tau>0 else None
    rhs=C0+mp.quad(lambda u:(1-mp.cos(tau*u))*K(u),pts)
    print(f" tau={float(tau):8.3f} m={mp.nstr(m(tau),18)} levy={mp.nstr(rhs,18)} d={mp.nstr(m(tau)-rhs,3)}")
