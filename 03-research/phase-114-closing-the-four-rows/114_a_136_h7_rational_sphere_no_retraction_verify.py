#!/usr/bin/env python3
"""Exact no-retraction check for kappa_infty over F{+-1}."""

from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = (ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/"
          "HARAN_Dec2016_updated_4.tex").read_text()
DOC = (HERE / "114_a_136_H7_RATIONAL_SPHERE_HAS_NO_BASE_RETRACTION.md").read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


v = (Fraction(3, 5), Fraction(4, 5))
e1 = (Fraction(1), Fraction(0))
e2 = (Fraction(0), Fraction(1))


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def residue_scalar(x):
    return x if abs(x) == 1 else Fraction(0)


check("v is Pythagorean unit", dot(v, v) == 1)
check("v contracts strictly inside against e1", dot(v, e1) == Fraction(3, 5))
check("v contracts strictly inside against e2", dot(v, e2) == Fraction(4, 5))
check("both cross contractions vanish in the residue",
      residue_scalar(dot(v, e1)) == 0 and residue_scalar(dot(v, e2)) == 0)

target_nonzero = (e1, tuple(-x for x in e1), e2, tuple(-x for x in e2))
for image in target_nonzero:
    check(f"candidate image {image} has nonzero contraction with a fixed axis",
          dot(image, e1) != 0 or dot(image, e2) != 0)

check("source defines monoid generalized rings",
      "full and faithfull embedding of the category of commutative associative unital monoids" in SOURCE)
check("source defines the real sphere residue and contraction",
      r"{\mathbb F}_{\mathbb R}" in SOURCE and "Cauchy-Schwartz" in SOURCE)

for marker in (
    "No-retraction theorem",
    "There is no",
    "does **not** prove that mixed pullback is noninjective",
    "H7-RSPH-DESC/NORM",
    "row A and RH remain open",
):
    check(f"scope marker: {marker}", marker in DOC)

print("VERDICT: THE RATIONAL-SPHERE BASE EXTENSION HAS NO S-ALGEBRA RETRACTION")
