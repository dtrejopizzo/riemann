#!/usr/bin/env python3
"""Exact Stirling-number audit for the first Eulerian idempotent."""

from __future__ import annotations

from fractions import Fraction
from math import factorial


def stirling2(n: int, r: int) -> int:
    table = [[0] * (r + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, r) + 1):
            table[i][j] = table[i - 1][j - 1] + j * table[i - 1][j]
    return table[n][r]


def eulerian_scalar(n: int) -> Fraction:
    # On x^n, N^{*r} has coefficient r! S(n,r).
    return sum(
        (Fraction((-1) ** (r - 1), r) * factorial(r) * stirling2(n, r)
         for r in range(1, n + 1)),
        Fraction(0),
    )


def main() -> None:
    for n in range(1, 13):
        value = eulerian_scalar(n)
        expected = Fraction(1 if n == 1 else 0)
        print(f"degree {n:2d}: e_1(x^{n}) = {value!s:>3s}  ok={value == expected}")


if __name__ == "__main__":
    main()
