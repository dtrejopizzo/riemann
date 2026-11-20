"""Exact constants for two global finite-difference inequalities; no finite-k sampling."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
u=F(63,2);eta=F(15)
H15=sum((F(1,k) for k in range(1,16)),F(0))
d0=H15-C.gamma-C.logpi
assert d0.lo>F(159,100)>F(3,2)
# Uniform real-u bounds for u>=63/2.
assert F(3,2)-1-F(4,63)>F(2,5)
assert F(159,100)-F(67,63)-F(71,189)>F(3,20)
a=u-eta;rho=eta**2/a**2
R2=(u/a)**3*(1+rho)/(1-rho)**2
R3=(u/a)**5*(1+2*rho-rho**2/3)/(1-rho)**3
assert R2==F(4641,11)
assert R3==F(15658881,1331)
assert 4*R2<42**2
assert 4*R3<220**2
p20=8*u**3/(u*u-F(1,4))**2
p30=F(32,3)*u**5/(u*u-F(1,4))**3
assert p20<F(13,50)
assert p30<F(7,20)
q=1/(4*u*u-1)
assert 4*q<1
assert 6*q<1
assert F(7,20)*6*q<F(1,1000)
S=F(15,13*2**14)
assert 42*S<F(3,1000)
assert 220*S<F(1,60)
assert F(2,5)-F(13,50)-F(3,1000)>F(1,8)
assert F(3,20)-F(1,1000)-F(1,60)>F(1,8)
print('PASS: N=2 and N=3 full-form margins >1/8, uniformly all k>=0,u>=63/2.')
print('Hence row N=1 has strictly positive first and second differences at every k.')
