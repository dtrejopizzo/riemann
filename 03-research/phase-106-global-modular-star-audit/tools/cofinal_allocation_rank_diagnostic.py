#!/usr/bin/env python3
"""Rank and scalar-cost diagnostic for adaptive Gamma allocation.

This is a floating-point diagnostic, not an interval certificate.  On the
weighted-orthonormal span of the first critical-line zero modes it forms

    B = P_PNT + 2 b_K,
    W = b_Gamma - 2 b_K,
    Q_phys = B + W,

and prints the negative index of B and the sharp scalar allocation

    kappa = max(0, -lambda_min(W^{-1/2} B W^{-1/2})).

The rank inequality in 106.142 says that every positive allocation which
repairs B must have rank at least n_-(B).  The calculation below only probes
how that exact obstruction behaves on finite zero spans.
"""

from __future__ import annotations

import argparse
import math

import numpy as np

from sufficient_gate_zero_span_diagnostic import (
    ZEROS,
    convolution_operator,
    prime_gram,
    riemann_kernel,
)


def inverse_square_root(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh((matrix + matrix.T) / 2.0)
    if values[0] <= 0.0:
        raise RuntimeError(
            f"Gamma remainder is not numerically positive: {values[0]:.3e}"
        )
    return (vectors / np.sqrt(values)) @ vectors.T


def run(dx: float, xmax: float, maximum_span: int, tolerance: float) -> None:
    x = np.arange(-xmax, xmax + dx / 2.0, dx)
    kernel = riemann_kernel(x)
    h = np.cosh(x / 2.0)
    mu = 2.0 * h * kernel
    sqrt_weight = np.sqrt(mu * dx)
    active = sqrt_weight > 1.0e-145

    ordinates = np.loadtxt(ZEROS)[:maximum_span]
    raw = (np.cos(ordinates[:, None] * x) / h).T
    u_qr, _ = np.linalg.qr(
        raw[active] * sqrt_weight[active, None], mode="reduced"
    )
    q = np.zeros_like(raw)
    q[active] = u_qr / sqrt_weight[active, None]

    def ideal_density(u: np.ndarray) -> np.ndarray:
        return np.exp(u / 2.0)

    def gamma_density(u: np.ndarray) -> np.ndarray:
        out = np.zeros_like(u)
        positive = u > 0.0
        out[positive] = np.exp(-2.5 * u[positive]) / (
            -np.expm1(-2.0 * u[positive])
        )
        return out

    def kernel_density(u: np.ndarray) -> np.ndarray:
        return np.interp(
            u, x[x >= 0.0], kernel[x >= 0.0], left=0.0, right=0.0
        )

    cutoff = int(math.exp(2.0 * xmax))
    prime = prime_gram(x, dx, kernel, q, cutoff)
    ideal = convolution_operator(x, dx, kernel, q, ideal_density)
    gamma = convolution_operator(x, dx, kernel, q, gamma_density)
    b_k = convolution_operator(x, dx, kernel, q, kernel_density)

    b_matrix = prime - ideal + 2.0 * b_k
    w_matrix = gamma - 2.0 * b_k
    physical = b_matrix + w_matrix

    print(
        f"dx={dx:g}; xmax={xmax:g}; span={maximum_span}; atoms<={cutoff}; "
        f"tol={tolerance:g}"
    )
    print(
        "span  n_-(B)  min(B)          min(W)          kappa_E        "
        "min(W-B_-)      min(Qphys)"
    )
    spans = sorted(set((1, 2, 4, 8, 12, 16, 20, 30, 40, maximum_span)))
    for span in spans:
        if span > maximum_span:
            continue
        b_now = (b_matrix[:span, :span] + b_matrix[:span, :span].T) / 2.0
        w_now = (w_matrix[:span, :span] + w_matrix[:span, :span].T) / 2.0
        q_now = (physical[:span, :span] + physical[:span, :span].T) / 2.0
        b_values = np.linalg.eigvalsh(b_now)
        b_eval, b_evec = np.linalg.eigh(b_now)
        b_negative = (
            b_evec * np.maximum(-b_eval, 0.0)
        ) @ b_evec.T
        w_values = np.linalg.eigvalsh(w_now)
        winv = inverse_square_root(w_now)
        relative = winv @ b_now @ winv
        relative = (relative + relative.T) / 2.0
        kappa = max(0.0, -float(np.linalg.eigvalsh(relative)[0]))
        negative_index = int(np.count_nonzero(b_values < -tolerance))
        print(
            f"{span:4d} {negative_index:7d} "
            f"{b_values[0]: .12e} {w_values[0]: .12e} "
            f"{kappa: .12e} "
            f"{np.linalg.eigvalsh(w_now - b_negative)[0]: .12e} "
            f"{np.linalg.eigvalsh(q_now)[0]: .12e}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dx", type=float, default=0.002)
    parser.add_argument("--xmax", type=float, default=3.8)
    parser.add_argument("--span", type=int, default=30)
    parser.add_argument("--tol", type=float, default=1.0e-8)
    args = parser.parse_args()
    run(args.dx, args.xmax, args.span, args.tol)


if __name__ == "__main__":
    main()
