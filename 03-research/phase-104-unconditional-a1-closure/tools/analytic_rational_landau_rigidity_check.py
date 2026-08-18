#!/usr/bin/env python3
"""Exact finite checks for 104_102.

The proof itself is algebraic.  This script checks its two finite pieces:

* the Jacobian of the finite-prime moment map is the stated nonzero
  Vandermonde determinant;
* the formal coefficients of 1/(c-L) obey a positive convolution
  recurrence, while c-L has the expected inverse identity.

Only Fraction arithmetic is used; no zeta zeros or floating point occur.
"""

from fractions import Fraction
from math import prod


def det(matrix):
    """Bare Gaussian determinant over Fraction."""
    a = [[Fraction(x) for x in row] for row in matrix]
    n = len(a)
    out = Fraction(1)
    for col in range(n):
        pivot = next((row for row in range(col, n) if a[row][col]), None)
        assert pivot is not None
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            out = -out
        pv = a[col][col]
        out *= pv
        for row in range(col + 1, n):
            ratio = a[row][col] / pv
            for k in range(col, n):
                a[row][k] -= ratio * a[col][k]
    return out


def vandermonde_checks(max_order=9):
    rows = []
    for order in range(max_order + 1):
        # Distinct positive rational surrogates for log(p_i).  The
        # determinant identity is polynomial, hence this checks its exact
        # algebraic form; the proof uses the actual distinct log(p_i).
        nodes = [Fraction(i + 2) for i in range(order + 1)]
        matrix = [
            [nodes[i] ** (j + 1) for i in range(order + 1)]
            for j in range(order + 1)
        ]
        expected = prod(nodes, start=Fraction(1))
        for i in range(order + 1):
            for k in range(i + 1, order + 1):
                expected *= nodes[k] - nodes[i]
        actual = det(matrix)
        assert actual == expected and actual != 0
        rows.append((order, actual))
    return rows


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def geometric_positive_check(limit=160, c=Fraction(7)):
    # Any nonnegative sequence b_n with b_1=0 models the only fact needed
    # from Lambda.  Use a sparse exact surrogate supported on prime powers.
    b = [Fraction(0)] * (limit + 1)
    for p in (2, 3, 5, 7, 11, 13):
        power = p
        while power <= limit:
            b[power] = Fraction(p)  # arbitrary strictly positive weight
            power *= p

    # From (c-L)F=1:
    #   a_1=1/c, c*a_n=sum_{d|n,d>=2} b_d*a_{n/d}.
    a = [Fraction(0)] * (limit + 1)
    a[1] = Fraction(1, 1) / c
    for n in range(2, limit + 1):
        a[n] = sum(
            (b[d] * a[n // d] for d in divisors(n) if d >= 2),
            start=Fraction(0),
        ) / c
        assert a[n] >= 0

    # Coefficients of (c-L)F are exactly delta_1 through the cutoff.
    for n in range(1, limit + 1):
        coefficient = c * a[n] - sum(
            (b[d] * a[n // d] for d in divisors(n) if d >= 2),
            start=Fraction(0),
        )
        assert coefficient == (1 if n == 1 else 0)

    assert any(a[n] > 0 for n in range(2, limit + 1))
    return sum(value > 0 for value in a[1:])


def main():
    rows = vandermonde_checks()
    positive = geometric_positive_check()
    print(
        "finite-prime Jacobian: exact Vandermonde identity for",
        len(rows),
        "orders; all determinants nonzero",
    )
    print(
        "geometric counterexample: exact positive recurrence and "
        f"(c-L)F=1 through n=160; {positive} nonzero coefficients"
    )
    print("PASS")


if __name__ == "__main__":
    main()
