#!/usr/bin/env python3
"""Finite checks for a33; H7-FMD descent is deliberately not asserted."""

from itertools import product
from math import comb, log
from sympy import nextprime


def l1_ball(r, q):
    return [v for v in product(range(-q, q + 1), repeat=r)
            if sum(abs(x) for x in v) <= q]


def moments(v, q, ell):
    inv_q = pow(q, -1, ell)
    return tuple(sum((3**j) * (1 if x > 0 else -1) *
                     pow((abs(x) * inv_q) % ell, s, ell)
                     for j, x in enumerate(v) if x) % ell
                 for s in range(1, 2 * len(v) + 1))


print("A. Exhaustive finite-moment injectivity")
for r, q in ((1, 3), (2, 3), (2, 5), (3, 3), (3, 4)):
    ell = int(nextprime(max(q, 3**r)))
    ball = l1_ball(r, q)
    images = {moments(v, q, ell) for v in ball}
    assert len(images) == len(ball)
    exact = sum(2**j * comb(r, j) * comb(q, j)
                for j in range(min(r, q) + 1))
    assert len(ball) == exact
    assert len(images) <= ell ** (2 * r)
    print(f"  r={r}, Q={q}, ell={ell}: {len(ball)} distinct codes")

print("\nB. Vandermonde determinants are nonzero modulo ell")
for r, q in ((2, 5), (3, 7), (4, 9)):
    ell = int(nextprime(max(q, 3**r)))
    inv_q = pow(q, -1, ell)
    xs = [(a * inv_q) % ell for a in range(1, min(q, 2 * r) + 1)]
    determinant = 1
    for x in xs:
        determinant = determinant * x % ell
    for i, x in enumerate(xs):
        for y in xs[i + 1:]:
            determinant = determinant * (y - x) % ell
    assert determinant != 0
print("  all sampled determinants nonzero")

print("\nC. Quadratic ray bounds")
q = 5
for d in (8, 16, 32, 64):
    n = d
    r = int(log(2 ** (d + 1) + 1, 3))
    ell = int(nextprime(max(q**n, 3**r)))
    upper = 2 * r * log(ell)
    lower_lead = r * n * log(q)
    assert upper >= lower_lead
    assert upper / (d * n) < 10
print("  finite-image log upper is O(d*n) on n=d")

print("\nVERDICT: H7 FINITE-MOMENT CHECKS PASS (DESCENT PROVED SEPARATELY IN a49)")
