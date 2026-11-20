"""Specific inherited-cutoff obstruction; no window/frequency scan."""
from fractions import Fraction as F
from math import factorial
import power_fixed_grid_003 as C
assert C.logq(F(2)).lo>F(69,100)
assert C.logq(F(3)).lo>F(109,100)
assert C.logq(F(5)).lo>F(8,5)
assert F(7,5)**2<2 and F(7,4)**2>3 and F(9,4)**2>5
Alo=F(12,5)*F(69,100)+F(8,7)*F(109,100)+F(8,9)*F(8,5)
assert Alo>F(17,4)
assert C.pi.lo>3 and C.pi.hi/F(480)<F(1,100)
assert F(1,16)+120**2<121**2
assert sum(F(187,50)**j/factorial(j) for j in range(15))>F(121,3)
assert F(15,4)-F(17,4)==-F(1,2)
print('PASS: fixed tau_N=240 mass-floor < -1/2 after contact5; no negativity of W or global certificate no-go.')
