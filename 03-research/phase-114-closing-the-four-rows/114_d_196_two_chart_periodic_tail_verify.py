#!/usr/bin/env python3
"""Finite/fiber certificates for the two-chart colligation D.196."""

from __future__ import annotations

import numpy as np


def main() -> None:
    r = 0.43
    c = (1.0 + r) / (1.0 - r)

    # Exact tails for a compactly supported fiber sequence.
    lo, hi = -3, 4
    indices = np.arange(lo, hi + 1)
    f = np.sin(0.7 * indices) + 0.2 * np.cos(1.3 * indices)
    b_plus = np.sum((r ** (-indices)) * f)
    b_minus = np.sum((r**indices) * f)

    def poisson_at(j: int) -> float:
        return float(np.sum((r ** np.abs(j - indices)) * f) / c)

    for j in range(hi + 1, hi + 8):
        assert abs(poisson_at(j) - (r**j) * b_plus / c) < 1e-11
    for j in range(lo - 7, lo):
        assert abs(poisson_at(j) - (r ** (-j)) * b_minus / c) < 1e-11

    # Periodic boundary functions can survive both scalar Tate constraints.
    m = 30
    u = np.linspace(0.0, 1.0, m, endpoint=False)
    moments = np.column_stack((np.exp(u / 2), np.exp(-u / 2)))
    pi = np.eye(m) - moments @ np.linalg.inv(moments.T @ moments) @ moments.T
    h = pi @ (np.sin(4.2 * u) + 0.3 * np.cos(8.1 * u))
    assert np.linalg.norm(moments.T @ h) < 1e-11
    assert np.linalg.norm(h) > 1e-2

    # AR(1) covariance inverse and endpoint feedthrough.
    n = 17
    idx = np.arange(n)
    g = (r ** np.abs(idx[:, None] - idx[None, :])) / c
    g_inv = np.linalg.inv(g)
    q = np.zeros_like(g)
    factor = c / (1.0 - r * r)
    for i in range(n):
        q[i, i] = factor * (1.0 + r * r)
        if i + 1 < n:
            q[i, i + 1] = q[i + 1, i] = -factor * r
    d = r * r / (1.0 - r) ** 2
    expected = np.zeros_like(g)
    expected[0, 0] = expected[-1, -1] = d
    assert np.linalg.norm((q - g_inv) - expected) < 2e-12

    # Laurent residues have opposite signs.
    residue_left = r
    residue_right = -1.0 / r
    assert residue_left > 0 > residue_right

    # Tensor the residue form with the periodic fiber and remove one scalar
    # moment in each chart: both infinite-sign sectors persist in sections.
    j_boundary = np.block(
        [
            [residue_left * np.eye(m), np.zeros((m, m))],
            [np.zeros((m, m)), residue_right * np.eye(m)],
        ]
    )
    pi2 = np.block([[pi, np.zeros((m, m))], [np.zeros((m, m)), pi]])
    compressed = pi2 @ j_boundary @ pi2
    eig = np.linalg.eigvalsh(compressed)
    assert np.sum(eig > 1e-9) == m - 2
    assert np.sum(eig < -1e-9) == m - 2

    print("D196 two-chart periodic-tail colligation: PASS")
    print(f"tail coefficients       = ({b_plus:.6e}, {b_minus:.6e})")
    print(f"periodic primitive norm = {np.linalg.norm(h):.6e}")
    print(f"feedthrough d_r         = {d:.12f}")
    print(f"primitive inertia       = ({np.sum(eig>1e-9)}, {np.sum(eig< -1e-9)})")


if __name__ == "__main__":
    main()
