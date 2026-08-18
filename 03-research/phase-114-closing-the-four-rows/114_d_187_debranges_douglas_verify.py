#!/usr/bin/env python3
"""Finite certificates for the D.187 Schur/Douglas equivalence.

The script checks only algebraic identities and elementary polynomial
Hermite--Biehler witnesses.  It does not assume RH.
"""

from __future__ import annotations

import numpy as np


rng = np.random.default_rng(187)


def psqrt(a):
    d, u = np.linalg.eigh((a + a.conj().T) / 2)
    return (u * np.sqrt(np.maximum(d, 0))) @ u.conj().T


# 1. A positive block is exactly its Douglas square plus a positive Schur
# remainder.
n, r = 11, 4
z = rng.normal(size=(n, n))
A = z.T @ z + 0.7 * np.eye(n)
C = rng.normal(size=(n, r)) * 0.08
S = rng.normal(size=(r, r))
S = S.T @ S + 0.3 * np.eye(r)
Ah = psqrt(A)
X = Ah @ C
B = C.T @ C + S
M = np.block([[A, X], [X.T, B]])
assert np.linalg.eigvalsh(M).min() > 0
schur = B - X.T @ np.linalg.solve(A, X)
assert np.linalg.norm(schur - S, 2) < 2e-12


# 2. Large common killing changes conditioning but preserves the inertia of
# the normalized defect.
qvals = np.linspace(-0.4, 1.2, n)
u, _ = np.linalg.qr(rng.normal(size=(n, n)))
Q = (u * qvals) @ u.T
R = rng.normal(size=(n, n))
R = R.T @ R + 3 * np.eye(n)
L = R - Q
inertia_Q = np.sign(np.linalg.eigvalsh(Q))
for lam in (0.0, 10.0, 1e5):
    RP = R + lam * np.eye(n)
    d, v = np.linalg.eigh(RP)
    Rmih = (v * (1 / np.sqrt(d))) @ v.T
    defect = np.eye(n) - Rmih @ (L + lam * np.eye(n)) @ Rmih
    congr = Rmih @ Q @ Rmih
    assert np.linalg.norm(defect - congr, 2) < 2e-10
    assert np.count_nonzero(np.linalg.eigvalsh(defect) < 0) == np.count_nonzero(
        inertia_Q < 0
    )


# 3. Real zeros give the elementary shifted Hermite--Biehler inequality;
# an off-real zero creates an upper-half-plane zero for shifts below its
# height.
gamma = 7.0


def xi_real(z):
    return 1 - z * z / gamma**2


for a in (0.1, 0.4, 1.0):
    for zc in (0.3 + 0.2j, 2.0 + 1.4j, -1.0 + 3.0j):
        E = xi_real(zc + 1j * a)
        Esharp = xi_real(zc - 1j * a)
        assert abs(E) > abs(Esharp)

x, y, a = 2.0, 0.3, 0.1


def xi_off(z):
    return ((z - x) ** 2 + y**2) * ((z + x) ** 2 + y**2)


upper_zero_of_shift = x + 1j * (y - a)
assert upper_zero_of_shift.imag > 0
assert abs(xi_off(upper_zero_of_shift + 1j * a)) < 1e-12


print("D187 de Branges/Douglas low-block equivalence: PASS")
