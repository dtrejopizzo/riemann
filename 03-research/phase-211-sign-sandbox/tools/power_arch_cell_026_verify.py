"""Exact bounds for one sharp arch deficit and one combined-kernel falsifier."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
u=F(63,2);N=129;a=F(17,4)
V=u*u/F(4*(2*N-3))
U=C.logq(a*a+V)/2-a/(2*(a*a+V))+F(1,2)/a-C.logpi
U-=sum((F(4*j+5,4)/(F(4*j+5,4)**2+V) for j in range(3)),F(0))
assert U.hi<-F(81,100)
assert U.hi+F(33,50)<-F(15,100)
Omega=F(4,9)*(F(5,4)+C.logq(5)-C.gamma-2*C.log2-C.logpi)
assert Omega.hi<-F(1,10)
print('PASS: ARCHsharp129 < -.81; benefit .66 alone leaves >.15 deficit.')
print('PASS: exact COMBINED arch+cell kernel Omega(3/2) < -.1; no actual W negative claim.')
