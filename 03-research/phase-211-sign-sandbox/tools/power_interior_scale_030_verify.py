"""One universal finite block; analytic N threshold, no dimension sampling."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
c=-C.gamma-2*C.log2-C.logpi
assert C.logq(F(9,4)).hi<1
# Exact integral against G_*(x)=(3/2)x^(-1/2), over[1,9/4].
J=F(8,9)-F(16,81)*C.logq(F(13,5))+F(2,3)*C.logq(F(5,2))-F(4,3)*C.atan_inv(5)
assert F(99,70)**2>2
Istar_lower=F(3,2)+F(19,27)*(c-1)+F(3,2)*J-C.log2*(F(99,70)-F(32,27))
assert Istar_lower.lo>F(1,50)
assert C.gamma.hi<1 and C.log2.hi<F(7,10) and C.logpi.hi<F(6,5)
assert F(3,2)+F(23,5)*F(3,5)+F(7,5)+F(7,25)<6
u=F(63,2);N0=2**20
error_upper=F(21,2)*u*u/F(2*N0-3)
assert error_upper<F(1,200)
assert F(1,50)-error_upper>F(1,100)
# Counterexample to positivity of the arithmetic primitive, same full kernel H.
T=F(5,2)
P=T-1+(c-1)*(1-1/T)-C.logq((T+1)/(T-1))/T+2*C.logq(T)-C.logq(T*T-1)+4*C.log2/T
assert P.hi<-F(1,50)
weighted=(T**3-1)/3+(c-1)*(T-1)+(T+1)*C.logq(T+1)-(T-1)*C.logq(T-1)-2*C.log2-4*C.log2*(T-2)
assert weighted.hi<-F(1,4)
print('PASS: actual fixed-u gamma block int_[1,9/4] G_N H > 1/100 for ALL N>=2^20.')
print('PASS: full arithmetic primitive at5/2 is negative; no total-W sign claimed.')
