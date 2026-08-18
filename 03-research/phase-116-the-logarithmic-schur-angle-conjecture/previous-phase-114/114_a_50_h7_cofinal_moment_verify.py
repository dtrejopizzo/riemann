#!/usr/bin/env python3
"""Checks for the compatible cofinal finite-moment system of a_50."""

from fractions import Fraction
from itertools import product
from math import log

from sympy import nextprime


Q_PRIME = 3


def rank(t):
    return int(log(2 ** (t + 1) + 1, 3))


levels = []
modulus = 1
for j in range(6):
    T = 2**j
    r = rank(T)
    H = max(Q_PRIME**T, 3**r)
    ell = int(nextprime(H))
    modulus *= ell
    levels.append((T, r, ell, modulus))


def residue(x: Fraction, modulus: int) -> int:
    return x.numerator * pow(x.denominator, -1, modulus) % modulus


def moments(terms, count, modulus):
    out = []
    for s in range(count):
        total = 0
        for coefficient, label in terms:
            total += coefficient * pow(residue(label, modulus), s, modulus)
        out.append(total % modulus)
    return tuple(out)


print("A. Nested cofinal moduli")
previous = 1
previous_ell = 1
for T, r, ell, M in levels:
    assert ell > max(Q_PRIME**T, 3**r)
    assert ell > previous_ell
    assert M % previous == 0
    assert M % Q_PRIME != 0
    previous = M
    previous_ell = ell
print("  M_j divides M_{j+1}; all ray denominators remain units")

print("\nB. Exact transition compatibility")
terms = (
    (7, Fraction(1, 3)),
    (-4, Fraction(5, 9)),
    (11, Fraction(8, 27)),
)
for i in range(len(levels)):
    Ti, ri, _, Mi = levels[i]
    low = moments(terms, 2 * ri, Mi)
    for j in range(i, len(levels)):
        _, rj, _, Mj = levels[j]
        high = moments(terms, 2 * rj, Mj)
        assert tuple(x % Mi for x in high[: 2 * ri]) == low
print("  reduction plus truncation commutes with every tested moment")

print("\nC. Exhaustive balanced-code separation at small levels")
for t in (1, 2):
    r = rank(t)
    Q = Q_PRIME**t
    j = next(k for k, (T, _, _, _) in enumerate(levels) if T >= t)
    M = levels[j][3]
    images = set()
    count = 0
    for c in product(range(-Q, Q + 1), repeat=r):
        if sum(abs(x) for x in c) > Q:
            continue
        terms_c = tuple(
            (3**position * (1 if value > 0 else -1), Fraction(abs(value), Q))
            for position, value in enumerate(c)
            if value
        )
        image = moments(terms_c, 2 * r, M)
        assert image not in images
        images.add(image)
        count += 1
    assert len(images) == count
print("  every code has a distinct compatible moment vector")

print("\nD. Cofinal quadratic target bound")
ratios = []
for T, r, _, M in levels:
    if r:
        ratios.append(2 * r * log(M) / (T * T))
assert max(ratios) < 20
assert ratios[-1] < 8
print("  log target / T^2 stays uniformly bounded on tested levels")

print("\nVERDICT: H7 COFINAL PROFINITE-MOMENT CHECKS PASS")
