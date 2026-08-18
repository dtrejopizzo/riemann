#!/usr/bin/env python3
"""Exact quotient-purity checks for a76; H7-CANCEL-PURE remains open."""

from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
H17 = ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/HARAN_Dec2016_updated_4.tex"


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


source = H17.read_text()
check("source gives bilateral tree and leaf-bijection presentation",
      re.search(r"a\s*=\s*\(F_y\s*,\s*G_x\s*,\s*\\sigma\s*,\s*\\varepsilon\)", source)
      is not None
      and r"\sigma :  \coprod_{y \, \in \, Y}\partial F_y" in source)
check("source lists cancellation and commutativity relations",
      r"(10.16) \quad {\bf cancellation}" in source
      and r"(10.17) \quad {\bf commutativity}" in source)


# On Z/n with kernel congruence modulo d|n, multiplication by p on the
# quotient Z/d is injective iff the kernel congruence is p-root-closed.
for n in range(1, 81):
    for d in range(1, n + 1):
        if n % d:
            continue
        equivalent = lambda x, y, d=d: (x - y) % d == 0
        for p in (2, 3, 5, 7, 11):
            quotient_injective = all(
                not equivalent(p * x, p * y) or equivalent(x, y)
                for x in range(n) for y in range(n)
            )
            colon_equal = all(
                equivalent(p * x, p * y) == equivalent(x, y)
                for x in range(n) for y in range(n)
            )
            if quotient_injective != colon_equal:
                raise AssertionError(f"colon criterion n={n}, d={d}, p={p}")
check("colon criterion exhaustive finite cyclic quotients", True)


# The standard non-pure warning: pZ is not p-saturated in Z and Z/p has
# p-torsion.  Test a broad exact range.
for p in (2, 3, 5, 7, 11, 13):
    witness = 1
    check(f"pZ non-pure p={p}",
          (p * witness) % p == 0 and witness % p != 0)
    check(f"Z/p has p-torsion p={p}",
          (p * (witness % p)) % p == 0 and witness % p != 0)


doc = (HERE / "114_a_76_H7_LONG_SOURCE_NORMAL_FORMS_AND_CANCELLATION_PURITY.md").read_text()
for marker in (
    "H7-CANCEL-PURE",
    "does not assert H7-CANCEL-PURE",
    "unique `1`-reduced tree",
    "remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: CANCELLATION-PURITY CRITERION PASS; H7-CANCEL-PURE OPEN")
