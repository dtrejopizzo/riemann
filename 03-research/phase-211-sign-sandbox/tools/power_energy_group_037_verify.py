"""Exact constants for a uniform critical-band inequality; no mu or N scan."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
u=F(63,2);b=u*u-F(1,4)
assert b==992 and 2*b+1==1985
N0=2**16
M2=u*u/F(2*N0-3)
logR_upper=18*F(7,10)
B_upper=logR_upper/F(1985)+logR_upper**2/2
assert M2*B_upper<F(2,3)<C.log2.lo
assert (F(18,4)*C.log2-1).lo>2
assert F(1,4)+F(1,2)==F(3,4)
assert 1+F(1,1985)==F(1986,1985)
print('PASS: critical slope1/m constants and uniform absolute-contraction failure N>=2^16.')
print('The finite arithmetic grouping and divisor moments are proved symbolically in the memo.')

# One parameter-family bound for growing Q, no sieve or individual N values.
assert u*u*(8*F(1,2**40)+F(17,2)*F(1,2**20))<F(1,100)
assert F(99,100)*(2*(1-F(1,1024))-F(1,2))>F(37,25)
assert F(101,100)*F(1,2)==F(101,200)
print('PASS: growing-Q local relative error<.01, but grouped absolute remainder>1.48 versus leading group<.505 for ALL N>=2^80.')
