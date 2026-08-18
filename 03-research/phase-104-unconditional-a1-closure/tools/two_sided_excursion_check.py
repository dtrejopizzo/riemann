#!/usr/bin/env python3
"""Exact finite checks for the two-sided quartet in 104_67."""

from fractions import Fraction
from math import log


def quartet(n: int) -> Fraction:
    if n % 2:
        return Fraction(4)
    magnitude = Fraction(2 ** n) + Fraction(1, 2 ** n)
    if n % 4 == 0:
        return Fraction(4) - 2 * magnitude
    return Fraction(4) + 2 * magnitude


def harmonic_weight(indices: range, x: int) -> Fraction:
    return sum((Fraction(1, n) for n in indices if n <= x), Fraction(0))


def main() -> None:
    # Exact signs and exponential lower bounds in the two residue classes.
    for n in range(4, 161):
        q = quartet(n)
        if n % 4 == 0:
            assert q < 0
            assert -q >= 2 ** n
        elif n % 4 == 2:
            assert q > 0
            assert q >= 2 ** n
        else:
            assert q == 4

    # Every four consecutive indices contain one positive and one negative
    # exponential excursion once the prefix is removed.
    for start in range(4, 145):
        block = [quartet(n) for n in range(start, start + 4)]
        assert any(q <= -(2 ** start) for q in block)
        assert any(q >= 2 ** start for q in block)

    # Harmonic densities tend to 1/4, 1/4 and 1/2.
    for x in (100, 1000, 10000):
        total = sum((Fraction(1, n) for n in range(1, x + 1)), Fraction(0))
        negative = harmonic_weight(range(4, x + 1, 4), x)
        positive = harmonic_weight(range(2, x + 1, 4), x)
        bilateral = negative + positive
        print(
            f"X={x:5d} neg={float(negative/total):.9f} "
            f"pos={float(positive/total):.9f} "
            f"bilateral={float(bilateral/total):.9f}"
        )

    neg_rates = [log(float(-quartet(n))) / n for n in range(4, 161, 4)]
    pos_rates = [log(float(quartet(n))) / n for n in range(2, 159, 4)]
    assert abs(neg_rates[-1] - log(2)) < 0.01
    assert abs(pos_rates[-1] - log(2)) < 0.01
    print(
        f"negative_rate={neg_rates[-1]:.12f} "
        f"positive_rate={pos_rates[-1]:.12f} log2={log(2):.12f}"
    )
    print("two_sided_excursion_check: PASS")


if __name__ == "__main__":
    main()
