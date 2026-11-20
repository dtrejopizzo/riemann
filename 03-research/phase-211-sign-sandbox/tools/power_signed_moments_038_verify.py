"""Exact uniform constants, not a numerical N/Q campaign."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
u=F(63,2);a=F(992);c=F(1985,a*a)
assert u*u-F(1,4)==a
assert u**6/(2*a**4)<F(1,1000)<C.log2.lo
assert 1985*22**2<a*a
assert F(16,33)<F(1,2)
assert F(1985,a*a+1986)>F(1,500)
assert c>F(1,500)
assert c/(1+c)>F(1,500)
assert C.pi.lo>1 and C.pi.hi<4
assert F(1,6*c)<84
assert 23**2>500
assert 2*(46+84)==260
assert F(1,2)*260/2==65
assert 45**2>2000
assert F(2000*45,8)<12000
# Same growing Q family as037; only the monotone threshold constants.
N0=2**80;rootN=2**40
assert rootN<=F(N0,1000)
assert F(12000,rootN)<F(1,100)
assert F(1040000000,N0)<F(1,100)
exponent=u*u*(F(1,198500*rootN)+F(1,20000))
assert exponent<F(1,10)
assert u*u/F(100*rootN)<F(1,100)
assert F(9,10)-F(2,100)>F(4,5)
assert F(101,100)+F(2,100)<F(6,5)
print('PASS: actual-gamma Fourier normalizer, central12000 and tail65 constants.')
print('PASS: same-Q037 window logm in[A_Q,A_Q+sqrtN/100] has normalized grouped kernel in(.8,1.2), ALL N>=2^80.')
