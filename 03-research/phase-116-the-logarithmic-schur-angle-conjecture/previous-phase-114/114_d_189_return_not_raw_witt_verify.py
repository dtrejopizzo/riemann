#!/usr/bin/env python3
"""Finite killed-graph certificate for D.189."""

import numpy as np

a, b = 0.8, 0.47
n = 4
R = np.zeros((n, n))
for i in range(n - 1):
    R[i, i] += 1.0
    R[i + 1, i + 1] += 1.0
    R[i, i + 1] -= 1.0
    R[i + 1, i] -= 1.0
R += np.diag([0.31, 0.12, 0.18, 0.27])
G = np.linalg.inv(R)

B = np.array([0.0, a, b, 0.0])
raw = a * a + b * b
weighted = B @ G @ B
diagonal_only = a * a * G[1, 1] + b * b * G[2, 2]

assert G[1, 2] > 0
assert abs(weighted - diagonal_only - 2 * a * b * G[1, 2]) < 2e-13
assert abs(weighted - diagonal_only) > 0.1

# Change only an interior killing coefficient.  Placements/raw Gram remain
# identical while the Green-weighted return changes.
R2 = R.copy()
R2[1, 1] += 0.9
G2 = np.linalg.inv(R2)
weighted2 = B @ G2 @ B
assert abs(weighted2 - weighted) > 0.1
assert raw == a * a + b * b

print("raw, two Green returns =", raw, weighted, weighted2)
print("D189 exact return is not raw Witt Gram: PASS")

