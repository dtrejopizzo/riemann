#!/usr/bin/env python3
"""Scalar checks for twisted fields; this is not a bio-lift verifier."""

from fractions import Fraction


def root_power(x, u):
    if x == 0:
        return 0.0
    return (1 if x > 0 else -1) * abs(float(x)) ** (1 / float(u))


def inverse_root_power(x, u):
    if x == 0:
        return 0.0
    return (1 if x > 0 else -1) * abs(float(x)) ** float(u)


def add_twisted(x, y, u):
    return inverse_root_power(root_power(x, u) + root_power(y, u), u)


def close(x, y, tolerance=1e-10):
    return abs(x - y) <= tolerance * max(1.0, abs(x), abs(y))


print("A. Multiplicative conjugations")
grid = (-5, -3, -1, 0, 1, 2, 4, 7)
parameters = (Fraction(1, 2), Fraction(2, 3), Fraction(3, 2), 2, 3)
for u in parameters:
    for x in grid:
        for y in grid:
            assert close(root_power(x * y, u),
                         root_power(x, u) * root_power(y, u))
print("  T_u(xy)=T_u(x)T_u(y) on all sampled grids")

print("\nB. Transported group laws and distributivity")
for u in parameters:
    for x in grid:
        assert close(add_twisted(x, 0, u), x)
        assert close(add_twisted(x, -x, u), 0)
        for y in grid:
            assert close(add_twisted(x, y, u), add_twisted(y, x, u))
            for z in (-3, -1, 0, 2, 5):
                left = z * add_twisted(x, y, u)
                right = add_twisted(z * x, z * y, u)
                assert close(left, right)
                lhs_assoc = add_twisted(add_twisted(x, y, u), z, u)
                rhs_assoc = add_twisted(x, add_twisted(y, z, u), u)
                assert close(lhs_assoc, rhs_assoc)
print("  identity, inverse, commutativity, associativity and distributivity pass")

print("\nC. Second integers are power characters")
for u in parameters:
    for n in range(-12, 13):
        value = 0.0
        step = 1 if n >= 0 else -1
        for _ in range(abs(n)):
            value = add_twisted(value, step, u)
        expected = (1 if n >= 0 else -1) * abs(n) ** float(u) if n else 0
        assert close(value, expected)
print("  i_2,u(n)=sgn(n)|n|^u")

print("\nD. Total interchange fails when u!=1")
for u in parameters:
    ordinary = 1 + 1
    twisted = add_twisted(1, 1, u)
    assert not close(ordinary, twisted)
    # The b=c=0 specialization of interchange compares these two sums.
    assert not close(1 + 1, add_twisted(1, 1, u))
print("  the two additions are non-total on every nontrivial parameter")

print("\nVERDICT: H7 TWISTED-FIELD SCALAR CHECKS PASS (BIO LIFT: a40/a49)")
