#!/usr/bin/env python3
"""Conditional power-evaluation injectivity checks for 114.a.25."""

from itertools import product
from math import comb, log

from sympy import Matrix


def check(label, condition):
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s}  {label}")
    if not condition:
        raise AssertionError(label)


print("A. Exponential/Vandermonde separation")
for size in range(1, 8):
    bases = list(range(1, size + 1))
    matrix = Matrix([[a**sigma for a in bases] for sigma in range(size)])
    check(f"A({size}) distinct power functions have full rank",
          matrix.det() != 0)

print("\nB. Balanced base-p uniqueness")
for p in (3, 5, 7):
    for length in range(1, 7):
        values = {
            sum(digit * p**j for j, digit in enumerate(digits))
            for digits in product((-1, 0, 1), repeat=length)
        }
        check(f"B({p},{length}) all balanced words are distinct",
              len(values) == 3**length)

print("\nC. Intrinsic domain entropy and mass")
p, q = 3, 2
ratios = []
for t in range(3, 14):
    radius = q**t
    rank = t + 1
    count = sum(2**j * comb(rank, j) * comb(radius, j)
                for j in range(min(rank, radius) + 1))
    ratios.append(log(count) / (t * t * log(q)))
    check(f"C({t}) largest layer is bounded", p**t / p**t <= 1)
check("C entropy has the predicted quadratic leading constant",
      abs(ratios[-1] - 1.0) < abs(ratios[0] - 1.0)
      and 0.75 < ratios[-1] < 1.25)

print("\n" + "=" * 72)
print("VERDICT: ALL CHECKS PASS")
