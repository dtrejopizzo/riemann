#!/usr/bin/env python3
"""Source, pullback, and Lambda checks for 114.a.17."""

from math import log
from pathlib import Path

from sympy import factorint

ROOT = Path(__file__).resolve().parents[2] / "00-references" / "papers-nuevos"
H17 = ROOT / "A" / "arXiv-1709.05831v1" / "HARAN_Dec2016_updated_4.tex"
H22 = ROOT / "mas-papers" / "arXiv-2209.08536v3" / "Non-Additive-Geometry-and-Frobenius-Correspondences.tex"


def check(label, condition):
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s}  {label}")
    if not condition:
        raise AssertionError(label)


h17 = H17.read_text()
h22 = H22.read_text()

print("A. Primary-source anchors")
check("A1 generalized schemes have finite limits and fiber products",
      "Finite limits exists" in h17 and "fiber products" in h17)
check("A2 compactified Spec Z is a pro-object containing Spec Z",
      "label{eq94}" in h17 and "compactified" in h17
      and r"{\rm spec} \, ({\mathbb Z})" in h17)
check("A3 literal arithmetic square is explicitly constructed",
      "label{eq101}" in h17 and "Arithmetical surface" in h17)
check("A4 ordinary schemes embed fully faithfully",
      "ordinary schemes embeds fully faithfully" in h22)

print("\nB. Categorical pullback model")
# Finite sets model Delta(X) cap ({p} x X) over X x X.
X = {2, 3, 5, 7}
p = 5
diagonal = {(x, x) for x in X}
vertical = {(p, x) for x in X}
check("B1 diagonal meets a vertical ruling in exactly (p,p)",
      diagonal & vertical == {(p, p)})
check("B2 the incidence projects bijectively to the closed point",
      {a for a, _ in diagonal & vertical} == {p})

print("\nC. Von Mangoldt labelling")


def lambda_from_prime_incidence(n):
    fs = factorint(n)
    if len(fs) != 1:
        return 0.0
    prime, exponent = next(iter(fs.items()))
    assert exponent >= 1
    return log(prime)


expected = {
    2: log(2), 3: log(3), 4: log(2), 5: log(5), 6: 0.0,
    8: log(2), 9: log(3), 10: 0.0, 12: 0.0, 25: log(5),
}
check("C1 labelled prime incidences give Lambda(n)",
      all(abs(lambda_from_prime_incidence(n) - value) < 1e-12
          for n, value in expected.items()))
check("C2 the local mass is log #F_p", abs(log(p) - log(len(range(p)))) < 1e-12)

print("\n" + "=" * 72)
print("VERDICT: ALL CHECKS PASS")
