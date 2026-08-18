#!/usr/bin/env python3
"""Undecorated parity Smith obstruction is killed by internal block swaps."""

from itertools import product
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
H17 = ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/HARAN_Dec2016_updated_4.tex"


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


source = H17.read_text()
check("source identifies isomorphic tree data",
      r"(10.14) \quad $\delta$-{\bf commutativity}: isomorphic data are equivalent."
      in source)


rows = [(part, value) for part in range(3) for value in (0, 1)]


def column(edge):
    return sp.Matrix([int(edge[part] == value) for part, value in rows])


def invariants(matrix):
    diagonal = smith_normal_form(matrix, domain=ZZ)
    return [abs(int(diagonal[i, i]))
            for i in range(min(diagonal.rows, diagonal.cols))
            if diagonal[i, i] != 0]


base = (0, 0, 0)
even_nonbase = [(0, 1, 1), (1, 0, 1), (1, 1, 0)]
B = sp.Matrix.hstack(*(column(edge) - column(base) for edge in even_nonbase))
check("starting fold-zero obstruction has Smith 1,1,2", invariants(B) == [1, 1, 2])


even = {edge for edge in product((0, 1), repeat=3) if sum(edge) % 2 == 0}
odd = set(product((0, 1), repeat=3)) - even
for mask in product((0, 1), repeat=3):
    flipped = {tuple(bit ^ mask[i] for i, bit in enumerate(edge)) for edge in even}
    expected = even if sum(mask) % 2 == 0 else odd
    check(f"coordinate flip mask={mask} has expected parity", flipped == expected)


omega = sp.Matrix([[0, 1, 0, 1, 0, 1]])
for part in range(3):
    swap = sp.zeros(6, 1)
    swap[2 * part, 0] = -1
    swap[2 * part + 1, 0] = 1
    extended = B.row_join(swap)
    check(f"part {part + 1} swap kills Smith two",
          invariants(extended) == [1, 1, 1])
    check(f"part {part + 1} swap preserves fold",
          int(sum(swap[2 * part:2 * part + 2, 0])) == 0)
    check(f"omega detects part {part + 1} swap",
          int((omega * swap)[0]) % 2 == 1)


doc = (HERE / "114_a_95_H7_UNDECORATED_PARITY_OBSTRUCTION_IS_KILLED_BY_COMMUTATIVITY.md").read_text()
for marker in (
    "does **not** yield H7-PARITY-SEPARATE",
    "H7-PARITY-RIGID",
    "closed negatively",
    "row A remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: UNDECORATED PARITY Z/2 IS KILLED; RIGIDIFIED VARIANT OPEN")
