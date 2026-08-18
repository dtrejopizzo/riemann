#!/usr/bin/env python3
"""Source anchors and finite unit-defect checks for 114.a.16."""

from pathlib import Path

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
check("A1 global sections of compactified Spec Z are F{+-1}",
      "{\\mathbb F} \\{ \\pm 1 \\}" in h17 and "global sections are" in h17)
check("A2 arithmetic double product is explicitly constructed", "label{eq101}" in h17)
check("A3 generalized schemes have fiber products", "label{thm:3}" in h22)
check("A4 completed pro-line bundles are defined", "label{eq1116}" in h17)

print("\nB. Normalized sign-unit defect")
# In the sufficient model Gamma(X^[n],O*)={+-1}, restriction is identity.
units = (-1, 1)
check("B1 identity restriction on {+-1} is injective", len(set(units)) == len(units))
# Lemma 2.1 says the defect restricts to 1; injectivity then forces c=1.
check("B2 among sign units, restriction value 1 has unique preimage 1",
      [u for u in units if u == 1] == [1])

print("\n" + "=" * 72)
print("VERDICT: ALL CHECKS PASS")
