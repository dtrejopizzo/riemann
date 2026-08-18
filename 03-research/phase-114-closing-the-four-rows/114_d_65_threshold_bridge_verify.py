#!/usr/bin/env python3
"""Exact rational inequalities in the D.65 threshold Schur bridge."""

from fractions import Fraction

# Directed endpoint below the positive root of the Schur determinant.
# All analytic estimates in D.65 remain valid here because T < .35.
delta = Fraction(37, 10**6)
gamma = Fraction(783, 10**4)
boundary = Fraction(13483, 10**4) - 40 * delta
cross_sq = 53**2 * delta

assert gamma > 0
assert boundary > 0
assert cross_sq < gamma * boundary

print("PASS endpoint-to-interior Schur determinant")
print("PASS QW_T>0 for log(2)/2 <= T <= log(2)/2 + 37/2000000")
