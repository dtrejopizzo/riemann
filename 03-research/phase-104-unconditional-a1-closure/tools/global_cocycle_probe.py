#!/usr/bin/env python3
"""Float64 diagnostic for the surviving global cocycle gate (104_20).

This is not a certificate.  It evaluates

    (Y(s_epsilon(z)-u)/Y(s_epsilon(z)) - 1) / (u(1-z))

on two Cauchy circles and extracts g_n by FFT.  Shared Borwein, Lanczos,
FFT, and float64 errors can survive the two-radius comparison.
"""

import argparse
import math
from pathlib import Path
import sys

import numpy as np

PHASE103 = Path(__file__).resolve().parents[2] / "phase-103-direct-a1-closure" / "tools"
sys.path.insert(0, str(PHASE103))
from zeta_tools import zeta_and_dzeta  # noqa: E402


LANCZOS_G = 7.0
LANCZOS = np.array([
    0.99999999999980993,
    676.5203681218851,
    -1259.1392167224028,
    771.32342877765313,
    -176.61502916214059,
    12.507343278686905,
    -0.13857109526572012,
    9.9843695780195716e-6,
    1.5056327351493116e-7,
], dtype=float)


def loggamma_lanczos(z):
    """Vectorized complex log Gamma for Re(z)>0 (the only regime used)."""
    z = np.asarray(z, dtype=complex)
    w = z - 1.0
    acc = np.full_like(z, LANCZOS[0])
    for i, coeff in enumerate(LANCZOS[1:], start=1):
        acc += coeff / (w + i)
    t = w + LANCZOS_G + 0.5
    return (0.5 * math.log(2.0 * math.pi)
            + (w + 0.5) * np.log(t) - t + np.log(acc))


def log_y(s):
    zeta, _ = zeta_and_dzeta(s)
    return (
        -math.log(4.0)
        + np.log(s)
        + 2.0 * np.log(s - 1.0)
        - 0.5 * s * math.log(math.pi)
        + loggamma_lanczos(s / 2.0)
        + 2.0 * np.log(zeta)
    )


def coefficients(nmax, epsilon, c, radius, samples):
    u = c * epsilon
    theta = 2.0 * math.pi * np.arange(samples) / samples
    z = radius * np.exp(1j * theta)
    s = 1.0 + epsilon + z / (1.0 - z)
    ratio = np.exp(log_y(s - u) - log_y(s))
    values = (ratio - 1.0) / (u * (1.0 - z))
    raw = np.fft.fft(values) / samples
    n = np.arange(nmax + 1)
    coeff = raw[n] / radius ** n
    return coeff


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmax", type=int, default=300)
    ap.add_argument("--samples", type=int, default=1 << 15)
    ap.add_argument("--r1", type=float, default=0.970)
    ap.add_argument("--r2", type=float, default=0.965)
    args = ap.parse_args()

    cases = [(1e-3, 0.5), (1e-2, 0.5), (1e-1, 0.5),
             (1.0, 0.5), (1e-1, 0.9)]
    print("FLOAT64 DIAGNOSTIC ONLY -- not a certificate")
    print(f"nmax={args.nmax} samples={args.samples} r=({args.r1},{args.r2})")
    print(" eps       c       max(g_n,n>=1)   argmax   max two-radius diff   sign")
    for epsilon, c in cases:
        g1 = coefficients(args.nmax, epsilon, c, args.r1, args.samples)
        g2 = coefficients(args.nmax, epsilon, c, args.r2, args.samples)
        real = g1.real[1:]
        idx = int(np.argmax(real)) + 1
        disagreement = float(np.max(np.abs(g1[1:] - g2[1:])))
        imag = float(np.max(np.abs(g1[1:].imag)))
        status = "negative" if float(np.max(real)) < 0.0 else "MIXED"
        print(f"{epsilon:8.3g} {c:7.3g} {float(np.max(real)):18.9e} "
              f"{idx:8d} {disagreement:21.3e}   {status}")
        print(f"          max imaginary leakage: {imag:.3e}")

    print("CAVEAT: two radii share zeta, Lanczos, FFT, and float64 errors.")


if __name__ == "__main__":
    main()
