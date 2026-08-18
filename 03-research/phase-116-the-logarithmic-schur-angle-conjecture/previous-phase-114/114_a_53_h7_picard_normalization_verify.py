#!/usr/bin/env python3
"""Checks for Picard normalization and the real-degree code coefficient."""

from itertools import product
from math import exp, floor, log


def standard_representative(lam):
    q = floor(lam)
    return q, lam / q


def rank_and_radius(t, d1, d2):
    depth = floor(t * d1 / (2 * log(2)))
    leaves = 2**depth
    rank = floor(log(2 * leaves + 1, 3))
    radius = floor(exp(t * d2))
    return depth, rank, radius


print("A. Standard Picard representatives")
for lam in (1.01, 1.5, 2.0, 3.7, 11.25, 101.125):
    q, rho = standard_representative(lam)
    assert q >= 1
    assert 1 <= rho < 1 + 1 / q + 1e-14
    assert abs(q * rho - lam) < 1e-12
print("  finite norm times residual metric recovers the class")

print("\nB. Principal presentation independence")
for lam in (2.5, 7.25, 19.75):
    canonical = standard_representative(lam)
    presentations = [(1, lam), (2, lam / 2), (5, lam / 5)]
    for finite, metric in presentations:
        assert abs(finite * metric - lam) < 1e-12
        assert standard_representative(finite * metric) == canonical
print("  all principal redistributions return to one standard representative")

print("\nC. Odd moments are invariant in cardinality under the unit -1")
p = 101
sections = tuple(range(-20, 21))
exponents = (1, 3, 5, 7)
image = {tuple(pow(x % p, s, p) for s in exponents) for x in sections}
negative_image = {
    tuple(pow((-x) % p, s, p) for s in exponents) for x in sections
}
assert image == negative_image
print("  changing transport by +/-1 permutes the finite image")

print("\nD. Residual metric budgets")
for d1, d2, t in product((0.7, 1.3, 2.1), (0.4, 1.1, 1.9), (5, 10, 20)):
    depth, rank, radius = rank_and_radius(t, d1, d2)
    assert 2 * depth * log(2) <= t * d1 + 1e-12
    assert log(radius) <= t * d2 + 1e-12
    assert rank <= log(2 * 2**depth + 1, 3)
print("  finite contractions fit inside every real degree budget")

print("\nE. Continuous quadratic coefficient")
for d1, d2 in ((0.8, 1.2), (1.3, 0.9), (2.0, 1.7)):
    target = d1 * d2 / (2 * log(3))
    approximations = []
    for t in (20, 40, 80, 160):
        _, rank, radius = rank_and_radius(t, d1, d2)
        leading_proxy = rank * log(radius) / (t * t)
        approximations.append(leading_proxy)
    assert abs(approximations[-1] - target) < 0.03
    assert abs(approximations[-1] - target) < abs(approximations[0] - target)
print("  rank*log(radius)/t^2 converges to d1*d2/(2log3)")

print("\nVERDICT: H7 PICARD CODE-NORMALIZATION CHECKS PASS; GLOBAL h_FM RETRACTED IN a57")
