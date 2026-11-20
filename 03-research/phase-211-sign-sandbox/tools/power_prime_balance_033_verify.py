"""Rational constants for uniform positive contraction, no N scan."""
from fractions import Fraction as F
import power_fixed_grid_003 as C
u=F(63,2)
rho=sum((F(1,j*j) for j in range(2,6)),F())+F(1,5)
assert rho==F(2389,3600)<F(2,3)
assert rho**100<F(1,10**17)
assert C.logq(5).lo>F(8,5)
# Endpoint region includes all N<=211; positivity is polynomial for ALL u>=63/2.
Nmax=2*u*u/9-u/3+F(3,2)
assert Nmax==F(423,2)
assert 64*u*u-216*u-270*Nmax+675==270
# General substitution Nmax(u) yields 4u(u-63/2)+270 in the written proof.
print('PASS uniform REGION contraction constants and signed Neumann remainder scale; no W-sign claim.')
