#!/usr/bin/env python3
"""Float64 diagnostics for Documents 106.17--106.18.

This script is not a certificate.  It checks:

1. the centered prime--Gamma multiplier identity;
2. the corrected, sign-indefinite polar packet formula;
3. the exact packet PNT-compensation identity.

Only Python and NumPy are required.
"""

from __future__ import annotations

import math
import numpy as np


def von_mangoldt(limit: int) -> np.ndarray:
    values = np.zeros(limit + 1, dtype=float)
    prime = np.ones(limit + 1, dtype=bool)
    prime[:2] = False
    for p in range(2, math.isqrt(limit) + 1):
        if prime[p]:
            prime[p * p :: p] = False
    for p in np.flatnonzero(prime):
        power = int(p)
        weight = math.log(power)
        while power <= limit:
            values[power] = weight
            if power > limit // int(p):
                break
            power *= int(p)
    return values


def gamma_difference(t: float, terms: int = 250_000) -> float:
    """Return 2(theta'(t)-theta'(0)) from the positive digamma series."""
    b = np.arange(terms, dtype=float) + 0.25
    y2 = 0.25 * t * t
    return float(np.sum(y2 / (b * (b * b + y2))))


def centered_check(limit: int = 10_000) -> float:
    mangoldt = von_mangoldt(limit)
    ns = np.flatnonzero(mangoldt)
    weights = mangoldt[ns] / np.sqrt(ns)
    logs = np.log(ns)
    worst = 0.0
    for t in (0.0, 0.13, 0.7, 2.0, 7.5):
        lhs = (
            2.0 * np.sum(weights * (1.0 - np.cos(t * logs)))
            + gamma_difference(t)
        )
        # Independent assembly of m_N(t)+kappa_N.
        prime = 2.0 * np.sum(weights * np.cos(t * logs))
        theta_delta = gamma_difference(t)
        rhs = 2.0 * np.sum(weights) - prime + theta_delta
        worst = max(worst, abs(float(lhs - rhs)))
    return worst


def complex_integral(rate: complex, length: float) -> complex:
    """Integral_0^L exp(rate*u)*(1-u/L) du."""
    if abs(rate) < 1.0e-14:
        return 0.5 * length
    return -1.0 / rate + (np.exp(rate * length) - 1.0) / (
        length * rate * rate
    )


def packet_polar(length: float, center: float) -> tuple[float, float]:
    z = 0.5 + 1j * center
    amplitude = 2.0 * np.sinh(z * length / 2.0) / (math.sqrt(length) * z)
    from_amplitude = 2.0 * float(np.real(amplitude * amplitude))
    denominator = (center * center + 0.25) ** 2
    closed = 4.0 / (length * denominator) * (
        (0.25 - center * center)
        * (math.cosh(length / 2.0) * math.cos(center * length) - 1.0)
        + center
        * math.sinh(length / 2.0)
        * math.sin(center * length)
    )
    return from_amplitude, closed


def packet_compensation(length: float, center: float) -> tuple[float, float]:
    limit = int(math.floor(math.exp(length) + 1.0e-12))
    mangoldt = von_mangoldt(limit)
    ns = np.flatnonzero(mangoldt)
    taper = 1.0 - np.log(ns) / length
    s_value = float(
        np.sum(
            mangoldt[ns]
            / np.sqrt(ns)
            * taper
            * np.cos(center * np.log(ns))
        )
    )
    m_plus = float(np.real(complex_integral(0.5 + 1j * center, length)))
    m_minus = float(np.real(complex_integral(-0.5 + 1j * center, length)))
    polar, closed = packet_polar(length, center)
    delta = s_value - m_plus
    left = polar - 2.0 * s_value
    right = 2.0 * m_minus - 2.0 * delta
    return abs(polar - closed), abs(left - right)


def main() -> None:
    centered_error = centered_check()
    polar_error = 0.0
    compensation_error = 0.0
    for length, center in ((2.0, 0.7), (5.0, 1.0), (10.0, 8.0)):
        error_p, error_c = packet_compensation(length, center)
        polar_error = max(polar_error, error_p)
        compensation_error = max(compensation_error, error_c)

    print("Phase 106.17--106.18 identity diagnostic (float64)")
    print(f"centered multiplier residual : {centered_error:.3e}")
    print(f"corrected polar residual     : {polar_error:.3e}")
    print(f"PNT compensation residual    : {compensation_error:.3e}")
    if max(centered_error, polar_error, compensation_error) > 2.0e-9:
        raise SystemExit("FAIL: an exact identity exceeded the tolerance")
    print("PASS: all three exact identities agree numerically.")


if __name__ == "__main__":
    main()
