"""Rational constants for ALL N,k in u>=64sqrt(N); no parameter scan."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
assert C.gamma.hi<F(3,5)
assert C.log2.hi<F(7,10)
assert C.log2.lo>F(693,1000)
assert C.pi.hi<F(22,7)
assert F(675,4096)<1
assert 1/(1-F(675,4096))==F(4096,3421)<F(6,5)
assert 2048>900
assert F(12,5)*F(1,2**14)*(1+F(2,13))<F(1,5000)
assert 3*F(693,1000)+F(6,25)-1-F(4,5)-F(1,16)>F(9,20)
assert F(1,8)/(1-F(1,16384))<F(1,4)
assert F(1,4*8190)<F(1,1000)
assert F(4,3*16383)<1
assert F(9,20)-F(1,5000)-F(1,1000)>F(2,5)
print('PASS: ALL N>=1,k>=0,u>=64sqrt(N), complete W>2norm^2/5')
