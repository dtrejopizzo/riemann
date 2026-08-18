#!/usr/bin/env python3
"""Float64 diagnostic for the adjacent flag-Schur inequality of 104_34.

This is not a certificate.  It compares two Cauchy radii, reports the
negative-curvature blocks of H_n=lambda_n-(501/2002)A_n, and evaluates

    T_n=4 H_n d_n-(H_n+d_n-H_{n+1})^2,
    d_n=(1501/2002)(A_{n+1}-A_n)+gamma.
"""

from __future__ import annotations

import argparse
import math
import os
import sys

import numpy as np


HERE = os.path.dirname(os.path.abspath(__file__))
P103 = os.path.normpath(
    os.path.join(HERE, "..", "..", "phase-103-direct-a1-closure", "tools")
)
sys.path.insert(0, P103)

from arch_and_margin import lambda_arch  # noqa: E402
from zeta_tools import li_lambda  # noqa: E402


def negative_runs(indices: np.ndarray) -> list[tuple[int, int]]:
    if not len(indices):
        return []
    out: list[tuple[int, int]] = []
    start = previous = int(indices[0])
    for raw in indices[1:]:
        value = int(raw)
        if value != previous + 1:
            out.append((start, previous))
            start = value
        previous = value
    out.append((start, previous))
    return out


def data(nmax: int, radius: float, fft_size: int, arch: np.ndarray):
    lam = np.zeros(nmax + 1)
    lam[1:] = li_lambda(nmax, r=radius, M=fft_size)
    c = 501.0 / 2002.0
    kappa = 1.0 - c
    h = lam - c * arch
    d = kappa * (arch[1:] - arch[:-1]) + np.euler_gamma
    schur = 4.0 * h[:-1] * d - (h[:-1] + d - h[1:]) ** 2
    curvature = h[2:] - 2.0 * h[1:-1] + h[:-2]
    return lam, h, d, schur, curvature


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nmax", type=int, default=500)
    parser.add_argument("--first", type=int, default=149)
    parser.add_argument("--radius-a", type=float, default=0.985)
    parser.add_argument("--radius-b", type=float, default=0.975)
    parser.add_argument("--fft-power", type=int, default=18)
    args = parser.parse_args()
    if args.nmax <= args.first:
        raise SystemExit("need nmax > first")

    arch = np.zeros(args.nmax + 1)
    for n in range(1, args.nmax + 1):
        arch[n] = lambda_arch(n)
    fft_size = 1 << args.fft_power
    left = data(args.nmax, args.radius_a, fft_size, arch)
    right = data(args.nmax, args.radius_b, fft_size, arch)

    lam_a, h_a, _, t_a, curv_a = left
    lam_b, h_b, _, t_b, curv_b = right
    first = args.first
    t_slice = t_a[first:]
    t_index = first + int(np.argmin(t_slice))
    curv_centers = np.arange(1, args.nmax)
    bad = curv_centers[(curv_a < 0.0) & (curv_centers >= first)]

    print("DIAGNOSTIC ONLY: shared float64/FFT errors are possible")
    print(
        f"n={first}..{args.nmax} radii=({args.radius_a},{args.radius_b}) "
        f"FFT={fft_size}"
    )
    print(
        f"max lambda radius discrepancy={np.max(np.abs(lam_a-lam_b)):.6e}; "
        f"max H discrepancy={np.max(np.abs(h_a-h_b)):.6e}"
    )
    print("negative centered-curvature blocks", negative_runs(bad))
    print(
        f"min adjacent Schur T_n={t_a[t_index]:.12e} at n={t_index}; "
        f"other radius={t_b[t_index]:.12e}"
    )
    print(
        f"min H_n={np.min(h_a[first:]):.12e} at "
        f"n={first+int(np.argmin(h_a[first:]))}"
    )
    if not math.isfinite(float(np.min(t_slice))):
        raise ArithmeticError("non-finite diagnostic")
    print("PASS: diagnostic completed; no all-n sign is certified")


if __name__ == "__main__":
    main()
