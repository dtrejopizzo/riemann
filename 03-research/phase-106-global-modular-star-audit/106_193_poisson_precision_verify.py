#!/usr/bin/env python3
"""Finite-section checks for the Poisson precision factorization."""

from __future__ import annotations

import numpy as np


def check(a: float, size: int) -> tuple[float, float]:
    idx = np.arange(size)
    kernel = a ** np.abs(idx[:, None] - idx[None, :])

    b = np.zeros((size, size))
    b[0, 0] = 1.0
    scale = np.sqrt(1.0 - a * a)
    for h in range(size - 1):
        b[h + 1, h] = -a / scale
        b[h + 1, h + 1] = 1.0 / scale

    # A finite section has a different last boundary.  Test the exact
    # precision identity away from that last-row correction.
    precision = np.linalg.inv(kernel)
    bulk = precision - b.T @ b
    interior_error = np.max(np.abs(bulk[:-1, :-1]))
    eigen_floor = np.min(np.linalg.eigvalsh(kernel))
    return float(interior_error), float(eigen_floor)


def main() -> None:
    for p in (2, 3, 5, 7, 11):
        error, floor = check(p ** -0.5, 48)
        print(f"p={p} precision_bulk_error={error:.3e} eigen_floor={floor:.6f}")


if __name__ == "__main__":
    main()

