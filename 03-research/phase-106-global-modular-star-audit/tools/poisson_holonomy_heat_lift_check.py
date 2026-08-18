#!/usr/bin/env python3
"""Numerical checks for 106.152.

The script checks the Poisson-holonomy moments and the equality between the
averaged twisted-circle heat trace and the literal prime-tower Gaussian sum.
It is a diagnostic for the exact formulas, not a proof of the global
completion equation.
"""

from __future__ import annotations

import math

import numpy as np


def poisson_density(theta: np.ndarray, r: float) -> np.ndarray:
    return (1.0 - r * r) / (
        1.0 - 2.0 * r * np.cos(theta) + r * r
    )


def check_prime(p: int, t: float, grid: int = 1 << 15) -> None:
    ell = math.log(p)
    r = p ** -0.5
    theta = 2.0 * math.pi * np.arange(grid) / grid
    density = poisson_density(theta, r)

    for k in range(7):
        moment = np.mean(density * np.exp(1j * k * theta))
        target = r**k
        error = abs(moment - target)
        assert error < 2.0e-12, (p, k, moment, target, error)

    modes = np.arange(-180, 181, dtype=float)
    fiber_traces = np.zeros(grid, dtype=float)
    chunk = 1024
    for start in range(0, grid, chunk):
        stop = min(start + chunk, grid)
        angles = theta[start:stop, None]
        eigenvalues = ((2.0 * math.pi * modes[None, :] + angles) / ell) ** 2
        fiber_traces[start:stop] = np.exp(-t * eigenvalues).sum(axis=1)
    averaged_trace = np.mean(density * fiber_traces)

    winding = ell / math.sqrt(4.0 * math.pi * t)
    for k in range(1, 10000):
        term = 2.0 * (r**k) * math.exp(-((k * ell) ** 2) / (4.0 * t))
        winding += ell / math.sqrt(4.0 * math.pi * t) * term
        if abs(term) < 1.0e-18:
            break

    error = abs(averaged_trace - winding)
    assert error < 2.0e-10, (p, t, averaged_trace, winding, error)
    print(
        f"p={p:2d} t={t:.3f} averaged={averaged_trace:.14e} "
        f"winding={winding:.14e} error={error:.3e}"
    )


def main() -> None:
    for p in (2, 3, 5, 7, 11):
        for t in (0.08, 0.3, 1.0):
            check_prime(p, t)
    print("PASS: Poisson-holonomy moments and prime heat lift")


if __name__ == "__main__":
    main()

