#!/usr/bin/env python3
"""Exact finite gates for 104_61.

This checks only the rational quartet falsifier.  It does not certify any
statement about the zeta zeros or the Abel boundary limit.
"""

from fractions import Fraction
from math import comb


def gaussian_mul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def gaussian_pow(z, n):
    out = (Fraction(1), Fraction(0))
    base = z
    while n:
        if n & 1:
            out = gaussian_mul(out, base)
        base = gaussian_mul(base, base)
        n //= 2
    return out


def quartet(n):
    w = (Fraction(0), Fraction(2))
    winv = (Fraction(0), Fraction(-1, 2))
    wn = gaussian_pow(w, n)
    wni = gaussian_pow(winv, n)
    return Fraction(4) - 2 * (wn[0] + wni[0])


def abel_germ(q):
    # Formula (16) of 104_17 for rho=(1+2i)/5.
    return (
        4 * q / (1 - q)
        + 8 * q * q / (1 + 4 * q * q)
        + 2 * q * q / (4 + q * q)
    )


def pole_term_project_form(n, epsilon):
    """Equation (17), with the sign convention used in 104_61."""
    return n * sum(
        Fraction(comb(n - 1, k - 1) * (-1) ** (k - 1), k)
        / epsilon**k
        for k in range(1, n + 1)
    )


def pole_term_laplace_form(n, epsilon):
    """Integral of exp(-epsilon*u)L_(n-1)^(1)(u), coefficientwise."""
    return sum(
        Fraction(comb(n, k + 1) * (-1) ** k, 1)
        / epsilon ** (k + 1)
        for k in range(n)
    )


def main():
    for k in range(1, 65):
        n = 4 * k
        qn = quartet(n)
        assert qn == 4 - 2 * (Fraction(2) ** n + Fraction(2) ** (-n))
        assert qn < -(n * n)

    # Every four consecutive indices contain exactly one residue 0 mod 4.
    for start in range(1, 101):
        assert sum(1 for n in range(start, start + 4) if n % 4 == 0) == 1

    # Exact periodic count: density of the bad residue class is 1/4.
    for blocks in (1, 10, 100, 1000):
        total = 4 * blocks
        bad = sum(1 for n in range(1, total + 1) if n % 4 == 0)
        assert Fraction(bad, total) == Fraction(1, 4)

    for q in (Fraction(1, 10), Fraction(1, 4), Fraction(2, 5), Fraction(49, 100)):
        assert 0 < q < Fraction(1, 2)
        assert abel_germ(q) > 0

    # Exact sign/normalization gate for (17)--(19): p_n is the positive
    # Laplace integral in 104_30, while E_n=p_n-prime_sum is its negative
    # convention.  This prevents reintroducing the former P-sign collision.
    for n in range(1, 13):
        for epsilon in (Fraction(1, 3), Fraction(2, 5), Fraction(7, 4)):
            assert pole_term_project_form(n, epsilon) == pole_term_laplace_form(n, epsilon)

    print("104_61 exact quartet gates: PASS")
    print("bad residue density: 1/4")
    print("polynomial lower barrier Q_(4k) < -(4k)^2: verified for 1 <= k <= 64")
    print("regulated pole term (17): exact sign and normalization PASS")


if __name__ == "__main__":
    main()
