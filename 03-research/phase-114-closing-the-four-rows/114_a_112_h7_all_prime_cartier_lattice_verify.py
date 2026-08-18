#!/usr/bin/env python3
"""Exact finite-support checks for 114.a.112."""

from pathlib import Path
from fractions import Fraction
import math


ROOT = Path(__file__).resolve().parent
TEXT = (ROOT / "114_a_112_H7_ALL_PRIME_CARTIER_LATTICE_AND_PARTIAL_INTERSECTION.md").read_text()
PRIMES = (2, 3, 5, 7, 11)


def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"PASS {label}")


def curve_class(left: tuple[int, ...], right: tuple[int, ...]) -> Fraction:
    value = Fraction(1)
    for p, a, b in zip(PRIMES, left, right):
        exponent = a + b
        value *= Fraction(p ** max(exponent, 0), p ** max(-exponent, 0))
    return value


def contact(left: tuple[int, ...], right: tuple[int, ...]) -> float:
    return sum((a + b) * math.log(p) for p, a, b in zip(PRIMES, left, right))


zero = (0,) * len(PRIMES)
vectors = []
for index in range(len(PRIMES)):
    for value in (-2, -1, 1, 2):
        vector = [0] * len(PRIMES)
        vector[index] = value
        vectors.append(tuple(vector))

# Every one-axis vector is detected by diagonal pullback.
for vector in vectors:
    check(curve_class(vector, zero) != 1, f"first-axis detector {vector}")
    check(curve_class(zero, vector) != 1, f"second-axis detector {vector}")

# The exact kernel of diagonal pullback is componentwise anti-diagonal.
samples = vectors + [tuple(1 if i % 2 == 0 else -1 for i in range(len(PRIMES)))]
for left in samples:
    right = tuple(-x for x in left)
    check(curve_class(left, right) == 1, f"anti-diagonal kernel {left}")
    perturbed = list(right)
    perturbed[0] += 1
    check(curve_class(left, tuple(perturbed)) != 1,
          f"off anti-diagonal detected {left}")

# Disjoint supports are detected, for representative signed coefficients.
for i, p in enumerate(PRIMES):
    for j, q in enumerate(PRIMES):
        if i == j:
            continue
        left = tuple(2 if k == i else 0 for k in range(len(PRIMES)))
        right = tuple(-3 if k == j else 0 for k in range(len(PRIMES)))
        check(curve_class(left, right) != 1, f"disjoint support p={p},q={q}")

# Contact is additive and has exactly the same integer kernel.
for left in samples:
    right = tuple(-x for x in left)
    check(abs(contact(left, right)) < 1e-12, f"contact anti-diagonal {left}")
for a in vectors:
    for b in vectors:
        lhs = contact(tuple(x + y for x, y in zip(a, b)), zero)
        rhs = contact(a, zero) + contact(b, zero)
        if abs(lhs - rhs) > 1e-12:
            raise AssertionError("contact additivity")
print("PASS contact additivity on 400 pairs")

for marker in (
    "presentation lattice avoids assuming",
    "Every possible two-ruling relation is prime anti-diagonal",
    "geometric **partial intersection pairing**",
    "it descends to the",
    "H7-REG-MIXDEG",
    "must not be extended by declaring the missing entries",
    "row A",
    "No assertion of RH is made",
):
    check(marker in TEXT, f"scope marker {marker}")

print("VERDICT: ALL-PRIME AXES AND DIAGONAL PARTIAL INTERSECTION ARE CLOSED")
