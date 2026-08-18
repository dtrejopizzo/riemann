#!/usr/bin/env python3
"""Verify the return-dissipation/Abel identities of D.176."""

from __future__ import annotations

import numpy as np


rng = np.random.default_rng(176)
n, b = 8, 3
U, _ = np.linalg.qr(rng.normal(size=(n, n)))
lam = np.array([0.91, 0.78, 0.62, 0.43, 0.27, 0.14, 0.06, 0.01])
T = (U * lam) @ U.T
D = np.eye(n) - T
q = rng.normal(size=(n, b)) * 0.15

te, tv = np.linalg.eigh(T)
Thalf = (tv * np.sqrt(np.maximum(te, 0.0))) @ tv.T

m = []
d = []
power = np.eye(n)
for _ in range(500):
    mk = q.T @ power @ q
    dk = q.T @ power @ D @ q
    m.append(mk)
    d.append(dk)
    assert np.allclose(dk, mk - q.T @ power @ T @ q, atol=2e-13)
    assert np.linalg.eigvalsh((dk + dk.T) / 2)[0] > -2e-13
    power = power @ T

# Finite Abel identity, including its tail.
for M in (0, 1, 2, 7, 31, 150):
    lhs = sum(m[: M + 1])
    rhs = sum((k + 1) * d[k] for k in range(M + 1)) + (M + 1) * m[M + 1]
    assert np.allclose(lhs, rhs, atol=3e-12)

closed = q.T @ np.linalg.solve(D, q)
weighted_diss = sum((k + 1) * d[k] for k in range(len(d)))
assert np.allclose(weighted_diss, closed, atol=2e-10)

# Direct half-power version d_k=(T^{k/2}q)^*D(T^{k/2}q).
z = q.copy()
for k in range(20):
    assert np.allclose(d[k], z.T @ D @ z, atol=2e-12)
    z = Thalf @ z

# Kernel component: the Abel tail records the infinite capacity.
Tk = np.diag([1.0, 0.5, 0.2])
Dk = np.eye(3) - Tk
qk = np.array([[1.0], [0.4], [-0.2]])
power = np.eye(3)
mk = []
dk = []
for _ in range(100):
    mk.append(qk.T @ power @ qk)
    dk.append(qk.T @ power @ Dk @ qk)
    power = power @ Tk
assert float(mk[-1][0, 0]) > 0.999999
for M in (2, 20, 80):
    lhs = sum(mk[: M + 1])
    rhs = sum((k + 1) * dk[k] for k in range(M + 1)) + (M + 1) * mk[M + 1]
    assert np.allclose(lhs, rhs, atol=2e-12)
assert (81.0 * float(mk[81][0, 0])) > 80.9

print("return capacity eigenvalues =", np.linalg.eigvalsh(closed))
print("D176 Tate-centered return dissipation: PASS")
