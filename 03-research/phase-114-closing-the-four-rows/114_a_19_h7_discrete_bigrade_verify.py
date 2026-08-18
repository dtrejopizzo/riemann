#!/usr/bin/env python3
"""Two-prime bidegree injectivity checks for 114.a.19."""

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
check("A1 Pic(overline Spec Z)=R+", "label{eq1119}" in h17 and "{\\mathbb R}^+" in h17)
check("A2 literal arithmetic square", "label{eq101}" in h17)
check("A3 completed pro-bundles", "label{eq1116}" in h17)

print("\nB. Two-prime injectivity")
p, q = 2, 3
box = range(-12, 13)
values = {(a, b): (p ** a) * (q ** b) for a in box for b in box}
check("B1 p^a q^b values do not collide in the exponent box",
      len(set(values.values())) == len(values))
check("B2 zero degree has only exponent pair (0,0)",
      [(a, b) for (a, b), value in values.items() if value == 1] == [(0, 0)])
check("B3 logarithmic and multiplicative degree laws agree",
      all(abs((a * log(p) + b * log(q)) - log(value)) < 1e-12
          for (a, b), value in values.items()))

print("\nC. Positive rank-two sector")
positive = {(a, b): values[(a, b)] for a in range(8) for b in range(8)}
check("C1 positive two-prime bidegrees are distinct",
      len(set(positive.values())) == len(positive))
check("C2 both coordinate axes are nontrivial",
      values[(1, 0)] != 1 and values[(0, 1)] != 1)

print("\n" + "=" * 72)
print("VERDICT: UNIT-TORSOR TWO-PRIME BIGRADE PASS; COMPLETED GAUGES REQUIRE H7-PB-REG")
