#!/usr/bin/env python3
"""Finite-section audit for D.190.

This checks only exact block identities, ranks and Schur/Douglas logic.
It makes no claim about the infinite Weil form.
"""

from __future__ import annotations

import numpy as np


def sym_sqrt(a: np.ndarray, inverse: bool = False) -> np.ndarray:
    w, v = np.linalg.eigh(a)
    if np.min(w) <= 1e-11:
        raise AssertionError("matrix is not strictly positive")
    power = -0.5 if inverse else 0.5
    return (v * (w**power)) @ v.T


def main() -> None:
    n_old, n_shell = 10, 8
    n = n_old + n_shell
    idx = np.arange(n)

    # Dense translation-invariant surrogate for the Gamma/resolvent kernel,
    # plus three exact finite shift channels (standing for selected p^k).
    rho = 0.79
    dist = np.abs(idx[:, None] - idx[None, :])
    off = -(rho**dist)
    np.fill_diagonal(off, 0.0)
    for shift, weight in ((1, 0.17), (3, 0.11), (7, 0.07)):
        for i in range(n - shift):
            off[i, i + shift] -= weight
            off[i + shift, i] -= weight

    # Choose one common Toeplitz diagonal so the old block is positive but
    # the enlarged block is indefinite.  This is the exact logical gate.
    lam_old = np.linalg.eigvalsh(off[:n_old, :n_old])[0]
    lam_full = np.linalg.eigvalsh(off)[0]
    assert lam_full < lam_old - 1e-8
    diagonal = -0.5 * (lam_old + lam_full)
    q = off + diagonal * np.eye(n)

    p = np.zeros((n, n))
    p[:n_old, :n_old] = np.eye(n_old)
    e = np.eye(n) - p
    cross = p @ q @ e
    comm = (p @ q - q @ p) @ e
    assert np.linalg.norm(cross - comm) < 1e-12

    a = q[:n_old, :n_old]
    x = q[:n_old, n_old:]
    b = q[n_old:, n_old:]
    assert np.linalg.eigvalsh(a)[0] > 1e-10
    assert np.linalg.eigvalsh(q)[0] < -1e-10
    assert np.linalg.matrix_rank(x, tol=1e-10) == min(n_old, n_shell)

    schur = b - x.T @ np.linalg.solve(a, x)
    assert np.linalg.eigvalsh(schur)[0] < -1e-10

    # Two Tate moment vectors.  Compression changes the cross by rank <= 4.
    t = np.linspace(-2.0, 2.0, n)
    moments = np.column_stack((np.exp(t / 2), np.exp(-t / 2)))
    f = moments @ np.linalg.inv(moments.T @ moments) @ moments.T
    pi = np.eye(n) - f
    cross_tate = p @ pi @ q @ pi @ e
    delta = cross_tate - cross
    assert np.linalg.matrix_rank(delta, tol=1e-10) <= 4
    assert np.linalg.matrix_rank(cross_tate, tol=1e-10) >= min(n_old, n_shell) - 4

    # Positive comparison: exact constant-one Douglas/Schur factorization.
    # Start from the same full matrix and shift it just above zero.
    q_pos = q + (-np.linalg.eigvalsh(q)[0] + 0.25) * np.eye(n)
    a_pos = q_pos[:n_old, :n_old]
    x_pos = q_pos[:n_old, n_old:]
    b_pos = q_pos[n_old:, n_old:]
    assert np.linalg.eigvalsh(q_pos)[0] > 0.2
    a_inv_sqrt = sym_sqrt(a_pos, inverse=True)
    c = a_inv_sqrt @ x_pos
    assert np.linalg.norm(sym_sqrt(a_pos) @ c - x_pos) < 1e-10
    budget = b_pos - c.T @ c
    assert np.linalg.eigvalsh(budget)[0] > -1e-10

    print("D190 Toeplitz--Hankel sharp Douglas gate: PASS")
    print(f"old min eigenvalue       = {np.linalg.eigvalsh(a)[0]:.6e}")
    print(f"full min eigenvalue      = {np.linalg.eigvalsh(q)[0]:.6e}")
    print(f"cross rank               = {np.linalg.matrix_rank(x, tol=1e-10)}")
    print(f"Tate correction rank     = {np.linalg.matrix_rank(delta, tol=1e-10)}")
    print(f"Tate-compressed rank      = {np.linalg.matrix_rank(cross_tate, tol=1e-10)}")
    print(f"failed Schur min          = {np.linalg.eigvalsh(schur)[0]:.6e}")
    print(f"positive Schur min        = {np.linalg.eigvalsh(budget)[0]:.6e}")


if __name__ == "__main__":
    main()
