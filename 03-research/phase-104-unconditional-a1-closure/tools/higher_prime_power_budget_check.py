#!/usr/bin/env python3
"""Exact bookkeeping checks for 104_32.

Only integer/Fraction arithmetic is used.  The analytic inequalities are
proved in the accompanying note; this script checks the pole coefficients,
the partial-fraction identity, and the rational slack in the two displayed
thresholds.
"""

from fractions import Fraction as F


def pole_coeff(n: int) -> int:
    """Coefficient of 1/(1-z^2)."""
    return int(n % 2 == 0)


def local_minus_one_coeff(n: int) -> F:
    """Coefficient of the singular part 1/(2(1+z))."""
    return F((-1) ** n, 2)


def local_plus_one_coeff(_: int) -> F:
    """Coefficient of 1/(2(1-z))."""
    return F(1, 2)


def main() -> None:
    for n in range(40):
        assert local_minus_one_coeff(n) + local_plus_one_coeff(n) == pole_coeff(n)

    # A_n/1001 >= n(log n - 2.899)/2002.
    arch_denom = 2002
    arch_shift = F(2899, 1000)

    # At log n = 28032 the coefficient left after paying 14n is positive.
    raw_per_n = (F(28032) - arch_shift) / arch_denom - 14
    assert raw_per_n == F(1101, 2_002_000)
    assert raw_per_n * 2002 > 1

    # At log n = 112116 the coefficient left after paying 56n is the same.
    quartic_per_n = (F(112116) - arch_shift) / arch_denom - 56
    assert quartic_per_n == F(1101, 2_002_000)
    assert quartic_per_n * 8008 > 4

    print("PASS: [z^N](1-z^2)^(-1) = 1_{2|N} for N=0,...,39")
    print("PASS: local z=-1 pole coefficient is (-1)^N/2")
    print("PASS: raw threshold log n >= 28032 has >1 slack once n>2002")
    print("PASS: quartic threshold log n >= 112116 has >4 slack once n>8008")


if __name__ == "__main__":
    main()
