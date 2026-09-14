#!/usr/bin/env python3
"""Exact rational/local-valuation checks for P123.009."""

from fractions import Fraction


def vp_int(n, p):
    n = abs(n)
    out = 0
    while n and n % p == 0:
        out += 1
        n //= p
    return out


def vp(q, p):
    return vp_int(q.numerator, p) - vp_int(q.denominator, p)


def pnorm(q, p):
    return Fraction(p) ** (-vp(q, p))


def local_a_squared(q, p):
    # Square of |q|_p^(-1/2)/|1-q^-1|_p avoids formal square roots.
    one_minus_inv = 1 - 1 / q
    return 1 / (pnorm(q, p) * pnorm(one_minus_inv, p) ** 2)


def local_a_inv_squared(q, p):
    return local_a_squared(1 / q, p)


qs = [Fraction(2), Fraction(3, 2), Fraction(5, 7), Fraction(11, 4)]
primes = [2, 3, 5, 7, 11, 13]

for q in qs:
    for p in primes:
        assert local_a_squared(q, p) == local_a_inv_squared(q, p)

        # Equivalent forms of the fixed-point coefficient, squared.
        lhs = local_a_squared(q, p)
        rhs = pnorm(q, p) / pnorm(q - 1, p) ** 2
        assert lhs == rhs

    # Away from primes dividing numerator, denominator, or q-1, the local
    # determinant factor is one.
    exceptional = set()
    for p in primes:
        if vp(q, p) or vp(q - 1, p):
            exceptional.add(p)
    for p in set(primes) - exceptional:
        assert local_a_squared(q, p) == 1

print("P123.009 local excess/dagger/unit-factor identities: PASS")
