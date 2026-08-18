#!/usr/bin/env python3
"""Algebraic verification of the D.155 three-moment reduction."""

import numpy as np


def sym(a: np.ndarray) -> np.ndarray:
    return (a + a.T) / 2.0


def main() -> None:
    rng = np.random.default_rng(155)
    n, q, k = 8, 17, 6
    b = sym(rng.normal(size=(n, n)))
    c = rng.normal(size=(q, n))
    z = rng.normal(size=(q, q))
    d = z.T @ z + 2.0 * np.eye(q)
    a = np.block([[b, c.T], [c, d]])

    h = [np.eye(n)]
    power = np.eye(n + q)
    for _ in range(4):
        power = power @ a
        h.append(power[:n, :n])

    m0 = h[2] - b @ b
    m1 = h[3] - b @ b @ b - b @ m0 - m0 @ b
    m2 = (
        h[4]
        - np.linalg.matrix_power(b, 4)
        - b @ b @ m0
        - b @ m0 @ b
        - m0 @ b @ b
        - m0 @ m0
        - b @ m1
        - m1 @ b
    )

    assert np.linalg.norm(m0 - c.T @ c) < 2.0e-10
    assert np.linalg.norm(m1 - c.T @ d @ c) < 2.0e-9
    assert np.linalg.norm(m2 - c.T @ d @ d @ c) < 2.0e-8

    rmat = rng.normal(size=(n, k))
    dy = rmat.T @ m1 @ rmat
    cy = rmat.T @ m0
    coeff = np.linalg.solve(dy, cy)

    graph_formula = b - cy.T @ coeff
    y = c @ rmat
    x = y @ coeff
    graph_direct = b - c.T @ x - x.T @ c + x.T @ d @ x
    assert np.linalg.norm(graph_formula - graph_direct) < 2.0e-10

    residual_formula = (
        m0
        - m1 @ rmat @ coeff
        - coeff.T @ rmat.T @ m1
        + coeff.T @ rmat.T @ m2 @ rmat @ coeff
    )
    residual_direct = (c - d @ x).T @ (c - d @ x)
    assert np.linalg.norm(residual_formula - residual_direct) < 2.0e-8

    print("D155 three-moment Krylov graph identities: PASS")


if __name__ == "__main__":
    main()
