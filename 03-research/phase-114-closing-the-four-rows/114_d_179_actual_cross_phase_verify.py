#!/usr/bin/env python3
"""Verify actual-cross cancellation at the balanced Hadamard phase."""

from __future__ import annotations

import numpy as np


for eps in np.logspace(-12, -2, 30):
    c = -eps / (2.0 - eps)
    r = 1.0 - c
    l = 1.0 + c
    d = (r - l) / r
    g = r - l
    assert abs(d - eps) < 2e-14
    actual_capacity = g * g / d
    arbitrary_capacity = (eps ** 0.25) ** 2 / d
    assert actual_capacity < 1.1 * eps
    assert arbitrary_capacity > eps ** (-0.49) * 0.9

# Commuting direct sum: q=g*h is automatically defect-divisible.
rng = np.random.default_rng(179)
r = rng.uniform(0.8, 2.0, 12)
d = rng.uniform(1e-6, 0.9, 12)
g = r * d
h = rng.normal(size=12)
q = g * h
assert np.allclose(np.sum(q * q / d), np.sum(r * g * h * h))

# A positive old corner alone does not control a noncommuting/off-diagonal
# block: the cross may be much larger than its corner defect.
for eps in (1e-4, 1e-8, 1e-12):
    G00 = eps
    G0E = eps ** 0.25
    assert G0E * G0E / G00 > eps ** (-0.49) * 0.9

print("D179 actual-cross phase divisibility: PASS")
