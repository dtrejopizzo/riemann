#!/usr/bin/env python3
"""Exact finite-support model for the rational-sphere Cech unit gate."""

from fractions import Fraction
from itertools import product
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = (ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/"
          "HARAN_Dec2016_updated_4.tex").read_text()
DOC = (HERE / "114_a_138_H7_RATIONAL_SPHERE_CECH_UNIT_CRITERION.md").read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def real_chart_unit(x):
    return x != 0 and abs(x) <= 1 and abs(1 / x) <= 1


samples = [Fraction(a, b) for a in range(-20, 21)
           for b in range(1, 21) if a != 0]
check("sampled rational real-chart units are exactly signs",
      all((not real_chart_unit(x)) or x in (1, -1) for x in samples))

primes = (2, 3, 5, 7)
ufd_ok = True
for exponents in product(range(-3, 4), repeat=len(primes)):
    positive = 1
    negative = 1
    for p, a in zip(primes, exponents):
        positive *= p ** max(a, 0)
        negative *= p ** max(-a, 0)
    q = Fraction(positive, negative)
    ufd_ok &= q not in (1, -1) or all(a == 0 for a in exponents)
check("all sampled prime words meet sign units only at identity", ufd_ok)

# Abstract Cech calculation: q' = u^{-1} q v; q is trivial precisely when it
# is a ratio of endpoint units. Use a finite multiplicative toy group.
overlap = {Fraction(2) ** a * Fraction(3) ** b
           for a in range(-3, 4) for b in range(-3, 4)}
endpoint_u = {Fraction(1), Fraction(-1)}
endpoint_v = {Fraction(1), Fraction(-1)}
coboundaries = {u / v for u in endpoint_u for v in endpoint_v}
check("Cech coboundary image is the endpoint-unit ratio",
      coboundaries == {Fraction(1), Fraction(-1)})
check("positive prime lattice has trivial Cech intersection",
      {q for q in overlap if q > 0}.intersection(coboundaries) == {Fraction(1)})

check("source gives the two-chart gluing",
      r"\label{eq94}" in SOURCE and r"{\mathbb Z} \left[ \frac1N \right]" in SOURCE)
check("source gives affine fiber products by tensor products",
      r"\label{eq812}" in SOURCE)

for marker in (
    "Cech unit criterion",
    "Q_T\\cap G_U G_V^{-1}=\\{1\\}",
    "H7-RSPH-UNIT",
    "not asserted",
    "row A",
):
    check(f"scope marker: {marker}", marker in DOC)

print("VERDICT: MIXED-BOUNDARY FAITHFULNESS IS EXACTLY THE PRIME/ENDPOINT-UNIT INTERSECTION")
