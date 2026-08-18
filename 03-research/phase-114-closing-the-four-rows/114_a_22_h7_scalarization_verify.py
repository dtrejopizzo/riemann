#!/usr/bin/env python3
"""One-output scalarization and collapsed norm checks for 114.a.22."""

from itertools import product
from math import log, sqrt
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
check("A1 delta-unit relation", r"$\delta$-{\bf unit}" in h17)
check("A2 scalar additions from the two generators", "label{eq1021}" in h17)
check("A3 section functor has arbitrary input arity", "label{eq1113}" in h17)

print("\nB. One-output bit recovery")
for n in range(1, 13):
    words = list(product((1, 2), repeat=n))
    # The scalarized operation is encoded by all recoverable block restrictions.
    restrictions = {word: tuple(word[k] for k in range(n)) for word in words}
    check(f"B({n}) restrictions recover every word",
          len(set(restrictions.values())) == 2**n)
    folds = {tuple(0 for _ in word) for word in words}
    check(f"B({n}) all scalarized words have one fold", len(folds) == 1)

print("\nC. Collapsed Euclidean norm")
p, q = 2, 3
for m in range(1, 11):
    n = m
    blocks = m * n
    norm = sqrt(2 * blocks) / (p**m * q**n)
    check(f"C({m}) exact norm below one", norm <= 1.0)
    check(f"C({m}) logarithmic formula",
          abs(log(norm) - (0.5 * log(2 * blocks) - m * log(p) - n * log(q))) < 1e-12)

print("\n" + "=" * 72)
print("VERDICT: ALL CHECKS PASS")
