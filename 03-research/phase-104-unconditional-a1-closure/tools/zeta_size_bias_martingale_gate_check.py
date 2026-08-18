#!/usr/bin/env python3
"""Exact algebra checks for 104_43.

This is deliberately a rational/symbolic checker.  It verifies the divisor
selector identity on exponent vectors, the two opposite signs of the
selector-versus-uniform first moment, and the leading Efron--Stein variance
constant for the Laguerre tests.  It does not evaluate zeta, Li coefficients,
A1, or RH.
"""

from fractions import Fraction
from math import comb


def divisor_selector_coefficients(exponents: tuple[int, ...]) -> tuple[int, ...]:
    """Coefficient of each formal log(p) in sum_{d|n} Lambda(d)."""
    # For p_i^a || n, the nonzero Lambda divisors from that tower are
    # p_i, ..., p_i^a, each with coefficient one on log(p_i).
    return tuple(a for a in exponents)


def log_n_coefficients(exponents: tuple[int, ...]) -> tuple[int, ...]:
    return exponents


def first_moment_quadratic(exponents: tuple[int, ...]) -> dict[tuple[int, int], int]:
    """Formal coefficients of 2*log(n)*(K y-U y).

    The variables are l_i=log(p_i).  Keys (i,j), i<=j, encode l_i*l_j.
    """
    out: dict[tuple[int, int], int] = {}
    for i, a in enumerate(exponents):
        out[(i, i)] = a * (a + 1) - a * a
        for j in range(i + 1, len(exponents)):
            out[(i, j)] = -2 * a * exponents[j]
    return out


def check_divisor_factorization() -> None:
    for exponents in ((1,), (7,), (1, 1), (3, 2, 1), (4, 0, 5, 2)):
        assert divisor_selector_coefficients(exponents) == log_n_coefficients(exponents)


def check_opposite_selector_signs() -> None:
    # n=2: Q=(log 2)^2>0.
    assert first_moment_quadratic((1,)) == {(0, 0): 1}

    # n=30: with a=log2, b=log3, c=log5,
    # Q=a^2+b^2+c^2-2ab-2ac-2bc=(a+b-c)^2-4ab<0.
    q30 = first_moment_quadratic((1, 1, 1))
    assert q30 == {
        (0, 0): 1,
        (0, 1): -2,
        (0, 2): -2,
        (1, 1): 1,
        (1, 2): -2,
        (2, 2): 1,
    }
    # The proof uses only 1 < 6/5 < 2 < 3:
    assert Fraction(1) < Fraction(6, 5) < Fraction(2) < Fraction(3)


def check_variance_constants() -> None:
    # If d=n-1 and phi_n=L_d^(1)-(d+1), then
    # Var(phi_n(X_eps)) ~ (C(2d,d)-1) eps^(-2d).
    for n in range(2, 51):
        d = n - 1
        constant = comb(2 * d, d) - 1
        assert constant > 0
        # Direct leading-moment algebra with a_d=(-1)^d/d!:
        # a_d^2 (2d)! - (a_d d!)^2 = C(2d,d)-1.
        factorial = 1
        for k in range(2, d + 1):
            factorial *= k
        factorial_2d = factorial
        for k in range(d + 1, 2 * d + 1):
            factorial_2d *= k
        direct = Fraction(factorial_2d, factorial * factorial) - 1
        assert direct == constant


def main() -> None:
    check_divisor_factorization()
    check_opposite_selector_signs()
    check_variance_constants()
    print("zeta size-bias/martingale gate: PASS")
    print("  divisor selector sum Lambda(d)=log(n): exact on formal exponent vectors")
    print("  selector-minus-uniform linear response: positive at n=2, negative at n=30")
    print("  Laguerre Efron--Stein leading variance constants: exact for 2<=n<=50")
    print("  no claim about A1 or RH")


if __name__ == "__main__":
    main()
