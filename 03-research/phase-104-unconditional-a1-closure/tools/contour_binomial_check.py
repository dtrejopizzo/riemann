#!/usr/bin/env python3
"""Audit the binomial contour for R(t)=-d log(t*zeta(1+t))/dt.

The FFT part is deliberately diagnostic (complex128).  With --certified the
same three lambda values are also enclosed by the outward fixed-point engine
used in 103_51.  The theorem checked algebraically is

    C_n = [z^n] (1-z)^(-1) R(z/(1-z)),
    lambda_N = A_N - sum_{n=0}^{N-1} C_n.

No deformation across zeta zeros is used by this program.
"""

from __future__ import annotations

import argparse
from math import comb
from pathlib import Path
import runpy
import sys

import numpy as np


HERE = Path(__file__).resolve().parent
P103 = HERE.parents[1] / "phase-103-direct-a1-closure" / "tools"
sys.path.insert(0, str(P103))

from arch_and_margin import GAMMA, lambda_arch  # noqa: E402
from zeta_tools import li_lambda, zeta_and_dzeta  # noqa: E402


def contour_coefficients(top: int, radius: float, points: int) -> np.ndarray:
    """Return C_0,...,C_top-1 by Cauchy extraction in the z-plane."""
    theta = 2.0 * np.pi * np.arange(points) / points
    z = radius * np.exp(1j * theta)
    t = z / (1.0 - z)
    s = 1.0 + t
    zeta, dzeta = zeta_and_dzeta(s)
    R = -dzeta / zeta - 1.0 / t
    generating = R / (1.0 - z)
    fft = np.fft.fft(generating) / points
    degree = np.arange(top)
    return (fft[:top] / radius**degree).real


def reconstructed_lambdas(top: int, radius: float, points: int) -> np.ndarray:
    C = contour_coefficients(top, radius, points)
    return np.array(
        [lambda_arch(n) - np.sum(C[:n]) for n in range(1, top + 1)],
        dtype=float,
    )


def certified_lambda_intervals(indices: tuple[int, ...], K: int, terms: int):
    """Outward intervals from exactly the 103_51 coefficient pipeline."""
    top = max(indices)
    eg = runpy.run_path(str(P103 / "eta_fixed_generator.py"))
    em = runpy.run_path(str(P103 / "stieltjes_em_interval_pilot.py"))
    F, S = eg["F"], eg["S"]

    def qfix(value):
        return eg["qf"](value)

    q = eg["q_coeffs"](K, top, terms)
    p = [F(0) for _ in range(top + 1)]
    for n in range(1, top + 1):
        value = q[n]
        for k in range(1, n):
            value = value - (p[k] * q[n - k]).mul_int(k).div(n)
        p[n] = value

    old = em["ns"]
    log4pi = qfix(old["log4pi"])
    zeta_values = {k: qfix(v) for k, v in old["zeta"].items() if k <= top}
    for k in range(9, top + 1):
        zeta_values[k] = qfix(em["zeta_interval"](k))

    answer = {}
    for n in indices:
        prime = F(0)
        for k in range(1, n + 1):
            prime = prime + p[k].mul_int(n * comb(n - 1, k - 1))
        arch = F(S) - (q[1] + log4pi).mul_int(n).div(2)
        for k in range(2, n + 1):
            multiplier = (-1 if k % 2 else 1) * comb(n, k) * (2**k - 1)
            arch = arch + zeta_values[k].mul_int(multiplier).div(2**k)
        lam = prime + arch
        answer[n] = (lam.l / S, lam.h / S)
    return answer


def trivial_zero_table(indices: tuple[int, ...], cutoff: int = 200001):
    """Compare the canonical trivial block with Delta A+c-1."""
    c = 0.5 * (GAMMA + np.log(4.0 * np.pi))
    rows = []
    for n in indices:
        canonical = 0.0
        raw = 0.0
        for a in range(3, cutoff + 1, 2):
            x = 1.0 - 1.0 / a
            canonical += -np.expm1(n * np.log1p(-1.0 / a)) / a
            raw -= x**n / a
        exact = lambda_arch(n + 1) - lambda_arch(n) + c - 1.0
        rows.append((n, canonical, exact, exact - canonical, raw))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--points", type=int, default=1 << 16)
    parser.add_argument("--radius-a", type=float, default=0.90)
    parser.add_argument("--radius-b", type=float, default=0.92)
    parser.add_argument("--direct-radius", type=float, default=0.97)
    parser.add_argument("--certified", action="store_true")
    parser.add_argument("--K", type=int, default=830)
    parser.add_argument("--terms", type=int, default=800)
    args = parser.parse_args()

    indices = (20, 60, 149)
    top = max(indices)
    rec_a = reconstructed_lambdas(top, args.radius_a, args.points)
    rec_b = reconstructed_lambdas(top, args.radius_b, args.points)
    direct = li_lambda(top, r=args.direct_radius, M=args.points)

    print("DIAGNOSTIC complex128 contour check (not a certificate)")
    print(" n       lambda(contour)       lambda(xi)       disagreement   radius-stability")
    for n in indices:
        disagreement = rec_b[n - 1] - direct[n - 1]
        stability = rec_b[n - 1] - rec_a[n - 1]
        print(
            f"{n:3d}  {rec_b[n-1]: .12f}  {direct[n-1]: .12f}"
            f"  {disagreement: .3e}  {stability: .3e}"
        )

    print("\nTRIVIAL ZEROS: canonical partial sum versus Delta A + c - 1")
    print(" n       partial canonical       exact block       tail       raw partial")
    for n, partial, exact, tail, raw in trivial_zero_table(indices):
        print(f"{n:3d}  {partial: .12f}  {exact: .12f}  {tail: .3e}  {raw: .6f}")
    print("The raw column diverges like -(1/2)log(cutoff); it is not a residue sum.")

    if args.certified:
        print("\nCERTIFIED outward intervals from the 103_51 engine")
        intervals = certified_lambda_intervals(indices, args.K, args.terms)
        for n in indices:
            lo, hi = intervals[n]
            value = rec_b[n - 1]
            inside = lo <= value <= hi
            distance = max(lo - value, value - hi, 0.0)
            # This tolerance labels compatibility of the float64 diagnostic;
            # it never enlarges the certified interval or certifies the FFT.
            float_floor = 5e-12 * (1.0 + abs(value))
            compatible = distance <= max(float_floor, abs(rec_b[n-1] - rec_a[n-1]))
            print(
                f"{n:3d}  [{lo:.12f}, {hi:.12f}]  strict_inside={inside}"
                f"  float64_compatible={compatible}"
            )


if __name__ == "__main__":
    main()
