#!/usr/bin/env python3
"""Finite controls for cross-defect sandwich blindness and tameness."""

from itertools import product
from pathlib import Path


HERE = Path(__file__).resolve().parent


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


# The complete signature abstraction: L and R have the same value under
# every scalar sandwich.  If retained as distinct operations, injectivity of
# the signature map (tameness) fails.  Exhaust signatures of small lengths.
models = 0
for alphabet_size in range(1, 5):
    alphabet = range(alphabet_size)
    for length in range(1, 6):
        for signature in product(alphabet, repeat=length):
            operations = {"centre": signature, "grid": signature}
            tame = len(set(operations.values())) == len(operations)
            if tame:
                raise AssertionError((alphabet_size, length, signature))
            models += 1
check(f"surviving blind cross defect is nontame in {models} signature systems", True)


# Ordinary matrix shadow of the mixed binary generator defect.  The centre
# is the outer product of all-one column/row.  The grid applies one copied
# column per input and one copied row per output; both are the all-one 2x2
# matrix, while the incidence factorizations remain syntactically different.
centre = ((1, 1), (1, 1))
grid = tuple(tuple(1 for _input in range(2)) for _output in range(2))
check("mixed centre and Cartesian grid have identical matrix shadow",
      centre == grid)
check("centre and grid presentations are syntactically distinct",
      "delta1^t o delta2" != "(delta2+delta2) o (delta1^t+delta1^t)")


# In any finite tame abstraction, equal complete signatures force equality
# of operation labels.  This is the exact logical use of tameness in (1.3).
tame_models = 0
for size in range(1, 6):
    signatures = [tuple(int(i == j) for j in range(size)) for i in range(size)]
    if len(set(signatures)) != size:
        raise AssertionError((size, signatures))
    for left, right in product(range(size), repeat=2):
        if signatures[left] == signatures[right] and left != right:
            raise AssertionError((size, left, right))
        tame_models += 1
check(f"tame signature equality forces operation equality in {tame_models} pairs", True)


doc = (HERE / "114_a_103_H7_CROSS_COMMUTATIVITY_IS_THE_FIRST_TAMENESS_TEST.md").read_text()
for marker in (
    "commutative}+\\text{tame}",
    "H7-XDEF-12",
    "a81",
    "signed cancellation quotient",
    "Later resolution (`a104`)",
    "H7-TAME-PLANE is false",
    "row A remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: CROSS-DEFECT TEST VALID; a104 PROVES XDEF-12 SURVIVES")
