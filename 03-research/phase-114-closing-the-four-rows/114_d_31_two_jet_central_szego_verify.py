#!/usr/bin/env python3
"""Exact checks for D.31 (no zeta zeros and no floating-point premise)."""

from fractions import Fraction


bound = (
    Fraction(1, 3)
    + Fraction(1, 8)
    + Fraction(1, 24)
    + Fraction(1, 48)
    + Fraction(1, 2) * (Fraction(1, 10) + Fraction(1, 11))
)

assert bound == Fraction(1627, 2640)
assert 1 - bound == Fraction(1013, 2640)
assert bound < 1

# For r^2=1/p, the squared norm after deleting coefficients 1 and z is
# (1-r^2) sum_{j>=2} r^(2j)=r^4=1/p^2.  The identity is algebraic, so
# checking it for all integers in this range also checks every prime there.
for p in range(2, 1000):
    r2 = Fraction(1, p)
    tail = (1 - r2) * r2**2 / (1 - r2)
    assert tail == Fraction(1, p * p)

print("D.31 exact two-jet identities: PASS")
print("uniform primitive gap >=", Fraction(1013, 2640))
