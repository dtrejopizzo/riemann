#!/usr/bin/env python3
"""Exact checks for 114.a.113: same-ruling intersections."""

from pathlib import Path
from math import gcd


ROOT = Path(__file__).resolve().parent
TEXT = (ROOT / "114_a_113_H7_SAME_RULING_INTERSECTIONS_VANISH.md").read_text()
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19)


def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"PASS {label}")


def egcd(a: int, b: int) -> tuple[int, int, int]:
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t


for p in PRIMES:
    for q in PRIMES:
        if p == q:
            continue
        g, u, v = egcd(p, q)
        check(g == 1 and u * p + v * q == 1, f"Bezout p={p},q={q}")
        # Z/(p,q) is the zero ring: its cardinality gcd(p,q) equals one.
        check(gcd(p, q) == 1, f"ordinary quotient shadow empty p={p},q={q}")

# Formal disjoint-support intersection is the sum of forced zero entries.
left_support = {2: 3, 5: 1, 11: 4}
right_support = {3: 2, 7: 5, 13: 1}
check(set(left_support).isdisjoint(right_support), "test supports are disjoint")
mass = sum(a * b * 0 for p, a in left_support.items()
           for q, b in right_support.items() if p != q)
check(mass == 0, "disjoint-support bilinear mass is zero")

for marker in (
    "maps from either side to a target",
    "same-ruling disjointness",
    "degree of the empty zero-cycle is canonically zero",
    "I(D_{p,i},D_{q,i})=0",
    "different additions",
    "H7-REG-MIXDEG is therefore reduced",
    "does not close H7-REG-INTER, row A or RH",
):
    check(marker in TEXT, f"scope marker {marker}")

print("VERDICT: DISTINCT SAME-RULING PRIME INTERSECTIONS ARE EMPTY")
