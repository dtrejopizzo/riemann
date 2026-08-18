#!/usr/bin/env python3
"""Diagnostic for the Gamma row constant in 106.145.

This is a floating-point normalization check only.  The theorem that the
row constant is unbounded is analytic and does not depend on this script.
"""

from __future__ import annotations

import math

import numpy as np


def theta_kernel(x: np.ndarray, terms: int = 12) -> np.ndarray:
    y = np.abs(x)
    e2y = np.exp(2.0 * y)
    out = np.zeros_like(y)
    for m in range(1, terms + 1):
        mm = float(m * m)
        out += (
            2.0
            * math.pi
            * mm
            * np.exp(2.5 * y)
            * (2.0 * math.pi * mm * e2y - 3.0)
            * np.exp(-math.pi * mm * e2y)
        )
    return out


def gamma_density(u: np.ndarray) -> np.ndarray:
    return np.exp(-2.5 * u) / (-np.expm1(-2.0 * u))


def main() -> None:
    # At x=0 the exact row formula reduces to an even one-dimensional
    # integral.  The theta tail beyond 8 is far below float64 resolution.
    u = np.linspace(1.0e-8, 8.0, 2_000_001)
    k = theta_kernel(u)
    integrand = k * np.cosh(0.5 * u) ** 2 / gamma_density(u)
    half_integral = float(np.trapz(integrand, u))

    c_k = 0.5
    row_constant = 4.0 * half_integral / c_k**3

    # Independent normalization check for int_R cosh(x/2)K(x) dx=1/2.
    c_k_numeric = float(
        2.0 * np.trapz(np.cosh(0.5 * u) * k, u)
    )

    print(f"c_K numeric       = {c_k_numeric:.10f}")
    print(f"S_Gamma(0)        = {row_constant:.10f}")
    print("theorem status    = diagnostic only; sup_x S_Gamma(x)=infinity analytically")


if __name__ == "__main__":
    main()
