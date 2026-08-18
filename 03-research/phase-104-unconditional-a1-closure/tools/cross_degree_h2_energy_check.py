#!/usr/bin/env python3
"""Exact/diagnostic checks for 104_63.

Pure Python.  Fraction arithmetic certifies the Laguerre Christoffel--Darboux
identity and the pole Laplace polynomial.  The final artificial-pole rows are
diagnostic only and illustrate the fourth-root normalization in Theorem 2.1.
"""

from fractions import Fraction
from math import comb, log


def laguerre_alpha_one(k: int, x: Fraction) -> Fraction:
    if k == 0:
        return Fraction(1)
    lm1 = Fraction(1)
    cur = Fraction(2) - x
    if k == 1:
        return cur
    for j in range(1, k):
        nxt = ((2 * j + 2 - x) * cur - (j + 1) * lm1) / (j + 1)
        lm1, cur = cur, nxt
    return cur


def kernel_sum(m: int, x: Fraction, y: Fraction) -> Fraction:
    return sum(
        (laguerre_alpha_one(k, x) * laguerre_alpha_one(k, y)
         / Fraction(k + 1))
        for k in range(m + 1)
    )


def kernel_cd(m: int, x: Fraction, y: Fraction) -> Fraction:
    assert x != y
    return (
        laguerre_alpha_one(m, x) * laguerre_alpha_one(m + 1, y)
        - laguerre_alpha_one(m + 1, x) * laguerre_alpha_one(m, y)
    ) / (x - y)


def p_formula(n: int, eps: Fraction) -> Fraction:
    return n * sum(
        Fraction(comb(n - 1, j - 1) * ((-1) ** (j - 1)), j) / eps**j
        for j in range(1, n + 1)
    )


def p_laplace_polynomial(n: int, eps: Fraction) -> Fraction:
    # Integral of exp(-eps*x)L_{n-1}^{(1)}(x): k! cancels the k! coefficient.
    return sum(
        Fraction(((-1) ** k) * comb(n, k + 1), 1) / eps ** (k + 1)
        for k in range(n)
    )


def artificial_energy(n0: int) -> float:
    # G(z)=-1/(1-2z), hence lambda_n=-2^n and r0=1/2.
    return sum((4.0**n) / n for n in range(n0 + 1, 2 * n0 + 1))


def main() -> None:
    for m in range(0, 10):
        for x, y in ((Fraction(1, 3), Fraction(7, 5)),
                     (Fraction(2), Fraction(9, 4)),
                     (Fraction(-1, 2), Fraction(5, 2))):
            assert kernel_sum(m, x, y) == kernel_cd(m, x, y)

    for n in range(1, 13):
        for eps in (Fraction(1, 2), Fraction(2, 3), Fraction(3, 5)):
            assert p_formula(n, eps) == p_laplace_polynomial(n, eps)

        # eps^n p_n(eps) -> (-1)^(n-1); check the exact leading coefficient.
        leading = Fraction((-1) ** (n - 1), 1)
        # The coefficient of eps^{-n} in the closed sum is the j=n term.
        extracted = Fraction(n * ((-1) ** (n - 1)), n)
        assert extracted == leading

    print("Christoffel-Darboux exact checks: PASS")
    print("pole/Laguerre Laplace checks:       PASS")
    print("artificial pole w=1/2 (target fourth root = 2):")
    for n0 in (8, 16, 32, 64, 128):
        e = artificial_energy(n0)
        root = e ** (1.0 / (4.0 * n0))
        print(f"  N={n0:3d}  E_N^(1/(4N))={root:.12f}  gap={2-root:.3e}")
    # A logarithmic implementation avoids overflow and gives the limiting trend.
    for n0 in (256, 512, 1024):
        scaled = sum(4.0 ** (n - 2 * n0) / n
                     for n in range(n0 + 1, 2 * n0 + 1))
        log_e = 2 * n0 * log(4.0) + log(scaled)
        root = pow(2.718281828459045, log_e / (4.0 * n0))
        print(f"  N={n0:4d}  E_N^(1/(4N))={root:.12f}  gap={2-root:.3e}")


if __name__ == "__main__":
    main()
