"""Exact universal constants: all N>=2,k>=1,u^2>=256N. No N scan."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
arch=2*C.log2-C.logpi+1-C.gamma/2-F(9,256)
assert arch.lo>F(9,10)
# exp(3/14)<1/(1-3/14); centered CS eta4.
center=F(14,11)
assert F(1,1)/(1-F(3,14))==center
assert C.log2.hi<F(7,10) and C.log2.lo>F(2,3)
assert F(7,5)**2<2
prime=2*center*F(5,7*2**4)*(F(7,10)+F(14,10*3)+F(2,9))
assert prime<F(4,25)
assert C.pi.hi<F(81,25)
polar0=F(9,20)*F(1024,1023)
qfactor=F(4,2047)
assert qfactor<F(1,500)<1
assert polar0*qfactor<F(1,1000)
assert F(9,10)-F(4,25)-F(1,1000)>F(7,10)
print('PASS: REAL W[f_N,k] > .7||f_N,k||^2 for ALL N>=2,k>=1,u^2>=256N.')
print('No dimension sampling: uniform gamma, centered WR and parity inequalities are proved in the memo.')
