"""Exact scalar constants for full real reflection asymmetry, no scan."""
from fractions import Fraction as F
u=F(63,2)
blo=u/2*(sum(F(1,r*r) for r in range(16,32))+F(1,32))
polar_loss=2*u*(1+4*u*u)/(u*u-F(1,4))**2
assert blo>1
assert polar_loss<F(1,2)
assert 2*blo-polar_loss>F(3,2)
print('PASS: W[g_Q]-W[g_L] > 3/2; full comb difference strictly positive.')
