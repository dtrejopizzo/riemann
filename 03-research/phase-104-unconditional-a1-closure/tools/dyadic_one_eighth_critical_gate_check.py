#!/usr/bin/env python3
"""Check the critical-line obstruction to the dyadic 1/8 target."""

from __future__ import annotations

import math

import numpy as np


L = math.log(2.0)
TARGET = 1.0 / 8.0
GAMMA1 = 14.134725141734695


def envelope(c: float, gamma: float) -> tuple[float, float]:
    center = c * c / (2.0 * L)
    radius = c * c * abs(math.sin(gamma * L)) / (2.0 * gamma * L * L)
    return center - radius, center + radius


def limiting_block(c: float, gamma: float, phi: float, j: int) -> float:
    return c * c * (
        1.0 / (2.0 * L)
        + math.sin(gamma * L)
        * math.cos(gamma * (2 * j - 1) * L + 2 * phi)
        / (2.0 * gamma * L * L)
    )


def literal_block(c: float, gamma: float, phi: float, j: int) -> float:
    lo = 1 << (j - 1)
    hi = 1 << j
    total = np.longdouble(0.0)
    chunk = 131_071
    for a in range(lo + 1, hi + 1, chunk):
        b = min(hi + 1, a + chunk)
        m = np.arange(a, b, dtype=np.longdouble)
        phase = gamma * np.log(m) + phi
        primitive = c * np.sqrt(m) * np.cos(phase) / np.log(m)
        total += np.sum(primitive * primitive / (m * (m + 1)), dtype=np.longdouble)
    return float(j * j * total)


def main() -> None:
    lo7, hi7 = envelope(1.0, 7.0)
    c_zeta4 = 8.0 / math.sqrt(0.25 + GAMMA1 * GAMMA1)
    lo_zeta4, hi_zeta4 = envelope(c_zeta4, GAMMA1)
    c_zeta1 = 2.0 / math.sqrt(0.25 + GAMMA1 * GAMMA1)
    lo_zeta1, hi_zeta1 = envelope(c_zeta1, GAMMA1)

    print("DYADIC 1/8 CRITICAL-LINE ADVERSARIAL GATE")
    print(f"target                                  = {TARGET:.15g}")
    print(f"unit critical gamma=7 envelope         = [{lo7:.15g}, {hi7:.15g}]")
    print(f"zeta-residue gamma1, M=1 envelope      = [{lo_zeta1:.15g}, {hi_zeta1:.15g}]")
    print(f"zeta-residue gamma1, M=4 envelope      = [{lo_zeta4:.15g}, {hi_zeta4:.15g}]")

    if not lo7 > TARGET:
        raise AssertionError("unit critical control does not clear 1/8")
    if not lo_zeta4 > TARGET:
        raise AssertionError("multiplicity-four line residue does not clear 1/8")
    if not hi_zeta1 < TARGET:
        raise AssertionError("single first-zero pair unexpectedly clears 1/8")

    print("literal discrete/asymptotic comparison (c=1, gamma=7, phi=0):")
    errors: list[float] = []
    for j in (12, 14, 16, 18, 20):
        direct = literal_block(1.0, 7.0, 0.0, j)
        limit = limiting_block(1.0, 7.0, 0.0, j)
        error = abs(direct - limit)
        errors.append(error)
        print(f"j={j:2d} direct={direct:.12g} limit={limit:.12g} abs.err={error:.4g}")

    if errors[-1] > 0.04:
        raise AssertionError("discrete block has not approached the closed profile")
    if errors[-1] >= errors[0]:
        raise AssertionError("no net convergence in the selected audit rows")

    print("PASS: 1/8 is not a universal critical-line block constant")
    print("NOTE: this is not a counterexample for the ordinary zeta weights")


if __name__ == "__main__":
    main()
