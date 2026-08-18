#!/usr/bin/env python3
"""Checks for the real-boundary cross-contraction in 114.a.28."""

from fractions import Fraction
from itertools import product
from math import comb, log


def check(label, condition):
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s}  {label}")
    if not condition:
        raise AssertionError(label)


print("A. Exact first-ruling Euclidean bound")
norm_checks = []
for p in (3, 5, 7, 11):
    for m in range(1, 15):
        norm_square = sum(Fraction(p ** (2 * j), p ** (2 * m))
                          for j in range(m))
        closed_form = Fraction(p ** (2 * m) - 1,
                               p ** (2 * m) * (p * p - 1))
        norm_checks.append(norm_square == closed_form and norm_square < 1)
check("A all geometric norms satisfy the exact strict bound",
      all(norm_checks))

print("\nB. Cross-polytope real bound and exact count")
polytope_checks = []
for rank in range(1, 6):
    for radius in range(1, 7):
        points = [vector for vector in
                  product(range(-radius, radius + 1), repeat=rank)
                  if sum(abs(value) for value in vector) <= radius]
        formula = sum(2**j * comb(rank, j) * comb(radius, j)
                      for j in range(min(rank, radius) + 1))
        l2_bound = all(sum(value * value for value in vector)
                       <= radius * radius for vector in points)
        polytope_checks.append(len(points) == formula and l2_bound)
check("B all finite polytopes satisfy count and l2<=l1",
      all(polytope_checks))

print("\nC. Finite trivialization and quadratic entropy")
finite_checks = []
for p in (3, 5):
    for m in range(1, 9):
        P = p**m
        trivialized = [Fraction(p**j, P) * P for j in range(m)]
        finite_checks.append(
            all(value.denominator == 1 for value in trivialized))
check("C all first vectors trivialize integrally", all(finite_checks))

q = 2
ratios = []
for t in range(20, 81, 10):
    Q = q**t
    count = sum(2**j * comb(t, j) * comb(Q, j)
                for j in range(t + 1))
    ratios.append(log(count) / (t * t * log(q)))
check("C quadratic entropy approaches leading constant one",
      0.94 < ratios[-1] < 1
      and ratios[-1] > ratios[0])

print("\n" + "=" * 72)
print("VERDICT: ALL CHECKS PASS")
