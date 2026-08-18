#!/usr/bin/env python3
"""Full fixed two-level relation lattice; nested macro contexts stay open."""

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
    r"(10.16) \quad {\bf cancellation}",
    r"(10.17) \quad {\bf commutativity}",
    r"\label{eq1018}",
    r"\label{eq1019}",
    r"\label{eq1020}",
):
    check(f"source marker {marker}", marker in source)


def total(table):
    return sum(value for row in table for value in row)


def normalize_by_relations(table):
    """Move every entry to the bottom-right using row then column contrasts."""
    rows = len(table)
    cols = len(table[0])
    work = [list(row) for row in table]
    # (e_i-e_last) tensor f_j moves each nonlast-row coefficient downward.
    for i in range(rows - 1):
        for j in range(cols):
            value = work[i][j]
            work[i][j] -= value
            work[rows - 1][j] += value
    # e_last tensor (f_j-f_last) moves each nonlast-column coefficient right.
    for j in range(cols - 1):
        value = work[rows - 1][j]
        work[rows - 1][j] -= value
        work[rows - 1][cols - 1] += value
    return tuple(tuple(row) for row in work)


models = 0
for rows, cols, bound in ((1, 1, 4), (1, 4, 2), (4, 1, 2),
                          (2, 2, 3), (2, 3, 2), (3, 2, 2), (3, 3, 1)):
    for entries in product(range(-bound, bound + 1), repeat=rows * cols):
        table = tuple(tuple(entries[i * cols + j] for j in range(cols))
                      for i in range(rows))
        normal = normalize_by_relations(table)
        expected = tuple(
            tuple(total(table) if i == rows - 1 and j == cols - 1 else 0
                  for j in range(cols))
            for i in range(rows)
        )
        if normal != expected:
            raise AssertionError((rows, cols, table, normal, expected))
        models += 1
check(f"total-mass normal form in {models} exact signed tables", True)


# Explicit generators from the two rulings have zero total and normalize to 0.
generator_count = 0
for rows, cols in ((2, 2), (2, 4), (4, 2), (3, 3)):
    for i in range(rows - 1):
        for vector in product(range(-2, 3), repeat=cols):
            table = [[0] * cols for _ in range(rows)]
            for j, value in enumerate(vector):
                table[i][j] += value
                table[rows - 1][j] -= value
            table = tuple(tuple(row) for row in table)
            if total(table) != 0 or any(any(row) for row in normalize_by_relations(table)):
                raise AssertionError(("row", rows, cols, i, vector, table))
            generator_count += 1
    for j in range(cols - 1):
        for vector in product(range(-2, 3), repeat=rows):
            table = [[0] * cols for _ in range(rows)]
            for i, value in enumerate(vector):
                table[i][j] += value
                table[i][cols - 1] -= value
            table = tuple(tuple(row) for row in table)
            if total(table) != 0 or any(any(row) for row in normalize_by_relations(table)):
                raise AssertionError(("column", rows, cols, j, vector, table))
            generator_count += 1
check(f"both-ruling context generators in {generator_count} models", True)


# Saturation is cancellation in the Z total-mass quotient.
sat_models = 0
for p in (2, 3, 5, 7, 11):
    for mass in range(-50, 51):
        if p * mass == 0 and mass != 0:
            raise AssertionError((p, mass))
        sat_models += 1
check(f"all-prime saturation in {sat_models} quotient tests", True)


K22 = ((1, 1), (-1, -1))
B0 = ((1, 0), (0, 2))
B1 = ((0, 1), (1, 1))
difference = tuple(tuple(B0[i][j] - B1[i][j] for j in range(2))
                   for i in range(2))
check("a81 K2,2 is a first-ruling contrast context",
      total(K22) == 0 and normalize_by_relations(K22) == ((0, 0), (0, 0)))
check("a81 regression: naive row margins are not invariant",
      tuple(map(sum, K22)) == (2, -2))
check("a88 pair has equal total mass", total(B0) == total(B1) == 3)
check("a88 difference is the checkerboard",
      difference == ((1, -1), (-1, 1))
      and normalize_by_relations(difference) == ((0, 0), (0, 0)))


doc = (HERE / "114_a_89_H7_TWO_LEVEL_MARGINAL_COMPLETENESS.md").read_text()
for marker in (
    "Correction made during the same construction",
    "row/column margins are not invariants",
    "H7-NESTED-CONTEXT-SAT",
    "does **not** identify",
    "row A remain",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: FIXED TWO-LEVEL QUOTIENT IS TOTAL MASS Z; NESTED CONTEXTS OPEN")
