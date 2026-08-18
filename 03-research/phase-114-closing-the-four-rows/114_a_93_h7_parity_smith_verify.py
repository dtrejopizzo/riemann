#!/usr/bin/env python3
"""Exact parity-incidence Smith obstruction; Haran macro realization remains open."""

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
even = [edge for edge in product((0, 1), repeat=3) if sum(edge) % 2 == 0]
odd = [edge for edge in product((0, 1), repeat=3) if sum(edge) % 2 == 1]


def incidence(edges):
    return sp.Matrix([[int(edge[part] == value) for edge in edges]
                      for part, value in rows])


def invariants(matrix):
    diagonal = smith_normal_form(matrix, domain=ZZ)
    return [abs(int(diagonal[i, i]))
            for i in range(min(diagonal.rows, diagonal.cols))
            if diagonal[i, i] != 0]


A = incidence(even)
check("parity incidence matrix shape", A.shape == (6, 4))
check("parity incidence rank four", A.rank() == 4)
check("exact Smith factors 1,1,1,2", invariants(A) == [1, 1, 1, 2])


maximal_minors = []
for selected_rows in combinations(range(6), 4):
    maximal_minors.append(abs(int(A.extract(selected_rows, range(4)).det())))
check("every maximal minor is even", all(value % 2 == 0 for value in maximal_minors))
check("maximal-minor gcd is two", sp.gcd_list(maximal_minors) == 2)


z = sp.ones(6, 1)
ones = sp.ones(4, 1)
check("sum of parity columns is twice z", A * ones == 2 * z)

omega = sp.Matrix([[0, 1, 0, 1, 0, 1]])
check("omega kills every even column mod two",
      all(int(value) % 2 == 0 for value in omega * A))
check("omega detects z mod two", int((omega * z)[0]) % 2 == 1)

solution = sp.linsolve((A, z))
check("unique rational half-column solution",
      solution == {(sp.Rational(1, 2),) * 4})

for edge in odd:
    extended = incidence(even + [edge])
    check(f"odd edge {edge} kills Smith two", invariants(extended) == [1, 1, 1, 1])
    check(f"omega detects odd edge {edge}", int((omega * extended[:, -1])[0]) % 2 == 1)


doc = (HERE / "114_a_93_H7_PARITY_INCIDENCE_HAS_EXACT_TWO_TORSION.md").read_text()
for marker in (
    "not yet a counterexample",
    "H7-PARITY-ENDPOINTS",
    "H7-PARITY-PRESERVE",
    "H7-PARITY-SEPARATE",
    "Only the conjunction",
    "row A remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: PARITY INCIDENCE HAS Z/2; FULL HARAN MACRO CLOSURE OPEN")
