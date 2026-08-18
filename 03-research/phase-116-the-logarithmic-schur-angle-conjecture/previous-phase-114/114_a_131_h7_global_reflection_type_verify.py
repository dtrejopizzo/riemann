#!/usr/bin/env python3
"""Checks that global Reg_Z is ill-typed on Haran's real charts (a131)."""

from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DOC = (HERE / "114_a_131_H7_GLOBAL_Z_REFLECTION_IS_ILL_TYPED_AT_INFINITY.md").read_text()
A110 = (HERE / "114_a_110_H7_REGULAR_REFLECTION_ON_THE_PRO_SQUARE.md").read_text()
H17 = (ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/"
       "HARAN_Dec2016_updated_4.tex").read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def in_real_chart(x):
    return abs(x) <= 1


for n in range(2, 101):
    check(f"integer {n} absent from real scalar ball", not in_real_chart(n))
    check(f"inverse 1/{n} present in real scalar ball",
          in_real_chart(Fraction(1, n)))
check("signed base scalars present", all(in_real_chart(x) for x in (-1, 0, 1)))

check("a110 domain says two integer rulings",
      "carrying two signed integer" in A110 and
      "rulings, define `Reg_Z(A)=" in A110)
check("a110 applies reflection to every chart",
      "Replace each chart by `Spec Reg_Z(A_alpha)`" in A110)
check("source A_N real chart anchor",
      "A_N = {\\mathbb Z} \\left[ \\frac1N \\right] \\cap {\\mathbb Z}_{\\mathbb R}" in H17)
check("source real interval anchor", "[-1,1]" in H17)
check("source global signs anchor",
      "{\\mathbb F} \\, \\{ \\pm 1 \\}" in H17)

markers = (
    "global Z-reflection is ill-typed on the real charts",
    "does not contain the scalar 2",
    "typing obstruction",
    "does not, as written",
    "H7-LOCAL-REG-GLUE",
    "Results `a110`--`a130`",
    "global space carrying it is not yet built",
    "Row A and RH remain open",
)
for marker in markers:
    check(f"scope marker {marker}", marker in DOC)

print("VERDICT: THE GLOBAL CHARTWISE Reg_Z CONSTRUCTION IS UNDEFINED ON THE ARCHIMEDEAN CHARTS")
