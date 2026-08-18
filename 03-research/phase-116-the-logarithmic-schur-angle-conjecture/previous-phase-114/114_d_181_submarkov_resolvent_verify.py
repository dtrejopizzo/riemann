#!/usr/bin/env python3
"""Finite-dimensional certificates for D.181.

Checks the exact semigroup Green decomposition, sub-Markov row/column
bounds, the prolate/min-max low-rank estimate, and the rank-two constrained
Green formula for two Tate moments.
"""

import numpy as np

rng = np.random.default_rng(181)
n = 54

# A symmetric killed jump generator: graph Laplacian (several jump lengths)
# plus exterior killing.  This is the finite-cell analogue of Gamma plus
# every antisymmetric prime-power reference channel.
R = np.zeros((n, n))
for jump, weight in [(1, 1.0), (2, 0.37), (5, 0.19), (11, 0.08)]:
    for i in range(n - jump):
        j = i + jump
        R[i, i] += weight
        R[j, j] += weight
        R[i, j] -= weight
        R[j, i] -= weight
R += np.diag(0.11 + 0.13 * (np.linspace(-1, 1, n) ** 2))

evals, U = np.linalg.eigh(R)
assert evals[0] > 0
G = (U * (1.0 / evals)) @ U.T

a = float(np.quantile(evals, 0.24))
L = 1.0 / a
Sa = (U * np.exp(-L * evals)) @ U.T
K = (U * ((1.0 - np.exp(-L * evals)) / evals)) @ U.T
H = (U * (np.exp(-L * evals) / evals)) @ U.T
assert np.linalg.norm(G - K - H, 2) < 2e-11

# The killed semigroup and its time integral are nonnegative/sub-Markov.
assert Sa.min() > -2e-13
assert np.max(Sa.sum(axis=0)) <= 1.0 + 2e-12
assert np.max(Sa.sum(axis=1)) <= 1.0 + 2e-12
assert K.min() > -2e-12
assert np.max(K.sum(axis=0)) <= L + 2e-11
assert np.max(K.sum(axis=1)) <= L + 2e-11

lo = evals < a
hi = ~lo
Hlo = (U[:, lo] * (np.exp(-L * evals[lo]) / evals[lo])) @ U[:, lo].T
Hhi = (U[:, hi] * (np.exp(-L * evals[hi]) / evals[hi])) @ U[:, hi].T
assert np.linalg.norm(H - Hlo - Hhi, 2) < 2e-11
assert np.linalg.norm(Hhi, 2) <= np.exp(-1.0) / a + 2e-12
assert np.linalg.matrix_rank(Hlo, tol=2e-9) <= int(np.sum(lo))

# Two exact Tate moments and the constrained inverse formula.
x = np.linspace(-1.0, 1.0, n)
M = np.vstack([np.ones(n), np.exp(0.5 * x)])
_, _, vh = np.linalg.svd(M, full_matrices=True)
Q = vh[2:].T  # columns span ker M
G_direct = Q @ np.linalg.inv(Q.T @ R @ Q) @ Q.T
MGMT = M @ G @ M.T
G_formula = G - G @ M.T @ np.linalg.inv(MGMT) @ M @ G
assert np.linalg.norm(G_direct - G_formula, 2) < 3e-10
Tate_corr = G - G_formula
assert np.linalg.matrix_rank(Tate_corr, tol=2e-9) <= 2
assert np.linalg.norm(M @ G_formula, 2) < 2e-10

# Independent min-max certificate for the prolate low-rank argument.
n2 = 46
W, _ = np.linalg.qr(rng.normal(size=(n2, n2)))
cvals = np.linspace(0.015, 0.985, n2)
C = (W * cvals) @ W.T
eta = 0.71
hR = 3.2
Plo_vecs = W[:, cvals > eta]
rank_plo = Plo_vecs.shape[1]
J = rng.normal(size=(18, n2))
R2 = hR * (np.eye(n2) - C) + J.T @ J / (9.0 * n2)
a2 = (1.0 - eta) * hR
rank_low_R2 = int(np.sum(np.linalg.eigvalsh(R2) < a2 - 2e-11))
assert rank_low_R2 <= rank_plo

print("sub-Markov K row/column mass =", np.max(K.sum(axis=1)), L)
print("low spectral rank / prolate allowance =", rank_low_R2, rank_plo)
print("Tate correction rank =", np.linalg.matrix_rank(Tate_corr, tol=2e-9))
print("D181 sub-Markov resolvent and Tate rank two: PASS")
