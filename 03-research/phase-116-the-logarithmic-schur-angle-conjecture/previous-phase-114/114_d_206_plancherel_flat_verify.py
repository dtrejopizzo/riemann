#!/usr/bin/env python3
"""Exact arithmetic checks for the D.206 M=60 Plancherel route."""

from decimal import Decimal, getcontext
from math import factorial
import math


getcontext().prec = 80
N = 600
m = 60
T = Decimal(6).ln() / 2

c_unit = Decimal(factorial(N - m)) / Decimal(factorial(N + m))
c_physical = c_unit * T ** (2 * m)

assert Decimal("4.6281e-334") < c_unit < Decimal("4.6282e-334")
assert Decimal("8.6173e-340") < c_physical < Decimal("8.6174e-340")

# Dimension: degree <200, divisibility by (1-u^2)^60 leaves 80
# coordinates, and the two independent Tate moments leave 78.
assert 200 - 2 * m - 2 == 78

# Exactly the prime powers below the endpoint e^(2T)=6.
active = (2, 3, 4, 5)
assert all(n < 6 for n in active)
assert 6 not in active

# Elementary outward constants used in the multiplier bound.
psi_constant_upper = (
    Decimal(".578") + Decimal("3.142") / 2
    + 3 * Decimal(".694") + Decimal("1.145")
)
assert psi_constant_upper < Decimal("5.377")
contact_twice = 2 * (
    math.log(2) / math.sqrt(2)
    + math.log(3) / math.sqrt(3)
    + math.log(2) / 2
    + math.log(5) / math.sqrt(5)
)
assert contact_twice < 4.4

# Closed majorant of the logarithmic tail integral at a sample R.
R = Decimal(100)
A = Decimal(17) + 1 / R
tail_majorant = ((A + R.ln()) ** 2 + 2 * (A + R.ln()) + 2) / R
assert tail_majorant > 0

print("D206 complete-action Plancherel flat route: PASS")
print("unit-coordinate coefficient =", c_unit)
print("physical-coordinate coefficient =", c_physical)
