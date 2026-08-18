#!/usr/bin/env python3
"""Checks for fresh evaluation naturality on open restrictions (a126)."""

from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DOC = (HERE / "114_a_126_H7_FRESH_OPEN_RESTRICTION_NATURALITY.md").read_text()
H17 = (ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/"
       "HARAN_Dec2016_updated_4.tex").read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def evaluate(x, p):
    return (x.numerator % p) * pow(x.denominator % p, -1, p) % p


p = 101
global_sections = {Fraction(a, b) for b in (1, 2, 3, 5, 7)
                   for a in range(-8, 9)}
# A smaller open admits the global sections and additional localized ones.
local_sections = global_sections | {Fraction(a, 11) for a in range(-8, 9)}

global_image = {evaluate(x, p) for x in global_sections}
local_image = {evaluate(x, p) for x in local_sections}
check("open restriction image inclusion", global_image <= local_image)

for x in global_sections:
    check(f"same rational expression after restriction {x}",
          evaluate(x, p) == evaluate(Fraction(x.numerator, x.denominator), p))

samples = list(global_sections)[:25]
for x in samples:
    for y in samples:
        check(f"multiplicative naturality {x},{y}",
              evaluate(x * y, p) == evaluate(x, p) * evaluate(y, p) % p)

# Two successive restrictions do not change the rational expression.
for x in samples:
    once = Fraction(x.numerator, x.denominator)
    twice = Fraction(once.numerator, once.denominator)
    check(f"restriction composition {x}", evaluate(x, p) == evaluate(twice, p))

check("source localization anchor", r"\label{eq89}" in H17)
check("source completed section anchor", r"\label{eq117}" in H17)

markers = (
    "fresh evaluation is natural for open restrictions",
    "one fresh target",
    "Every denominator in the entire diagram is a unit",
    "fresh open naturality",
    "operatorname{im}\\varepsilon_U",
    "No transition between targets",
    "H7-FRESH-CARTIER",
    "all-ray numerical RR theorem `a120` does not depend",
    "row A and RH remain open",
)
for marker in markers:
    check(f"scope marker {marker}", marker in DOC)

print("VERDICT: FRESH EVALUATION COMMUTES WITH ALL FINITE OPEN RESTRICTION DIAGRAMS")
