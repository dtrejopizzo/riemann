#!/usr/bin/env python3
"""Exact finite checks for R161_001, Theorems 2.1 and 4.1.

This script checks coefficient identities only.  It does not test a sign of the
Weil form and uses no floating-point approximation except for display.
"""

from fractions import Fraction
from math import log


def primes_upto(limit: int) -> list[int]:
    sieve = [True] * (limit + 1)
    sieve[:2] = [False, False]
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = [False] * (((limit - p * p) // p) + 1)
    return [p for p in range(2, limit + 1) if sieve[p]]


def prime_power_base(n: int, primes: list[int]) -> int | None:
    for p in primes:
        value = p
        while value < n:
            value *= p
        if value == n:
            return p
    return None


def lambda_coeff(n: int, primes: list[int]) -> dict[int, Fraction]:
    """Formal log-prime vector for Lambda(n)."""
    p = prime_power_base(n, primes)
    return {} if p is None else {p: Fraction(1)}


def add_vectors(left: dict[int, Fraction], right: dict[int, Fraction]) -> dict[int, Fraction]:
    result = dict(left)
    for p, value in right.items():
        result[p] = result.get(p, Fraction()) + value
        if result[p] == 0:
            del result[p]
    return result


def scale_vector(vector: dict[int, Fraction], scalar: Fraction) -> dict[int, Fraction]:
    return {p: scalar * value for p, value in vector.items() if scalar * value}


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def formal_log(n: int, primes: list[int]) -> dict[int, Fraction]:
    result: dict[int, Fraction] = {}
    value = n
    for p in primes:
        exponent = 0
        while value % p == 0:
            exponent += 1
            value //= p
        if exponent:
            result[p] = Fraction(exponent)
    assert value == 1
    return result


def convolved_coefficient(k: int, m_limit: int, d_limit: int, coefficient) -> dict[int, Fraction]:
    result: dict[int, Fraction] = {}
    for d in divisors(k):
        m = k // d
        if d <= d_limit and m <= m_limit:
            result = add_vectors(result, coefficient(d))
    return result


def main() -> None:
    n_limit = 40
    m_limit = 40
    d_limit = 80
    primes = primes_upto(d_limit * m_limit)

    lam = lambda n: lambda_coeff(n, primes)

    for k in range(1, n_limit + 1):
        got = convolved_coefficient(k, m_limit, d_limit, lam)
        want = formal_log(k, primes)
        assert got == want, (k, got, want)

    # Deletion of Lambda(2): delta(2)=-log 2.
    deleted = lambda n: {} if n == 2 else lam(n)
    got_deleted = convolved_coefficient(2, m_limit, d_limit, deleted)
    assert got_deleted == {}
    assert add_vectors(got_deleted, scale_vector(formal_log(2, primes), Fraction(-1))) == {2: Fraction(-1)}

    # Amplification at n0=6 by c=3: delta(k)=3 on multiples of 6.
    n0 = 6
    c = Fraction(3)

    def amplified(n: int) -> dict[int, Fraction]:
        value = lam(n)
        if n == n0:
            # A separate formal marker -1 represents the scalar c, independent of log p.
            value = add_vectors(value, {-1: c})
        return value

    got_amp = convolved_coefficient(n0, m_limit, d_limit, amplified)
    want_amp = add_vectors(formal_log(n0, primes), {-1: c})
    assert got_amp == want_amp

    # Sign flip at 2: Lambda(2) -> -Lambda(2), hence delta(2)=-2 log 2.
    def sign_flip_2(n: int) -> dict[int, Fraction]:
        value = lam(n)
        if n == 2:
            value = scale_vector(value, Fraction(-1))
        return value

    flip_defect = add_vectors(
        convolved_coefficient(2, m_limit, d_limit, sign_flip_2),
        scale_vector(formal_log(2, primes), Fraction(-1)),
    )
    assert flip_defect == {2: Fraction(-2)}

    # Hyperbola tail coefficients are nonnegative formal log-prime vectors.
    for k in range(m_limit + 1, d_limit * m_limit + 1):
        coeff = convolved_coefficient(k, m_limit, d_limit, lam)
        assert all(value >= 0 for value in coeff.values())

    print("PASS: Lambda*1=log on the completed interior k<=N")
    print("PASS: hyperbola-tail coefficients are nonnegative")
    print("PASS: deletion, amplification and sign-flip defects survive in the interior")
    print(f"display only: -2 log 2 = {-2 * log(2):.15f}")


if __name__ == "__main__":
    main()
