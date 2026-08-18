#!/usr/bin/env python3
"""Finite models for the weighted Mellin/graph gate D.192."""

from __future__ import annotations

import numpy as np


def main() -> None:
    # Adjoint/inverse gate for diagonal central scaling.
    sigma = np.array([0.31, 0.50, 0.68, 0.50])
    tau = np.array([2.0, -1.0, 3.2, 7.0])
    s = sigma + 1j * tau
    u = 0.73
    scale = np.diag(np.exp(u * (s - 0.5)))
    inverse = np.diag(np.exp(-u * (s - 0.5)))
    adjoint = scale.conj().T
    residual = np.abs(np.diag(adjoint - inverse))
    assert residual[1] < 1e-12 and residual[3] < 1e-12
    assert residual[0] > 1e-3 and residual[2] > 1e-3

    # A graph weight can make multiplication an onto isometry, hence its
    # Hilbert cokernel is zero.  Without the weight, inverse norms diverge.
    n = 80
    xi = np.exp(-np.linspace(0.0, 8.0, n))
    z = np.diag(xi)
    inverse_norm = np.linalg.norm(np.linalg.inv(z), 2)
    assert inverse_norm > 2.9e3
    # Source norm matrix W_+=|Xi|^2 W_- with W_-=I.
    w_plus = np.diag(xi**2)
    gram_pullback = z.conj().T @ z
    assert np.linalg.norm(gram_pullback - w_plus) < 1e-13
    assert np.linalg.matrix_rank(z) == n  # onto at every finite section

    # Finite model-space spectral points: adjoint kernels are eigenvectors.
    rho = np.array([0.5 + 14.0j, 0.63 + 21.0j, 0.41 + 32.0j])
    for time in (0.2, 1.0, 2.5):
        eig_pos = np.exp(time * (rho.real - 0.5))
        eig_neg = np.exp(-time * (rho.real - 0.5))
        two_sided = np.maximum(eig_pos, eig_neg)
        bound = np.exp(time * np.abs(rho.real - 0.5))
        assert np.linalg.norm(two_sided - bound, np.inf) < 1e-13
        assert abs(two_sided[0] - 1.0) < 1e-13
        assert two_sided[1] > 1.0 and two_sided[2] > 1.0

    print("D192 weighted Mellin/graph Hilbertization gate: PASS")
    print(f"critical adjoint residuals = {residual.tolist()}")
    print(f"unweighted inverse norm    = {inverse_norm:.6e}")
    print(f"two-sided growth at u=2.5 = {np.exp(2.5*np.abs(rho.real-0.5)).tolist()}")


if __name__ == "__main__":
    main()
