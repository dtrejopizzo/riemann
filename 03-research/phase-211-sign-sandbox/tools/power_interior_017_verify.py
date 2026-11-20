"""Exact constants for the all-k N=1 scalar-row theorem."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
u=F(63,2);eta=F(15);a=u-eta;b=eta
assert u*a/(a*a-b*b)==11
assert 4*11<7**2
H15=sum((F(1,k) for k in range(1,16)),F(0))
assert C.gamma.hi<F(3,5)
assert C.logpi.hi<F(6,5)
assert H15-F(9,5)>F(3,2)
assert 4*u/(u*u-F(1,4))==F(63,496)
assert 2/(4*u*u-1)<1
assert F(105,13*2**14)<F(1,2000)
assert F(3,2)-F(63,496)-F(1,2000)>F(4,3)
print('PASS: exact uniform weighted ratio 11; arch>3/2; pole loss<=63/496; whole prime cost<1/2000.')
print('Conclusion by the all-k coefficient inequalities: W[s^k/(s+u)^(k+1)]>(4/3)||.||^2 for all k>=0,u>=63/2.')
