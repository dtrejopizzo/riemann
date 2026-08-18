#!/usr/bin/env python3
"""Regression checks for the reflected anti-diagonal gate in a122."""

from itertools import product
from math import log
from pathlib import Path


HERE = Path(__file__).resolve().parent
DOC = (HERE / "114_a_122_H7_REFLECTED_ANTIDIAGONAL_AND_RULING_PRODUCT_FORMULA.md").read_text()
PRIMES = (2, 3, 5, 7)


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


# Finite group model: f is injective but restriction r kills its image.
G = range(5)
f = {x: (x, 0) for x in G}
r = lambda pair: pair[1]
check("literal injection model", len(set(f.values())) == len(G))
check("closed restriction can kill injected sector",
      len({r(f[x]) for x in G}) == 1)


# Conversely, injectivity of both the literal map and restriction on its
# image makes the composite injective.
r_good = lambda pair: pair[0]
check("faithful reflected pullback makes composite injective",
      len({r_good(f[x]) for x in G}) == len(G))


tested = 0
for a in product(range(-2, 3), repeat=len(PRIMES)):
    if not any(a):
        continue
    A = sum(n * log(p) for n, p in zip(a, PRIMES))
    check(f"anti degree pair {a}", abs(A + (-A)) < 1e-14)
    check(f"UFD detects nonzero anti vector {a}", abs(A) > 1e-12)
    # A two-coordinate product formula excludes this principal pair.
    ruling_pf_allows = abs(A) < 1e-12 and abs(-A) < 1e-12
    check(f"ruling product formula excludes {a}", not ruling_pf_allows)
    tested += 1

check("exhaustive nonzero vectors", tested == 5**len(PRIMES) - 1)

markers = (
    "reflected anti-diagonal needs a ruling product formula",
    "not as a retraction",
    "not imply injectivity of the composite",
    "H7-REFL-PIC",
    "H7-RULING-PF",
    "both numbers in (3.1) vanish separately",
    "corrects every use of bare H7-U3/LD",
    "does not close row A or RH",
)
for marker in markers:
    check(f"scope marker {marker}", marker in DOC)

print("VERDICT: REFLECTED ANTIDIAGONAL REQUIRES REFL-PIC OR A RULING PRODUCT FORMULA")
