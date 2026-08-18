#!/usr/bin/env python3
"""Exact rational checks for the near-quartic reduction (104_23).

This verifies the sharp fixed exponent at T=1000, the signs of the
generalized-binomial polar channels for r in (3,4), and the coefficientwise
identity with the confluent-hypergeometric density.  It is an algebra check,
not a proof of the remaining global coefficient sign.
"""

from fractions import Fraction


def generalized_binomial(r, j):
    value = Fraction(1)
    for k in range(j):
        value *= r - k
        value /= k + 1
    return value


def pochhammer(a, k):
    value = Fraction(1)
    for j in range(k):
        value *= a + j
    return value


def main():
    cutoff_floor = 1000
    r_star = Fraction(2002, 501)
    r_max = Fraction(4 * (cutoff_floor + 1), cutoff_floor + 2)
    assert r_star == r_max

    residual = (Fraction(1, 1) / r_star
                - Fraction(1, 4)
                - Fraction(1, 4 * (cutoff_floor + 1)))
    assert residual == 0

    # For 3 < r < 4, (-1)^j binom(r,j) is negative only at j=1,3.
    signs = {}
    for j in range(1, 21):
        coefficient = (-1) ** j * generalized_binomial(r_star, j)
        signs[j] = (coefficient > 0) - (coefficient < 0)
    assert signs[1] == -1 and signs[3] == -1
    assert signs[2] == 1
    assert all(signs[j] == 1 for j in range(4, 21))

    # Compare the q^k coefficient in
    #   sum_{j>=1} (-1)^j binom(r,j)c^j q^(j-1)/(j-1)!
    # with -r*c*1F1(1-r;2;c*q), for an exact rational c.
    c = Fraction(1, 2)
    for k in range(12):
        j = k + 1
        direct = ((-1) ** j * generalized_binomial(r_star, j)
                  * c ** j / factorial(k))
        hyper = (-r_star * c * pochhammer(1 - r_star, k) * c ** k
                 / (pochhammer(Fraction(2), k) * factorial(k)))
        assert direct == hyper

    # Euler logarithmic atoms are positive for u>0: use p=2, u=1/2.
    p = 2
    u = Fraction(1, 2)
    # Compare p^(k*u)>1 without introducing irrational arithmetic.
    # Squaring gives p^k>1 for every k>=1.
    assert all(p ** k > 1 for k in range(1, 9)) and u > 0

    print(f"PASS: r_* = {r_star} = 4(T+1)/(T+2) at T={cutoff_floor}")
    print("PASS: exact A0 residual at T=1000 is zero")
    print("PASS: polar channels j=1,3 negative and j=2,j>=4 positive")
    print("PASS: generalized-binomial and 1F1 coefficients agree (12 terms)")
    print("No floating-point sign decision was used.")


def factorial(n):
    value = 1
    for k in range(2, n + 1):
        value *= k
    return value


if __name__ == "__main__":
    main()
