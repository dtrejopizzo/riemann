#!/usr/bin/env python3
"""Exact axis-section and diagonal-ceiling checks for 114.a.20."""

from fractions import Fraction
from math import log
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "00-references" / "papers-nuevos"
H17 = ROOT / "A" / "arXiv-1709.05831v1" / "HARAN_Dec2016_updated_4.tex"


def check(label, condition):
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s}  {label}")
    if not condition:
        raise AssertionError(label)


h17 = H17.read_text()

print("A. Source anchors")
check("A1 adelic completed bundles", "label{eq1117}" in h17)
check("A2 pro-section definition", "label{eq1113}" in h17)
check("A3 real local unit ball", "widehat{\\mathcal O}_{K,v}^{\\oplus d}" in h17)

print("\nB. Exact prime-axis sections")
for p in (2, 3, 5, 7):
    for m in range(7):
        sections = {Fraction(k, p**m) for k in range(-(p**m), p**m + 1)}
        check(f"B({p},{m}) count 2p^m+1", len(sections) == 2 * p**m + 1)
        check(f"B({p},{m}) all real-bounded", all(abs(s) <= 1 for s in sections))

print("\nC. Noncolliding two-prime grid")
p, q, m, n = 2, 3, 8, 7
grid_diagonal_values = {
    (i, j): Fraction(1, p**i * q**j)
    for i in range(m + 1) for j in range(n + 1)
}
check("C1 diagonal values separate all grid atoms",
      len(set(grid_diagonal_values.values())) == (m + 1) * (n + 1))

print("\nD. Diagonal ceiling")
for m in range(6):
    for n in range(6):
        diagonal = {
            Fraction(k, p**m * q**n)
            for k in range(-(p**m * q**n), p**m * q**n + 1)
        }
        check(f"D({m},{n}) exact diagonal count",
              len(diagonal) == 2 * p**m * q**n + 1)
        check(f"D({m},{n}) logarithmic ceiling",
              log(len(diagonal)) <= m * log(p) + n * log(q) + log(3))

print("\n" + "=" * 72)
print("VERDICT: CURVE AXIS/ABSTRACT TORSOR GRID PASS; COMPLETED BOUNDED CEILING CONDITIONAL")
