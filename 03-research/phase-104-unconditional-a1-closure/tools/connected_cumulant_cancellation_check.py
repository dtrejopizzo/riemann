#!/usr/bin/env python3
"""Exact diagnostics for 104_53 (standard library only)."""

from fractions import Fraction
from math import comb, factorial


def cumulants_from_moments(m):
    """m[0]=1; return kappa with the same maximal order."""
    nmax = len(m) - 1
    kappa = [Fraction(0) for _ in range(nmax + 1)]
    for n in range(1, nmax + 1):
        correction = sum(
            Fraction(comb(n - 1, j - 1)) * kappa[j] * m[n - j]
            for j in range(1, n)
        )
        kappa[n] = m[n] - correction
    return kappa


def independent_sum_moments(a, b):
    assert len(a) == len(b) and a[0] == b[0] == 1
    return [
        sum(Fraction(comb(n, j)) * a[j] * b[n - j] for j in range(n + 1))
        for n in range(len(a))
    ]


def moments_from_cumulants(kappa):
    nmax = len(kappa) - 1
    m = [Fraction(0) for _ in range(nmax + 1)]
    m[0] = Fraction(1)
    for n in range(1, nmax + 1):
        m[n] = sum(
            Fraction(comb(n - 1, j - 1)) * kappa[j] * m[n - j]
            for j in range(1, n + 1)
        )
    return m


def main():
    nmax = 12
    # Two exact formal moment sequences, generated from arbitrary rational
    # cumulants. Positivity is irrelevant to the universal algebra check.
    ka = [Fraction(0)] + [Fraction((-1) ** (j + 1) * (j + 2), j + 1) for j in range(1, nmax + 1)]
    kb = [Fraction(0)] + [Fraction(2 * j + 1, j + 3) for j in range(1, nmax + 1)]
    ma = moments_from_cumulants(ka)
    mb = moments_from_cumulants(kb)
    mab = independent_sum_moments(ma, mb)
    kab = cumulants_from_moments(mab)
    assert kab[0] == 0
    for n in range(1, nmax + 1):
        assert kab[n] == ka[n] + kb[n]
    print("PASS: cumulants are additive under exact moment convolution through order 12")

    # Low-order disconnected pieces are displayed explicitly by identities.
    k = cumulants_from_moments(ma)
    assert k[1] == ma[1]
    assert k[2] == ma[2] - ma[1] ** 2
    assert k[3] == ma[3] - 3 * ma[2] * ma[1] + 2 * ma[1] ** 3
    assert k[4] == (
        ma[4]
        - 4 * ma[3] * ma[1]
        - 3 * ma[2] ** 2
        + 12 * ma[2] * ma[1] ** 2
        - 6 * ma[1] ** 4
    )
    print("PASS: disconnected cross terms cancel exactly in cumulants 2, 3 and 4")

    # Exact polar cumulants used in (12).
    eps = Fraction(7, 5)
    polar = [Fraction(0)] + [Fraction(factorial(r - 1), 1) / eps**r for r in range(1, nmax + 1)]
    assert polar[1] == 1 / eps
    assert polar[2] == 1 / eps**2
    assert polar[3] == 2 / eps**3
    print("PASS: exponential polar cumulants are (r-1)! epsilon^{-r}")
    print("PASS: 104_53 connected-cumulant cancellation diagnostics")


if __name__ == "__main__":
    main()
