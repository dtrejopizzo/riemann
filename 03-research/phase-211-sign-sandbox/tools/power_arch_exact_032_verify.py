"""Stable ARCH formula and certified Euler--Maclaurin remainder; one atom only."""
from fractions import Fraction as F
from math import factorial,prod
from functools import lru_cache
import power_fixed_grid_003 as C
N=211;u=F(63,2);d=N-1;CUT=32;ORDER=8
@lru_cache(None)
def hurwitz(p):
    """Raw rational endpoints: NEVER round before multiplying by b_r."""
    assert p>=2
    center=sum((F(1,j**p) for j in range(16,CUT)),F())
    center+=F(1,(p-1)*CUT**(p-1))+F(1,2*CUT**p)
    for k in range(1,ORDER+1):
        center+=C.B[k-1]*prod(range(p,p+2*k-1))/F(factorial(2*k)*CUT**(p+2*k-1))
    err=abs(C.B[ORDER-1])*prod(range(p,p+2*ORDER-1))/F(factorial(2*ORDER)*CUT**(p+2*ORDER-1))
    return center-err,center+err,err
D0=sum((F(1,j) for j in range(1,16)),F())-C.gamma-C.logpi
slo,shi,e2=hurwitz(2)
ARCH=D0+C.I(u*slo/2,u*shi/2)
b=F(1);remainder=u*e2/2
for r in range(1,d+1):
    b*=u*F(d-r+1,2*d-r+1)
    lo,hi,e=hurwitz(r+1);lo1,hi1,e1=hurwitz(r+2)
    blo=lo-u*hi1/2;bhi=hi-u*lo1/2
    assert 0<blo<bhi
    coeff=(r+1)*b
    ARCH-=C.I(coeff*blo,coeff*bhi)
    remainder+=coeff*(e+u*e1/2)
assert remainder<F(1,2*10**18)
assert ARCH.hi-ARCH.lo<F(1,10**18)
assert -F(1095,1000)<ARCH.lo<ARCH.hi<-F(1094,1000)
if __name__=='__main__':
    print('PASS: normalized ARCH2111 certified, width<1e-18; EM8/CUT32, no quadrature.')
    scale=10**21
    print('ARCH endpoints outward /10^21:',(ARCH.lo*scale).__floor__(),(ARCH.hi*scale).__ceil__())
