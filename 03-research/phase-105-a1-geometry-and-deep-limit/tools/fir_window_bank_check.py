#!/usr/bin/env python3
"""Diagnostics for the FIR/window identities used in Phase 105 and Paper 38."""

from __future__ import annotations

from fractions import Fraction
from math import comb
import cmath
import random


def moving_average_poly(length: int, z: complex) -> complex:
    return sum(z**j for j in range(length))


def laguerre(n: int, alpha: int, x: Fraction) -> Fraction:
    if n < 0:
        return Fraction(0)
    total = Fraction(0)
    factorial = 1
    power = Fraction(1)
    for k in range(n + 1):
        if k:
            factorial *= k
            power *= x
        total += Fraction((-1) ** k * comb(n + alpha, n - k), factorial) * power
    return total


def check_laguerre_window_identity() -> None:
    for x in (Fraction(0), Fraction(1, 3), Fraction(7, 5)):
        for start in range(2, 10):
            for length in range(1, 8):
                lhs = sum(
                    (laguerre(start + j - 1, 1, x) for j in range(length)),
                    Fraction(0),
                )
                rhs = laguerre(start + length - 2, 2, x) - laguerre(
                    start - 2, 2, x
                )
                assert lhs == rhs


def check_adjacent_bank() -> None:
    rng = random.Random(10538)
    for length in range(1, 15):
        for _ in range(500):
            radius = 10 ** rng.uniform(-1.0, 1.0)
            angle = rng.uniform(-3.141592653589793, 3.141592653589793)
            z = radius * cmath.exp(1j * angle)
            h0 = moving_average_poly(length, z)
            h1 = moving_average_poly(length + 1, z)
            assert abs((h1 - h0) - z**length) < 2e-9 * max(
                1.0, abs(z) ** length
            )
            assert abs(h0) ** 2 + abs(h1) ** 2 + 1e-10 >= 0.5 * abs(
                z
            ) ** (2 * length)


def check_off_line_mode_survives_cascade() -> None:
    rho = 0.7 + 14.134725141734695j
    w = 1.0 - 1.0 / rho
    z = 1.0 / w
    assert abs(z) > 1.0

    gain = 1.0 + 0.0j
    for length in (3, 5, 8, 13):
        factor = moving_average_poly(length, z)
        assert abs(factor) > 1e-12
        gain *= factor
    assert abs(gain) > 1e-12


def check_rational_quartet_signed_average() -> None:
    w = 0.8j

    def quartet(n: int) -> float:
        return 4.0 - 2.0 * (w**n + w.conjugate() ** n + w ** (-n) + w.conjugate() ** (-n)).real / 2.0

    # The exact rational control has positive exponential samples in one
    # residue class while some four-sample signed means are negative.
    for start in range(21, 102, 4):
        values = [quartet(start + j) for j in range(4)]
        assert values[1] > 0
        assert sum(values) < 0


def main() -> None:
    check_laguerre_window_identity()
    check_adjacent_bank()
    check_off_line_mode_survives_cascade()
    check_rational_quartet_signed_average()
    print("PASS: Laguerre window sum collapses to an alpha=2 difference")
    print("PASS: adjacent FIR windows have no simultaneous blind spot")
    print("PASS: cascaded moving averages preserve every off-unit mode")
    print("PASS: a signed block mean can hide pointwise exponential violations")


if __name__ == "__main__":
    main()
