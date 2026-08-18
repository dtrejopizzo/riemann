#!/usr/bin/env python3
"""Diagnostic for joint-prime observation distances and Kalman gains.

For a weighted-orthonormal zero-mode basis this script compares, row by
row,

    * the signed Schur deficit at a finite head X0;
    * the observation-space distance supplied by a consecutive block of
      literal prime-power atoms;
    * the exact adaptive Schur/Kalman gain produced by that block.

The identity behind the comparison is

    Delta_B >= dist(D_B phi_M, D_B V_{M-1})**2.

All integrations and eigensolves use float64 quadrature.  The output is a
diagnostic, not an interval certificate.
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve()
sys.path.insert(0, str(HERE.parent))

from finite_head_mean_periodic_gram import (  # noqa: E402
    ZEROS,
    riemann_kernel,
    source_gram,
)


def schur_pivot(matrix: np.ndarray, dimension: int) -> float:
    """Return the last Schur pivot of the leading ``dimension`` block."""
    block = matrix[:dimension, :dimension]
    if dimension == 1:
        return float(block[0, 0])
    old = block[:-1, :-1]
    cross = block[:-1, -1]
    return float(block[-1, -1] - cross @ np.linalg.solve(old, cross))


def observation_distance(block: np.ndarray, dimension: int) -> tuple[float, float]:
    """Distance square and determinant-ratio cross-check for one row."""
    gram = block[:dimension, :dimension]
    if dimension == 1:
        return float(gram[0, 0]), float(gram[0, 0])
    old = gram[:-1, :-1]
    cross = gram[:-1, -1]
    distance = float(gram[-1, -1] - cross @ np.linalg.solve(old, cross))
    sign_full, logdet_full = np.linalg.slogdet(gram)
    sign_old, logdet_old = np.linalg.slogdet(old)
    ratio = float(sign_full * sign_old * math.exp(logdet_full - logdet_old))
    return distance, ratio


def augmented_gain_ratio(
    defect: np.ndarray, block: np.ndarray, dimension: int
) -> tuple[float, float]:
    """Evaluate the exact gain and its directional Cauchy lower bound."""
    old_defect = defect[: dimension - 1, : dimension - 1]
    old_cross = defect[: dimension - 1, dimension - 1]
    regression = np.linalg.solve(old_defect, old_cross)

    observation_old = block[: dimension - 1, : dimension - 1]
    observation_cross = block[: dimension - 1, dimension - 1]
    observation_new = float(block[dimension - 1, dimension - 1])
    residual_cross = observation_cross - observation_old @ regression
    residual_norm = float(
        observation_new
        - 2.0 * regression @ observation_cross
        + regression @ observation_old @ regression
    )
    augmented_old = old_defect + observation_old
    augmented = np.block(
        [
            [augmented_old, residual_cross[:, None]],
            [residual_cross[None, :], np.array([[residual_norm]])],
        ]
    )
    sign_augmented, logdet_augmented = np.linalg.slogdet(augmented)
    sign_old, logdet_old = np.linalg.slogdet(augmented_old)
    exact = float(
        sign_augmented
        * sign_old
        * math.exp(logdet_augmented - logdet_old)
    )
    directional_cost = float(
        residual_cross @ np.linalg.solve(old_defect, residual_cross)
    )
    directional = residual_norm**2 / (residual_norm + directional_cost)
    return exact, directional


def weighted_zero_basis(
    dx: float, span: int
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    x_max = 3.2
    x = np.arange(-x_max, x_max + dx / 2.0, dx)
    kernel = riemann_kernel(x)
    measure = 2.0 * np.cosh(x / 2.0) * kernel
    sqrt_weight = np.sqrt(measure * dx)
    active = sqrt_weight > 1.0e-140
    ordinates = np.loadtxt(ZEROS)[:span]
    raw = (
        np.cos(ordinates[:, None] * x) / np.cosh(x[None, :] / 2.0)
    ).T
    orthogonal, _ = np.linalg.qr(
        raw[active] * sqrt_weight[active, None], mode="reduced"
    )
    basis = np.zeros_like(raw)
    basis[active] = orthogonal / sqrt_weight[active, None]
    return x, kernel, measure, basis


def run(dx: float, span: int, heads: list[int]) -> None:
    x, kernel, measure, basis = weighted_zero_basis(dx, span)
    norm_error = np.linalg.norm(
        basis.T @ (basis * (measure * dx)[:, None]) - np.eye(span)
    )
    source = {
        head: source_gram(x, dx, kernel, basis, head) for head in heads
    }
    defects = {head: source[head] - 0.5 * np.eye(span) for head in heads}

    print(f"dx={dx:g}; span={span}; norm-orthogonality={norm_error:.3e}")
    print(
        "M  X0->X1  min(A0)       sigma0       dist2        "
        "det-ratio    exact-gain   aug-ratio    dir-bound    "
        "dir/gain     closes  dir-closes"
    )

    for dimension in range(2, span + 1):
        for left_index, head0 in enumerate(heads[:-1]):
            preceding = defects[head0][: dimension - 1, : dimension - 1]
            minimum = float(np.linalg.eigvalsh(preceding)[0])
            if minimum <= 1.0e-9:
                continue
            sigma0 = schur_pivot(defects[head0], dimension)
            for head1 in heads[left_index + 1 :]:
                block = source[head1] - source[head0]
                distance, ratio = observation_distance(block, dimension)
                sigma1 = schur_pivot(defects[head1], dimension)
                gain = sigma1 - sigma0
                augmented, directional = augmented_gain_ratio(
                    defects[head0], block, dimension
                )
                tolerance = 5.0e-8 * max(1.0, abs(gain), abs(distance))
                if gain + tolerance < distance:
                    flag = "BOUND-FAIL"
                elif sigma1 > 0.0:
                    flag = "yes"
                else:
                    flag = "no"
                directional_flag = "yes" if sigma0 + directional > 0.0 else "no"
                print(
                    f"{dimension:2d} {head0:3d}->{head1:<3d} "
                    f"{minimum: .3e} {sigma0: .3e} {distance: .3e} "
                    f"{ratio: .3e} {gain: .3e} {augmented: .3e} "
                    f"{directional: .3e} {directional/gain: .3e} "
                    f"{flag:>3s} {directional_flag:>3s}"
                )
            # Use the first head which has closed the preceding row.
            break


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dx", type=float, default=0.001)
    parser.add_argument("--span", type=int, default=12)
    parser.add_argument("--heads", default="1,2,3,4,5,7,11,13,17,19")
    args = parser.parse_args()
    heads = sorted({int(value) for value in args.heads.split(",")})
    if heads[0] != 1:
        parser.error("the head list must begin with 1 (Gamma only)")
    run(args.dx, args.span, heads)


if __name__ == "__main__":
    main()
