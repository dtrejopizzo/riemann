#!/usr/bin/env python3
"""Exact checks for 104_44 (Fraction only)."""

from fractions import Fraction
from math import comb, factorial


def poly_add(a, b):
    out = [Fraction(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return trim(out)


def poly_scale(a, scalar):
    return trim([scalar * value for value in a])


def poly_eval(a, x):
    value = Fraction(0)
    for coefficient in reversed(a):
        value = value * x + coefficient
    return value


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def laguerre(n, alpha=0):
    return [
        Fraction((-1) ** k * comb(n + alpha, n - k), factorial(k))
        for k in range(n + 1)
    ]


def prime_factorization(n):
    factors = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


PRIME_WEIGHTS = {
    2: Fraction(2),
    3: Fraction(3),
    5: Fraction(5),
    7: Fraction(7),
    11: Fraction(11),
    13: Fraction(13),
    17: Fraction(17),
    19: Fraction(19),
}


def formal_log(n):
    return sum(
        (exponent * PRIME_WEIGHTS[prime]
         for prime, exponent in prime_factorization(n).items()),
        Fraction(0),
    )


def formal_lambda(n):
    factors = prime_factorization(n)
    if len(factors) != 1:
        return Fraction(0)
    prime = next(iter(factors))
    return PRIME_WEIGHTS[prime]


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def check_divisor_identity():
    for n in range(2, 20):
        lhs = sum((formal_lambda(d) for d in divisors(n)), Fraction(0))
        assert lhs == formal_log(n), (n, lhs, formal_log(n))


def check_addition():
    points = [(Fraction(2, 3), Fraction(5, 4)),
              (Fraction(7, 5), Fraction(3, 2))]
    for n in range(8):
        target = laguerre(n, 1)
        for x, y in points:
            lhs = poly_eval(target, x + y)
            rhs = sum(
                (poly_eval(laguerre(j), x)
                 * poly_eval(laguerre(n - j), y)
                 for j in range(n + 1)),
                Fraction(0),
            )
            assert lhs == rhs, (n, lhs, rhs)


def integrate_poly_zero_to_x(poly):
    out = [Fraction(0)]
    out.extend(coefficient / (degree + 1)
               for degree, coefficient in enumerate(poly))
    return out


def check_continuous_operator():
    # It suffices to set epsilon=1; scaling then proves general epsilon.
    for n in range(8):
        integral = integrate_poly_zero_to_x(laguerre(n))
        # (1/x) integral_0^x L_n = L_n^(1)/(n+1).
        quotient = integral[1:]
        target = poly_scale(laguerre(n, 1), Fraction(1, n + 1))
        assert trim(quotient) == trim(target), (n, quotient, target)

        # Gamma(2,1) squared norm: integral x e^-x p(x)^2 dx.
        square = [Fraction(0)] * (2 * n + 1)
        for i, ai in enumerate(target):
            for j, aj in enumerate(target):
                square[i + j] += ai * aj
        norm = sum((coefficient * factorial(k + 1)
                    for k, coefficient in enumerate(square)), Fraction(0))
        assert norm == Fraction(1, n + 1), (n, norm)


def check_dilation():
    x = Fraction(7, 9)
    for n in range(9):
        for beta in (Fraction(2), Fraction(3, 2), Fraction(5, 3)):
            lhs = poly_eval(laguerre(n), beta * x)
            rhs = sum(
                (Fraction(comb(n, j)) * beta ** j * (1 - beta) ** (n - j)
                 * poly_eval(laguerre(j), x)
                 for j in range(n + 1)),
                Fraction(0),
            )
            assert lhs == rhs, (n, beta, lhs, rhs)

    for n in range(1, 9):
        epsilon = Fraction(1, n + 2)
        load = sum(
            (Fraction(comb(n, j)) * epsilon ** (-j)
             * abs(1 - epsilon ** (-1)) ** (n - j)
             for j in range(n + 1)),
            Fraction(0),
        )
        assert load == (Fraction(2, 1) / epsilon - 1) ** n


def main():
    check_divisor_identity()
    check_addition()
    check_continuous_operator()
    check_dilation()
    print("104_44 exact checks: PASS")


if __name__ == "__main__":
    main()
