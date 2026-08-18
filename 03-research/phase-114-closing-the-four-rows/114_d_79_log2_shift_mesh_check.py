#!/usr/bin/env python3
"""Exact combinatorial check of the two-contact mesh at T=log(2).

Endpoints are represented in the free Q-vector space on log(2), log(3),
so no floating comparison enters the shift identities.
"""
from fractions import Fraction as Q


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


L2, L3 = (Q(1), Q(0)), (Q(0), Q(1))
endpoints = [
    (Q(-1), Q(0)),       # -log 2
    (Q(1), Q(-1)),       # log 2-log 3
    (Q(-2), Q(1)),       # log 3-2 log 2
    (Q(0), Q(0)),
    (Q(2), Q(-1)),       # 2 log 2-log 3
    (Q(-1), Q(1)),       # log 3-log 2
    (Q(1), Q(0)),
]

# Translation of whole macro intervals, with the source and target indices.
claims = [
    (0, 3, L2),
    (1, 4, L2),
    (2, 5, L2),
    (0, 5, L3),
]
for source, target, shift in claims:
    assert add(endpoints[source], shift) == endpoints[target]
    assert add(endpoints[source + 1], shift) == endpoints[target + 1]

# The six lengths are d,e,d,d,e,d in the same exact vector space.
lengths = [
    (endpoints[j + 1][0] - endpoints[j][0],
     endpoints[j + 1][1] - endpoints[j][1])
    for j in range(6)
]
d, e = (Q(2), Q(-1)), (Q(-3), Q(2))
assert lengths == [d, e, d, d, e, d]

# Equal subdivisions on macros of equal type inherit every identity above.
counts = [20, 8, 20, 20, 8, 20]
for source, target, _ in claims:
    assert counts[source] == counts[target]

print("PASS exact log(2)/log(3) macro-shift mesh")
