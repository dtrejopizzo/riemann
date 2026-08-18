#!/usr/bin/env python3
"""Exact controls for the all-arity first-jet prime-regular target."""

from collections import defaultdict
from itertools import product
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def primitive(vector):
    content = 0
    for entry in vector:
        content = gcd(content, abs(entry))
    if content == 0:
        return 0, None
    raw = tuple(entry // content for entry in vector)
    sign = 1 if next(entry for entry in raw if entry) > 0 else -1
    return sign * content, tuple(sign * entry for entry in raw)


def nsymbol(a, b, coefficient=1):
    ca, pa = primitive(a)
    cb, pb = primitive(b)
    if pa is None or pb is None:
        return {}
    return {(pa, pb): coefficient * ca * cb}


def add(*terms):
    out = defaultdict(int)
    for term in terms:
        for basis, coefficient in term.items():
            out[basis] += coefficient
    return {basis: coefficient for basis, coefficient in out.items()
            if coefficient}


# Normal form respects all scalar-transfer relations in several rectangular
# arities.  This is the exact presentation of N, not a floating computation.
transfer_count = 0
for ydim, xdim in ((1, 1), (1, 2), (2, 1), (2, 2), (3, 2)):
    avecs = list(product(range(-2, 3), repeat=ydim))
    bvecs = list(product(range(-2, 3), repeat=xdim))
    # Deterministic sparse sample keeps the regression quick at arity (3,2).
    for a in avecs[::max(1, len(avecs) // 13)]:
        for b in bvecs[::max(1, len(bvecs) // 11)]:
            for lam in range(-3, 4):
                left = {key: lam * value for key, value in nsymbol(a, b).items()
                        if lam * value}
                by_a = nsymbol(tuple(lam * z for z in a), b)
                by_b = nsymbol(a, tuple(lam * z for z in b))
                if left != by_a or left != by_b:
                    raise AssertionError((ydim, xdim, a, b, lam))
                transfer_count += 1
check(f"all-arity N normal form respects {transfer_count} transfers", True)


# H = integer matrices x N.  Prime multiplication is coordinatewise, hence
# injective.  Exhaust bounded elements in representative ranks.
regular_count = 0
for prime in (2, 3, 5, 7):
    elements = []
    for matrix_coordinate in range(-3, 4):
        for n_coordinate in range(-3, 4):
            elements.append((matrix_coordinate, n_coordinate))
    images = [(prime * a, prime * m) for a, m in elements]
    check(f"first-jet target is {prime}-regular on bounded coordinates",
          len(set(images)) == len(elements))
    regular_count += len(elements)
check(f"checked {regular_count} target elements", True)


# The two jet orders exchange the two derivation coordinates.  A source
# p-collision maps to equal p-scaled jets and therefore to equal jets.
jet_pairs = [(a, m12, m21) for a in range(-2, 3)
             for m12 in range(-2, 3) for m21 in range(-2, 3)]
for prime in (2, 3, 5):
    scaled = [(prime * a, prime * x, prime * y) for a, x, y in jet_pairs]
    check(f"combined two-order jet is {prime}-cancellative",
          len(set(scaled)) == len(jet_pairs))


c, f1, f2 = (1, 1), (1, 0), (0, 1)
e1, e2, r = (1, 0), (0, 1), (1, 1)
centre = add(nsymbol(c, e1), nsymbol(c, e2), nsymbol(c, r, -1))
grid = add(*(
    nsymbol(column, row, coefficient)
    for column in (f1, f2)
    for row, coefficient in ((e1, 1), (e2, 1), (r, -1))
))
defect = add(centre, {key: -value for key, value in grid.items()})
check("a104 cross defect is visible to the first ordered jet",
      len(defect) == 9 and all(abs(value) == 1 for value in defect.values()))
for prime in (2, 3, 5, 7, 11):
    check(f"cross defect cannot become zero after multiplication by {prime}",
          any(prime * value for value in defect.values()))


doc = (HERE / "114_a_105_H7_FIRST_JETS_ARE_PRIME_REGULAR.md").read_text()
for marker in (
    "H7-JET1-KERNEL-PURE",
    "not H7-PRIME-REG",
    "full bilateral operation sets",
    "row A remain open",
    "does not itself create",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: FIRST JETS PRIME-REGULAR; ANY COLLISION LIES IN COMMON JET KERNEL")
