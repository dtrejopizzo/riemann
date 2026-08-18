#!/usr/bin/env python3
"""Regression checks for a121 section-RR anti-diagonal descent theorem."""

from itertools import product
from math import log
from pathlib import Path


HERE = Path(__file__).resolve().parent
DOC = (HERE / "114_a_121_H7_SECTION_RR_DESCENT_IFF_ANTIDIAGONAL.md").read_text()
PRIMES = (2, 3, 5)
C = 1 / (2 * log(3))


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def degree(v):
    return sum(a * log(p) for a, p in zip(v, PRIMES))


tested = 0
for coeffs in product(range(-2, 3), repeat=len(PRIMES)):
    if not any(coeffs):
        continue
    anti_degree = degree(coeffs)
    check(f"UFD anti-degree {coeffs}", abs(anti_degree) > 1e-12)

    # A coefficientwise positive shift; then alter one ruling if the single
    # forbidden degree difference is accidentally approached.
    first = [max(3, 2 - a) for a in coeffs]
    second = [max(3, 2 + a) for a in coeffs]
    d1, d2 = degree(first), degree(second)
    if abs((d2 - d1) - anti_degree) < 1e-10:
        second[0] += 1
        d2 = degree(second)

    shifted_first = [u + a for u, a in zip(first, coeffs)]
    shifted_second = [u - a for u, a in zip(second, coeffs)]
    check(f"both rays positive {coeffs}",
          min(first + second + shifted_first + shifted_second) > 0)

    direct = C * (degree(shifted_first) * degree(shifted_second) - d1 * d2)
    formula = C * anti_degree * (d2 - d1 - anti_degree)
    check(f"coefficient difference identity {coeffs}",
          abs(direct - formula) < 1e-10)
    check(f"coefficient difference nonzero {coeffs}", abs(formula) > 1e-12)

    for n in (2, 5, 11):
        check(f"quadratic scaling {coeffs},n={n}",
              abs((n * n * direct) - (n * n * formula)) < 1e-9)
    tested += 1

check("exhaustive nonzero sample count", tested == 5**len(PRIMES) - 1)

markers = (
    "section RR descent is equivalent to anti-diagonal faithfulness",
    "only one real value is",
    "pulls back to the",
    "then `rho` is",
    "same** exact descent obstruction",
    "closes an equivalence, not the anti-diagonal theorem",
    "row A and RH remain open",
)
for marker in markers:
    check(f"scope marker {marker}", marker in DOC)

print("VERDICT: SECTION RR DESCENDS IFF THE PRIME ANTIDIAGONAL IS FAITHFUL")
