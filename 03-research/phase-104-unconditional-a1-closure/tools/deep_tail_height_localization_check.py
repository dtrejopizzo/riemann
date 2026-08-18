#!/usr/bin/env python3
"""Checks for 104_76: quartet geometry and the X^(1/4) scale."""

from __future__ import annotations

import cmath
import math


def quartet_direct(n: int, rho: complex) -> float:
    zeros = (rho, rho.conjugate(), 1.0 - rho, 1.0 - rho.conjugate())
    return sum((1.0 - (1.0 - 1.0 / z) ** n).real for z in zeros)


def quartet_closed(n: int, rho: complex) -> float:
    w = 1.0 - 1.0 / rho
    return 4.0 - 2.0 * (w**n + w ** (-n)).real


def check_quartet_and_radial_bound() -> None:
    for beta in (0.5, 0.61, 0.9):
        for gamma in (14.2, 30.0, 100.0):
            rho = complex(beta, gamma)
            w = 1.0 - 1.0 / rho
            a = -math.log(abs(w))
            assert a >= -1e-15
            assert a <= 1.0 / (2.0 * gamma * gamma) + 1e-15
            for n in (1, 2, 7, 31):
                # At beta=1/2 the explicit four-point tuple repeats each zero;
                # both formulas deliberately use that doubled convention.
                assert abs(quartet_direct(n, rho) - quartet_closed(n, rho)) < 1e-8


def check_very_high_tail_pointwise_bound() -> None:
    # The proof uses an absolute constant in |q_n| <= C n^2/gamma^2.
    # C=10 safely covers the elementary estimates on this grid.
    for x in (10, 50, 200):
        for n in (1, x // 2, x):
            for gamma in (2.01 * x, 3.0 * x, 10.0 * x):
                rho = complex(0.9, gamma)
                q = abs(quartet_closed(n, rho))
                assert q <= 10.0 * n * n / (gamma * gamma)


def check_scale_separation() -> None:
    # log[X log X exp(sqrt(X)/2) / exp(sqrt(X))] -> -infinity.
    vals = []
    for x in (10**4, 10**6, 10**8):
        log_ratio = math.log(x) + math.log(math.log(x)) - 0.5 * math.sqrt(x)
        vals.append(log_ratio)
    assert vals[-1] < vals[-2] < vals[0]
    assert vals[-1] < -1000.0


def check_rational_falsifier() -> None:
    # For w=2i, deep negative excursions occur at multiples of four.
    # Their harmonic mass from sqrt(X) to X tends to 1/8 of H_X.
    for x in (10_000, 100_000):
        lower = math.ceil(math.sqrt(x) / math.log(2.0))
        h_x = sum(1.0 / n for n in range(1, x + 1))
        mass = sum(1.0 / n for n in range(lower, x + 1) if n % 4 == 0)
        ratio = mass / h_x
        assert 0.07 < ratio < 0.15


def main() -> None:
    check_quartet_and_radial_bound()
    check_very_high_tail_pointwise_bound()
    check_scale_separation()
    check_rational_falsifier()
    print("deep_tail_height_localization_check: PASS")


if __name__ == "__main__":
    main()
