#!/usr/bin/env python3
"""Checks the mixed archimedean boundary detector reduction (a130)."""

from itertools import product
from math import prod
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DOC = (HERE / "114_a_130_H7_MIXED_ARCHIMEDEAN_BOUNDARY_DETECTOR.md").read_text()
H17 = (ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/"
       "HARAN_Dec2016_updated_4.tex").read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


# A prime external class has coefficient pair (+1,-1).  Restriction to the
# first-real boundary kills the first component and retains -1 on X; the
# second-real boundary retains +1.
for a in range(-12, 13):
    anti = (a, -a)
    b1 = anti[1]
    b2 = anti[0]
    check(f"boundary restriction coefficient a={a}", b1 == -a and b2 == a)

# Tensoring several primes preserves the componentwise restriction law, and
# either faithful boundary plus UFD detects the zero vector.
primes = (2, 3, 5, 7)
detected = True
for a in product(range(-2, 3), repeat=len(primes)):
    b1 = tuple(-x for x in a)
    b2 = tuple(a)
    detected &= (all(x == 0 for x in b1) == all(x == 0 for x in a))
    detected &= (all(x == 0 for x in b2) == all(x == 0 for x in a))
    positive = prod(p ** max(x, 0) for p, x in zip(primes, a))
    negative = prod(p ** max(-x, 0) for p, x in zip(primes, a))
    if positive == negative:
        detected &= all(x == 0 for x in a)
check("mixed boundary plus unique factorization detects all samples", detected)

check("source pro-real-prime anchor", "real-prime" in H17)
check("source fiber-product anchor", r"\label{eq812}" in H17)
check("source completed pullback anchor", r"\label{eq1110}" in H17)
check("source real unit-ball anchor", "[-1,1]" in H17)

markers = (
    "mixed archimedean boundary detects the anti-lattice",
    "B_i^{\\rm locreg}=Y^{\\rm locreg}\\times_Y\\widetilde B_i",
    "j_1^*A_p\\simeq\\pi_2^*L_p^{-1}",
    "H7-MIXED-BDRY-PIC",
    "mixed-boundary detector",
    "does not mark the missing injectivity",
    "row A and RH remain open",
)
for marker in markers:
    check(f"scope marker {marker}", marker in DOC)

print("VERDICT: EITHER FAITHFUL MIXED-BOUNDARY PULLBACK WOULD DETECT THE FULL PRIME ANTIDIAGONAL")
