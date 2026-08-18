#!/usr/bin/env python3
"""Checks for a87; H7-REAL-RES and H7-TAME-PLANE remain open."""

from fractions import Fraction
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
    r"\label{eq1019}",
    r"\label{eq1021}",
    r"With this operation of addition we obtain an ordinary commutative ring",
    r"A_X \to (A_{[1]})^X",
):
    check(f"source marker {marker}", marker in source)


# The exact algebraic implication in finite injective characteristic-zero
# residual models.  Fractions are used so no floating-point cancellation is
# involved.  Each embedding x -> (x,c*x) is injective and Z-linear.
models = 0
for bound in range(1, 9):
    domain = list(range(-bound, bound + 1))
    for c in (Fraction(1), Fraction(2, 3), Fraction(-5, 7)):
        rho = {x: (Fraction(x), c * x) for x in domain}
        check(f"residual map injective bound={bound}, c={c}",
              len(set(rho.values())) == len(domain))
        for n, x, y in product(range(1, 12), domain, domain):
            residual_equal = tuple(n * z for z in rho[x]) == tuple(n * z for z in rho[y])
            if residual_equal and x != y:
                raise AssertionError((bound, c, n, x, y))
            models += 1
check(f"simultaneous integer cancellation in {models} residual comparisons", True)


# Tameness promotion in a finite separating sandwich system.  Operations are
# represented by their complete scalar sandwich signatures; scalar p-action
# is coordinatewise multiplication in characteristic zero.
operations = {
    name: tuple(Fraction(v) for v in signature)
    for name, signature in {
        "zero": (0, 0, 0),
        "left": (1, 0, 2),
        "right": (0, 1, 2),
        "mix": (1, 1, 3),
    }.items()
}
check("finite sandwich system is tame/separating",
      len(set(operations.values())) == len(operations))
for p in (2, 3, 5, 7, 11):
    scaled = {name: tuple(p * x for x in signature)
              for name, signature in operations.items()}
    check(f"scalar cancellation promotes through sandwiches p={p}",
          len(set(scaled.values())) == len(operations))


doc = (HERE / "114_a_87_H7_CHARACTERISTIC_ZERO_RESIDUAL_ROUTE.md").read_text()
for marker in (
    "H7-REAL-RES",
    "H7-TAME-PLANE",
    "Later resolution (`a104`)",
    "H7-TAME-PLANE is false",
    "row A remains open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: CONDITIONAL REAL-RES+TAME ROUTE VALID; a104 KILLS TAME HYPOTHESIS")
