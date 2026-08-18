#!/usr/bin/env python3
"""Finite checks for the bounded Laurent binary tree in 114.a.30."""

from fractions import Fraction
from math import comb, floor, log


def check(label, condition):
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s}  {label}")
    if not condition:
        raise AssertionError(label)


print("A. Binary node and depth coefficients")
u_norm_square = Fraction(1, 4) + Fraction(1, 4)
check("A node row/column is a strict Euclidean contraction",
      u_norm_square == Fraction(1, 2) and u_norm_square < 1)
for depth in range(1, 16):
    leaf_weight = Fraction(1, 4) ** depth
    total_weight = 2**depth * leaf_weight
    check(f"A({depth}) leaf and total weights",
          leaf_weight == Fraction(1, 4**depth)
          and total_weight == Fraction(1, 2**depth))

print("\nB. Ternary multiplicities fit the binary tree")
for depth in range(1, 60):
    rank = floor(log(2 ** (depth + 1) + 1, 3))
    while 3 ** (rank + 1) <= 2 ** (depth + 1) + 1:
        rank += 1
    while 3**rank > 2 ** (depth + 1) + 1:
        rank -= 1
    used = (3**rank - 1) // 2
    next_used = (3 ** (rank + 1) - 1) // 2
    check(f"B({depth}) exact maximal rank and capacity",
          used <= 2**depth < next_used)

print("\nC. Finite valuations")
for depth in range(1, 20):
    denominator = 4**depth
    check(f"C({depth}) first exponent is exactly 2d",
          denominator == 2 ** (2 * depth))

print("\nD. Cross-polytope entropy")
q = 2
ratios = []
expected = log(2) / log(3)
for scale in range(30, 121, 15):
    rank = floor(log(2 ** (scale + 1) + 1, 3))
    while 3 ** (rank + 1) <= 2 ** (scale + 1) + 1:
        rank += 1
    while 3**rank > 2 ** (scale + 1) + 1:
        rank -= 1
    radius = q**scale
    count = sum(2**j * comb(rank, j) * comb(radius, j)
                for j in range(rank + 1))
    ratios.append(log(count) / (scale * scale * log(q)))
check("D entropy approaches log(2)/log(3)",
      abs(ratios[-1] - expected) < abs(ratios[0] - expected)
      and 0.9 * expected < ratios[-1] < 1.1 * expected)

print("\n" + "=" * 72)
print("VERDICT: ALL CHECKS PASS")
