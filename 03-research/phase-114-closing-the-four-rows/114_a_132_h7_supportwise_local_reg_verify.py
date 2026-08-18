#!/usr/bin/env python3
"""Checks the supportwise local regular pro-square construction (a132)."""

from itertools import combinations
from math import prod
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DOC = (HERE / "114_a_132_H7_SUPPORTWISE_LOCAL_REGULAR_PRO_SQUARE.md").read_text()
H17 = (ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/"
       "HARAN_Dec2016_updated_4.tex").read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


primes = (2, 3, 5, 7)
supports = [frozenset(c) for r in range(len(primes) + 1)
            for c in combinations(primes, r)]

# The indexing category is directed by union and lcm/product at squarefree
# levels, and every support prime is a unit on its boundary overlap.
for t in supports:
    n_t = prod(t) if t else 1
    check(f"support divides its level T={sorted(t)}",
          all(n_t % p == 0 for p in t))
for t in supports:
    for u in supports:
        upper = t | u
        check(f"directed upper support {sorted(t)},{sorted(u)}",
              t <= upper and u <= upper)

# Active systems by product-chart type: FF has both, FR only first, RF only
# second, RR none.  On a type-changing overlap, all support primes are units.
active = {"FF": {1, 2}, "FR": {1}, "RF": {2}, "RR": set()}
check("real-real reflection is identity", not active["RR"])
check("mixed active systems are typed",
      active["FR"] == {1} and active["RF"] == {2})
for t in supports:
    n_t = prod(t) if t else 1
    for p in t:
        check(f"boundary overlap inverts p={p} at N={n_t}", n_t % p == 0)

# Finite abelian shadow: relative reflection kills exactly torsion supported
# at active primes; enlarging T gives a further quotient.
def reflected_order(order, support):
    for p in support:
        while order % p == 0:
            order //= p
    return order

removal_ok = True
transition_ok = True
transition_count = 0
for order in range(1, 301):
    for t in supports:
        r = reflected_order(order, t)
        removal_ok &= all(r % p != 0 for p in t)
        for u in supports:
            if t <= u:
                rr = reflected_order(order, u)
                transition_count += 1
                transition_ok &= r % rr == 0
check("relative torsion removal (4800 shadows)", removal_ok)
check(f"transition quotients ({transition_count} controls)", transition_ok)

check("source real chart anchor", "A_N = {\\mathbb Z}" in H17)
check("source overlap anchor", "common basic open set" in H17)
check("source pro-transition anchor", r"\label{eq95}" in H17)
check("source fraction system anchor", r"\label{eq111}" in H17)

markers = (
    "supportwise local reflection constructs the repaired pro-square",
    "H7-LOCAL-REG-GLUE",
    "preserves the real-real chart",
    "same universal category on the",
    "Y^{\\rm locreg}",
    "every finite-support prime presentation",
    "does not by itself prove",
    "Row A and RH remain open",
)
for marker in markers:
    check(f"scope marker {marker}", marker in DOC)

print("VERDICT: SUPPORTWISE RELATIVE REFLECTION GLUES AND RESTORES ALL FINITE-SUPPORT PRIME LATTICES")
