#!/usr/bin/env python3
"""Exact common-refinement falsifier for finite root intersections."""

from fractions import Fraction
from math import gcd, lcm


def root_stratum(M: int, level: int, common: int) -> set[int]:
    """The unique order-M*level subgroup of R_{M*common}."""
    step = common // level
    return {(step * a) % (M * common) for a in range(M * level)}


def cross_intersection(M: int, m: int, n: int) -> Fraction:
    L = lcm(m, n)
    Sm = root_stratum(M, m, L)
    Sn = root_stratum(M, n, L)
    return Fraction(len(Sm & Sn), M)


def primitive_determinant(m: int, n: int) -> int:
    c = gcd(m, n) - (m + n)
    return m * n - c * c


def main() -> None:
    pairs_checked = 0
    for M in (1, 2, 3, 5, 7):
        for m in range(1, 11):
            for n in range(1, 11):
                value = cross_intersection(M, m, n)
                assert value == gcd(m, n)
                if m != n:
                    assert primitive_determinant(m, n) < 0
                else:
                    assert primitive_determinant(m, n) == 0
                pairs_checked += 1

    I23 = cross_intersection(5, 2, 3)
    c23 = int(I23) - 2 - 3
    det23 = 2 * 3 - c23 * c23
    assert I23 == 1
    assert c23 == -4
    assert det23 == -10

    # Exact square-root test without floating point:
    # |c| > sqrt(mn) iff c^2 > mn.
    for m in range(1, 30):
        for n in range(1, 30):
            if m == n:
                continue
            c = gcd(m, n) - (m + n)
            assert c * c > m * n

    print("common-refinement rows checked:", pairs_checked)
    print("I(Gamma_2,Gamma_3):", I23)
    print("primitive cross term c_23:", c23)
    print("primitive determinant det G^0_{2,3}:", det23)
    print("all distinct pairs in 1..29 indefinite: yes")


if __name__ == "__main__":
    main()
