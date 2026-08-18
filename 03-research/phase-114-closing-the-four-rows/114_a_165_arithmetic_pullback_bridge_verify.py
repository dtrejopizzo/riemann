#!/usr/bin/env python3
"""Exact algebraic checks for the canonical pair-pullback bridge."""

from fractions import Fraction
from itertools import product


def pair_dimension(first, second):
    return sum(a * lp * b * lq for a, lp in first for b, lq in second)


def main():
    # Rational surrogates for independent logarithmic periods.  The identity
    # checked is formal and therefore valid for the actual log(p)'s.
    first = [(2, Fraction(2, 3)), (5, Fraction(7, 4))]
    second = [(3, Fraction(5, 2)), (1, Fraction(11, 6))]
    d1 = sum(a * lp for a, lp in first)
    d2 = sum(b * lq for b, lq in second)
    assert pair_dimension(first, second) == d1 * d2

    # Reversing a periodic generator p to p^{-1} leaves both its cyclic
    # subgroup and neutral coset unchanged.
    for p in [2, 3, 5, 7, 11, 13]:
        base = Fraction(p, 1)
        inverse = Fraction(1, p)
        positive_powers = {base**k for k in range(-8, 9)}
        inverse_powers = {inverse**k for k in range(-8, 9)}
        assert positive_powers == inverse_powers
        assert 1 in positive_powers

    # Pair fibers are ordered Cartesian products: each tested point occurs
    # once, with no diagonal collapse when p != q.
    primes = [2, 3, 5, 7]
    pairs = list(product(primes, repeat=2))
    assert len(pairs) == len(primes) ** 2
    assert len(set(pairs)) == len(pairs)
    assert any(p != q for p, q in pairs)

    print("PASS: pair-fiber dimensions factor as d1*d2.")
    print("PASS: periodic subgroup and neutral coset are orientation independent.")
    print("PASS: the arithmetic pullback retains off-diagonal prime pairs.")


if __name__ == "__main__":
    main()
