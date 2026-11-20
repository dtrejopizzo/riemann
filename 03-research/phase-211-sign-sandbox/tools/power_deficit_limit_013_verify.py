"""Exact scope-limited obstruction to the separable pointwise-deficit criterion."""
from fractions import Fraction as F
from math import comb,factorial
import power_fixed_grid_003 as C
u=F(63,2);n=8;ps={};M=2000
for j in range(1,n):
 part=sum((C.I(F(1,k**(j+1))) for k in range(16,M+1)),C.I(0))
 tail=C.I(F(1,j*(M+1)**j),F(1,j*M**j))
 ps[j]=(-1)**(j+1)*factorial(j)*(part+tail)
r=F(32,31)
bands=[sum((F(1,k) for k in range(1,16)),F(0))-C.gamma-C.logpi+4*u/(u*u-F(1,4))]
for k in range(1,n):
 arch=sum((ps[j]*F(1,2**(j+1))*(2*u)**j*F(comb(k-1,j-1),factorial(j)) for j in range(1,k+1)),C.I(0))
 polar=2*u/(u*u-F(1,4))*(-1)**k*(r**k+r**(-k))
 bands.append(arch+polar)
v=[169,-310,405,-460,460,-405,310,-169]
N=sum(t*t for t in v)
energy=sum((v[i]*v[j]*bands[abs(i-j)] for i in range(n) for j in range(n)),C.I(0))/N
assert energy.lo>0
assert energy.hi<F(1,25)
# m(4) upper bound: positive partial sum plus integral tail.
mzero=-C.gamma-C.pi/2-3*C.log2-C.logpi
x=F(16)
partial=sum((x/(F(4*k+1,4)*(4*F(4*k+1,4)**2+x)) for k in range(32)),F(0))
tail=x/(8*F(125,4)**2)
m4upper=mzero.hi+partial+tail
assert m4upper<-F(2,5)
loss=F(2,5)*((1+16/(u*u))**n-1)
assert loss>F(1,20)>F(1,25)
print('PASS: explicit rational AP8 Rayleigh <1/25, m(4)<-2/5, unavoidable uniform pointwise loss>1/20.')
print('Only the uniform pointwise negative-envelope method is excluded; no sign counterexample.')
