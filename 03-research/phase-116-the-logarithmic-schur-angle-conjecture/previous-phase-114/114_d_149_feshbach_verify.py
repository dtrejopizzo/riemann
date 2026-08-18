#!/usr/bin/env python3
"""Finite-dimensional checks of the D.149 primitive/Feshbach identities."""

from __future__ import annotations

import numpy as np


rng = np.random.default_rng(149)
h = 31
n = 11

# Two independent Tate rows and their exact Euclidean projector.
M = rng.normal(size=(2, h))
GM = M @ M.T
P0 = np.eye(h) - M.T @ np.linalg.inv(GM) @ M
assert np.linalg.norm(P0 @ P0 - P0) < 1e-12

# L is the first n coordinate modes.  V=L cap ker(M), W=P0 L.
Phi = np.eye(h)[:, :n]
J = M @ Phi
_, _, vh = np.linalg.svd(J)
V = Phi @ vh[2:].T
S = P0 @ Phi
G = S.T @ S
assert np.linalg.matrix_rank(V) == n - 2
assert np.linalg.matrix_rank(S) == n
assert np.linalg.eigvalsh(G)[0] > 0

# Orthogonal complement of W inside ker M equals ker M cap L^perp.
_, _, vh0 = np.linalg.svd(M)
H0 = vh0[2:].T
PW = S @ np.linalg.inv(G) @ S.T
Q0 = P0 - PW
assert np.linalg.norm(Q0 @ Phi) < 1e-11
assert np.linalg.norm(M @ Q0) < 1e-11

# The complement of V has a genuine two-dimensional low defect.
PV = V @ np.linalg.inv(V.T @ V) @ V.T
defect = P0 - PV
low_defect = Phi.T @ defect
assert np.linalg.matrix_rank(low_defect, tol=1e-10) == 2

# Feshbach identity and sufficiency.  Build A with a strictly positive
# complement, while allowing a nonzero finite/complement coupling.
qvals, Qbasis_e = np.linalg.eigh(Q0)
Qbasis = Qbasis_e[:, qvals > 0.5]
wvals, Wbasis_e = np.linalg.eigh(PW)
Wbasis = Wbasis_e[:, wvals > 0.5]
delta = 1.7
C = 0.08 * rng.normal(size=(Wbasis.shape[1], Qbasis.shape[1]))
Borth = 2.4 * np.eye(Wbasis.shape[1])
A0 = (
    Wbasis @ Borth @ Wbasis.T
    + Qbasis @ (delta * np.eye(Qbasis.shape[1])) @ Qbasis.T
    + Wbasis @ C @ Qbasis.T
    + Qbasis @ C.T @ Wbasis.T
)
A = P0 @ A0 @ P0
B = S.T @ A @ S
R = S.T @ A @ Q0 @ A @ S
Rformula = S.T @ A @ A @ S - B @ np.linalg.inv(G) @ B
assert np.linalg.norm(R - Rformula) < 1e-10
assert np.linalg.eigvalsh(R)[0] > -1e-11

certificate = B - R / delta
assert np.linalg.eigvalsh(certificate)[0] > 0
assert np.linalg.eigvalsh(H0.T @ A @ H0)[0] > 0

print("D149 primitive defect and Feshbach certificate: PASS")
