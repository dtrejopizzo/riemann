#!/usr/bin/env python3
"""Finite zero-span diagnostic for the compensated physical gate.

The calculation uses weighted QR on the exact complement modes
cos(gamma*x)/cosh(x/2).  It is a floating-point falsification harness,
not an interval certificate.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np

from physical_sufficient_gate_diagnostic import (
    THETA,
    riemann_kernel,
    von_mangoldt_atoms,
)


HERE = Path(__file__).resolve()
REPO = HERE.parents[3]
ZEROS = REPO / "06-grafico" / "zeros_10000.txt"


def convolution_operator(
    x: np.ndarray,
    dx: float,
    kernel: np.ndarray,
    q: np.ndarray,
    density,
) -> np.ndarray:
    size = len(x)
    nfft = 1
    while nfft < 3 * size:
        nfft *= 2
    delta = np.arange(-(size - 1), size) * dx
    values = density(np.abs(delta))
    values[size - 1] = 0.0 if not np.isfinite(values[size - 1]) else values[size - 1]
    density_fft = np.fft.rfft(values, nfft)

    def conv(vector: np.ndarray) -> np.ndarray:
        full = np.fft.irfft(np.fft.rfft(vector, nfft) * density_fft, nfft)
        return full[size - 1 : size - 1 + size] * dx

    rate = conv(kernel)
    lq = np.empty_like(q)
    for j in range(q.shape[1]):
        lq[:, j] = kernel * (rate * q[:, j] - conv(kernel * q[:, j]))
    gram = q.T @ (lq * dx)
    return (gram + gram.T) / 2.0


def prime_gram(
    x: np.ndarray,
    dx: float,
    kernel: np.ndarray,
    q: np.ndarray,
    cutoff: int,
) -> np.ndarray:
    gram = np.zeros((q.shape[1], q.shape[1]))
    for n, mangoldt in von_mangoldt_atoms(cutoff):
        u = math.log(n)
        shifted_kernel = np.interp(x - u, x, kernel, left=0.0, right=0.0)
        shifted_q = np.empty_like(q)
        for j in range(q.shape[1]):
            shifted_q[:, j] = np.interp(
                x - u, x, q[:, j], left=0.0, right=0.0
            )
        difference = q - shifted_q
        gram += (
            mangoldt
            / math.sqrt(n)
            * difference.T
            @ (difference * (kernel * shifted_kernel * dx)[:, None])
        )
    return (gram + gram.T) / 2.0


def run(dx: float, xmax: float, maximum_span: int) -> None:
    x = np.arange(-xmax, xmax + dx / 2.0, dx)
    kernel = riemann_kernel(x)
    h = np.cosh(x / 2.0)
    mu = 2.0 * h * kernel
    sqrt_weight = np.sqrt(mu * dx)
    active = sqrt_weight > 1.0e-145
    ordinates = np.loadtxt(ZEROS)[:maximum_span]
    raw = (np.cos(ordinates[:, None] * x) / h).T
    u_qr, r_qr = np.linalg.qr(
        raw[active] * sqrt_weight[active, None], mode="reduced"
    )
    q = np.zeros_like(raw)
    q[active] = u_qr / sqrt_weight[active, None]

    def ideal_density(u: np.ndarray) -> np.ndarray:
        return np.exp(u / 2.0)

    def gamma_remainder_density(u: np.ndarray) -> np.ndarray:
        out = np.zeros_like(u)
        positive = u > 0.0
        out[positive] = np.exp(-2.5 * u[positive]) / (
            -np.expm1(-2.0 * u[positive])
        )
        return out

    def k_density(u: np.ndarray) -> np.ndarray:
        return np.interp(u, x[x >= 0.0], kernel[x >= 0.0], left=0.0, right=0.0)

    cutoff = int(math.exp(2.0 * xmax))
    p = prime_gram(x, dx, kernel, q, cutoff)
    ideal = convolution_operator(x, dx, kernel, q, ideal_density)
    gamma = convolution_operator(x, dx, kernel, q, gamma_remainder_density)
    b_k = convolution_operator(x, dx, kernel, q, k_density)

    p_pnt = p - ideal
    q_phys = p_pnt + gamma
    q_old = p_pnt + THETA * gamma
    q_suff = p_pnt + 2.0 * b_k + THETA * gamma
    margin = (1.0 - THETA) * gamma - 2.0 * b_k

    print(
        f"dx={dx:g}; xmax={xmax:g}; span={maximum_span}; atoms<={cutoff}; "
        f"orth={np.linalg.norm(q.T @ (q * (mu * dx)[:, None]) - np.eye(maximum_span)):.3e}"
    )
    print(
        "span        min(Qphys)        min(Qold)       min(Qsuff)      min(margin)"
    )
    spans = sorted(set((1, 2, 4, 8, 12, 16, 20, 30, 40, maximum_span)))
    for span in spans:
        if span > maximum_span:
            continue
        values = []
        for matrix in (q_phys, q_old, q_suff, margin):
            values.append(np.linalg.eigvalsh(matrix[:span, :span])[0])
        print(
            f"{span:4d} " + " ".join(f"{value: .12e}" for value in values)
        )

    # A fixed, non-optimized complement witness.  Since
    #
    #     raw = q @ r_qr,
    #
    # its coordinates in the weighted-orthonormal q basis are r_qr @ a.
    # Keeping integer coefficients makes this row suitable for a later
    # outward-interval certification; the values printed here remain only
    # floating-point diagnostics.
    if maximum_span >= 4:
        raw_coefficients = np.array([4.0, -15.0, 16.0, -5.0])
        coordinates = r_qr[:4, :4] @ raw_coefficients
        norm = float(coordinates @ coordinates)
        print("fixed witness raw coefficients: 4, -15, 16, -5")
        print(f"  norm    {norm: .15e}")
        for name, matrix in (
            ("Qphys", q_phys),
            ("Qold", q_old),
            ("Qsuff", q_suff),
            ("margin", margin),
        ):
            value = float(coordinates @ matrix[:4, :4] @ coordinates)
            print(f"  {name:6s}  {value: .15e}   quotient={value / norm: .15e}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dx", type=float, default=0.002)
    parser.add_argument("--xmax", type=float, default=3.8)
    parser.add_argument("--span", type=int, default=30)
    args = parser.parse_args()
    run(args.dx, args.xmax, args.span)


if __name__ == "__main__":
    main()
