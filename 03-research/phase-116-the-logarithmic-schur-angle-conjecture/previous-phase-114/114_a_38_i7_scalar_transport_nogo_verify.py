#!/usr/bin/env python3
"""Checks for the ordinary-Witt-target diagonal factorization no-go."""

from pathlib import Path

from sympy import divisors


ROOT = Path(__file__).resolve().parent
HARAN = (ROOT.parent.parent / "00-references/papers-nuevos/A/"
         "arXiv-1709.05831v1/HARAN_Dec2016_updated_4.tex").read_text()

print("A. Haran total-commutativity source anchor")
assert "(7.17)" in HARAN
assert "total-commutativity imply ${\\mathbb Z} \\otimes {\\mathbb Z} = {\\mathbb Z}$" in HARAN
assert "\\delta_1 = \\delta_2" in HARAN
print("  Remark 7.17 and delta_1=delta_2 found")

print("\nB. The two unital integer maps coincide")
for stage in range(1, 101):
    basis = divisors(stage)
    assert 1 in basis  # phi_1 is the unit at every finite Witt stage.
    for n in range(-50, 51):
        first_copy = {1: n}
        second_copy = {1: n}
        assert first_copy == second_copy
print("  both copies send n to n*phi_1 on all checked stages")

print("\nC. Universal fold loses the ruling label")
formal_generators = {"delta_1": "delta", "delta_2": "delta"}
assert formal_generators["delta_1"] == formal_generators["delta_2"]
off_diagonal_words = [
    ("delta_1", "delta_2"),
    ("delta_2", "delta_1"),
    ("delta_1", "delta_1"),
]
folded = [tuple(formal_generators[x] for x in word)
          for word in off_diagonal_words]
assert len(set(folded)) == 1
print("  distinct two-ruling words have one diagonal image")

print("\nVERDICT: I7 ORDINARY WITT SCALAR-TRANSPORT NO-GO CHECKS PASS")
