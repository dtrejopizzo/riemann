#!/usr/bin/env python3
"""Diagnostic Gram test for finite-head coercivity on the exact complement.

This is deliberately a *diagnostic*, not an interval certificate.  It uses
the certified low critical-line ordinates supplied in ``06-grafico`` and
the exact elementary complement modes

    q_gamma(x) = cos(gamma*x) / cosh(x/2).

The weighted QR is performed before the source form is assembled.  This
avoids the catastrophic generalized-eigenvalue conditioning which occurs
if the raw cosine Gram matrix is inverted.

Only numpy is required.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve()
REPO = HERE.parents[3]
ZEROS = REPO / "06-grafico" / "zeros_10000.txt"


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    return all(n % d for d in range(2, int(math.isqrt(n)) + 1))


def prime_power_atoms(limit: int) -> list[tuple[int, float]]:
    atoms: list[tuple[int, float]] = []
    for p in range(2, limit + 1):
        if not is_prime(p):
            continue
        value = p
        while value <= limit:
            atoms.append((value, math.log(p)))
            value *= p
    atoms.sort()
    return atoms


def riemann_kernel(x: np.ndarray) -> np.ndarray:
    """Theta expansion normalized by int cosh(x/2) K(x) dx = 1/2."""
    xa = np.abs(x)
    out = np.zeros_like(xa)
    active = xa < 3.0
    y = xa[active]
    e2y = np.exp(2.0 * y)
    for m in range(1, 30):
        out[active] += (
            math.pi
            * m
            * m
            * np.exp(2.5 * y)
            * (2.0 * math.pi * m * m * e2y - 3.0)
            * np.exp(-math.pi * m * m * e2y)
        )
    h = np.cosh(x / 2.0)
    out *= 0.5 / np.trapz(h * out, x)
    return out


def gamma_convolution_setup(x: np.ndarray, dx: float, k: np.ndarray):
    size = len(x)
    nfft = 1
    while nfft < 3 * size:
        nfft *= 2
    delta = np.arange(-(size - 1), size) * dx
    adelta = np.abs(delta)
    density = np.zeros_like(adelta)
    nonzero = adelta > 0
    density[nonzero] = np.exp(-adelta[nonzero] / 2.0) / (
        -np.expm1(-2.0 * adelta[nonzero])
    )
    density_fft = np.fft.rfft(density, nfft)

    def conv(vector: np.ndarray) -> np.ndarray:
        full = np.fft.irfft(np.fft.rfft(vector, nfft) * density_fft, nfft)
        return full[size - 1 : size - 1 + size] * dx

    return conv, conv(k)


def source_gram(
    x: np.ndarray,
    dx: float,
    k: np.ndarray,
    q: np.ndarray,
    head: int,
) -> np.ndarray:
    """Gamma plus all von Mangoldt atoms m <= head on orthonormal columns q."""
    conv, gamma_rate = gamma_convolution_setup(x, dx, k)
    lq = np.empty_like(q)
    for j in range(q.shape[1]):
        lq[:, j] = k * (gamma_rate * q[:, j] - conv(k * q[:, j]))
    gram = q.T @ lq * dx

    for m, mangoldt in prime_power_atoms(head):
        u = math.log(m)
        shifted_k = np.interp(x - u, x, k, left=0.0, right=0.0)
        shifted_q = np.empty_like(q)
        for j in range(q.shape[1]):
            shifted_q[:, j] = np.interp(
                x - u, x, q[:, j], left=0.0, right=0.0
            )
        difference = q - shifted_q
        gram += (
            mangoldt
            / math.sqrt(m)
            * (difference.T @ (difference * (k * shifted_k * dx)[:, None]))
        )
    return (gram + gram.T) / 2.0


def run(dx: float, maximum_span: int, heads: list[int]) -> None:
    x_max = 3.2
    x = np.arange(-x_max, x_max + dx / 2.0, dx)
    k = riemann_kernel(x)
    h = np.cosh(x / 2.0)
    mu = 2.0 * h * k
    sqrt_weight = np.sqrt(mu * dx)
    active = sqrt_weight > 1.0e-140
    ordinates = np.loadtxt(ZEROS)[:maximum_span]

    raw = (np.cos(ordinates[:, None] * x) / h).T
    u, r = np.linalg.qr(raw[active] * sqrt_weight[active, None], mode="reduced")
    q = np.zeros_like(raw)
    q[active] = u / sqrt_weight[active, None]

    print(f"dx={dx:g}; span={maximum_span}; weighted-QR orthogonality="
          f"{np.linalg.norm(q.T @ (q * (mu * dx)[:, None]) - np.eye(maximum_span)):.3e}")
    print("relative smallest QR diagonal =",
          f"{np.min(np.abs(np.diag(r))) / np.max(np.abs(np.diag(r))):.3e}")

    for head in heads:
        gram = source_gram(x, dx, k, q, head)
        print(f"head={head}")
        for span in (4, 10, 15, 20, 30, 40, 50, maximum_span):
            if span > maximum_span:
                continue
            eigenvalues = np.linalg.eigvalsh(gram[:span, :span])
            print(f"  span={span:3d}  min={eigenvalues[0]: .12f}")

    # A simple, well-conditioned Gamma-only falsifier.
    coeff = np.array([1.0, -2.0, 2.0, -1.0])
    q4 = raw[:, :4] @ coeff
    norm = np.trapz(q4 * q4 * mu, x)
    gamma4 = source_gram(x, dx, k, q[:, :4], 1)
    # Convert coefficients from the raw basis to the weighted-QR basis.
    qr_coeff = r[:4, :4] @ coeff
    energy = float(qr_coeff @ gamma4 @ qr_coeff)
    print("Gamma-only explicit q=(1,-2,2,-1):")
    print(f"  norm={norm:.12f}; energy={energy:.12f}; quotient={energy / norm:.12f}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dx", type=float, default=0.0005)
    parser.add_argument("--span", type=int, default=50)
    parser.add_argument("--heads", default="1,2,3,4,5,7")
    args = parser.parse_args()
    run(args.dx, args.span, [int(item) for item in args.heads.split(",")])


if __name__ == "__main__":
    main()
