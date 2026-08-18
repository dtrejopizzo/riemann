#!/usr/bin/env python3
"""Exact checks for 104_93 (standard library, rational arithmetic only)."""

from fractions import Fraction


def prefix_energy(values):
    """Sum B_m^2/[m(m+1)] for values indexed from m=2."""
    total = Fraction(0)
    prefix = Fraction(0)
    for m, value in enumerate(values, start=2):
        prefix += value
        total += prefix * prefix / (m * (m + 1))
    return total


def max_kernel_energy(values):
    """Finite max-kernel form including the exact moving boundary."""
    n_max = len(values) + 1
    total = Fraction(0)
    for i, left in enumerate(values, start=2):
        for j, right in enumerate(values, start=2):
            kernel = Fraction(1, max(i, j)) - Fraction(1, n_max + 1)
            total += left * right * kernel
    return total


def check_max_kernel_identity():
    families = [
        [Fraction(1), Fraction(-2), Fraction(3), Fraction(-5)],
        [Fraction(2, 3), Fraction(7, 5), Fraction(-11, 13)],
        [Fraction((-1) ** k * (k + 1), k + 2) for k in range(12)],
        [Fraction(0), Fraction(0), Fraction(5, 7), Fraction(0)],
    ]
    for values in families:
        assert prefix_energy(values) == max_kernel_energy(values)


def log_interval(integer, terms):
    """Rational interval for log(integer) via 2*atanh((x-1)/(x+1))."""
    y = Fraction(integer - 1, integer + 1)
    lower = Fraction(0)
    for j in range(terms):
        lower += 2 * y ** (2 * j + 1) / (2 * j + 1)
    # Positive tail, with 1/(2j+1) bounded by its first denominator.
    first = 2 * terms + 1
    remainder_upper = 2 * y ** first / (first * (1 - y * y))
    return lower, lower + remainder_upper


def check_centered_selberg_prime_signs():
    log2_lower, log2_upper = log_interval(2, 1)
    log3_lower, log3_upper = log_interval(3, 2)

    assert 0 < log2_lower <= log2_upper < 1
    assert 1 < log3_lower <= log3_upper

    # For a prime p, r(p)=log(p)*(log(p)-1). Positivity of log(p)
    # and the certified intervals decide the signs without floats.
    r2_is_negative = log2_lower > 0 and log2_upper < 1
    r3_is_positive = log3_lower > 1
    assert r2_is_negative
    assert r3_is_positive


def check_telescoping_kernel():
    for start in range(2, 20):
        for end in range(start, 30):
            lhs = sum(Fraction(1, m * (m + 1))
                      for m in range(start, end + 1))
            rhs = Fraction(1, start) - Fraction(1, end + 1)
            assert lhs == rhs


def main():
    check_telescoping_kernel()
    check_max_kernel_identity()
    check_centered_selberg_prime_signs()
    print("104_93 checker: PASS")
    print("exact max-kernel identity and moving boundary verified")
    print("r(2)<0<r(3) certified with rational log intervals")


if __name__ == "__main__":
    main()
