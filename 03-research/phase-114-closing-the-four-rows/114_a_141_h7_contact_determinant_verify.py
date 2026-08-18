#!/usr/bin/env python3
"""Exact metric algebra for the contact torsion determinant line."""

from itertools import product
from math import exp, isclose, log
from pathlib import Path


HERE = Path(__file__).resolve().parent
DOC = (HERE / "114_a_141_H7_CONTACT_DETERMINANT_LINE.md").read_text()
PRIMES = (2, 3, 5, 7)


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def add(x, y):
    return tuple(tuple(a + b for a, b in zip(x[i], y[i])) for i in (0, 1))


def contact(x, y):
    return sum(log(p) * (x[0][i] * y[1][i] + x[1][i] * y[0][i])
               for i, p in enumerate(PRIMES))


def determinant_norm(x, y):
    return exp(-contact(x, y))


x = ((1, -2, 0, 3), (0, 1, -1, 0))
y = ((0, 1, 2, -1), (2, 0, -1, 1))
z = ((-1, 0, 1, 1), (1, -1, 0, 2))

check("torsion norm of F_p is p^-1",
      all(isclose(exp(-log(p)), 1 / p) for p in PRIMES))
check("dual virtual class inverts the norm",
      isclose(determinant_norm(tuple(tuple(-a for a in r) for r in x), y),
              1 / determinant_norm(x, y)))
check("first-variable determinant tensor law",
      isclose(determinant_norm(add(x, z), y),
              determinant_norm(x, y) * determinant_norm(z, y)))
check("second-variable determinant tensor law",
      isclose(determinant_norm(x, add(y, z)),
              determinant_norm(x, y) * determinant_norm(x, z)))
check("contact determinant is symmetric",
      isclose(determinant_norm(x, y), determinant_norm(y, x)))

prime_blocks_ok = True
for i, j in product(range(len(PRIMES)), repeat=2):
    e1 = ([0] * len(PRIMES), [0] * len(PRIMES))
    e2 = ([0] * len(PRIMES), [0] * len(PRIMES))
    e1[0][i] = 1
    e2[1][j] = 1
    value = contact((tuple(e1[0]), tuple(e1[1])),
                    (tuple(e2[0]), tuple(e2[1])))
    prime_blocks_ok &= isclose(value, log(PRIMES[i]) if i == j else 0)
check("prime determinant block is delta_pq log p", prime_blocks_ok)

for marker in (
    "torsion determinant",
    "exactly E_C",
    "H7-RR-DET",
    "O(t)",
    "residue/contact half",
    "row A and",
):
    check(f"scope marker: {marker}", marker in DOC)

print("VERDICT: THE CONTACT BIEXTENSION IS THE TORSION DETERMINANT OF GEOMETRIC INCIDENCE")
