"""First next-contact test only: prime3, rational-square prefix, recovery at4."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
c=-C.gamma-2*C.log2-C.logpi

def common(z):
    T=z*z
    J=F(8,3)*(1-1/z)-F(2,3)/z**3*C.logq((T+1)/(T-1))
    J+=F(2,3)*C.logq((z+1)/(2*(z-1)))-F(4,3)*C.atan_inv((z+1)/(z-1))
    return 3*(z-1)+(c-1)*(1-1/z**3)+F(3,2)*J+2/z**3*(2*C.log2+3*C.logq(3))
assert F(140,99)**2<2<F(99,70)**2
assert F(265,153)**2<3<F(97,56)**2
# Upper bound: reciprocal square roots replaced by smaller rationals.
Ibad_upper=common(F(15,8))-2*C.log2*F(70,99)-2*C.logq(3)*F(56,97)
assert Ibad_upper.hi<-F(1,250)
# Lower bound: reciprocal square roots replaced by larger rationals.
I4_lower=common(F(2))-2*C.log2*F(99,140)-2*C.logq(3)*F(153,265)
assert I4_lower.lo>F(1,50)
assert C.logq(4).hi<F(7,5)
assert F(3,4)*F(7,5)**2+F(7,5)<3
assert C.gamma.hi<1 and C.log2.hi<F(7,10) and C.logpi.hi<F(6,5)
assert C.logq(3).hi<F(11,10)
# H absolute integral on[1,4]: length, constant, log kernel, contacts2/3.
assert 3+F(23,5)*F(3,4)+F(7,5)+F(7,10)+F(11,20)<10
u=F(63,2)
assert 30*u*u/F(2*2**22-3)<F(1,200)
assert 30*u*u/F(2*2**24-3)<F(1,1000)
assert F(1,50)-F(1,200)==F(3,200)
assert -F(1,250)+F(1,1000)==-F(3,1000)
assert F(3,200)+F(3,1000)==F(9,500)
print('PASS: fixed-u REAL prefix[1,225/64] < -.003 for ALL N>=2^24.')
print('PASS: fixed-u REAL block[1,4] > .015 for ALL N>=2^22; recovery subblock > .018 for N>=2^24.')
print('No total-W sign; no other contact or dimension campaign.')
