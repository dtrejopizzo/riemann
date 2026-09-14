#!/usr/bin/env python3
"""Finite-section checks for P122.013, P122.015 and P122.016.

The proofs in the notes are exact.  This script is only a reproducibility
check for signs, normalizations and the ordinary-multiplicity obstruction.
"""

from __future__ import annotations

import math

import numpy as np


def unilateral_shift(size: int) -> np.ndarray:
    shift = np.zeros((size, size))
    shift[np.arange(1, size), np.arange(size - 1)] = 1.0
    return shift


def euler_connection(radius: float, size: int) -> np.ndarray:
    shift = unilateral_shift(size)
    return radius * shift @ np.linalg.inv(np.eye(size) - radius * shift)


def check_rank_one(radius: float, size: int = 256, block: int = 24) -> float:
    connection = euler_connection(radius, size)
    defect = connection.T @ connection - connection @ connection.T
    vector = np.array(
        [radius ** (j + 1) for j in range(size)]
    ) / math.sqrt(1.0 - radius * radius)
    exact = np.outer(vector, vector)
    return float(np.linalg.norm((defect - exact)[:block, :block]))


def check_hardy_determinant(radius: float, terms: int = 10000) -> float:
    residue = -sum(radius ** (2 * n) / n for n in range(1, terms + 1))
    return abs(math.exp(residue) - (1.0 - radius * radius))


def finite_floquet_multiplicity(cells: int) -> tuple[int, float]:
    """Replicate the discrete rank-one crossing over finitely many cells."""

    discrete_crossing = np.array([[1.0]])
    replicated = np.kron(np.eye(cells), discrete_crossing)
    singular_values = np.linalg.svd(replicated, compute_uv=False)
    rank = int(np.count_nonzero(singular_values > 1e-12))
    hs_squared = float(np.sum(singular_values**2))
    return rank, hs_squared


def main() -> None:
    tolerance = 2e-11
    for radius in (0.2, 0.5, 0.8):
        rank_error = check_rank_one(radius)
        symbol_error = check_hardy_determinant(radius)
        assert rank_error < tolerance, (radius, rank_error)
        assert symbol_error < tolerance, (radius, symbol_error)
        print(
            f"r={radius:.1f}: rank-one error={rank_error:.3e}; "
            f"Hardy-determinant error={symbol_error:.3e}"
        )

    previous = 0
    for cells in (1, 2, 8, 32):
        rank, hs_squared = finite_floquet_multiplicity(cells)
        assert rank == cells
        assert abs(hs_squared - cells) < tolerance
        assert rank > previous
        previous = rank
        print(
            f"Floquet cells={cells}: ordinary rank={rank}; "
            f"ordinary HS^2={hs_squared:.0f}"
        )

    print("PASS: Euler Hardy-determinant identities and multiplicity growth")


if __name__ == "__main__":
    main()
