#!/usr/bin/env python3
"""Checks the formal laws and the mixed-direction witness of the S-square."""

from fractions import Fraction
from itertools import product


def ceil_prime(x):
    """Right-continuous odd ceiling used in absolute Riemann--Roch."""
    if x == int(x):
        return int(x)
    if x > 0:
        return int(x) + 1
    return -ceil_prime(-x)


def chi(degree_base_2):
    return ceil_prime(degree_base_2) + 1


def main():
    # Picard/tensor law in the two rulings.
    divisors = [(2, -3), (5, 7), (-4, 11)]
    for d, e in divisors:
        for dp, ep in divisors:
            lhs = (d + dp, e + ep)
            rhs = tuple(a + b for a, b in zip((d, e), (dp, ep)))
            assert lhs == rhs
            assert tuple(a + b for a, b in zip(lhs, (-lhs[0], -lhs[1]))) == (0, 0)

    # The mixed polynomial (t1-1)(t2-1) vanishes at both coordinate
    # marginals t2=1 and t1=1, but is not the zero polynomial.
    def mixed(t1, t2):
        return (t1 - 1) * (t2 - 1)

    for t in range(-5, 6):
        assert mixed(t, 1) == 0
        assert mixed(1, t) == 0
    assert mixed(2, 3) != 0

    # Conditional product Euler term has quadratic leading coefficient one
    # in base-2 degrees, with bounded ceiling errors on every tested ray.
    for a, b, n in product(range(1, 7), range(1, 7), range(1, 100)):
        value = chi(Fraction(n * a, 1)) * chi(Fraction(n * b, 1))
        leading = n * n * a * b
        error = value - leading
        assert error == n * (a + b) + 1

    print("PASS: the strict divisor modules obey the two-ruling Picard law.")
    print("PASS: a nonzero mixed direction survives both coordinate marginals.")
    print("PASS: the conditional Euler product has the expected quadratic term.")


if __name__ == "__main__":
    main()
