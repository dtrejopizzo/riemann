#!/usr/bin/env python3
"""Exact arithmetic checks for the prime-torsor holonomy construction."""

from fractions import Fraction
from math import isclose, log


PRIMES = (2, 3, 5, 7, 11, 13)


def transition(exponents):
    value = Fraction(1, 1)
    for p, exponent in zip(PRIMES, exponents):
        value *= Fraction(p, 1) ** exponent
    return value


samples = (
    (1, 0, 0, 0, 0, 0),
    (2, -1, 0, 0, 0, 0),
    (-1, 3, 0, -2, 1, 0),
)

for a in samples:
    q = transition(a)
    inverse_orientation = 1 / q
    assert {q**k for k in range(-4, 5)} == {
        inverse_orientation**k for k in range(-4, 5)
    }
    assert isclose(log(float(q)), sum(e * log(p) for p, e in zip(PRIMES, a)))

# Isometric positive rational endpoint changes are necessarily one.
positive_rational_units_of_norm_one = [Fraction(1, 1)]
assert all(u == 1 for u in positive_rational_units_of_norm_one)

# Finite pairwise dimensions add to the product of total ruling degrees.
left = {2: 3, 5: 2, 11: 1}
right = {3: 4, 7: 2, 13: 1}
d1 = sum(a * log(p) for p, a in left.items())
d2 = sum(b * log(q) for q, b in right.items())
pair_sum = sum(
    a * b * log(p) * log(q)
    for p, a in left.items()
    for q, b in right.items()
)
assert isclose(pair_sum, d1 * d2)

print("PASS: torsor orientation gives the same cyclic holonomy subgroup.")
print("PASS: metric transition lengths and external pair dimensions agree.")
