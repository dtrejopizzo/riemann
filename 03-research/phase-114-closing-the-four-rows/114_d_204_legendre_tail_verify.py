#!/usr/bin/env python3
"""Exact checks for the D.204 Legendre-tail identities."""

from fractions import Fraction
from math import factorial


def ratio(n: int, m: int) -> Fraction:
    return Fraction(factorial(n - m), factorial(n + m))


def tail_closed(N: int, m: int) -> Fraction:
    return Fraction(factorial(N - m), (2 * m - 1) * factorial(N + m - 1))


def sharp_constant(N: int, m: int) -> Fraction:
    return Fraction(factorial(N - m), factorial(N + m))


def falling_tail(N: int, m: int, cutoff: int) -> Fraction:
    return sum((ratio(n, m) for n in range(N, cutoff)), Fraction(0))


for m in range(1, 12):
    for N in range(m, m + 20):
        # Exact telescoping identity term by term.
        a_n = tail_closed(N, m)
        a_np1 = tail_closed(N + 1, m)
        assert a_n - a_np1 == ratio(N, m)

        # A finite partial sum plus its exact remainder is the closed tail.
        cutoff = N + 50
        assert falling_tail(N, m, cutoff) + tail_closed(cutoff, m) == a_n
        assert tail_closed(N, m) / sharp_constant(N, m) == Fraction(
            N + m, 2 * m - 1
        )


# Spot-check the Jacobi norm after all powers of two and factorials cancel
# in the normalized coefficient estimate (1.4).
for m in range(1, 9):
    for n in range(m, m + 20):
        prefactor_sq = Fraction(factorial(n - m) ** 2,
                                2 ** (2 * m) * factorial(n) ** 2)
        jacobi_norm = Fraction(
            2 ** (2 * m + 1) * factorial(n) ** 2,
            (2 * n + 1) * factorial(n - m) * factorial(n + m),
        )
        normalized = Fraction(2 * n + 1, 2) * prefactor_sq * jacobi_norm
        assert normalized == ratio(n, m)

        # Exact weighted derivative norm of the normalized Legendre mode.
        derivative_weight = Fraction(factorial(n + m), factorial(n - m))
        assert derivative_weight * ratio(n, m) == 1


print("D204 weighted-Sobolev to Legendre-tail identities: PASS")
