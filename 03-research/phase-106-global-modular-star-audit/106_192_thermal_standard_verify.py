#!/usr/bin/env python3
"""Finite-matrix checks for 106.192."""

from __future__ import annotations

import numpy as np


def hs_inner(x: np.ndarray, y: np.ndarray) -> complex:
    return np.trace(x.conj().T @ y)


def shift(dim: int) -> np.ndarray:
    s = np.zeros((dim, dim), dtype=complex)
    for j in range(dim - 1):
        s[j + 1, j] = 1.0
    return s


def local_check(p: int, dim: int, max_k: int) -> tuple[float, float, float]:
    r = 1.0 / p
    s = shift(dim)
    rho_half = np.diag(np.sqrt((1 - r) * r ** np.arange(dim)))

    powers = [np.linalg.matrix_power(s, k) for k in range(max_k + 1)]
    adjoint_powers = [x.conj().T for x in powers]
    vectors = {
        (a, b): powers[a] @ rho_half @ adjoint_powers[b]
        for a in range(max_k + 1)
        for b in range(max_k + 1)
    }

    coefficient_error = 0.0
    poisson_error = 0.0
    modular_collapse_error = 0.0
    for k in range(max_k + 1):
        sk = powers[k]
        got = hs_inner(sk @ rho_half, rho_half @ sk)
        coefficient_error = max(coefficient_error, abs(got - r ** (k / 2)))
        modular_collapse_error = max(
            modular_collapse_error,
            np.linalg.norm(rho_half @ sk - r ** (k / 2) * sk @ rho_half),
        )

    for a in range(max_k + 1):
        for b in range(max_k + 1):
            eab = vectors[a, b]
            for c in range(max_k + 1):
                for d in range(max_k + 1):
                    ecd = vectors[c, d]
                    expected = 0.0 if a - b != c - d else r ** (abs(c - a) / 2)
                    poisson_error = max(poisson_error, abs(hs_inner(eab, ecd) - expected))
    return coefficient_error, poisson_error, modular_collapse_error


def main() -> None:
    # Truncation errors are geometric.  A large dimension makes them negligible.
    for p in (2, 3, 5, 7):
        coefficient_error, poisson_error, collapse_error = local_check(p, dim=64, max_k=4)
        print(
            f"p={p} coefficient_error={coefficient_error:.3e} "
            f"poisson_error={poisson_error:.3e} "
            f"collapse_error={collapse_error:.3e}"
        )


if __name__ == "__main__":
    main()
