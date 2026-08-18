#!/usr/bin/env python3
"""Finite model for D.191: propagation, dense range and trace pairings."""

from __future__ import annotations

import numpy as np


def main() -> None:
    # Finite convolution has the expected propagation radius.
    n = 31
    center = n // 2
    f = np.zeros(n)
    f[center - 2 : center + 3] = np.array([1.0, -0.7, 0.3, 0.2, -0.1])
    g = np.zeros(n)
    g[center - 3 : center + 4] = np.arange(1.0, 8.0)
    conv = np.convolve(f, g, mode="full")
    support_f = np.flatnonzero(np.abs(f) > 0)
    support_g = np.flatnonzero(np.abs(g) > 0)
    support_conv = np.flatnonzero(np.abs(conv) > 1e-13)
    assert support_conv[0] == support_f[0] + support_g[0]
    assert support_conv[-1] == support_f[-1] + support_g[-1]

    # Diagonal finite sections model a multiplication symbol tending to 0.
    # Every finite range is all of C^N, while inverse norms diverge; the
    # infinite range is dense/nonclosed and the Hausdorff cokernel is zero.
    inverse_norms = []
    for size in (8, 16, 32, 64, 128):
        symbol = 1.0 / np.arange(1, size + 1, dtype=float)
        d = np.diag(symbol)
        assert np.linalg.matrix_rank(d) == size
        inverse_norms.append(np.linalg.norm(np.linalg.inv(d), 2))
    assert all(b > a for a, b in zip(inverse_norms, inverse_norms[1:]))
    assert abs(inverse_norms[-1] - 128.0) < 1e-10

    # Positive Hilbert adjoint versus indefinite Tate/Krein transpose.
    j = np.array([[0.0, 1.0], [1.0, 0.0]])

    def sharp(a: np.ndarray) -> np.ndarray:
        return j @ a.conj().T @ j

    a_plus = np.eye(2)
    a_minus = np.diag([1.0, -1.0])
    hilbert_plus = np.trace(a_plus @ a_plus.conj().T).real
    hilbert_minus = np.trace(a_minus @ a_minus.conj().T).real
    krein_plus = np.trace(a_plus @ sharp(a_plus)).real
    krein_minus = np.trace(a_minus @ sharp(a_minus)).real
    assert hilbert_plus > 0 and hilbert_minus > 0
    assert krein_plus > 0 and krein_minus < 0
    assert np.linalg.norm(sharp(sharp(a_minus)) - a_minus) < 1e-12

    print("D191 pre-trace Meyer/Plancherel audit: PASS")
    print(f"Moore--Penrose inverse norms = {inverse_norms}")
    print(f"Hilbert trace squares        = {hilbert_plus:.1f}, {hilbert_minus:.1f}")
    print(f"Krein character pairings     = {krein_plus:.1f}, {krein_minus:.1f}")


if __name__ == "__main__":
    main()
