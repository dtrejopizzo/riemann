"""Exact one-point obstruction to contact2-only signed balance; no scan."""
import power_fixed_grid_003 as C
from fractions import Fraction as F
from math import factorial,comb
N=211;u=F(63,2);x=u*C.log2
K=F(N*2**(N-1),factorial(N)*comb(2*N-2,N-1))
p=[F(factorial(2*N-j),2**(N-j)*factorial(N-j)*factorial(j)) for j in range(N+1)]
r=[p[j]*F(j*(j+1)-2*N,(2*N-j)*(2*N-j-1)) for j in range(N+1)]
zl=zh=F(0)
for v in reversed(r):
    w=[zl*x.lo,zl*x.hi,zh*x.lo,zh*x.hi]
    zl=min(w)+K*v;zh=max(w)+K*v
contact=C.log2*C.I(zl,zh)/2**31
E=u*u*F(3,2*N-3)/4
a=F(17,4)
B=C.logq(a*a+E)/2+F(1,2)/a-C.logpi
B-=a/(2*(a*a+E))
B-=sum((F(4*j+1,4)/(F(4*j+1,4)**2+E) for j in range(4)),F(0))
assert B.hi < -F(74,100)
assert 0 < contact.lo < contact.hi < F(75,1000)
assert (B+contact).hi < -F(66,100)
print('PASS: ARCH < -.74; 0 < contact2 < .075; ARCH+POLAR+contact2 < -.66 normalized.')
