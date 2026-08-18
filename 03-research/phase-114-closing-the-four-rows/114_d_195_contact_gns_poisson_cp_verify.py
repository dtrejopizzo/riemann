#!/usr/bin/env python3
"""Finite CP/Poisson/Tate certificates for D.195."""

from __future__ import annotations

import numpy as np


def cyclic_shift(n: int) -> np.ndarray:
    u = np.zeros((n, n))
    for j in range(n):
        u[(j + 1) % n, j] = 1.0
    return u


def main() -> None:
    n, r = 41, 0.37
    u = cyclic_shift(n)
    eye = np.eye(n)
    a = np.sqrt(1.0 - r * r) * np.linalg.inv(eye - r * u)
    poisson = a.conj().T @ a
    c = (1.0 + r) / (1.0 - r)
    m = poisson / c
    eig_m = np.linalg.eigvalsh(m)
    assert eig_m[0] > 0 and eig_m[-1] <= 1.0 + 1e-12
    assert abs(np.linalg.norm(a, 2) ** 2 - c) < 1e-10
    assert np.linalg.norm((poisson - eye) - ((c - 1) * eye - c * (eye - m))) < 1e-11

    # Critical weighted tails: each translated atom contributes one after
    # r^k e^{ka/2}, because r=e^{-a/2}.
    a_log = -2.0 * np.log(r)
    partial = []
    for depth in (5, 10, 20, 40):
        partial.append(sum((r**k) * np.exp(k * a_log / 2) for k in range(depth)))
    assert np.allclose(partial, [5.0, 10.0, 20.0, 40.0])

    # Zero-extension compression of a symmetric geometric random walk.
    size, max_shift = 51, 12
    grid = np.linspace(-2.5, 2.5, size)
    walk = np.zeros((size, size))
    norm = sum(r ** abs(k) for k in range(-max_shift, max_shift + 1))
    for k in range(-max_shift, max_shift + 1):
        weight = r ** abs(k) / norm
        for j in range(size):
            i = j + k
            if 0 <= i < size:
                walk[i, j] += weight
    ones = np.ones(size)
    assert np.linalg.norm(walk @ ones - ones) > 1e-3

    # Build a deterministic nonzero vector in the two-moment kernel.
    moments = np.column_stack((np.exp(grid / 2), np.exp(-grid / 2)))
    pi = np.eye(size) - moments @ np.linalg.inv(moments.T @ moments) @ moments.T
    seed = np.sin(2.3 * grid) + 0.4 * np.cos(5.1 * grid)
    primitive = pi @ seed
    assert np.linalg.norm(moments.T @ primitive) < 1e-11
    escaped = moments.T @ (walk @ primitive)
    assert np.linalg.norm(escaped) > 1e-6

    # Positive unital Schur multiplier, but diagonal removal is indefinite.
    idx = np.arange(20)
    schur_symbol = r ** np.abs(idx[:, None] - idx[None, :])
    assert np.linalg.eigvalsh(schur_symbol)[0] > 0
    assert np.allclose(np.diag(schur_symbol), 1.0)
    removed = schur_symbol - np.eye(20)
    eig_removed = np.linalg.eigvalsh(removed)
    assert eig_removed[0] < 0 < eig_removed[-1]

    print("D195 contact-GNS Poisson CP/Tate-jet defect: PASS")
    print(f"Poisson normalization c_r = {c:.12f}")
    print(f"Markov spectral interval  = [{eig_m[0]:.6e}, {eig_m[-1]:.6e}]")
    print(f"critical tail partials    = {partial}")
    print(f"compressed jet escape     = {np.linalg.norm(escaped):.6e}")
    print(f"diag-removed Schur range  = [{eig_removed[0]:.6e}, {eig_removed[-1]:.6e}]")


if __name__ == "__main__":
    main()
