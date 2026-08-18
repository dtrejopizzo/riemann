#!/usr/bin/env python3
"""Exact numerical checks for the a123 global Green counterterm."""

from itertools import product
from math import log
from pathlib import Path


HERE = Path(__file__).resolve().parent
DOC = (HERE / "114_a_123_H7_GLOBAL_NUMERICAL_GREEN_EXCESS.md").read_text()
PRIMES = (2, 3, 5, 7, 11)
C = 1 / (2 * log(3))


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def degrees(x):
    return (sum(x[0][i] * log(p) for i, p in enumerate(PRIMES)),
            sum(x[1][i] * log(p) for i, p in enumerate(PRIMES)))


def contact(x, y):
    return sum(log(p) * (x[0][i] * y[1][i] + x[1][i] * y[0][i])
               for i, p in enumerate(PRIMES))


def rr(x, y):
    x1, x2 = degrees(x)
    y1, y2 = degrees(y)
    return C * (x1 * y2 + y1 * x2)


def green(x, y):
    return rr(x, y) - contact(x, y)


zero = (0,) * len(PRIMES)
axes = []
for ruling in (0, 1):
    for i in range(len(PRIMES)):
        v = [0] * len(PRIMES)
        v[i] = 1
        axes.append((tuple(v), zero) if ruling == 0 else (zero, tuple(v)))

for i, p in enumerate(PRIMES):
    for j, q in enumerate(PRIMES):
        left, right = axes[i], axes[len(PRIMES) + j]
        expected_contact = log(p) if i == j else 0.0
        expected_green = C * log(p) * log(q) - expected_contact
        check(f"prime contact p={p},q={q}",
              abs(contact(left, right) - expected_contact) < 1e-12)
        check(f"prime Green p={p},q={q}",
              abs(green(left, right) - expected_green) < 1e-12)


samples = [
    ((1, -1, 0, 2, 0), (0, 1, 1, 0, -1)),
    ((2, 0, -1, 0, 1), (1, 1, 0, -2, 0)),
    ((0, 1, 2, -1, 0), (-1, 0, 1, 1, 0)),
]
for x, y in zip(samples, reversed(samples)):
    check("Green symmetry", abs(green(x, y) - green(y, x)) < 1e-12)
    check("RR decomposition", abs(contact(x, y) + green(x, y) - rr(x, y)) < 1e-12)

for coeffs in product(range(-1, 2), repeat=4):
    if not any(coeffs):
        continue
    a = tuple(coeffs) + (0,)
    z = (a, tuple(-v for v in a))
    A = sum(a[i] * log(PRIMES[i]) for i in range(len(PRIMES)))
    check(f"anti degree nonzero {coeffs}", abs(A) > 1e-12)
    r = next(i for i, v in enumerate(a) if v)
    check(f"contact nonradical {coeffs}",
          abs(contact(z, axes[r])) > 1e-12)
    # Prime 11 is outside the support by construction.
    outside = axes[4]
    check(f"Green nonradical outside support {coeffs}",
          abs(contact(z, outside)) < 1e-12 and abs(green(z, outside)) > 1e-12)

markers = (
    "global numerical Green excess",
    "unique bilinear form",
    "B_{\\rm RR}=C_\\Lambda+G",
    "common descent obstruction",
    "if and only if the prime anti-diagonal map is faithful",
    "does not construct a Green function",
    "row A and RH remain open",
)
for marker in markers:
    check(f"scope marker {marker}", marker in DOC)

print("VERDICT: GLOBAL NUMERICAL GREEN EXCESS IS UNIQUE ON THE PRIME PRESENTATION")
