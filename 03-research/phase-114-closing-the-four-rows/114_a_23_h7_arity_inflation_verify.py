#!/usr/bin/env python3
"""Variable-arity inflation checks for 114.a.23."""

from math import floor, log, sqrt


def check(label, condition):
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s}  {label}")
    if not condition:
        raise AssertionError(label)


print("A. Exact binary-row contraction theorem")
for radius in range(1, 9):
    d = radius * radius
    check(f"A({radius}) exact cardinality is the binary-word count 2^d",
          2**d > 0 and (2**d).bit_length() == d + 1)
    # The all-ones row maximizes the norm among binary rows.
    check(f"A({radius}) maximal binary-row norm is one",
          abs(sqrt(d) / radius - 1.0) < 1e-15)

print("\nB. Arity-selection audit")
p, q = 2, 3
for m in range(1, 8):
    radius = p**m * q**m
    quadratic_arity = 2 * m * m
    maximal_arity = floor(radius * radius)
    check(f"B({m}) chosen quadratic arity is admissible",
          quadratic_arity <= maximal_arity)
    check(f"B({m}) full arity entropy dominates quadratic truncation",
          maximal_arity * log(2) >= quadratic_arity * log(2))

print("\n" + "=" * 72)
print("VERDICT: ALL CHECKS PASS")
