#!/usr/bin/env python3
"""Exact Smith checks for rectangular macro contexts; overlaps stay open."""

from itertools import product
from pathlib import Path

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
H17 = ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/HARAN_Dec2016_updated_4.tex"


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


source = H17.read_text()
for marker in (r"(10.16) \quad {\bf cancellation}", r"\label{eq1019}"):
    check(f"source marker {marker}", marker in source)


def incidence(shape, quotient=None):
    vertices = list(product(*[range(n) for n in shape]))
    if quotient is None:
        quotient = {v: i for i, v in enumerate(vertices)}
    classes = sorted(set(quotient.values()))
    renumber = {c: i for i, c in enumerate(classes)}
    rows = []
    for v in vertices:
        for axis, size in enumerate(shape):
            if size < 2 or v[axis] + 1 >= size:
                continue
            w = list(v)
            w[axis] += 1
            w = tuple(w)
            u_class = renumber[quotient[v]]
            v_class = renumber[quotient[w]]
            if u_class == v_class:
                continue
            row = [0] * len(classes)
            row[u_class] = -1
            row[v_class] = 1
            rows.append(row)
    return rows, len(classes)


def nonzero_smith(rows, columns):
    if not rows or not columns:
        return []
    diagonal = smith_normal_form(Matrix(rows), domain=ZZ)
    return [abs(int(diagonal[i, i]))
            for i in range(min(diagonal.rows, diagonal.cols))
            if diagonal[i, i]]


shapes = [(2,), (3,), (4,), (2, 2), (2, 3), (3, 3),
          (2, 2, 2), (2, 2, 3), (2, 3, 3), (2, 2, 2, 2)]
for shape in shapes:
    rows, columns = incidence(shape)
    invariants = nonzero_smith(rows, columns)
    check(f"rectangular Smith invariants shape={shape}",
          all(d == 1 for d in invariants))


# Exhaust all vertex identifications (all maps to at most n labels) for the
# grids with at most four vertices.  Duplicated labelings are harmless and
# deliberately test repeated quotient presentations.
quotient_count = 0
for shape in ((2,), (3,), (2, 2)):
    vertices = list(product(*[range(n) for n in shape]))
    n = len(vertices)
    for labels in product(range(n), repeat=n):
        quotient = dict(zip(vertices, labels))
        rows, columns = incidence(shape, quotient)
        invariants = nonzero_smith(rows, columns)
        if any(d != 1 for d in invariants):
            raise AssertionError((shape, labels, invariants))
        quotient_count += 1
check(f"vertex-quotient incidence saturation for {quotient_count} presentations", True)


# K2,2 is the 2x2 context and has a free rank-one cokernel because it is
# connected; its relation subgroup has rank 3 and all Smith factors one.
rows, columns = incidence((2, 2))
invariants = nonzero_smith(rows, columns)
check("K2,2 macro context is saturated", columns == 4 and invariants == [1, 1, 1])


doc = (HERE / "114_a_82_H7_RECTANGULAR_MACRO_CONTEXTS_ARE_SATURATED.md").read_text()
for marker in (
    "H7-MACRO-OVERLAP",
    "does not settle H7-MACRO-CONTEXT-SAT",
    "nonseparable fiber overlap",
    "row A remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: ALL RECTANGULAR MACRO CONTEXTS ARE SATURATED; NONSEPARABLE OVERLAPS OPEN")
