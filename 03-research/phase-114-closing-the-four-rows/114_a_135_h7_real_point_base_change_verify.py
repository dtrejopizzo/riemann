#!/usr/bin/env python3
"""Type/source audit of the real reduced point and mixed base change."""

from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = (ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/"
          "HARAN_Dec2016_updated_4.tex").read_text()
DOC = (HERE / "114_a_135_H7_REAL_POINT_AND_MIXED_BASE_CHANGE.md").read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


check("Haran defines the real sphere residue",
      "surjective homomorphisms" in SOURCE
      and r"{\mathbb Z}_{\mathbb R} \twoheadrightarrow {\mathbb F}_{\mathbb R}" in SOURCE)
check("Haran defines the level real chart and maximal ideal",
      r"\label{eq94}" in SOURCE and r"the maximal ideal $\eta_N$ of $A_N" in SOURCE)
check("Haran identifies the limit real local object",
      r"\label{eq97}" in SOURCE
      and r"{\mathbb Z}_{(\eta)} = {\mathbb Q} \cap {\mathbb Z}_{\mathbb R}" in SOURCE)
check("Haran supplies affine fiber products by tensor products",
      r"\label{eq812}" in SOURCE and "fiber product" in SOURCE)
check("Haran warns residue coefficient maps need not be injective",
      "they are not!" in SOURCE and r"{\mathbb F}_{\mathbb R}" in SOURCE)

v = (Fraction(3, 5), Fraction(4, 5))
check("3/5,4/5 is a rational unit vector", sum(x * x for x in v) == 1)
check("3/5,4/5 is not a signed coordinate vector",
      sum(x != 0 for x in v) == 2)

for marker in (
    "rational sphere object",
    "H7-RSPH-CONS",
    "no faithfully-flat descent theorem",
    "does not prove its",
    "row A and RH remain open",
):
    check(f"scope marker: {marker}", marker in DOC)

print("VERDICT: THE MIXED EDGE IS RATIONAL-SPHERICAL BASE CHANGE; CONSERVATIVITY IS OPEN")
