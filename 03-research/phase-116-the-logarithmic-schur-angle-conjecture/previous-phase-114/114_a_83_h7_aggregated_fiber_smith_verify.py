#!/usr/bin/env python3
"""Exact Smith obstruction models for aggregated macro-context fibers."""

from pathlib import Path

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


HERE = Path(__file__).resolve().parent


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def smith_nonzero(matrix):
    d = smith_normal_form(Matrix(matrix), domain=ZZ)
    return [abs(int(d[i, i])) for i in range(min(d.rows, d.cols)) if d[i, i]]


def cycle_incidence(n):
    b = [[0] * n for _ in range(n)]
    for edge in range(n):
        b[edge][edge] = -1
        b[edge][(edge + 1) % n] = 1
    return Matrix(b)


for n in range(3, 13):
    b = cycle_incidence(n)
    incidence_smith = smith_nonzero(b)
    laplacian = b.T * b
    laplacian_smith = smith_nonzero(laplacian)
    check(f"C_{n} incidence subgroup saturated", incidence_smith == [1] * (n - 1))
    check(f"C_{n} Laplacian has critical factor {n}",
          laplacian_smith == [1] * (n - 2) + [n])

triangle = smith_nonzero(cycle_incidence(3).T * cycle_incidence(3))
check("triangle gives exact 3-torsion", triangle == [1, 3])
six_cycle = smith_nonzero(cycle_incidence(6).T * cycle_incidence(6))
check("bipartite C6 still has odd Smith factor", six_cycle[-1] == 6)


doc = (HERE / "114_a_83_H7_AGGREGATED_FIBER_SMITH_OBSTRUCTIONS.md").read_text()
for marker in (
    "H7-FIBER-RETENTION",
    "No Haran cycle-Laplacian context is asserted",
    "same normalized",
    "row A remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: AGGREGATED FIBERS CAN CREATE Z/n SMITH TORSION; FIBER RETENTION OPEN")
