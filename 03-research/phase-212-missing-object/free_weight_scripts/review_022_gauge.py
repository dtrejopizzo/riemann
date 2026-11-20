# Control (revisión 022-027) del caso gauge en el lema (U) de ROUND_022_A:
# para phi par, C^2, soporte [-a,a], phi(0)=0, int phi = 0, los valores polares de S_zeta(iota phi) son
# Phi(1) = int_0^a phi(u) log u du  y  Phi(0) = zeta(0) int_0^a phi(u)/u du; se comprueba que no se anulan.
import numpy as np
from scipy.integrate import quad
a = 0.3
base = lambda u, c: u**2*(a**2-u**2)**3*(1-c*u**2)
m0 = quad(lambda u: u**2*(a**2-u**2)**3, 0, a)[0]; m2 = quad(lambda u: u**4*(a**2-u**2)**3, 0, a)[0]
c = m0/m2
phi = lambda u: base(u, c)
print('int phi       =', quad(phi, 0, a)[0])
print('Phi(1)=int phi log u =', quad(lambda u: phi(u)*np.log(u), 0, a)[0])
print('Phi(0)=-1/2 int phi/u =', -0.5*quad(lambda u: phi(u)/u, 0, a)[0])
