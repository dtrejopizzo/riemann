#!/usr/bin/env python3
"""Finite checks for the optimal signed rank and candidate RR coefficient."""

from itertools import product
from math import comb, floor, log


def cross_polytope_count(r, q):
    return sum(2**j * comb(r, j) * comb(q, j)
               for j in range(min(r, q) + 1))


print("A. Sharp signed leaf capacity")
for n_leaves in range(1, 101):
    r = floor(log(2 * n_leaves + 1, 3))
    weights = [3**j for j in range(r)]
    assert sum(weights) <= n_leaves
    assert 3 ** (r + 1) > 2 * n_leaves + 1
    values = {sum(e * w for e, w in zip(word, weights))
              for word in product((-1, 0, 1), repeat=r)}
    assert len(values) == 3**r
print("  N=1,...,100 attain the information bound")

print("\nB. Dyadic rank agrees with a_30")
for d in range(1, 80):
    direct = floor(log(2 ** (d + 1) + 1, 3))
    capacity = max(r for r in range(1, d + 2)
                   if (3**r - 1) // 2 <= 2**d)
    assert direct == capacity
print("  d=1,...,79 agree")

print("\nC. Code entropy approaches the forced RR coefficient")
q = 5
target = log(2) * log(q) / (2 * log(3))
ratios = []
for t in (8, 16, 32, 64, 96):
    m = 2 * t
    n = t
    r = floor(log(2 ** (t + 1) + 1, 3))
    count = cross_polytope_count(r, q**n)
    ratio = log(count) / (m * n)
    ratios.append(ratio)
assert abs(ratios[-1] - target) < abs(ratios[0] - target)
assert abs(ratios[-1] - target) < 0.08
print(f"  final ratio={ratios[-1]:.8f}, target={target:.8f}")

print("\nD. Degree-unit form")
for m, n in ((2, 3), (10, 7), (22, 19)):
    coordinate = target * m * n
    degree_form = (m * log(2)) * (n * log(q)) / (2 * log(3))
    assert abs(coordinate - degree_form) < 1e-12
print("  coordinate and degree-normalized coefficients agree")

print("\nVERDICT: H7 OPTIMAL-RANK/RR-COEFFICIENT CHECKS PASS")
