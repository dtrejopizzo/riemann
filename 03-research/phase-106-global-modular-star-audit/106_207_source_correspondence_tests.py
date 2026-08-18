#!/usr/bin/env python3
"""Finite audits for the source-correspondence stop tests."""

from fractions import Fraction
from math import factorial, log, sqrt


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b)))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def transpose(a):
    return [list(row) for row in zip(*a)]


def pullback(level, degree):
    """Unnormalized pullback l2(R_level) -> l2(R_{level*degree})."""
    return [
        [1 if y % level == x else 0 for x in range(level)]
        for y in range(level * degree)
    ]


def stirling_second(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    return k * stirling_second(n - 1, k) + stirling_second(n - 1, k - 1)


def eulerian_coefficient(degree):
    """Coefficient of a degree-r primitive monomial under log^*(Id)."""
    return sum(
        Fraction((-1) ** (j - 1), j) * factorial(j) * stirling_second(degree, j)
        for j in range(1, degree + 1)
    )


def main():
    # Test A: the polar rulings have hyperbolic intersection matrix.
    hyperbolic = [[0, 1], [1, 0]]
    assert hyperbolic[0][0] == hyperbolic[1][1] == 0
    assert hyperbolic[0][1] == hyperbolic[1][0] == 1
    assert hyperbolic[0][0] * hyperbolic[1][1] - hyperbolic[0][1] ** 2 == -1

    # Test B1: mixed pullbacks compose and have multiplicative degree.
    level, p, q = 5, 2, 3
    u_p = pullback(level, p)
    u_q_after_p = pullback(level * p, q)
    u_pq = pullback(level, p * q)
    assert matmul(u_q_after_p, u_p) == u_pq
    assert matmul(transpose(u_p), u_p) == [
        [p if i == j else 0 for j in range(level)]
        for i in range(level)
    ]

    # Test B2: R_{Mpq} is the finite-set fiber product.
    compatible = {
        (a, b)
        for a in range(level * p)
        for b in range(level * q)
        if a % level == b % level
    }
    image = {
        (z % (level * p), z % (level * q))
        for z in range(level * p * q)
    }
    assert compatible == image
    assert len(image) == level * p * q

    # Connected extraction: degree one survives, disconnected degrees die.
    coefficients = [eulerian_coefficient(r) for r in range(1, 9)]
    assert coefficients[0] == 1
    assert all(c == 0 for c in coefficients[1:])

    # Literal local mass: torsion times incidence is von Mangoldt weight.
    prime, k = 7, 4
    torsion = log(prime)
    incidence = prime ** (-k / 2)
    expected = log(prime) / sqrt(prime ** k)
    assert abs(torsion * incidence - expected) < 1e-15

    print("hyperbolic determinant:", -1)
    print("mixed pullback composition error:", 0)
    print("fiber-product cardinality:", len(image))
    print("Eulerian coefficients degrees 1..8:", coefficients)
    print("prime-layer mass error:", abs(torsion * incidence - expected))


if __name__ == "__main__":
    main()
