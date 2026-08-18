#!/usr/bin/env python3
"""Checks the finite cancellation and archimedean nonunit defect (a128)."""

from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DOC = (HERE / "114_a_128_H7_ANTIDIAGONAL_IS_PRINCIPAL.md").read_text()
H17 = (ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/"
       "HARAN_Dec2016_updated_4.tex").read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


h = (-1, 1)
finite_data = {
    ("p", "p"): ((-1, 1), (0, 0)),
    ("p", "away"): ((-1, 0), (0, -1)),
    ("away", "p"): ((0, 1), (1, 0)),
    ("away", "away"): ((0, 0), (1, -1)),
}
for chart, (f, expected) in finite_data.items():
    quotient = (f[0] - h[0], f[1] - h[1])
    check(f"finite exponent cancellation {chart}", quotient == expected)


def real_integral(x):
    return abs(x) <= 1


def real_unit(x):
    return x != 0 and real_integral(x) and real_integral(1 / x)


for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
    inv = Fraction(1, p)
    check(f"1/{p} is real-integral", real_integral(inv))
    check(f"1/{p} is not a real unit", not real_unit(inv))
    check(f"{p} is not real-integral", not real_integral(p))
    check(f"signs are real units for p={p}", real_unit(1) and real_unit(-1))

check("Haran fraction anchor", r"\label{eq111}" in H17)
check("Haran equivalence anchor", "(11.4)" in H17)
check("Haran real unit-ball anchor", "[-1,1]" in H17)

markers = (
    "finite principalization leaves an archimedean boundary defect",
    "does not trivialize the completed anti-lattice",
    "failure of naive principalization",
    "bounded nonunits at infinity",
    "B_p^\\infty",
    "H7-ARCH-BDRY",
    "Neither conclusion is asserted",
    "Row A and RH remain open",
)
for marker in markers:
    check(f"scope marker {marker}", marker in DOC)

print("VERDICT: p_2/p_1 CANCELS FINITE VALUATIONS BUT LEAVES A NONUNIT ARCHIMEDEAN BOUNDARY DEFECT")
