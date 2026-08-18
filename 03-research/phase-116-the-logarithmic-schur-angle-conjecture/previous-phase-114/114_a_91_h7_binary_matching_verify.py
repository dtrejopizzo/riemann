#!/usr/bin/env python3
"""Binary regular matching and ternary parity checks; no Haran counterexample claimed."""

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
    r"(3.7) \quad {\bf multiplication}",
    r"(3.8) \quad {\bf contraction}",
    r"fiber by fiber",
    r"(10.16) \quad {\bf cancellation}",
):
    check(f"source marker {marker}", marker in source)


def perfect_matching(matrix):
    """Return one matching as column choices, or None (small exact DFS)."""
    n = len(matrix)
    choice = [-1] * n
    used = [False] * n

    def visit(row):
        if row == n:
            return True
        for col in range(n):
            if matrix[row][col] > 0 and not used[col]:
                choice[row] = col
                used[col] = True
                if visit(row + 1):
                    return True
                used[col] = False
                choice[row] = -1
        return False

    return tuple(choice) if visit(0) else None


def decompose_regular(matrix):
    work = [list(row) for row in matrix]
    degree = sum(work[0]) if work else 0
    layers = []
    for _ in range(degree):
        matching = perfect_matching(work)
        if matching is None:
            return None
        layers.append(matching)
        for row, col in enumerate(matching):
            work[row][col] -= 1
    if any(value for row in work for value in row):
        raise AssertionError((matrix, layers, work))
    return layers


models = 0
for n, max_entry in ((1, 4), (2, 3), (3, 2)):
    for entries in product(range(max_entry + 1), repeat=n * n):
        matrix = tuple(tuple(entries[i * n + j] for j in range(n))
                       for i in range(n))
        row_degrees = [sum(row) for row in matrix]
        col_degrees = [sum(matrix[i][j] for i in range(n)) for j in range(n)]
        if len(set(row_degrees + col_degrees)) != 1:
            continue
        layers = decompose_regular(matrix)
        if layers is None or len(layers) != row_degrees[0]:
            raise AssertionError((n, matrix, row_degrees, col_degrees, layers))
        models += 1
check(f"regular bipartite decomposition in {models} exact multigraphs", True)


edges = {(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)}
for part in range(3):
    for vertex in (0, 1):
        check(f"parity degree part={part}, vertex={vertex}",
              sum(edge[part] == vertex for edge in edges) == 2)


def disjoint(left, right):
    return all(a != b for a, b in zip(left, right))


matchings = [{left, right} for left in edges for right in edges
             if left < right and disjoint(left, right)]
check("even parity hypergraph has no perfect matching", matchings == [])
check("every edge complement has odd parity and is absent",
      all(tuple(1 - bit for bit in edge) not in edges for edge in edges))


doc = (HERE / "114_a_91_H7_BINARY_MATCHING_AND_THE_TERNARY_PARITY_GATE.md").read_text()
for marker in (
    "H7-PARITY-REALIZE",
    "H7-PARITY-CLOSED",
    "H7-PARITY-NONZERO",
    "not a 2-torsion class",
    "row A remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: BINARY REGULAR MIXING DIVIDES; TERNARY PARITY REALIZATION OPEN")
