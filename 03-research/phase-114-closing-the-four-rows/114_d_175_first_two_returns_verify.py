#!/usr/bin/env python3
"""Verify the exact first-two-return cancellation of D.175."""

from __future__ import annotations

import numpy as np


rng = np.random.default_rng(175)
ns, no, nb, nr = 7, 9, 3, 11

# Reference feature with full source rank.
X0 = rng.normal(size=(nr, ns))
R = X0.T @ X0 + 0.7 * np.eye(ns)
re, rv = np.linalg.eigh(R)
Rhalf = (rv * np.sqrt(re)) @ rv.T
Rinvhalf = (rv * (1.0 / np.sqrt(re))) @ rv.T

# Build an old load with T<1 in normalized source coordinates.
U, _ = np.linalg.qr(rng.normal(size=(no, ns)))
V, _ = np.linalg.qr(rng.normal(size=(ns, ns)))
sing = np.linspace(0.16, 0.86, ns)
A = U @ np.diag(sing) @ V.T
Y0 = A @ Rhalf
T = Rinvhalf @ (Y0.T @ Y0) @ Rinvhalf
T = (T + T.T) / 2
D = np.eye(ns) - T
assert np.linalg.eigvalsh(D)[0] > 0

# Born reference/load crosses.  It is enough to prescribe r and l; choose
# compatible X_E,Y_E through least squares and add harmless orthogonal parts.
r = rng.normal(size=(ns, nb))
l = rng.normal(size=(ns, nb))
H = np.linalg.solve(R, r)
S0 = rng.normal(size=(nb, nb))
S = S0.T @ S0 + np.eye(nb)
Shalf_inv = np.linalg.inv(np.linalg.cholesky(S)).T

# Direct normalized vectors from the algebraic definitions.
b = (l - (Y0.T @ Y0) @ H) @ Shalf_inv
u = Rinvhalf @ b
h = Rhalf @ H @ Shalf_inv
q = Rinvhalf @ (r - l) @ Shalf_inv
assert np.allclose(u, D @ h - q, atol=2e-12)

c1 = u.T @ u
c2 = u.T @ T @ u
assert np.allclose(c1 - c2, u.T @ D @ u, atol=2e-12)

# Sum returns directly and compare with the defect inverse and expanded form.
series = np.zeros((nb, nb))
power = np.eye(ns)
for _ in range(2000):
    series += u.T @ power @ u
    power = power @ T
closed = u.T @ np.linalg.solve(D, u)
expanded = h.T @ D @ h - h.T @ q - q.T @ h + q.T @ np.linalg.solve(D, q)
factor = (np.linalg.cholesky(D).T @ h
          - np.linalg.solve(np.linalg.cholesky(D), q))
assert np.allclose(series, closed, atol=2e-11)
assert np.allclose(closed, expanded, atol=2e-11)
assert np.allclose(closed, factor.T @ factor, atol=2e-11)

# Consecutive differences are positive matrix Grams.
power = np.eye(ns)
for _ in range(12):
    ck = u.T @ power @ u
    ck1 = u.T @ power @ T @ u
    diff = (ck - ck1 + (ck - ck1).T) / 2
    assert np.linalg.eigvalsh(diff)[0] > -2e-12
    power = power @ T

print("first-return capacity eigenvalues =", np.linalg.eigvalsh(closed))
print("D175 first two return cancellation: PASS")
