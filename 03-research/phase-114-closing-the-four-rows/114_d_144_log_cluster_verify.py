#!/usr/bin/env python3
"""Numerical log-cluster certificates illustrating the theorem in D.144."""

from __future__ import annotations

import math
import numpy as np


# For the normalized Gaussian h, translation covariance is
# <U_a h,U_b h> = exp(-(a-b)^2/4).  Consecutive log blocks therefore become
# nearly rank one and their top Gram eigenvalue grows like the block size.
for r in (4, 8, 16, 32, 64):
    n0 = 10 ** 8
    times = np.log(np.arange(n0, n0 + r, dtype=float))
    delta = times[:, None] - times[None, :]
    gram = np.exp(-(delta**2) / 4.0)
    eigmax = np.linalg.eigvalsh(gram)[-1]
    assert eigmax > 0.999999 * r

# The normalized equal-coefficient synthesis vector has norm squared equal
# to the Rayleigh quotient of the all-ones vector and grows linearly.
rayleigh = []
for r in (10, 20, 40, 80):
    n0 = 10 ** 9
    times = np.log(np.arange(n0, n0 + r, dtype=float))
    delta = times[:, None] - times[None, :]
    gram = np.exp(-(delta**2) / 4.0)
    ones = np.ones(r) / math.sqrt(r)
    value = float(ones @ gram @ ones)
    rayleigh.append(value)
    assert value > 0.999999 * r

assert all(a < b for a, b in zip(rayleigh, rayleigh[1:]))

print("D144 log-cluster intertwiner certificates: PASS")
print("equal-block Rayleigh values:", rayleigh)
