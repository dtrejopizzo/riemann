#!/usr/bin/env python3
"""Certificates for the Lorentzian Szego tower construction."""

from fractions import Fraction
import math

import numpy as np
from sympy import primerange


bound = (
    Fraction(1, 3)
    + Fraction(1, 8)
    + Fraction(1, 24)
    + Fraction(1, 48)
    + Fraction(1, 2) * (Fraction(1, 10) + Fraction(1, 11))
)
assert bound == Fraction(1627, 2640)
assert bound < 1
print(f"PASS: rigorous global tail bound = {bound} < 1")


def gram(labels):
    xs = np.array([1.0 / n for n in labels])
    return np.sqrt((1 - xs[:, None] ** 2) * (1 - xs[None, :] ** 2)) / (
        1 - xs[:, None] * xs[None, :]
    )


primes = list(primerange(2, 50))
for prime_count, depth in [(2, 2), (3, 4), (5, 5), (10, 5)]:
    labels = [p**k for p in primes[:prime_count] for k in range(1, depth + 1)]
    q = gram(labels) - np.eye(len(labels))
    eig = np.linalg.eigvalsh(q)
    tolerance = 1e-10
    inertia = (
        int(np.sum(eig > tolerance)),
        int(np.sum(np.abs(eig) <= tolerance)),
        int(np.sum(eig < -tolerance)),
    )
    assert inertia == (1, 0, len(labels) - 1)
    print(
        "PASS:",
        f"{prime_count} primes x depth {depth}",
        f"has inertia {inertia}",
        f"and primitive theoretical gap >= {float(1-bound):.6f}",
    )

    xs = np.array([1.0 / n for n in labels])
    a = np.sqrt(1 - xs**2)
    c = gram(labels)
    tail = c - np.outer(a, a)
    diagonal_block = tail - np.eye(len(labels))
    cross_block = np.outer(a, a)
    doubled = np.block(
        [[diagonal_block, cross_block], [cross_block, diagonal_block]]
    )
    doubled_eig = np.linalg.eigvalsh(doubled)
    doubled_inertia = (
        int(np.sum(doubled_eig > tolerance)),
        int(np.sum(np.abs(doubled_eig) <= tolerance)),
        int(np.sum(doubled_eig < -tolerance)),
    )
    assert doubled_inertia == (1, 0, 2 * len(labels) - 1)
    print("PASS:", f"Tate double has inertia {doubled_inertia}")
