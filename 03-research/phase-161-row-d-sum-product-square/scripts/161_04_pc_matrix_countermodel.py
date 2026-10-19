#!/usr/bin/env python3
"""Verify the 2x2 countermodel in R161_038."""

import numpy as np


X = np.array([[1.0, 0.0], [0.0, -1.0]])
J = np.array([[0.0, 1.0], [1.0, 0.0]])
F = J.copy()
S = np.array([[0.0, 1.0], [0.0, 0.0]])
L = np.zeros((2, 2))
I = np.eye(2)

M = X + F @ X @ F
A = M - (L + L.T)
K = -(X @ S - S @ X)
E = S @ F - J @ S
H = L @ S - K

pc_left = S @ A @ F
pc_right = X @ E + E @ X - L.T @ E - J @ H - H @ F
mean_left = S @ M @ F
mean_right = J @ K + K @ F + X @ E + E @ X
U = K @ F
V = J @ K

assert np.allclose(J @ J, I)
assert np.allclose(F @ F, I)
assert np.allclose(M, 0)
assert np.allclose(A, 0)
assert np.allclose(pc_left, pc_right)
assert np.allclose(pc_left, 0)
assert np.allclose(mean_left, mean_right)
assert np.allclose(U - V, -2 * X)
assert np.allclose((U - V).T @ (U - V) / 4, I)

print("PC residual:", np.linalg.norm(pc_left - pc_right))
print("mean residual:", np.linalg.norm(mean_left - mean_right))
print("coherent-square matrix:\n", (U - V).T @ (U - V) / 4)
