"""Exact structural constants only; no evaluated W, N scan, or prime cutoff."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
u=F(63,2);v=u-F(1,2);r=u/v
lam=r*r/(2*r-1);tau=(r-1)/(2*r-1);alpha=(2*r-1)/lam
assert v==31 and r==F(63,62)
assert lam==F(3969,3968)==1/(1-F(1,3969))
assert tau==F(1,64)
assert 2*r*tau/(1+(2*r-1)*tau)==F(1,32)
assert alpha==F(64,63)**2
assert F(63,128*64)<tau
assert F(4,3)*F(64,63)==F(256,189)
assert alpha/36==F(1024,35721)
c0=4*r*r/(r-1)
assert c0*v/2==3969
assert c0*2*v==15876
# Endpoint inequality for the analytical Chebyshev lower bound on all x>=32.
assert (30*C.log2-C.logq(33)).lo>16
assert F(1,6)-F(1,33)>0
# This checks only a monotone sufficient threshold, not a W datum at this N.
N0=2**20
polar_lower=4/u*F(N0*(N0+1),2*3969**2)
assert polar_lower>132
print('PASS: exact tilted mode1/32, exponential factor3969/3968, and comparison constants.')
print('PASS: elementary Chebyshev endpoint and uniform component-energy threshold; no W sign claim.')
