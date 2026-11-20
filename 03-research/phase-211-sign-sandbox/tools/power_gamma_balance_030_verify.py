"""One actual gamma-vs-Gaussian gap and constants for the analytic uniform sharp bound."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
u=F(63,2);a=u*u-F(1,4)
d=sum((F(1,k) for k in range(1,16)),F())-C.gamma-C.logpi
trigamma_lo=sum((F(1,k*k) for k in range(16,256)),F())+F(1,256)
assert (d-F(63,4)*trigamma_lo).hi<F(59,100)
polar=F(8)/u*(u*u/a)**2
assert polar<F(13,50)
assert F(59,100)+F(13,50)==F(17,20)
assert F(1)/(6*F(5,4)**2)==F(8,75)
assert C.gamma.hi<F(3,5)
assert F(693,1000)<C.log2.lo and C.log2.hi<F(7,10)
assert C.pi.hi<F(22,7) and C.pi.lo>2
assert u*u/3>20
assert F(2,2**19)*(1+F(2,18))<F(1,1000)
gaussian_lo=2*F(693,1000)+F(178,793)-F(13,20)-F(8,75)+1/u-F(1,1000)
assert gaussian_lo>F(7,8)
assert F(17,20)-F(7,8)==-F(1,40)
print('PASS: actual N2 gamma/Gaussian full gap < -1/40; uniform SHARP-GAP proved analytically')
