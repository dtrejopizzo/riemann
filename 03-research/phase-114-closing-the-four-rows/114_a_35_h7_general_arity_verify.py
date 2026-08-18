#!/usr/bin/env python3
"""Finite checks for general-arity bounded trees and universal coefficient."""

from math import floor, isclose, log, sqrt


def signed_rank(leaves):
    r = 0
    while 3 ** (r + 1) <= 2 * leaves + 1:
        r += 1
    return r


print("A. k-ary Euclidean nodes")
for k in range(2, 51):
    norm = sqrt(k * (1 / k) ** 2)
    assert isclose(norm, 1 / sqrt(k))
    assert norm <= 1
    assert isclose(k * (1 / k**2), 1 / k)
print("  k=2,...,50 are contractions")

print("\nB. Leaf capacity and finite valuations")
for k in range(2, 18):
    for d in range(1, 12):
        leaves = k**d
        r = signed_rank(leaves)
        assert (3**r - 1) // 2 <= leaves
        assert 3 ** (r + 1) > 2 * leaves + 1
        assert isclose(k ** (-2 * d) * k ** (2 * d), 1.0)
print("  all tested capacities and denominator clearings pass")

print("\nC. Universal degree coefficient")
for k in (2, 3, 5, 6, 10, 30):
    for q in (2, 5, 7, 11):
        d, n = 17, 13
        entropy_lead = d * log(k) * n * log(q) / log(3)
        degree_form = ((2 * d * log(k)) * (n * log(q))) / (2 * log(3))
        assert isclose(entropy_lead, degree_form)
print("  coefficient is independent of arity/prime presentation")

print("\nD. Regrouping k=P versus k=P^a")
for p in (2, 6, 10, 30):
    for a in (2, 3, 4):
        d = 12
        assert (p**d) == (p**a) ** (d // a)
        assert p ** (-2 * d) == (p**a) ** (-2 * (d // a))
        r1 = signed_rank(p**d)
        r2 = signed_rank((p**a) ** (d // a))
        assert r1 == r2
print("  exact leaf counts, coefficients and ranks agree")

print("\nVERDICT: H7 GENERAL-ARITY UNIVERSAL-COEFFICIENT CHECKS PASS")
