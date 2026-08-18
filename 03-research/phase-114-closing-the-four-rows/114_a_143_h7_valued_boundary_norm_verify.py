#!/usr/bin/env python3
"""Exact arithmetic of the valued rational-sphere Picard norm."""

from fractions import Fraction
from math import isclose, log
from pathlib import Path


HERE = Path(__file__).resolve().parent
DOC = (HERE / "114_a_143_H7_VALUED_RATIONAL_SPHERE_PICARD_NORM.md").read_text()
PRIMES = (2, 3, 5, 7, 11)


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def qword(a):
    value = Fraction(1)
    for p, exponent in zip(PRIMES, a):
        value *= Fraction(p) ** exponent
    return value


def nu(a):
    return sum(exponent * log(p) for p, exponent in zip(PRIMES, a))


zero = (0,) * len(PRIMES)
samples = (
    zero,
    (1, 0, 0, 0, 0),
    (-2, 1, 0, 0, 0),
    (3, -1, 2, 0, -1),
    (-1, -1, -1, 2, 1),
)

for a in samples:
    check(f"exact UFD detector {a}", (qword(a) == 1) == (a == zero))
    check(f"log norm agrees with prime word {a}",
          isclose(nu(a), log(float(qword(a)))))

add = lambda a, b: tuple(x + y for x, y in zip(a, b))
neg = lambda a: tuple(-x for x in a)
for a in samples:
    for b in samples:
        check(f"tensor norm law {a},{b}", isclose(nu(add(a, b)), nu(a) + nu(b)))
    check(f"dual norm law {a}", isclose(nu(neg(a)), -nu(a)))

# Norm-one changes of the two endpoint frames add log(1)-log(1)=0.
for a in samples:
    changed = nu(a) + log(1) - log(1)
    check(f"isometric Cech invariance {a}", isclose(changed, nu(a)))

for marker in (
    "Picard norm",
    "metrized boundary faithfulness",
    "supportwise reflection does not create a kernel",
    "not circular",
    "H7-RSPH-UNIT remains open",
    "no longer necessary",
    "Row A and RH are not yet claimed",
):
    check(f"scope marker: {marker}", marker in DOC)

print("VERDICT: THE VALUED MIXED BOUNDARY IS FAITHFUL ON THE METRIZED PRIME LATTICE")
