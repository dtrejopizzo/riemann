#!/usr/bin/env python3
"""Exact algebra checks for 104_19 (Fraction only).

This script does not test A1.  It verifies the prime-power convolution
formula and the two elementary polar identities used by the stop-gate.
"""

from fractions import Fraction


def jordan_prime_power(q: Fraction, k: int) -> Fraction:
    if k == 0:
        return Fraction(1)
    return (q - 1) * q ** (k - 1)


def convolution_prime_power(q: Fraction, k: int) -> Fraction:
    return sum(
        (jordan_prime_power(q, j) * jordan_prime_power(q, k - j)
         for j in range(k + 1)),
        Fraction(0),
    )


def closed_prime_power(q: Fraction, k: int) -> Fraction:
    if k == 0:
        return Fraction(1)
    return (
        2 * (q - 1) * q ** (k - 1)
        + (k - 1) * (q - 1) ** 2 * q ** (k - 2)
    )


def scaled_polar_laplace(c: Fraction, x: Fraction) -> Fraction:
    """Laplace transform of delta_0+c(cr-2)e^{-r}dr at x."""
    return 1 + c * (c / (1 + x) ** 2 - 2 / (1 + x))


def scaled_polar_closed(c: Fraction, x: Fraction) -> Fraction:
    return (1 - c / (1 + x)) ** 2


def polar_z1(c: Fraction, epsilon: Fraction) -> Fraction:
    """[z] (1-z)^-1 (1-c eps/(eps+z/(1-z)))^2."""
    return (1 - c) ** 2 + 2 * c * (1 - c) / epsilon


def main() -> None:
    for q in (Fraction(3, 2), Fraction(5, 3), Fraction(2)):
        for k in range(0, 10):
            lhs = convolution_prime_power(q, k)
            rhs = closed_prime_power(q, k)
            assert lhs == rhs, (q, k, lhs, rhs)

    for c in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
        for x in (Fraction(0), Fraction(1, 3), Fraction(2), Fraction(9, 2)):
            lhs = scaled_polar_laplace(c, x)
            rhs = scaled_polar_closed(c, x)
            assert lhs == rhs, (c, x, lhs, rhs)

        epsilon = Fraction(1, 100)
        z1 = polar_z1(c, epsilon)
        assert z1 > 0
        # The continuous density c(cr-2)e^{-r} is negative at r=1
        # for every c in (0,1).
        assert c * (c - 2) < 0

    print("PASS: b_u(p^k) convolution formula (exact Fractions)")
    print("PASS: signed polar Laplace identity (exact Fractions)")
    print("PASS: z^1 polar coefficient and negative-density witness")


if __name__ == "__main__":
    main()
