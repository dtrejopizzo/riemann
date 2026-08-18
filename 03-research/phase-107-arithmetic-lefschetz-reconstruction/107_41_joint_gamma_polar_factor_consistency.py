#!/usr/bin/env python3
"""Consistency audit for the joint Gamma--polar factor.

This script checks the explicit archimedean identity used in `107_05`
and imported by `107_09`:

    A_infty(s)
      = 1/2 * s * (s - 1) * pi^(-s/2) * Gamma(s/2)
      = sqrt(pi) * (2*pi)^(-s/2) * det_triv(s) / det_gamma(s),

where

    det_triv(s)  = s(s-1),
    det_gamma(s) = sqrt(2*pi) * 2^(1/2 - s/2) / Gamma(s/2).

The purpose is narrow: numerically verify that the Gamma and polar
factors enter as one coupled archimedean expression at representative
sample points.  The script is self-contained and uses a Lanczos
approximation for the complex Gamma function.
"""

from __future__ import annotations

import cmath
import math


LANCZOS_G = 7
LANCZOS_COEFFS = [
    0.99999999999980993,
    676.5203681218851,
    -1259.1392167224028,
    771.3234287776531,
    -176.6150291621406,
    12.507343278686905,
    -0.13857109526572012,
    9.984369578019572e-6,
    1.5056327351493116e-7,
]


def complex_gamma(z: complex) -> complex:
    if z.real < 0.5:
        return math.pi / (cmath.sin(math.pi * z) * complex_gamma(1 - z))
    z_minus_1 = z - 1
    x = LANCZOS_COEFFS[0]
    for i, coeff in enumerate(LANCZOS_COEFFS[1:], start=1):
        x += coeff / (z_minus_1 + i)
    t = z_minus_1 + LANCZOS_G + 0.5
    return cmath.sqrt(2 * math.pi) * (t ** (z_minus_1 + 0.5)) * cmath.exp(-t) * x


def det_gamma(s: complex) -> complex:
    return cmath.sqrt(2 * math.pi) * (2 ** (0.5 - s / 2)) / complex_gamma(s / 2)


def det_triv(s: complex) -> complex:
    return s * (s - 1)


def a_infty_closed(s: complex) -> complex:
    return 0.5 * s * (s - 1) * (math.pi ** (-s / 2)) * complex_gamma(s / 2)


def a_infty_ratio(s: complex) -> complex:
    return (
        math.sqrt(math.pi)
        * ((2 * math.pi) ** (-s / 2))
        * det_triv(s)
        / det_gamma(s)
    )


def main() -> None:
    samples = [
        2.0 + 0.0j,
        1.5 + 0.0j,
        2.0 + 3.0j,
        0.5 + 14.134725141734694j,
        0.5 + 85.7j,
    ]

    print("Joint Gamma--polar factor consistency audit")
    print(" sample s                      |A_closed - A_ratio|")
    for s in samples:
        lhs = a_infty_closed(s)
        rhs = a_infty_ratio(s)
        diff = abs(lhs - rhs)
        assert diff < 1e-12
        print(f" {str(s):28s} {diff:.3e}")

    print("\nAll joint Gamma--polar factor consistency checks passed.")


if __name__ == "__main__":
    main()
