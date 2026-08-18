#!/usr/bin/env python3
"""Finite Lyapunov blocks for D.193."""

from __future__ import annotations

import numpy as np


def lyap_residual(alpha: np.ndarray, w: np.ndarray) -> float:
    a = np.diag(alpha)
    return float(np.linalg.norm(a.conj().T @ w + w @ a))


def main() -> None:
    # Ruling pair and one reflected correspondence pair.
    z = 0.17 + 3.0j
    alpha = np.array([-0.5, 0.5, z, -np.conj(z), 4.0j])
    w = np.zeros((5, 5), dtype=complex)
    w[0, 1] = w[1, 0] = 1.0
    w[2, 3] = 2.0 - 0.3j
    w[3, 2] = np.conj(w[2, 3])
    w[4, 4] = 1.7
    assert lyap_residual(alpha, w) < 1e-12

    ruling_eigs = np.linalg.eigvalsh(w[:2, :2])
    reflected_eigs = np.linalg.eigvalsh(w[2:4, 2:4])
    assert ruling_eigs[0] < 0 < ruling_eigs[1]
    assert reflected_eigs[0] < 0 < reflected_eigs[1]
    assert w[4, 4] > 0  # purely imaginary/critical exponent

    # A PSD matrix with a zero diagonal cannot retain a cross entry.
    for c in (0.2, 1.0, 3.0):
        block = np.array([[0.0, c], [c, 0.0]])
        assert np.linalg.eigvalsh(block)[0] < 0

    # Invariance of a positive diagonal scalar occurs iff Re(alpha)=0.
    u = 0.81
    invariant_error = []
    for a in alpha:
        invariant_error.append(abs(abs(np.exp(u * a)) ** 2 - 1.0))
    assert invariant_error[4] < 1e-12
    assert invariant_error[0] > 1e-3 and invariant_error[1] > 1e-3
    assert invariant_error[2] > 1e-3 and invariant_error[3] > 1e-3

    print("D193 three-component Lyapunov gate: PASS")
    print(f"ruling eigenvalues        = {ruling_eigs.tolist()}")
    print(f"reflected eigenvalues     = {reflected_eigs.tolist()}")
    print(f"Lyapunov residual         = {lyap_residual(alpha, w):.3e}")


if __name__ == "__main__":
    main()
