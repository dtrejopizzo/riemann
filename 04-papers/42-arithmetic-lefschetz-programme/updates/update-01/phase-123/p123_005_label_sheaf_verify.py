#!/usr/bin/env python3
"""Finite exact checks for the support/sheaf identities in P123.005."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import gcd


PRIMES = (2, 3, 5, 7)


def prime_factors(value: int) -> set[int]:
    out: set[int] = set()
    d = 2
    while d * d <= value:
        if value % d == 0:
            out.add(d)
            while value % d == 0:
                value //= d
        d += 1
    if value > 1:
        out.add(value)
    return out


def valuation_support(q: Fraction) -> frozenset[int]:
    support: set[int] = set()
    support.update(prime_factors(q.numerator))
    support.update(prime_factors(q.denominator))
    return frozenset(support)


def gamma_box(s: frozenset[int], bound: int = 30) -> set[Fraction]:
    return {
        Fraction(a, b)
        for a in range(1, bound + 1)
        for b in range(1, bound + 1)
        if gcd(a, b) == 1 and valuation_support(Fraction(a, b)) <= s
    }


def main() -> None:
    finite_sets = [
        frozenset(c)
        for r in range(len(PRIMES) + 1)
        for c in combinations(PRIMES, r)
    ]

    for s in finite_sets:
        gamma_s = gamma_box(s)
        assert Fraction(1) in gamma_s
        assert {1 / q for q in gamma_s} == gamma_s

    for s in finite_sets:
        for t in finite_sets:
            lhs = gamma_box(s) & gamma_box(t)
            rhs = gamma_box(s & t)
            assert lhs == rhs

    # The height truncation is finite and every label in it uses finitely
    # many primes, the density mechanism in Theorem 4.1.
    height_box = {
        Fraction(a, b)
        for a in range(1, 41)
        for b in range(1, 41)
        if gcd(a, b) == 1 and max(a, b) <= 40
    }
    used_primes = set().union(*(valuation_support(q) for q in height_box))
    assert used_primes == {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}

    print("P123.005 local-unit intersection/sheaf identity: PASS")
    print("P123.005 finite-height finite-prime density check: PASS")
    print("Scope: label sheaf only; completed Bruhat-Schwartz action remains OPEN")


if __name__ == "__main__":
    main()
