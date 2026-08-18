#!/usr/bin/env python3
"""Exact checks for 104_80 (standard library only)."""

from fractions import Fraction
from math import comb, factorial
from itertools import product


def laguerre(n, alpha=0):
    """Coefficients of L_n^(alpha), low degree first."""
    return [
        Fraction((-1) ** k * comb(n + alpha, n - k), factorial(k))
        for k in range(n + 1)
    ]


def add_poly(a, b):
    out = [Fraction(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return out


def mul_bivariate_x_y(px, py):
    """Dictionary (x-degree,y-degree) for px(x)py(y)."""
    return {(i, j): a * b for i, a in enumerate(px)
            for j, b in enumerate(py) if a * b}


def add_bivariate(dst, src):
    for key, value in src.items():
        dst[key] = dst.get(key, Fraction(0)) + value
        if not dst[key]:
            del dst[key]


def shifted_univariate(poly):
    """Dictionary for poly(x+y)."""
    out = {}
    for k, value in enumerate(poly):
        for j in range(k + 1):
            key = (j, k - j)
            out[key] = out.get(key, Fraction(0)) + value * comb(k, j)
    return {k: v for k, v in out.items() if v}


def check_laguerre_addition():
    for n in range(1, 13):
        lhs = shifted_univariate(laguerre(n - 1, 1))
        rhs = {}
        for j in range(n):
            add_bivariate(rhs, mul_bivariate_x_y(
                laguerre(j, 0), laguerre(n - 1 - j, 0)))
        assert lhs == rhs, (n, lhs, rhs)


def mobius_squarefree(bits):
    return -1 if sum(bits) % 2 else 1


def check_mobius_toggle():
    # Formal coefficients of log p_j in sum_{d|rad(r)} mu(d) log(r/d).
    for k in range(2, 5):
        for exponents in product(range(1, 5), repeat=k):
            coeff = [0] * k
            for bits in product((0, 1), repeat=k):
                mu = mobius_squarefree(bits)
                for j, a_j in enumerate(exponents):
                    coeff[j] += mu * (a_j - bits[j])
            assert coeff == [0] * k
    for a in range(1, 12):
        coeff = 0
        for bit in (0, 1):
            coeff += (-1 if bit else 1) * (a - bit)
        assert coeff == 1


def check_pole_disk_identity():
    samples = [
        (Fraction(3, 4), Fraction(7, 3), Fraction(1, 10)),
        (Fraction(1, 2), Fraction(14), Fraction(1, 100)),
        (Fraction(2, 5), Fraction(9, 2), Fraction(1, 20)),
        (Fraction(9, 10), Fraction(5), Fraction(2, 5)),
    ]
    for beta, gamma, eps in samples:
        numerator = (beta - 1 - eps) ** 2 + gamma ** 2
        denominator = (beta - eps) ** 2 + gamma ** 2
        difference = denominator - numerator
        assert difference == 2 * beta - 1 - 2 * eps
        assert (numerator < denominator) == (beta > Fraction(1, 2) + eps)


def check_geometric_pole_coefficients():
    # (m/z0)/(1-z/z0) has coefficient m*z0^(-n) at z^(n-1).
    m = Fraction(7)
    z0 = Fraction(-3, 5)
    residue = (m / z0) / (-1 / z0)
    assert residue == -m
    coefficients = [m / z0 * (1 / z0) ** k for k in range(10)]
    expected = [m * z0 ** (-n) for n in range(1, 11)]
    assert coefficients == expected


def main():
    check_laguerre_addition()
    check_mobius_toggle()
    check_pole_disk_identity()
    check_geometric_pole_coefficients()
    print("PASS: maximal signed Lambda identity checks")


if __name__ == "__main__":
    main()
