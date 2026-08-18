#!/usr/bin/env python3
"""Exact arithmetic checks for the sharp associated-Legendre tail."""

from fractions import Fraction
from math import factorial


def sharp(N: int, m: int) -> Fraction:
    return Fraction(factorial(N - m), factorial(N + m))


def summed(N: int, m: int) -> Fraction:
    return Fraction(
        factorial(N - m),
        (2 * m - 1) * factorial(N + m - 1),
    )


for m in range(1, 12):
    for N in range(m, m + 30):
        assert summed(N, m) / sharp(N, m) == Fraction(
            N + m, 2 * m - 1
        )
        weights = [
            Fraction(factorial(n + m), factorial(n - m))
            for n in range(m, N + 10)
        ]
        assert all(a < b for a, b in zip(weights, weights[1:]))

c = sharp(260, 20)
assert 2.425e-97 < float(c) < 2.426e-97
budget = Fraction(1, 20) / c
assert 2.061e95 < float(budget) < 2.062e95

print("D205 sharp associated-Legendre tail: PASS")
print("c_sharp(260,20) =", float(c))
print("0.05 sharp derivative budget =", float(budget))
print("improvement factor =", float(summed(260, 20) / c))
