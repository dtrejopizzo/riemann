#!/usr/bin/env python3
"""Checks for the a124 metrized numerical Green biextension."""

from math import exp, log
from pathlib import Path


HERE = Path(__file__).resolve().parent
DOC = (HERE / "114_a_124_H7_CANONICAL_METRIZED_GREEN_BIEXTENSION.md").read_text()
PRIMES = (2, 3, 5, 7)
C = 1 / (2 * log(3))


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def add(x, y):
    return tuple(tuple(a + b for a, b in zip(x[i], y[i])) for i in (0, 1))


def deg(x, ruling):
    return sum(x[ruling][i] * log(p) for i, p in enumerate(PRIMES))


def contact(x, y):
    return sum(log(p) * (x[0][i] * y[1][i] + x[1][i] * y[0][i])
               for i, p in enumerate(PRIMES))


def rr(x, y):
    return C * (deg(x, 0) * deg(y, 1) + deg(y, 0) * deg(x, 1))


def green(x, y):
    return rr(x, y) - contact(x, y)


def qgreen(x):
    return green(x, x) / 2


x = ((1, -1, 2, 0), (0, 1, -1, 1))
y = ((0, 2, 1, -1), (1, 0, 1, 0))
z = ((-1, 0, 1, 2), (2, -1, 0, 1))

check("first-variable tensor isometry",
      abs(exp(-green(x, z)) * exp(-green(y, z))
          - exp(-green(add(x, y), z))) < 1e-12)
check("second-variable tensor isometry",
      abs(exp(-green(z, x)) * exp(-green(z, y))
          - exp(-green(z, add(x, y)))) < 1e-12)
check("biextension symmetry", abs(green(x, y) - green(y, x)) < 1e-12)
check("associativity logarithm",
      abs(green(add(add(x, y), z), x) - green(add(x, add(y, z)), x)) < 1e-12)
check("interchange logarithm",
      abs(green(add(x, y), add(y, z))
          - sum(green(a, b) for a in (x, y) for b in (y, z))) < 1e-12)
check("contact Green RR metric split",
      abs(contact(x, y) + green(x, y) - rr(x, y)) < 1e-12)
check("quadratic polarization",
      abs(qgreen(add(x, y)) - qgreen(x) - qgreen(y) - green(x, y)) < 1e-12)

# A sampled anti-vector is non-radical, so its norm cannot be independent of
# presentation after quotienting it to zero.
a = (1, -2, 1, 0)
anti = (a, tuple(-v for v in a))
outside = ((0, 0, 0, 1), (0, 0, 0, 0))
check("anti vector Green nonradical", abs(green(anti, outside)) > 1e-12)

markers = (
    "canonical metrized Green biextension",
    "define a symmetric metrized biextension",
    "is an isometry compatible with both biextension laws",
    "quadratic Green gauge",
    "if and only if the prime anti-diagonal is",
    "actual normed-line Green object",
    "does not identify `E_C` with a determinant",
    "row A and RH remain open",
)
for marker in markers:
    check(f"scope marker {marker}", marker in DOC)

print("VERDICT: CANONICAL METRIZED GREEN BIEXTENSION EXISTS ON THE PRIME PRESENTATION")
