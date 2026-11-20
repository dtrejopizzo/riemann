"""Uniform structural constants; no evaluated W or parameter campaign."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
u=F(63,2);a0=u*u-F(1,4);amin=u*u-4
bmin=2*(u*u+F(1,4));bmax=2*(u*u+4)
assert a0==992 and amin==F(3953,4)
assert bmax*22**2<amin**2
assert 8*u**6/amin**4<F(1,100)<C.log2.lo
assert bmin/(a0*a0+bmax+1)>F(1,500)
cmin=bmin/(a0*a0)
assert cmin>F(1,500) and cmin/(1+cmin)>F(1,500)
assert C.logq(5).hi<2 and C.log2.hi<F(7,10)
assert F(17,10)*7<12 # induction psi(n)<=2n from n>=6.
K=1000
assert K*K>5*a0 # shifted point stays physical.
assert F(5,K*K)<F(1,1000)
tail=65*F(17,2)*6*2000**3/F(8*K**5)
assert tail<F(1,200)
assert 1-15*u*u/F(K*K)-F(60000,K*K)-F(1,200)>F(9,10)
assert 1/(1-F(5,K*K))+F(60000,K*K)+F(1,200)<F(11,10)
assert u*u/F(4*K*K)<F(5,4) # right tail contraction at q>=2.
assert F(2,1)/(u*u-1)<F(1,330)
print('PASS: full infinite signed inverse positive beyond the explicit shoulder, ALL N>=4,000,000.')
print('Both h and K covered; uniform-v Fourier/Cheby constants only, no W sign claim.')
