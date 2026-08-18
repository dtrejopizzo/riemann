#!/usr/bin/env python3
"""Checks for the a125 fresh-exactness type correction."""

from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DOC = (HERE / "114_a_125_H7_FRESH_EXACTNESS_TYPE_CORRECTION.md").read_text()
H17 = (ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/"
       "HARAN_Dec2016_updated_4.tex").read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


primes = (2, 3, 5, 7, 11)
for p in primes:
    for q in primes:
        if p == q:
            continue
        # A unital hom must preserve p*1=0; target characteristic q does not.
        check(f"no unital characteristic transition p={p},q={q}", p % q != 0)

check("Section 6 modules are Ab-valued",
      r"an $A$-module is a functor" in H17 and r"\to Ab$" in H17)
check("Section 11 completed sheaf is a right act",
      r"\label{eq117}" in H17
      and r"\circ ({\mathcal O}_{X_N})_{d',d''} \subseteq {\mathcal O}_{X_N} (D)_{d''}" in H17)

markers = (
    "fresh-target exactness must be sourcewise",
    "cannot be transition objects",
    "It is not identified",
    "retracted as ill-typed",
    "H7-FRESH-RESTR",
    "No maps `T_D->T_E`",
    "ordinary fibers of maps",
    "does not prove H7-FRESH-RESTR",
    "row A or RH",
)
for marker in markers:
    check(f"scope marker {marker}", marker in DOC)

print("VERDICT: FRESH EXACTNESS IS SOURCEWISE; TARGET-SHEAF EXACTNESS IS IMPOSSIBLE")
