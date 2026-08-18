#!/usr/bin/env python3
"""Finite-measure checks for the Cauchy defect identity in D.140."""

from __future__ import annotations

import numpy as np

rng = np.random.default_rng(140)

for size in (7, 23, 101):
    tau = np.sort(rng.normal(size=size))
    mass = rng.random(size=size) + 0.05
    nrm = mass.sum()
    for alpha in (0.4 + 0.2j, -1.3 + 0.7j, 2.0 - 0.45j):
        b = alpha.imag
        uhat = -1j / (tau + alpha)
        z = np.sum(mass * uhat)
        j = np.sum(mass * np.abs(uhat) ** 2)

        # Re z = -Im(alpha) J.
        assert abs(z.real + b * j) < 2e-12 * max(1.0, j)

        # Strict Cauchy variance.
        variance = nrm * j - abs(z) ** 2
        assert variance > 1e-10

        # Defect from the eigen-equation Du + alpha u = -i k.
        du_k = -alpha * z - 1j * nrm
        defect_direct = (
            -du_k * np.conj(z) + z * np.conj(du_k)
        ) / nrm
        defect_formula = 2j * b * (abs(z) ** 2 - nrm * j) / nrm
        assert abs(defect_direct - defect_formula) < 3e-11

# For real alpha, a symmetric discrete measure and a removable zero model
# make z purely imaginary, so the diagonal defect vanishes.
tau = np.array([-3.0, -1.0, 1.0, 3.0])
mass = np.array([0.2, 1.1, 1.1, 0.2])
alpha = 0.0
z = np.sum(mass * (-1j / (tau + alpha)))
assert abs(z.real) < 1e-14

print("D140 theta Cauchy-defect certificates: PASS")
