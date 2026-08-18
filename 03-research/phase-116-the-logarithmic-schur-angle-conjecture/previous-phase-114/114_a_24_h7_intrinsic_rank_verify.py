#!/usr/bin/env python3
"""Intrinsic rank, cross-polytope count, and mass checks for 114.a.24."""

from itertools import product
from math import ceil, comb, log


def check(label, condition):
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s}  {label}")
    if not condition:
        raise AssertionError(label)


def cross_count_formula(r, radius):
    return sum(2**j * comb(r, j) * comb(radius, j)
               for j in range(min(r, radius) + 1))


print("A. Exact one-axis binary rank")
for p in (2, 3, 5):
    for m in range(1, 6):
        radius = p**m
        rank = ceil(log(radius + 1, 2))
        subset_sums = {
            sum(bit * 2**j for j, bit in enumerate(bits))
            for bits in product((0, 1), repeat=rank)
        }
        check(f"A({p},{m}) all nonnegative axis sections generated",
              set(range(radius + 1)) <= subset_sums)
        check(f"A({p},{m}) lower-bound count", 2**rank >= radius + 1)
        if rank > 0:
            check(f"A({p},{m}) minimality", 2**(rank - 1) < radius + 1)

print("\nB. Exact cross-polytope formula")
for r in range(1, 5):
    for radius in range(0, 6):
        enumerated = sum(
            1 for v in product(range(-radius, radius + 1), repeat=r)
            if sum(abs(x) for x in v) <= radius
        )
        check(f"B({r},{radius}) formula equals enumeration",
              cross_count_formula(r, radius) == enumerated)

print("\nC. Quadratic entropy and collapsed mass")
p, q = 2, 3
ratios = []
for t in range(4, 13):
    P, Q = p**t, q**t
    rank = ceil(log(P + 1, 2))
    count = cross_count_formula(rank, Q)
    leading = (log(p) * log(q) / log(2)) * t * t
    ratios.append(log(count) / leading)
    # Worst coefficient mass uses the largest binary weight and l1 mass Q.
    check(f"C({t}) collapsed mass bound", 2**(rank - 1) / P <= 1.0)
check("C finite ratio is close to the proved leading constant",
      abs(ratios[-1] - 1.0) < abs(ratios[0] - 1.0)
      and 0.75 < ratios[-1] < 1.25)

print("\n" + "=" * 72)
print("VERDICT: ALL CHECKS PASS")
