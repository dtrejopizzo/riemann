"""One explicit window: constants for the compact-repair obstruction only."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
T=F(3,5)
assert C.logq(3).hi<2*T<(2*C.log2).lo
assert 2*T<C.logq(5).lo
m0=-C.gamma-C.pi/2-3*C.log2-C.logpi
assert m0.hi<-F(53,10)
assert F(10,7)**2>2 and F(26,15)**2>3
v2_lower=F(7,5)*C.log2
v3_lower=F(15,13)*C.logq(3)
assert v2_lower.lo>F(19,20)
assert v3_lower.lo>F(5,4)
assert m0.hi-v2_lower.lo-v3_lower.lo<-F(15,2)
print('PASS: T=3/5 has exactly contacts2,3 and q_T(0)<-15/2.')
print('With the written even compact-annihilator lemma: no fixed-tail compact repair with slack<=15/2. No W-negative claim.')
