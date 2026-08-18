#!/usr/bin/env python3
"""Certificates for the Fourier--J multiplier audit in D.39."""

from __future__ import annotations

import mpmath as mp


def gamma_factor(s: complex) -> complex:
    return mp.pi ** (mp.mpf("0.5") - s) * mp.gamma(s / 2) / mp.gamma((1 - s) / 2)


def f(x: mp.mpf) -> mp.mpf:
    return x**2 * (x**2 - 3 / (2 * mp.pi)) * mp.e ** (-mp.pi * x**2)


def main() -> None:
    mp.mp.dps = 60
    for tau in (mp.mpf("0.1"), mp.mpf("1"), mp.mpf("10")):
        s = mp.mpf("0.5") + 1j * tau
        assert abs(abs(gamma_factor(s)) - 1) < mp.mpf("1e-50")
        assert abs(gamma_factor(s) * gamma_factor(1 - s) - 1) < mp.mpf("1e-50")

    real_integral = 2 * mp.quad(lambda x: f(x), [0, mp.inf])
    mellin_zero = mp.quad(lambda x: f(x) / x, [0, mp.inf])
    assert abs(real_integral) < mp.mpf("1e-50")
    assert abs(mellin_zero + 1 / (4 * mp.pi**2)) < mp.mpf("1e-50")
    assert abs(mp.zeta(0) * mellin_zero - 1 / (8 * mp.pi**2)) < mp.mpf("1e-50")

    print("PASS: central unitarity, primitive witness, and nonzero Mellin residue")


if __name__ == "__main__":
    main()
