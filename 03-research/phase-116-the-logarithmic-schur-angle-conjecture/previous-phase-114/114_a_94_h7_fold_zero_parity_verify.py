#!/usr/bin/env python3
"""Fold-zero parity-difference Smith obstruction; macro paths remain open."""

from itertools import combinations, product
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


HERE = Path(__file__).resolve().parent


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


rows = [(part, value) for part in range(3) for value in (0, 1)]


def column(edge):
    return sp.Matrix([int(edge[part] == value) for part, value in rows])


base = (0, 0, 0)
even_nonbase = [(0, 1, 1), (1, 0, 1), (1, 1, 0)]
odd = [edge for edge in product((0, 1), repeat=3) if sum(edge) % 2 == 1]
B = sp.Matrix.hstack(*(column(edge) - column(base) for edge in even_nonbase))


def invariants(matrix):
    diagonal = smith_normal_form(matrix, domain=ZZ)
    return [abs(int(diagonal[i, i]))
            for i in range(min(diagonal.rows, diagonal.cols))
            if diagonal[i, i] != 0]


check("fold-zero parity matrix shape", B.shape == (6, 3))
for index in range(B.cols):
    for part in range(3):
        check(f"column {index} preserves part {part} total",
              int(B[2 * part, index] + B[2 * part + 1, index]) == 0)

check("fold-zero matrix rank three", B.rank() == 3)
check("fold-zero Smith factors 1,1,2", invariants(B) == [1, 1, 2])
minors = [abs(int(B.extract(selected_rows, range(3)).det()))
          for selected_rows in combinations(range(6), 3)]
check("all full-rank minors even", all(value % 2 == 0 for value in minors))
check("full-rank minor gcd two", sp.gcd_list(minors) == 2)

w = sp.Matrix([-1, 1, -1, 1, -1, 1])
check("three even differences sum to twice w", B * sp.ones(3, 1) == 2 * w)
omega = sp.Matrix([[0, 1, 0, 1, 0, 1]])
check("omega kills fold-zero even differences",
      all(int(value) % 2 == 0 for value in omega * B))
check("omega detects w", int((omega * w)[0]) % 2 == 1)
check("unique rational half solution",
      sp.linsolve((B, w)) == {(sp.Rational(1, 2),) * 3})

for edge in odd:
    extended = B.row_join(column(edge) - column(base))
    check(f"odd difference {edge} kills Smith two",
          invariants(extended) == [1, 1, 1])
    check(f"omega detects odd difference {edge}",
          int((omega * extended[:, -1])[0]) % 2 == 1)


doc = (HERE / "114_a_94_H7_FOLD_ZERO_PARITY_DIFFERENCES_RETAIN_TWO_TORSION.md").read_text()
for marker in (
    "H7-EVEN-MOVES",
    "H7-ODD-MOVE",
    "H7-PARITY-ENDPOINTS",
    "H7-PARITY-SEPARATE",
    "No torsion class",
    "row A remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: FOLD-ZERO EVEN DIFFERENCES RETAIN Z/2; MACRO MOVES OPEN")
