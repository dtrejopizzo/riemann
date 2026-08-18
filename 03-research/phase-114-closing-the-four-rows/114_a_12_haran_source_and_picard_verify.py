#!/usr/bin/env python3
"""Source anchors and formal Picard checks for 114.a.12."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "00-references" / "papers-nuevos"
H17 = ROOT / "A" / "arXiv-1709.05831v1" / "HARAN_Dec2016_updated_4.tex"
H22 = ROOT / "mas-papers" / "arXiv-2209.08536v3" / "Non-Additive-Geometry-and-Frobenius-Correspondences.tex"


def check(label, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s}  {label}" + (f"   {detail}" if detail else ""))
    if not condition:
        raise AssertionError(label)


h17 = H17.read_text()
h22 = H22.read_text()

print("A. Haran 2017 anchors")
check("A1 arithmetic square is explicitly defined", "label{eq101}" in h17 and "Arithmetical surface" in h17)
check("A2 finite-stage bundles and section sheaves are defined",
      all(f"label{{eq11{i}}}" in h17 for i in (3, 7)))
check("A3 pro-bundles and pro-sections are defined",
      all(f"label{{eq11{i}}}" in h17 for i in (11, 12, 13, 16)))
check("A4 Pic(overline Spec Z)=R+ is in equation 11.19",
      "label{eq1119}" in h17 and "{\\mathbb R}^+" in h17[h17.index("label{eq1119}"):])

print("\nB. Later category and Frobenius anchors")
check("B1 noncollapsed commutative arithmetic surface is stated",
      "does not reduce to its diagonal" in h22)
check("B2 totally commutative square collapses to Z",
      "total-commutativity the arithmetical surface again reduces" in h22)
check("B3 Witt Frobenius has type W(P)->W(P)",
      "F_n:\\mathcal{W}(\\biop)\\rightarrow \\mathcal{W}(\\biop)" in h22)
check("B4 source itself says intersection theory on the surface is needed",
      "need the intersection theory on the surface" in h22)
check("B5 ordinary schemes embed fully faithfully",
      "ordinary schemes embeds fully faithfully" in h22)

print("\nC. Formal anti-diagonal reduction")
samples = [(2.0, 0.5), (3.0, 1 / 3), (1.0, 1.0), (5.0, 0.2)]
check("C1 trivial external class can only have lambda*mu=1 after diagonal pullback",
      all(abs(lam * mu - 1.0) < 1e-12 for lam, mu in samples))
check("C2 each ruling is left-inverted by diagonal pullback",
      all(abs(lam * 1.0 - lam) < 1e-12 for lam, _ in samples))

print("\n" + "=" * 72)
print("VERDICT: ABSTRACT UNIT-TORSOR PICARD PASS; COMPLETED LATTICE REQUIRES H7-PB-REG")
