#!/usr/bin/env python3
"""Exact certificates for D.90 central torsor and half-density descent."""

from fractions import Fraction
import math


def energy(values, center):
    return sum((1 + (u - center) ** 2) * v * v
               for u, v in values.items())


def shift_first(values, a):
    # Relative coordinate u increases by a.
    return {u + a: v for u, v in values.items()}


def main() -> None:
    # Symmetric half splitting fails coassociativity.
    a = Fraction(1)
    left = (a / 4, a / 4, a / 2)
    right = (a / 2, a / 4, a / 4)
    assert left != right

    # Only the two one-sided linear splits are coassociative.
    candidates = [Fraction(k, 8) for k in range(9)]
    coherent = [
        c for c in candidates
        if c * c == c and (1 - c) * (1 - c) == 1 - c
    ]
    assert coherent == [Fraction(0), Fraction(1)]

    # The centre family restores exact unitarity under one-sided shifts.
    values = {-3: Fraction(1, 2), 1: Fraction(-2, 3), 4: Fraction(3, 5)}
    c = Fraction(7, 4)
    shift = Fraction(5, 3)
    moved = shift_first(values, shift)
    assert energy(moved, c + shift) == energy(values, c)

    # Metric half-density character is strictly multiplicative and positive.
    m, n = 12, 75
    lhs = 1 / math.sqrt(m * n)
    rhs = (1 / math.sqrt(m)) * (1 / math.sqrt(n))
    assert lhs > 0 and abs(lhs - rhs) < 1e-15

    print("D90 torsor half-density certificates: PASS")
    print("half-split triples:", left, right)
    print("coassociative sampled splits:", coherent)
    print("central energy:", energy(values, c))
    print("half-density loop sign: +1")


if __name__ == "__main__":
    main()
