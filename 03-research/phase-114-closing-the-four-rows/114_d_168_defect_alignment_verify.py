#!/usr/bin/env python3
"""Finite algebra for the exact core-resolvent alignment obstruction."""
import numpy as np


def main():
    rng = np.random.default_rng(168)
    q, _ = np.linalg.qr(rng.normal(size=(5, 5)))
    eig = np.array([.999, .8, .4, .1, 0.0])
    K = q @ np.diag(eig) @ q.T
    gamma = np.diag([2.0, 3.0, 5.0, 7.0, 11.0])
    gh = np.diag(np.sqrt(np.diag(gamma)))
    gih = np.diag(1 / np.sqrt(np.diag(gamma)))
    A = gh @ (np.eye(5) - K) @ gh
    B = rng.normal(size=(5, 2))
    z = gih @ B
    lhs = B.T @ np.linalg.inv(A) @ B
    rhs = z.T @ np.linalg.inv(np.eye(5) - K) @ z
    assert np.linalg.norm(lhs - rhs) < 1e-9

    # Spectral formula for the excess over the pure Gamma inverse.
    excess = rhs - z.T @ z
    spec = np.zeros((2, 2))
    for j, lam in enumerate(eig):
        zj = q[:, j].T @ z
        spec += lam / (1 - lam) * np.outer(zj, zj)
    assert np.linalg.norm(excess - spec) < 1e-9

    # Fixed Gram, arbitrarily large full shorting.
    values = []
    for eps in (1e-2, 1e-6, 1e-10):
        Ke = np.diag([1 - eps, 0.0])
        ze = np.array([1.0, 0.0])
        values.append(ze @ np.linalg.inv(np.eye(2) - Ke) @ ze)
    assert np.allclose(values, [1e2, 1e6, 1e10], rtol=2e-7)
    print("counter-scaling =", values)
    print("D168 core-resolvent defect alignment audit: PASS")


if __name__ == "__main__":
    main()
