#!/usr/bin/env python3
"""Checks for the H7-LNF versus H7-U no-go in 114.a.31."""

from math import comb, log


def check(label, condition):
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s}  {label}")
    if not condition:
        raise AssertionError(label)


print("A. Leaf capacities and stars-and-bars")
for d in range(1, 16):
    leaves = 2**d
    types = 3**d
    count = comb(leaves + types - 1, leaves)
    check(f"A({d}) enough distinct positive leaf types",
          types >= leaves)
    check(f"A({d}) stars-and-bars dominates binary lower bound",
          count >= 2 ** (leaves - 1))

print("\nB. Exponential logarithm defeats every quadratic scale")
ratios = []
for d in range(4, 31):
    lower_log = (2**d - 1) * log(2)
    ratios.append(lower_log / (2 * d * d))
check("B ratio to mn diverges on the checked range",
      all(right > left for left, right in zip(ratios[8:], ratios[9:]))
      and ratios[-1] > 10_000)

print("\nC. Exact bidegree bookkeeping")
for d in range(1, 30):
    m, n = 2 * d, d
    check(f"C({d}) divisor product is quadratic",
          m * n == 2 * d * d)

print("\n" + "=" * 72)
print("VERDICT: ALL CHECKS PASS")
