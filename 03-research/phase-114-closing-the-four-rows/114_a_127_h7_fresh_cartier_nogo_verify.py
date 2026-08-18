#!/usr/bin/env python3
"""Checks the common-target obstruction for fresh Cartier restriction (a127)."""

from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent
DOC = (HERE / "114_a_127_H7_FRESH_CARTIER_COMMON_TARGET_NOGO.md").read_text()
A57 = (HERE / "114_a_57_H7_GLOBAL_DENOMINATOR_COFINALITY_NOGO.md").read_text()
A67 = (HERE / "114_a_67_H7_TYPED_PRINCIPAL_CARTIER_ACT_AND_DIAGONAL_SHADOW.md").read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


# In Z/nZ, ell is invertible exactly when gcd(ell,n)=1, while ell is zero
# exactly when n divides ell.  For n>1 these conditions never coexist.
for n in range(2, 301):
    for ell in (2, 3, 5, 7, 11, 13, 17, 19):
        invertible = gcd(ell, n) == 1
        killed = ell % n == 0
        check(f"unit-zero exclusion n={n}, ell={ell}",
              not (invertible and killed))

# A fresh prime q != ell makes ell invertible, hence cannot be an ell-residue
# target.  The same-prime field kills ell, hence cannot evaluate 1/ell.
for ell in (2, 3, 5, 7, 11, 13, 17, 19):
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23):
        if q != ell:
            check(f"fresh target inverts ell={ell} mod q={q}",
                  pow(ell, -1, q) * ell % q == 1)
            check(f"fresh target does not kill ell={ell} mod q={q}",
                  ell % q != 0)
        else:
            check(f"residue target kills ell={ell}", ell % q == 0)

check("a57 localization anchor", "There is no unital ring map" in A57)
check("a67 quotient universal-property anchor",
      "for which `s` maps to zero" in A67)

markers = (
    "fresh generic target cannot also be a Cartier residue target",
    "unit-zero obstruction",
    "characteristic-free",
    "common-target Cartier no-go",
    "does **not** say that Haran's source closed quotient is absent",
    "H7-TWO-TARGET-DELIGNE",
    "closed **negatively as a common-target strategy**",
    "row A and RH remain open",
)
for marker in markers:
    check(f"scope marker {marker}", marker in DOC)

print("VERDICT: A GENERIC LOCALIZATION AND ITS SAME-DIVISOR RESIDUE CANNOT SHARE A NONZERO UNITAL TARGET")
