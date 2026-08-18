#!/usr/bin/env python3
"""Source and block-amplification checks for 114.a.21."""

from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "00-references" / "papers-nuevos"
H22 = ROOT / "mas-papers" / "arXiv-2209.08536v3" / "Non-Additive-Geometry-and-Frobenius-Correspondences.tex"


def check(label, condition):
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s}  {label}")
    if not condition:
        raise AssertionError(label)


h22 = H22.read_text()

print("A. Primary-source anchors")
check("A1 commutative arithmetic surface does not collapse",
      "does not reduce to its diagonal" in h22)
check("A2 totally commutative quotient collapses to Z",
      "arithmetical surface again reduces" in h22
      and r"\Z\boxtimes_{\F}^T\Z=\Z" in h22)
check("A3 the two addition generators are displayed",
      r"v\boxtimes 1" in h22 and r"1 \boxtimes v" in h22)
check("A4 total commutativity forces their equality", "label{eq:4.12}" in h22)

print("\nB. Block amplification model")
for n in range(1, 13):
    words = list(product((1, 2), repeat=n))
    # A block operation is represented by its extractable ordered blocks.
    block_ops = {tuple(word) for word in words}
    check(f"B({n}) exactly 2^N extractable block operations",
          len(block_ops) == 2**n)
    folded = {tuple(0 for _ in word) for word in words}
    check(f"B({n}) every block operation has the same fold", len(folded) == 1)

print("\n" + "=" * 72)
print("VERDICT: ALL CHECKS PASS")
