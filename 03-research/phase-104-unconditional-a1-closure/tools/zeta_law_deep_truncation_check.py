#!/usr/bin/env python3
"""Finite algebra checks for 104_79 (no numerical PNT certification)."""

from fractions import Fraction
from math import comb, exp, factorial, log


def laguerre_p(n):
    """Coefficients of L_{n-1}^{(1)} in increasing powers."""
    return [Fraction((-1) ** j * comb(n, j + 1), factorial(j))
            for j in range(n)]


def primitive(p):
    out = [Fraction(0)] * (len(p) + 1)
    for j, value in enumerate(p):
        out[j + 1] = value / (j + 1)
    return out


def eval_poly(p, x):
    value = Fraction(0)
    for coefficient in reversed(p):
        value = value * x + coefficient
    return value


def prime_formula(n, x, y):
    return sum(
        Fraction((-1) ** (k - 1) * comb(n, k), factorial(k))
        * (k * x**k - y**k)
        for k in range(1, n + 1)
    )


def semiprime_formula(n, x, z, y):
    return sum(
        Fraction((-1) ** (k - 1) * comb(n, k), factorial(k))
        * (k * (x**k + z**k) - y**k)
        for k in range(1, n + 1)
    )


def check_expansions():
    for n in range(2, 13):
        p = laguerre_p(n)
        u = primitive(p)
        for epsilon in (Fraction(1, 3), Fraction(2, 5)):
            laplace = sum(coefficient * factorial(j) / epsilon ** (j + 1)
                          for j, coefficient in enumerate(p))
            assert laplace == 1 - (1 - 1 / epsilon) ** n
        for x, z, y in [(Fraction(11), Fraction(12), Fraction(7)),
                        (Fraction(17), Fraction(18), Fraction(23))]:
            lhs_p = x * eval_poly(p, x) - eval_poly(u, y)
            assert lhs_p == prime_formula(n, x, y)
            lhs_s = x * eval_poly(p, x) + z * eval_poly(p, z) - eval_poly(u, y)
            assert lhs_s == semiprime_formula(n, x, z, y)


def check_dominance():
    # Rational points satisfy the hypotheses of (15) and (20).
    for n in (8, 9, 20, 21):
        x = Fraction(1000 * n**3)
        y = x
        zp = prime_formula(n, x, y)
        prime_lower = Fraction(n - 1, 2 * factorial(n)) * x**n
        assert ((-1) ** (n - 1)) * zp >= prime_lower

        z = Fraction(21, 20) * x
        w = x + z
        pole = Fraction(n + 1, n) * w
        zs = semiprime_formula(n, x, z, pole)
        semi_lower = Fraction(1, 4 * factorial(n)) * w**n
        assert ((-1) ** n) * zs >= semi_lower


def check_analytic_constants():
    assert 2 * (exp(Fraction(1, 8)) - 1) < Fraction(1, 2)
    for n in range(5, 101):
        assert 2 * n * Fraction(11, 21) ** n <= Fraction(1, 2)
    for n in (10, 100, 1000):
        a = Fraction(1, 100 * n)
        assert 6 * n * (exp(a) - 1) < Fraction(1, 2)
    assert Fraction(11, 21) < Fraction(524, 1000)


def check_scale():
    # The inequalities are asymptotic; these rows merely check the announced
    # separation once the elementary threshold has been crossed.
    for x_cap in (100_000, 200_000):
        for n in (x_cap // 2, x_cap):
            lower_log = n * (x_cap / 100 - log(x_cap))
            assert lower_log >= x_cap * x_cap / 400
        tail_log = x_cap * x_cap / 400 - x_cap / 100 - log(x_cap)
        assert tail_log >= x_cap * x_cap / 500
        assert x_cap * x_cap / 400 > x_cap**0.5


def main():
    check_expansions()
    check_dominance()
    check_analytic_constants()
    check_scale()
    print("PASS: zeta-law deep truncation algebra and scale checks")


if __name__ == "__main__":
    main()
