#!/usr/bin/env python3
"""Finite-dimensional audit of the bilinear Green identity in 106.176."""

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(176)
    phases = np.array([0.23, 0.71, 1.37, 2.11])
    weights = np.array([0.8, 0.35, 0.2, 0.1])
    f = rng.normal(size=4) + 1j * rng.normal(size=4)
    g = rng.normal(size=4) + 1j * rng.normal(size=4)

    inner = np.vdot(g, f)  # linear in f, conjugate-linear in g
    c = 2.0 * np.sum(weights)
    correlation = 0.0j
    energy = 0.0j

    for theta, weight in zip(phases, weights):
        u = np.diag(np.exp(1j * theta * np.arange(1, 5)))
        for op in (u, u.conj().T):
            correlation += weight * np.vdot(op @ g, f)
            df = f - op @ f
            dg = g - op @ g
            energy += 0.5 * weight * np.vdot(dg, df)

    error = abs(c * inner - correlation - energy)
    print(f"|c<f,g> - I(f,g) - E(f,g)|  {error:.3e}")


if __name__ == "__main__":
    main()
