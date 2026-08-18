#!/usr/bin/env python3
"""Matrix certificate for the D.186 common-killing congruence."""

import numpy as np

rng = np.random.default_rng(186)
n = 15
X = rng.normal(size=(n, n))
R = X.T @ X + 2.0 * np.eye(n)
U = rng.normal(size=(n, n))
Qbasis, _ = np.linalg.qr(U)
qvals = np.linspace(-0.7, 1.3, n)
Q = (Qbasis * qvals) @ Qbasis.T
L = R - Q

for scale in (0.0, 1.0, 100.0, 1e5):
    P = scale * np.eye(n)
    A = R + P
    ev, V = np.linalg.eigh(A)
    Aim = (V * (1.0 / np.sqrt(ev))) @ V.T
    T = Aim @ (L + P) @ Aim
    D = np.eye(n) - T
    congr = Aim @ Q @ Aim
    assert np.linalg.norm(D - congr, 2) < 2e-10
    # Q has a negative direction, hence T has an eigenvalue above one for
    # every common killing scale, although the excess tends to zero.
    assert np.linalg.eigvalsh(T)[-1] > 1.0

excess_small = np.linalg.eigvalsh(
    np.linalg.inv(np.linalg.cholesky(R + 1e5 * np.eye(n)))
    @ (L + 1e5 * np.eye(n))
    @ np.linalg.inv(np.linalg.cholesky(R + 1e5 * np.eye(n))).T
)[-1] - 1.0

print("large-killing eigenvalue excess is positive =", excess_small)
print("D186 common killing does not prove sign: PASS")

