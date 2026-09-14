#!/usr/bin/env python3
"""Exact finite model for the Tate-refined vector numerical radical."""

from fractions import Fraction


# Model D by Q^4.  The partial pairing detects the first two coordinates;
# the Tate moments are the last two with hyperbolic pairing.
def i_partial(x, y):
    return x[0] * y[0] + x[1] * y[1]


def moments(x):
    return (x[2], x[3])


def beta(m, n):
    return m[0] * n[1] + m[1] * n[0]


def i_vec(x, y):
    return (i_partial(x, y), beta(moments(x), moments(y)))


basis = [tuple(Fraction(int(i == j)) for i in range(4)) for j in range(4)]
zero = (Fraction(0),) * 4

# The vector radical is exactly the intersection of the two radicals and
# hence zero in this separated finite model.
for x in basis:
    assert any(i_vec(x, y) != (0, 0) for y in basis)
assert all(i_vec(zero, y) == (0, 0) for y in basis)

# Tate quotient is surjective and its matrix is hyperbolic.
assert moments(basis[2]) == (1, 0)
assert moments(basis[3]) == (0, 1)
assert beta(moments(basis[2]), moments(basis[2])) == 0
assert beta(moments(basis[3]), moments(basis[3])) == 0
assert beta(moments(basis[2]), moments(basis[3])) == 1

print("P123.017 vector radical/Tate exact-sequence identities: PASS")

