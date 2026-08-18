#!/usr/bin/env python3
"""Resolve the exact augmented block gain into predictable channels.

For each admissible finite-head transition this diagnostic compares

    Delta = <r,(I+U A^{-1} U*)^{-1}r>

with three rigorous algebraic lower bounds:

    harmonic = ||r||^4 / (||r||^2 + <r,U A^{-1}U* r>),
    operator = ||r||^2 / (1 + ||U A^{-1}U*||),
    k_one    = det(A)||r||^2 / det(A+U*U).

It also reconstructs Delta from the singular channels of U A^{-1/2}.
All quadrature is float64; the output is diagnostic, not a certificate.
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve()
sys.path.insert(0, str(HERE.parent))

from finite_head_mean_periodic_gram import source_gram  # noqa: E402
from joint_block_innovation_diagnostic import (  # noqa: E402
    schur_pivot,
    weighted_zero_basis,
)


def inverse_square_root(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    if values[0] <= 0.0:
        raise ValueError("preceding block is not positive")
    return (vectors / np.sqrt(values)) @ vectors.T


def krylov_lower_bound(
    eigenvalues: np.ndarray,
    channel_energy: np.ndarray,
    perpendicular: float,
    order: int,
) -> float:
    """Best matched-filter bound on span{r, Br, ..., B^(order-1)r}.

    The spectral mass at zero includes the component perpendicular to the
    range of the old observation map.  This is a floating-point diagnostic;
    a singular moment matrix is handled by its Moore--Penrose inverse.
    """
    moments = np.empty(2 * order, dtype=float)
    moments[0] = perpendicular + float(channel_energy.sum())
    for power in range(1, 2 * order):
        moments[power] = float(
            np.sum(channel_energy * eigenvalues**power)
        )
    hankel = np.empty((order, order), dtype=float)
    for row in range(order):
        for column in range(order):
            hankel[row, column] = (
                moments[row + column] + moments[row + column + 1]
            )
    response = moments[:order]
    value = float(response @ np.linalg.pinv(hankel) @ response)
    return max(0.0, value)


def diagnostics(
    defect: np.ndarray, block: np.ndarray, dimension: int
) -> dict[str, float]:
    old = defect[: dimension - 1, : dimension - 1]
    cross = defect[: dimension - 1, dimension - 1]
    regression = np.linalg.solve(old, cross)

    gram = block[: dimension, : dimension]
    old_gram = gram[:-1, :-1]
    prime_cross = gram[:-1, -1]
    prime_new = float(gram[-1, -1])

    residual_cross = prime_cross - old_gram @ regression
    residual_norm = float(
        prime_new
        - 2.0 * regression @ prime_cross
        + regression @ old_gram @ regression
    )

    old_inverse = np.linalg.inv(old)
    second = float(residual_cross @ old_inverse @ residual_cross)
    harmonic = residual_norm**2 / (residual_norm + second)
    new_residual_overlap = float(
        prime_new - prime_cross @ regression
    )
    new_leakage = float(prime_cross @ old_inverse @ prime_cross)
    new_mode_filter = (
        new_residual_overlap**2 / (prime_new + new_leakage)
    )

    old_inv_sqrt = inverse_square_root(old)
    whitened = old_inv_sqrt @ old_gram @ old_inv_sqrt
    eigenvalues, eigenvectors = np.linalg.eigh(whitened)
    eigenvalues = np.maximum(eigenvalues, 0.0)
    operator = residual_norm / (1.0 + float(eigenvalues[-1]))
    k_one = residual_norm / float(np.prod(1.0 + eigenvalues))

    whitened_cross = old_inv_sqrt @ residual_cross
    coordinates = eigenvectors.T @ whitened_cross
    positive = eigenvalues > 1.0e-13
    channel_energy = np.zeros_like(eigenvalues)
    channel_energy[positive] = (
        coordinates[positive] ** 2 / eigenvalues[positive]
    )
    perpendicular = max(0.0, residual_norm - float(channel_energy.sum()))
    spectral = perpendicular + float(
        np.sum(channel_energy / (1.0 + eigenvalues))
    )
    krylov_2 = krylov_lower_bound(
        eigenvalues, channel_energy, perpendicular, 2
    )
    krylov_3 = krylov_lower_bound(
        eigenvalues, channel_energy, perpendicular, 3
    )

    augmented_old = old + old_gram
    exact = float(
        residual_norm
        - residual_cross @ np.linalg.solve(augmented_old, residual_cross)
    )
    return {
        "norm": residual_norm,
        "second": second,
        "exact": exact,
        "spectral": spectral,
        "harmonic": harmonic,
        "krylov_2": krylov_2,
        "krylov_3": krylov_3,
        "krylov_2_gap": max(0.0, exact - krylov_2),
        "new_mode_filter": new_mode_filter,
        "operator": operator,
        "k_one": k_one,
        "lambda_max": float(eigenvalues[-1]),
        "perpendicular": perpendicular,
    }


def run(dx: float, span: int, heads: list[int]) -> None:
    x, kernel, _, basis = weighted_zero_basis(dx, span)
    source = {
        head: source_gram(x, dx, kernel, basis, head) for head in heads
    }
    defects = {head: source[head] - 0.5 * np.eye(span) for head in heads}

    print(f"dx={dx:g}; span={span}")
    print(
        "M X0->X1 sigma0      norm-r2     exact        harmonic     "
        "krylov-2    krylov-3    new-filter   operator     "
        "k=1-minor   exact-K2    lmax       rperp2     flags"
    )
    for dimension in range(2, span + 1):
        for left_index, head0 in enumerate(heads[:-1]):
            old = defects[head0][: dimension - 1, : dimension - 1]
            if np.linalg.eigvalsh(old)[0] <= 1.0e-9:
                continue
            sigma0 = schur_pivot(defects[head0], dimension)
            # Print the first later head which closes the exact pivot.
            for head1 in heads[left_index + 1 :]:
                sigma1 = schur_pivot(defects[head1], dimension)
                if sigma1 <= 0.0:
                    continue
                values = diagnostics(
                    defects[head0], source[head1] - source[head0], dimension
                )
                deficit = max(0.0, -sigma0)
                names = ("harmonic", "new_mode_filter", "operator", "k_one")
                flags = "/".join(
                    name[0].upper() if values[name] > deficit else "-"
                    for name in names
                )
                print(
                    f"{dimension:2d} {head0:2d}->{head1:<2d} "
                    f"{sigma0: .3e} {values['norm']: .3e} "
                    f"{values['exact']: .3e} {values['harmonic']: .3e} "
                    f"{values['krylov_2']: .3e} "
                    f"{values['krylov_3']: .3e} "
                    f"{values['new_mode_filter']: .3e} "
                    f"{values['operator']: .3e} {values['k_one']: .3e} "
                    f"{values['krylov_2_gap']: .2e} "
                    f"{values['lambda_max']: .2e} "
                    f"{values['perpendicular']: .2e} {flags}"
                )
                error = abs(values["spectral"] - values["exact"])
                if error > 2.0e-8 * max(1.0, abs(values["exact"])):
                    raise RuntimeError(
                        f"spectral reconstruction failed: {error:.3e}"
                    )
                break
            break


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dx", type=float, default=0.001)
    parser.add_argument("--span", type=int, default=12)
    parser.add_argument("--heads", default="1,2,3,4,5,7,11,13,17,19")
    args = parser.parse_args()
    heads = sorted({int(value) for value in args.heads.split(",")})
    if not heads or heads[0] != 1:
        parser.error("the head list must begin with 1 (Gamma only)")
    run(args.dx, args.span, heads)


if __name__ == "__main__":
    main()
