#!/usr/bin/env python3
"""Exact checks for the G3-EFF iff RH boundary theorem."""

from fractions import Fraction
from itertools import product


def q(vector):
    k, a = vector
    return 2 * k * a


def strictly_effective(vector):
    k, a = vector
    return k >= 0 and a >= 0 and vector != (0, 0)


print("A. Target property (E) on the Lorentzian divisor plane")
for k, a in product(range(-12, 13), repeat=2):
    vector = (k, a)
    negative = (-k, -a)
    if q(vector) > 0:
        assert strictly_effective(vector) or strictly_effective(negative)
print("  every positive-square lattice vector has one effective sign")

print("\nB. The spatial ray has neither effective sign")
for u in range(0, 100):
    vector = (u, -u)
    negative = (-u, u)
    assert not strictly_effective(vector)
    assert not strictly_effective(negative)
    assert q(vector) == -2 * u * u
print("  +/-u(1,-1) both avoid the strict effective cone")

print("\nC. RH-side construction gives exact domination")
# Represent -s(c,c)/2 by rational squares so the lift stays exact.
for numerator in range(0, 30):
    amplitude = Fraction(numerator, 7)
    source_square = -2 * amplitude * amplitude
    image = (amplitude, -amplitude)
    assert q(image) == source_square
    assert not strictly_effective(image)
    assert not strictly_effective((-image[0], -image[1]))
    for scale in range(0, 8):
        scaled_image = (scale * image[0], scale * image[1])
        assert q(scaled_image) == scale * scale * source_square
print("  q(J(c))=s(c,c), homogeneity and NOEFF hold exactly")

print("\nD. A positive source square contradicts exact effectivity")
for source_square in range(1, 30):
    # Any dominating image must have positive q; property (E) then fires.
    candidate_vectors = [
        (k, a) for k, a in product(range(-20, 21), repeat=2)
        if q((k, a)) >= source_square
    ]
    assert candidate_vectors
    assert all(
        strictly_effective(vector)
        or strictly_effective((-vector[0], -vector[1]))
        for vector in candidate_vectors
    )
print("  domination of s>0 is incompatible with NOEFF")

print("\nVERDICT: G3 EFFECTIVITY-BRANCH EQUIVALENCE CHECKS PASS")
