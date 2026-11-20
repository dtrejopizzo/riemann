"""Exact one-atom bound for the first three contacts; no parameter scan."""
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

# Exact extra contacts; each contact already known positive by019.
def prime_contact(q,prime):
    xq=u*C.logq(q)
    lo=hi=F(0)
    for v in reversed(r):
        products=[lo*xq.lo,lo*xq.hi,hi*xq.lo,hi*xq.hi]
        lo=min(products)+K*v;hi=max(products)+K*v
    return 2*C.logq(prime)*C.I(lo,hi)/q**32
contacts=sum((prime_contact(q,p) for q,p in ((2,2),(3,3),(4,2))),C.I(0))
norm=F(comb(2*N-2,N-1),N*2**(2*N))/u**(2*N-1)
polar=-F(1,2)/(u*u-F(1,4))**(N+1)/norm
assert B.hi < -F(74,100)
assert polar < -F(36,100)
assert 0 < contacts.lo < contacts.hi < F(89,100)
assert (B+polar+contacts).hi < -F(21,100)
print('PASS: ARCH+POLAR+contacts(2,3,4) < -.21 normalized; remaining positive contacts retained.')
# Analytic upper bound for the ENTIRE tail q>300; no contact enumeration.
Lhi=C.logq(300).hi
Ival=F(1,31*300**31)
total=F(0)
for ell in range(1,N+2):
    Ival=Lhi**ell/F(31*300**31)+F(ell,31)*Ival
    total+=abs(K*r[ell-1])*u**(ell-1)*Ival
tail_upper=F(166,75)*total
assert 0<tail_upper<F(5,10**13)
print('PASS: complete positive arithmetic tail q>300 < 5e-13 normalized, analytically.')
