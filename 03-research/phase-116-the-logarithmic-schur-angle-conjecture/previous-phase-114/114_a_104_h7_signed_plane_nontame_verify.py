#!/usr/bin/env python3
"""Exact normal-form check for the signed-plane cross-defect separator."""

from collections import defaultdict
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def primitive(vector):
    """Return signed content and oriented primitive direction; zero -> None."""
    content = 0
    for entry in vector:
        content = gcd(content, abs(entry))
    if content == 0:
        return 0, None
    raw = tuple(entry // content for entry in vector)
    first = next(entry for entry in raw if entry)
    sign = 1 if first > 0 else -1
    return sign * content, tuple(sign * entry for entry in raw)


def symbol(a, b, coefficient=1):
    ca, pa = primitive(a)
    cb, pb = primitive(b)
    if pa is None or pb is None:
        return {}
    return {(pa, pb): coefficient * ca * cb}


def add(*terms):
    total = defaultdict(int)
    for term in terms:
        for basis, coefficient in term.items():
            total[basis] += coefficient
    return {basis: coefficient for basis, coefficient in total.items()
            if coefficient}


# Scaling-transfer relations, including signs and zero, hold in normal form.
scaling_checks = 0
vectors = ((0, 0), (1, 0), (0, 1), (1, 1), (-1, 2), (2, -4))
for a in vectors:
    for b in vectors:
        for lam in range(-4, 5):
            left = {basis: lam * value for basis, value in symbol(a, b).items()
                    if lam * value}
            scale_a = symbol(tuple(lam * x for x in a), b)
            scale_b = symbol(a, tuple(lam * x for x in b))
            check_data = left == scale_a == scale_b
            if not check_data:
                raise AssertionError((a, b, lam, left, scale_a, scale_b))
            scaling_checks += 1
check(f"normal form respects {scaling_checks} scaling-transfer relations", True)


c, f1, f2 = (1, 1), (1, 0), (0, 1)
e1, e2, r = (1, 0), (0, 1), (1, 1)

centre = add(symbol(c, e1), symbol(c, e2), symbol(c, r, -1))
grid = add(*(
    symbol(column, row, coefficient)
    for column in (f1, f2)
    for row, coefficient in ((e1, 1), (e2, 1), (r, -1))
))
defect = add(centre, {basis: -coefficient for basis, coefficient in grid.items()})

check("centre has three primitive-direction coordinates", len(centre) == 3)
check("grid has six primitive-direction coordinates", len(grid) == 6)
check("cross defect has nine independent nonzero coordinates",
      len(defect) == 9 and set(map(abs, defect.values())) == {1})
check("centre and grid are unequal in Haran N", centre != grid)


def outer_sum(expression):
    matrix = [[0, 0], [0, 0]]
    for (column, row), coefficient in expression.items():
        for i in range(2):
            for j in range(2):
                matrix[i][j] += coefficient * column[i] * row[j]
    return tuple(tuple(row) for row in matrix)


zero = ((0, 0), (0, 0))
check("centre infinitesimal part has zero ordinary matrix image",
      outer_sum(centre) == zero)
check("grid infinitesimal part has the same zero matrix image",
      outer_sum(grid) == zero)
check("nonzero N-defect lies in the matrix kernel", outer_sum(defect) == ((0, 0), (0, 0)))

# The common base R-component of the two complete operations is the all-one
# matrix; this is separate from the zero matrix image of their N-components.
base_centre = tuple(tuple(c[i] * r[j] for j in range(2)) for i in range(2))
base_grid = tuple(tuple(1 for _j in range(2)) for _i in range(2))
check("complete operations have common all-one base component",
      base_centre == base_grid == ((1, 1), (1, 1)))


doc = (HERE / "114_a_104_H7_SIGNED_PLANE_IS_NOT_TAME.md").read_text()
for marker in (
    "H7-XDEF-12 is closed negatively",
    "H7-TAME-PLANE is false",
    "does **not** prove that H7-PRIME-REG is false",
    "full signed plane",
    "commented out",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: XDEF-12 SURVIVES; SIGNED ARITHMETIC PLANE IS NOT TAME")
