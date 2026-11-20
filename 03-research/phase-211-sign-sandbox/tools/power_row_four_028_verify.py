"""Exact constants for the COMPLETE fourth row, all k and all u>=63/2."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
u=F(63,2);eta=F(12);B=115
D=sum((F(1,j) for j in range(1,16)),F(0))-C.gamma-C.logpi
S=lambda p:sum((F(1,j**p) for j in range(16,B+1)),F(0))+F(1,(p-1)*B**(p-1))
A_lower=D-u/2*S(2)-u*u/5*S(3)-u**3/20*S(4)
assert A_lower.lo>F(11,400)
a=u-eta;rho=(eta/a)**2
R=(u/a)**7*(1+3*rho-rho*rho+rho**3/5)/(1-rho)**4
assert rho==F(64,169) and u/a==F(21,13)
assert 4*R<40**2
assert C.log2.hi<F(7,10) and C.log2.lo>F(2,3)
assert F(7,5)**2<2 # q^(-1/2)<=2^(-1/2)<5/7.
prime_upper=F(200,7*2**12)*(F(7,10)+F(14,10*11)+F(2,121))
assert prime_upper<F(3,500)
polar0=F(64,5)*u**7/(u*u-F(1,4))**4
q=1/(4*u*u-1)
assert 8*q<1
assert polar0*8*q<F(1,1000)
assert F(11,400)-F(3,500)-F(1,1000)>F(1,50)
print('PASS: COMPLETE W[f_4,k] > (1/50)||f_4,k||^2 for every k>=0 and every real u>=63/2.')
print('Exact constants only; uniformity in k/u is proved analytically in POWER_ROW_FOUR_028.md.')
