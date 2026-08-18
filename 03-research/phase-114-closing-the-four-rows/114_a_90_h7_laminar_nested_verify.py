#!/usr/bin/env python3
"""Laminar fiber-incidence saturation checks; nonlaminar reuse stays open."""

from itertools import combinations
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
for marker in (
    r"(10.16) \quad {\bf cancellation}",
    r"(10.17) \quad {\bf commutativity}",
    r"\label{eq1018}",
    r"\label{eq1019}",
):
    check(f"source marker {marker}", marker in source)


def component_count(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            parent[y] = x

    for u, v in edges:
        union(u, v)
    return len({find(i) for i in range(n)})


def incidence(n, edges, signs=None):
    signs = [1] * len(edges) if signs is None else signs
    matrix = sp.zeros(n, len(edges))
    for k, ((u, v), sign) in enumerate(zip(edges, signs)):
        matrix[u, k] = -sign
        matrix[v, k] = sign
    return matrix


graph_count = 0
for n in range(1, 6):
    possible = list(combinations(range(n), 2))
    for mask in range(1 << len(possible)):
        edges = [edge for i, edge in enumerate(possible) if mask >> i & 1]
        matrix = incidence(n, edges)
        diagonal = smith_normal_form(matrix, domain=ZZ)
        invariants = [abs(int(diagonal[i, i]))
                      for i in range(min(diagonal.rows, diagonal.cols))
                      if diagonal[i, i] != 0]
        expected_rank = n - component_count(n, edges)
        if invariants != [1] * expected_rank:
            raise AssertionError((n, edges, invariants, expected_rank))
        # Reversing arbitrary edge orientations changes columns by units.
        signs = [(-1 if i % 2 else 1) for i in range(len(edges))]
        signed_diagonal = smith_normal_form(incidence(n, edges, signs), domain=ZZ)
        signed_invariants = [abs(int(signed_diagonal[i, i]))
                             for i in range(min(signed_diagonal.rows,
                                                signed_diagonal.cols))
                             if signed_diagonal[i, i] != 0]
        if signed_invariants != invariants:
            raise AssertionError((n, edges, invariants, signed_invariants))
        graph_count += 1
check(f"unit Smith factors in {graph_count} overlap graphs", True)


# Direct sums over independent fibers preserve only unit nonzero factors.
blocks = [incidence(3, [(0, 1), (1, 2)]),
          incidence(4, [(0, 1), (1, 2), (2, 3), (0, 3)]),
          incidence(2, [(0, 1)])]
direct = sp.diag(*blocks)
diagonal = smith_normal_form(direct, domain=ZZ)
invariants = [abs(int(diagonal[i, i]))
              for i in range(min(diagonal.rows, diagonal.cols))
              if diagonal[i, i] != 0]
check("direct sum of strand-fiber incidence blocks is saturated",
      invariants == [1] * sum(block.rank() for block in blocks))


# Contrast with aggregated C_n Laplacian: its critical Smith factor is n.
for n in range(3, 9):
    cycle_edges = [(i, (i + 1) % n) for i in range(n)]
    boundary = incidence(n, cycle_edges)
    laplacian = boundary * boundary.T
    diagonal = smith_normal_form(laplacian, domain=ZZ)
    invariants = [abs(int(diagonal[i, i]))
                  for i in range(n) if diagonal[i, i] != 0]
    check(f"aggregated cycle warning C_{n}", invariants[-1] == n)


doc = (HERE / "114_a_90_H7_LAMINAR_NESTED_CONTEXTS_ARE_SATURATED.md").read_text()
for marker in (
    "H7-FIBER-RETENTION",
    "H7-NONLAMINAR-FIBER",
    "does not assert",
    "row A remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: LAMINAR NESTED FIBERS ARE SATURATED; NONLAMINAR REUSE OPEN")
