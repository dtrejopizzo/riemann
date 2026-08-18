#!/usr/bin/env python3
"""Finite exact checks for the split holonomy Euler identities.

This script verifies only the algebraic consequences claimed in 114_a_160.
It deliberately does not label the split graded package as derived
cohomology and does not manufacture a determinant from covering dimension.
"""

from fractions import Fraction
from itertools import product


def pair_terms(h_pos, h_neg, k_pos, k_neg):
    """Dimensions of degrees 0, 1 and 2 in the split external product."""
    return (
        h_pos * k_pos,
        h_pos * k_neg + h_neg * k_pos,
        h_neg * k_neg,
    )


def euler(terms):
    return terms[0] - terms[1] + terms[2]


def check_kunneth():
    vals = [Fraction(0), Fraction(1, 3), Fraction(2), Fraction(7, 2)]
    for hp, hm, kp, km in product(vals, repeat=4):
        lhs = euler(pair_terms(hp, hm, kp, km))
        rhs = (hp - hm) * (kp - km)
        assert lhs == rhs, (hp, hm, kp, km, lhs, rhs)


def check_surface_sum():
    # Formal degree data; logarithms are represented by independent rational
    # test values because only distributivity is at issue here.
    first = [(2, Fraction(3, 2)), (1, Fraction(5, 3))]
    second = [(3, Fraction(7, 4)), (4, Fraction(11, 5))]
    pair_sum = sum(
        a * lp * b * lq for a, lp in first for b, lq in second
    )
    d1 = sum(a * lp for a, lp in first)
    d2 = sum(b * lq for b, lq in second)
    assert pair_sum == d1 * d2


def check_no_false_monoidal_target():
    # A mixed graded product H^0(D) x H^0(-E) has divisor degree D-E.
    # Except in degenerate cases this differs from both +(D+E) and -(D+E),
    # so it is not a term of the proposed two-term package for D+E.
    for d, e in [(-3, 5), (2, 7), (4, -1)]:
        mixed = d - e
        assert mixed not in {d + e, -(d + e)}


if __name__ == "__main__":
    check_kunneth()
    check_surface_sum()
    check_no_false_monoidal_target()
    print("PASS: split Kunneth Euler identity is exact.")
    print("PASS: prime-pair Euler sum factors as d1*d2.")
    print("PASS: no unsupported monoidal structure is inferred.")
