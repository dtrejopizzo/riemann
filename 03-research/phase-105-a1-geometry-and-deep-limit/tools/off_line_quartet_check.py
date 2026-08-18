#!/usr/bin/env python3
"""Numerical diagnostics for the exact quartet identities in 105_02."""

from __future__ import annotations

import cmath
import math


def cayley(rho: complex) -> complex:
    return 1.0 - 1.0 / rho


def direct_quartet(rho: complex, n: int) -> complex:
    orbit = (rho, rho.conjugate(), 1.0 - rho, 1.0 - rho.conjugate())
    return sum(1.0 - cayley(z) ** n for z in orbit)


def closed_quartet(rho: complex, n: int) -> float:
    w = cayley(rho)
    a = -math.log(abs(w))
    theta = cmath.phase(w)
    return 4.0 - 4.0 * math.cosh(n * a) * math.cos(n * theta)


def critical_pair(gamma: float, n: int) -> complex:
    rho = 0.5 + 1j * gamma
    return sum(1.0 - cayley(z) ** n for z in (rho, rho.conjugate()))


def main() -> None:
    rho = 0.7 + 14.134725141734695j
    for n in range(1, 201):
        direct = direct_quartet(rho, n)
        closed = closed_quartet(rho, n)
        assert abs(direct.imag) < 2e-9
        assert abs(direct.real - closed) < 2e-8 * max(1.0, abs(closed))

        pair = critical_pair(rho.imag, n)
        assert abs(pair.imag) < 2e-12
        assert -2e-12 <= pair.real <= 4.0 + 2e-12

    w = cayley(rho)
    modulus_identity = 1.0 + (1.0 - 2.0 * rho.real) / abs(rho) ** 2
    assert abs(abs(w) ** 2 - modulus_identity) < 2e-15
    assert abs(w) < 1.0

    print("PASS: Cayley modulus identity")
    print("PASS: direct quartet equals 4 - 4 cosh(n a) cos(n theta)")
    print("PASS: critical-line conjugate-pair contribution lies in [0, 4]")


if __name__ == "__main__":
    main()
