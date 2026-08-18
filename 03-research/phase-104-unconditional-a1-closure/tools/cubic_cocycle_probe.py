#!/usr/bin/env python3
"""Float64 diagnostic for the cubic-margin cocycle of 104_22.

For a real r > 1, put (as a local logarithmic germ)

    Y_r(s) = xi(s)^r / (s*pi^(-s/2)*Gamma(s/2)).

The script extracts coefficients of either

    (Y_r(s_epsilon(z)-u)/Y_r(s_epsilon(z)) - 1)/(u*(1-z)).

or the direct-margin normalization with denominator ``u*(1-z)^2``.

The first limit is ``-Delta(r*lambda_n-A_n)``.  Coefficient ``n-1`` of the
second tends directly to ``-(r*lambda_n-A_n)``.  This program is a two-radius
numerical diagnostic only; it is not an interval certificate.
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
    for i, coefficient in enumerate(LANCZOS[1:], start=1):
        acc += coefficient / (w + i)
    t = w + LANCZOS_G + 0.5
    return (0.5 * math.log(2.0 * math.pi)
            + (w + 0.5) * np.log(t) - t + np.log(acc))


def log_y_r(s, power):
    """A consistent logarithm of Y_r in the right-half-plane probe."""
    zeta, _ = zeta_and_dzeta(s)
    return (
        -power * math.log(2.0)
        + (power - 1.0) * np.log(s)
        + power * np.log(s - 1.0)
        - 0.5 * (power - 1.0) * s * math.log(math.pi)
        + (power - 1.0) * loggamma_lanczos(s / 2.0)
        + power * np.log(zeta)
    )


def coefficients(nmax, epsilon, c, power, denominator_power, radius, samples):
    u = c * epsilon
    theta = 2.0 * math.pi * np.arange(samples) / samples
    z = radius * np.exp(1j * theta)
    s = 1.0 + epsilon + z / (1.0 - z)
    ratio = np.exp(log_y_r(s - u, power) - log_y_r(s, power))
    values = (ratio - 1.0) / (u * (1.0 - z) ** denominator_power)
    raw = np.fft.fft(values) / samples
    n = np.arange(nmax + 1)
    return raw[n] / radius ** n


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--nmax", type=int, default=300)
    parser.add_argument("--samples", type=int, default=1 << 15)
    parser.add_argument("--r1", type=float, default=0.970)
    parser.add_argument("--r2", type=float, default=0.965)
    parser.add_argument("--powers", type=float, nargs="+", default=[2.0, 3.0, 4.0, 6.0])
    parser.add_argument("--epsilon", type=float, default=0.1)
    parser.add_argument("--c", type=float, default=0.5)
    parser.add_argument("--mode", choices=("direct", "difference"),
                        default="direct")
    parser.add_argument("--min-index", type=int, default=None,
                        help="first extracted coefficient included in the sign summary")
    args = parser.parse_args()

    print("FLOAT64 DIAGNOSTIC ONLY -- not a certificate")
    print(f"nmax={args.nmax} samples={args.samples} r=({args.r1},{args.r2})")
    print(f"epsilon={args.epsilon} c={args.c} mode={args.mode}")
    denominator_power = 2 if args.mode == "direct" else 1
    default_start = 0 if args.mode == "direct" else 1
    start = default_start if args.min_index is None else args.min_index
    if start < default_start or start > args.nmax:
        raise ValueError("min-index is outside the extracted range")
    print(f"summary uses coefficient indices {start}..{args.nmax}")
    print(" power       max(coef)   argmax   max two-radius diff   sign")
    for power in args.powers:
        if power <= 1:
            raise ValueError("every power must be greater than 1")
        g1 = coefficients(args.nmax, args.epsilon, args.c, power,
                          denominator_power,
                          args.r1, args.samples)
        g2 = coefficients(args.nmax, args.epsilon, args.c, power,
                          denominator_power,
                          args.r2, args.samples)
        real = g1.real[start:]
        index = int(np.argmax(real)) + start
        disagreement = float(np.max(np.abs(g1[start:] - g2[start:])))
        imaginary = float(np.max(np.abs(g1[start:].imag)))
        status = "negative" if float(np.max(real)) < 0.0 else "MIXED"
        print(f"{power:8.5g} {float(np.max(real)):18.9e} {index:8d} "
              f"{disagreement:21.3e}   {status}")
        print(f"         max imaginary leakage: {imaginary:.3e}")

    print("CAVEAT: two radii share zeta, Lanczos, FFT, and float64 errors.")


if __name__ == "__main__":
    main()
