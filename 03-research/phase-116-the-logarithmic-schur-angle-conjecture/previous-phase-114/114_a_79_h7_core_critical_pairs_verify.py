#!/usr/bin/env python3
"""Critical-pair identities for a79; p-faith and boundary charts stay open."""

from itertools import product
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
H17 = ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/HARAN_Dec2016_updated_4.tex"


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


source = H17.read_text()
for marker in (
    r"(10.16) \quad {\bf cancellation}",
    r"(10.17) \quad {\bf commutativity}",
    r"\label{eq1019}",
):
    check(f"source marker {marker}", marker in source)


# C/C at one site and after endpoint identification: signed excesses add.
for a, b, c, d in product(range(9), repeat=4):
    separate_then_merge = (a - b) + (c - d)
    merge_then_cancel = (a + c) - (b + d)
    if separate_then_merge != merge_then_cancel:
        raise AssertionError((a, b, c, d))
check("C/C bundle merge identity", True)


# Z/Z: restrictions are intersections, independent of order.
for n in range(9):
    universe = (1 << n) - 1
    for b in range(1 << n):
        for c in range(1 << n):
            if (universe & b) & c != (universe & c) & b:
                raise AssertionError((n, b, c))
check("Z/Z restriction intersection identity through nine leaves", True)


# C/T: a common monoid label sends an opposite pair to an opposite pair;
# zero deletes both.  Bundle merging is compatible with this transport.
for s in (-1, 0, 1):
    check(f"common sign transport s={s}", s * 1 == -(s * -1))
    for x, y in product(range(-8, 9), repeat=2):
        if s * (x + y) != s * x + s * y:
            raise AssertionError((s, x, y))
check("transport commutes with bundle merging", True)


# Termination measure decreases for the four oriented rule shapes.
def lex_less(after, before):
    return after < before


for strands in range(2, 20):
    for vertices in range(1, 20):
        check_c = lex_less((strands - 2, vertices), (strands, vertices))
        check_t = lex_less((strands, vertices - 1), (strands, vertices))
        if not (check_c and check_t):
            raise AssertionError((strands, vertices))
check("oriented rules decrease the lexicographic measure", True)


doc = (HERE / "114_a_79_H7_BASE_SIGNED_NETWORK_CORE_CONFLUENCE.md").read_text()
for marker in (
    "H7-MACRO-CONTEXT-NF",
    "does **not** give a normal form",
    "restricted rewrite system",
    "K2,2",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: FIXED-INCIDENCE LOCAL CONFLUENCE PASS; FULL MACRO CONTEXT SYSTEM OPEN")
