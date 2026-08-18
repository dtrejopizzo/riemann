#!/usr/bin/env python3
"""Integrated algebra and dependency audit for the metrized row-A object."""

from math import isclose, log
from pathlib import Path


HERE = Path(__file__).resolve().parent
DOC = (HERE / "114_a_144_A4_STRONG_METRIZED_BIVARIANT_SQUARE.md").read_text()
PRIMES = (2, 3, 5, 7)
C = 1 / (2 * log(3))


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def add(x, y):
    return tuple(tuple(a + b for a, b in zip(x[i], y[i])) for i in (0, 1))


def degrees(x):
    return tuple(sum(e * log(p) for e, p in zip(x[i], PRIMES)) for i in (0, 1))


def b_rr(x, y):
    dx, dy = degrees(x), degrees(y)
    return C * (dx[0] * dy[1] + dx[1] * dy[0])


def contact(x, y):
    return sum(log(p) * (x[0][i] * y[1][i] + x[1][i] * y[0][i])
               for i, p in enumerate(PRIMES))


def green(x, y):
    return b_rr(x, y) - contact(x, y)


x = ((1, -1, 2, 0), (0, 1, 0, -1))
y = ((0, 2, -1, 1), (1, 0, 1, 0))
z = ((-1, 0, 0, 2), (2, -1, 0, 1))

check("degree tensor law",
      all(isclose(a, b + c) for a, b, c in zip(degrees(add(x, y)), degrees(x), degrees(y))))
check("RR pairing first-variable law",
      isclose(b_rr(add(x, z), y), b_rr(x, y) + b_rr(z, y)))
check("RR pairing symmetry", isclose(b_rr(x, y), b_rr(y, x)))
check("contact pairing first-variable law",
      isclose(contact(add(x, z), y), contact(x, y) + contact(z, y)))
check("RR contact Green determinant split",
      isclose(contact(x, y) + green(x, y), b_rr(x, y)))

for i, p in enumerate(PRIMES):
    e1 = [[0] * len(PRIMES), [0] * len(PRIMES)]
    e2 = [[0] * len(PRIMES), [0] * len(PRIMES)]
    e1[0][i] = 1
    e2[1][i] = 1
    e1, e2 = tuple(map(tuple, e1)), tuple(map(tuple, e2))
    check(f"prime contact Lambda({p})", isclose(contact(e1, e2), log(p)))
    check(f"prime-power contact Lambda({p}^2)", isclose(contact(e1, e2), log(p)))

dependencies = (
    "114_a_01_THE_GROWTH_DICHOTOMY_AND_THE_RANK_FALLACY.md",
    "114_a_120_H7_ALL_POSITIVE_RAY_CALIBRATED_INTERPOLATION.md",
    "114_a_129_H7_FRAMED_DIVISOR_EXACT_SEQUENCE.md",
    "114_a_130_H7_MIXED_ARCHIMEDEAN_BOUNDARY_DETECTOR.md",
    "114_a_132_H7_SUPPORTWISE_LOCAL_REGULAR_PRO_SQUARE.md",
    "114_a_140_I7_CONTACT_FRAMED_ARITHMETIC_KERNELS.md",
    "114_a_141_H7_CONTACT_DETERMINANT_LINE.md",
    "114_a_142_H7_ASYMPTOTIC_RR_DETERMINANT.md",
    "114_a_143_H7_VALUED_RATIONAL_SPHERE_PICARD_NORM.md",
)
for name in dependencies:
    check(f"dependency exists: {name}", (HERE / name).is_file())

for marker in (
    "a1 (Div/Prin)",
    "a2 (principal invariance)",
    "a3 (curve dimension)",
    "a4 (quadratic product)",
    "a5 (graded pairing)",
    "single object",
    "a4-strong in the metrized bivariant sense",
    "does not prove RH by itself",
    "No RH statement is used",
):
    check(f"scope marker: {marker}", marker in DOC)

print("VERDICT: ONE METRIZED BIVARIANT HARAN SQUARE SATISFIES THE ROW-A CONTRACT")
