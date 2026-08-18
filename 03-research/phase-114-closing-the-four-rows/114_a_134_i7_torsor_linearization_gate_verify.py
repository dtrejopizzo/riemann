#!/usr/bin/env python3
"""Source/type audit for the conditional torsor-linearization route."""

from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/HARAN_Dec2016_updated_4.tex"
DOC = HERE / "114_a_134_I7_TORSOR_LINEARIZATION_GATE.md"

source = SOURCE.read_text()
doc = DOC.read_text()
section6 = source[source.index(r"\section{Modules and differentials}"):
                  source.index(r"\section{${\mathbb N}$ and ${\mathbb Z}$ as generalized rings}")]


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


check("Section 6 defines modules as Ab-valued functors",
      r"\to Ab" in section6 and "an $A$-module is a functor" in section6)
check("Section 6 states the abelian-category properties",
      "complete and co-complete abelian category" in section6
      and "enough projective and injectives" in section6)
check("Section 6 contains scalar extension and the cotangent complex",
      r"\label{eq63}" in section6 and r"\label{eq66}" in section6
      and "Quillen cotangent complex" in section6)
check("the cited section does not define the A^[1] shorthand",
      "A^[1]" not in section6 and "A^{[1]}" not in section6)

for gate in (
    "Aut_A(P_A)=GL_1(A)",
    "effective descent",
    "symmetric monoidal structure",
    "full faithfulness",
    "derived diagonal contact",
):
    check(f"document records gate: {gate}", gate in doc)

check("scope remains conditional",
      "conditional route" in doc and "I7 and row A remain open" in doc
      and "does not" in doc)

print("VERDICT: SECTION 6 ENABLES HOMOLOGICAL ALGEBRA BUT DOES NOT SUPPLY TORSOR LINEARIZATION")
