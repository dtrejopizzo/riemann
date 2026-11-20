"""Rational constants in the analytic curvature counterexample, no parameter scan."""
from fractions import Fraction as F
from math import factorial
assert sum((F(2)**j/F(factorial(j)) for j in range(5)),F())>6
assert 3*2*3*F(8,7)<24
assert -F(1,8)+F(24,256)<0
assert 256**2==65536
print('PASS: constants in strict negative curvature range v>=65536')
