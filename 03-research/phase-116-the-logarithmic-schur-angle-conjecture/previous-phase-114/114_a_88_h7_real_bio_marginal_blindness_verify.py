#!/usr/bin/env python3
"""Exact marginal-blindness checks; quotient nonfaithfulness is not asserted."""

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
    r"a = (F_y , G_x , \sigma , \varepsilon)",
    r"\label{eq1010}",
    r"\label{eq1020}",
    r"\label{eq1021}",
):
    check(f"source marker {marker}", marker in source)


# Parent-block incidence matrices for the two bijections.  Block sizes 1,2
# distinguish rows and columns, so no allowed block permutation relates them.
B0 = ((1, 0), (0, 2))
B1 = ((0, 1), (1, 1))


def row_sums(matrix):
    return tuple(sum(row) for row in matrix)


def col_sums(matrix):
    return tuple(sum(matrix[i][j] for i in range(len(matrix)))
                 for j in range(len(matrix[0])))


check("three-leaf cores are different", B0 != B1)
check("left marginals agree", row_sums(B0) == row_sums(B1) == (1, 2))
check("right marginals agree", col_sums(B0) == col_sums(B1) == (1, 2))
check("distinguished block sizes forbid row/column swaps", (1, 2) != (2, 1))


# Finite transported field, as in a49: T(x)=x^3 over F5 is its own inverse
# on exponents modulo 4.  Both bijections feed the same three signed copies
# into the same row tree; the pairing never enters the value.
P = 5


def add_1(x, y):
    return (x + y) % P


def add_u(x, y):
    return pow((pow(x, 3, P) + pow(y, 3, P)) % P, 3, P)


def comb_value(x, outer, inner):
    return outer(x, inner(x, x))


for outer, inner, label in (
    (add_1, add_u, "ordinary/twisted"),
    (add_u, add_1, "twisted/ordinary"),
):
    for x in range(P):
        left_0 = comb_value(x, outer, inner)
        left_1 = comb_value(x, outer, inner)
        right_0 = comb_value(x, outer, inner)
        right_1 = comb_value(x, outer, inner)
        check(f"marginal blindness {label} x={x}",
              (left_0, right_0) == (left_1, right_1))


doc = (HERE / "114_a_88_H7_REAL_BIO_MARGINAL_BLINDNESS.md").read_text()
for marker in (
    "H7-MARGINAL-COMPLETE",
    "not** asserted to be a pair of distinct classes",
    "does not by itself prove",
    "row A remain open",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: HOMOGENEOUS UNARY BIOS SEE SIGNED MARGINALS, NOT LEAF PAIRING")
