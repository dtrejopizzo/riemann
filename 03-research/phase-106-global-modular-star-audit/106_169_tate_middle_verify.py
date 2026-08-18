#!/usr/bin/env python3
"""Numerical algebra audit for the Tate middle projection in 106.169."""

from __future__ import annotations

import math
import numpy as np


def block_diag(*blocks: np.ndarray) -> np.ndarray:
    rows = sum(block.shape[0] for block in blocks)
    out = np.zeros((rows, rows))
    offset = 0
    for block in blocks:
        n = block.shape[0]
        out[offset : offset + n, offset : offset + n] = block
        offset += n
    return out


def build(primes: list[int], coefficient_dim: int = 3):
    n = len(primes)
    eye = np.eye(coefficient_dim)
    ell = np.log(np.asarray(primes, dtype=float))
    c = 2.0 * math.pi / ell
    alpha = ell / np.sqrt(2.0 * math.pi * np.asarray(primes, dtype=float))
    capital_c = float(np.sum(c * alpha**2))

    gx = block_diag(*(cp * eye for cp in c))
    gy = block_diag(*((1.0 / cp) * eye for cp in c))
    metric = block_diag(gx, gy)

    zero = np.zeros_like(gx)
    cdiag = block_diag(*(cp * eye for cp in c))
    cinvdiag = block_diag(*((1.0 / cp) * eye for cp in c))
    complex_structure = np.block([[zero, -cinvdiag], [cdiag, zero]])

    ax = np.concatenate([ap * eye for ap in alpha], axis=0)
    ay = np.concatenate([ap * cp * eye for ap, cp in zip(alpha, c)], axis=0)
    gamma = np.block(
        [
            [ax, np.zeros_like(ax)],
            [np.zeros_like(ay), ay],
        ]
    )

    gram_generic = gamma.T @ metric @ gamma
    projection = np.eye(2 * n * coefficient_dim) - gamma @ (
        np.linalg.solve(gram_generic, gamma.T @ metric)
    )

    boundary_x = np.concatenate(
        [ap * cp * eye for ap, cp in zip(alpha, c)], axis=1
    )
    boundary_y = np.concatenate([ap * eye for ap in alpha], axis=1)
    boundary = np.block(
        [
            [boundary_x, np.zeros_like(boundary_x)],
            [np.zeros_like(boundary_y), boundary_y],
        ]
    )
    return metric, complex_structure, gamma, projection, boundary, capital_c


def main() -> None:
    metric, j_op, gamma, proj, boundary, capital_c = build([2, 3, 5, 7, 11])
    rng = np.random.default_rng(106169)
    vector = rng.normal(size=proj.shape[0])
    middle = proj @ vector

    checks = {
        "J^2 + I": np.linalg.norm(j_op @ j_op + np.eye(j_op.shape[0])),
        "P^2 - P": np.linalg.norm(proj @ proj - proj),
        "PJ - JP": np.linalg.norm(proj @ j_op - j_op @ proj),
        "boundary(Pv)": np.linalg.norm(boundary @ middle),
        "P(generic)": np.linalg.norm(proj @ gamma),
        "G-self-adjoint P": np.linalg.norm(proj.T @ metric - metric @ proj),
        "generic Gram - C I": np.linalg.norm(
            gamma.T @ metric @ gamma
            - capital_c * np.eye(gamma.shape[1])
        ),
    }
    for label, error in checks.items():
        print(f"{label:24s} {error:.3e}")

    energy = float(middle.T @ metric @ middle)
    print(f"middle energy            {energy:.12e}")
    if energy <= 0:
        raise SystemExit("positive metric check failed")
    if max(checks.values()) > 1e-11:
        raise SystemExit("projection identity check failed")


if __name__ == "__main__":
    main()
