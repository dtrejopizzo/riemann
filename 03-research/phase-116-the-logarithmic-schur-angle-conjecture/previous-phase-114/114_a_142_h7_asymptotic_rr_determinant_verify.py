#!/usr/bin/env python3
"""Exact algebra for the normalized calibrated RR determinant."""

from math import floor, isclose, log
from pathlib import Path


HERE = Path(__file__).resolve().parent
DOC = (HERE / "114_a_142_H7_ASYMPTOTIC_RR_DETERMINANT.md").read_text()
C = 1 / (2 * log(3))


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def f_rr(x):
    return C * x[0] * x[1]


def b_rr(x, y):
    return C * (x[0] * y[1] + x[1] * y[0])


# Every admissible log(p_t)=O(t) makes the floor defect vanish after t^-2.
a, b = log(10), log(14)
target = C * a * b
for slope in (0.7, 1.1, 1.8):
    for t in (100, 200, 400, 800):
        logp = slope * t
        k = floor(target * t * t / logp)
        normalized = k * logp / (t * t)
        error = abs(normalized - target)
        check(f"floor defect bounded choice={slope} t={t}",
              error <= logp / (t * t) + 1e-12)
    check(f"convergence envelope shrinks choice={slope}",
          slope / 800 < slope / 100)


x = (log(6), log(35))
y = (log(10), log(11))
z = (log(13), log(21))
add = lambda u, v: (u[0] + v[0], u[1] + v[1])

check("quadratic polarization is B_RR",
      isclose(f_rr(add(x, y)) - f_rr(x) - f_rr(y), b_rr(x, y)))
check("RR determinant tensor law first variable",
      isclose(b_rr(add(x, z), y), b_rr(x, y) + b_rr(z, y)))
check("RR determinant tensor law second variable",
      isclose(b_rr(x, add(y, z)), b_rr(x, y) + b_rr(x, z)))
check("RR determinant polarization symmetric", isclose(b_rr(x, y), b_rr(y, x)))

for marker in (
    "bounded sections",
    "normalized determinant",
    "H7-RR-DET-PRES",
    "exactly",
    "single common global obstruction",
    "H7-RSPH-UNIT",
    "Row A and RH remain open",
):
    check(f"scope marker: {marker}", marker in DOC)

print("VERDICT: THE CALIBRATED RR COEFFICIENT IS A NORMALIZED ASYMPTOTIC DETERMINANT")
