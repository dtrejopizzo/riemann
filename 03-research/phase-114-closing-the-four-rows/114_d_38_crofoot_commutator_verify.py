#!/usr/bin/env python3
"""Numerical certificate for the exact Crofoot translation commutator."""

from __future__ import annotations

import cmath
import math


def cfun(tau: float, r: float, L: float) -> complex:
    return math.sqrt(1.0 - r * r) / (1.0 - r * cmath.exp(1j * L * tau))


def closed_difference(tau: float, s: float, r: float, L: float) -> complex:
    num = math.sqrt(1.0 - r * r) * r * cmath.exp(1j * L * tau)
    num *= cmath.exp(-1j * L * s) - 1.0
    den = (1.0 - r * cmath.exp(1j * L * (tau - s)))
    den *= 1.0 - r * cmath.exp(1j * L * tau)
    return num / den


def main() -> None:
    for p in (2, 3, 5, 11):
        r = p ** -0.5
        L = math.log(p)
        for tau, s in ((0.17, 0.31), (-0.8, 1.2), (2.1, -0.43)):
            direct = cfun(tau - s, r, L) - cfun(tau, r, L)
            exact = closed_difference(tau, s, r, L)
            assert abs(direct - exact) < 2e-14
            assert abs(direct) > 1e-8

        period = 2.0 * math.pi / L
        for k in (-2, -1, 0, 1, 3):
            direct = cfun(0.37 - k * period, r, L) - cfun(0.37, r, L)
            assert abs(direct) < 2e-13

    print("PASS: exact commutator formula and discrete covariance subgroup")


if __name__ == "__main__":
    main()
