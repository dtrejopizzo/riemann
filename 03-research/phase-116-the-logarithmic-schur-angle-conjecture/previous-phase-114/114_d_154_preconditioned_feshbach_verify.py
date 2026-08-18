#!/usr/bin/env python3
"""Verify the exact preconditioned Feshbach graph identity in D.154."""

import numpy as np


def main() -> None:
    rng = np.random.default_rng(154)
    p = 7
    q = 19

    z = rng.normal(size=(q, q))
    d = z.T @ z + 1.3 * np.eye(q)
    c = rng.normal(size=(q, p))

    # Choose B so that the exact Schur complement is strictly positive.
    b = c.T @ np.linalg.solve(d, c) + 0.7 * np.eye(p)

    # Deliberately use an inexact graph, so the residual is nonzero.
    x = np.linalg.solve(d + 0.11 * np.eye(q), c)
    r = c - d @ x

    exact = b - c.T @ np.linalg.solve(d, c)
    graph = b - x.T @ c - c.T @ x + x.T @ d @ x
    identity = graph - r.T @ np.linalg.solve(d, r)

    err = np.linalg.norm(exact - identity, ord=2)
    scale = max(1.0, np.linalg.norm(exact, ord=2))
    assert err <= 2.0e-13 * scale, (err, scale)

    delta = np.linalg.eigvalsh(d)[0]
    lower = graph - (r.T @ r) / delta
    assert np.linalg.eigvalsh(exact - lower)[0] >= -2.0e-13
    assert np.linalg.eigvalsh(lower)[0] > 0.0

    print("D154 preconditioned Feshbach identity: PASS")
    print(f"identity error = {err:.3e}")
    print(f"delta = {delta:.12g}")
    print(f"lower minimum = {np.linalg.eigvalsh(lower)[0]:.12g}")


if __name__ == "__main__":
    main()
