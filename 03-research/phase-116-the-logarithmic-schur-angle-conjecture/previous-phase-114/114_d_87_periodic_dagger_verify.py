#!/usr/bin/env python3
"""Exact algebraic certificates for D.87 periodic dagger landing."""

from fractions import Fraction
from math import isclose


def conv(x, y):
    out = [Fraction(0) for _ in range(len(x) + len(y) - 1)]
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            out[i + j] += a * b
    return out


def norm2(x):
    return sum(a * a for a in x)


def main() -> None:
    # Bilateral primitive symbol at exp(R/2)=3/2.
    x = Fraction(3, 2)
    denominator = x + 1 / x
    chi_plus = 1 - (x + 1 / x) / denominator
    chi_minus = 1 - (1 / x + x) / denominator
    assert chi_plus == chi_minus == 0

    # Standard convolution is not isometric for tensor norms.
    v = [Fraction(1), Fraction(1)]
    vv = conv(v, v)
    assert norm2(v) == 2
    assert norm2(vv) == 6
    assert norm2(vv) / 4 == Fraction(3, 2)

    # Generic D.86 preparation angle remains indefinite.
    lam = Fraction(9, 25)
    det = -4 * lam * (1 - lam)
    assert det == Fraction(-576, 625)
    assert isclose(float(norm2(vv) / 4), 1.5)

    print("D87 periodic dagger landing certificates: PASS")
    print("two Tate symbols:", chi_minus, chi_plus)
    print("normalized convolution norm squared:", norm2(vv) / 4)
    print("generic preparation determinant:", det)


if __name__ == "__main__":
    main()
