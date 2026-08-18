#!/usr/bin/env python3
"""Numerical check of the exact exchange-Mecke identity from 104_116.

The zeta law is truncated only in the geometric exponents.  Consequently
the discrepancy decays geometrically with the truncation height.  The
pointwise conservation J1=0 is exact up to floating-point roundoff.
"""

from __future__ import annotations

import itertools
import math
import numpy as np


def build_triangle_omega(primes: np.ndarray, s: float, kappa: float = 1.0) -> np.ndarray:
    if len(primes) != 3:
        raise ValueError("the checker uses one triple")
    u = primes ** (-s / 2.0)
    omega = np.zeros((3, 3), dtype=float)
    # Orientation 0 -> 1 -> 2 -> 0; kernel vector u.
    omega[0, 1] = kappa * u[2]
    omega[1, 2] = kappa * u[0]
    omega[2, 0] = kappa * u[1]
    omega -= omega.T
    return omega


def f(x: float) -> float:
    return 1.0 + 0.3 * x + 0.07 * x * x


def g(x: float) -> float:
    return 2.0 - 0.4 * x + 0.05 * x**3


def evaluate(cutoff: int, s: float = 2.0) -> tuple[float, float, float]:
    primes = np.array([2.0, 3.0, 5.0])
    logs = np.log(primes)
    omega = build_triangle_omega(primes, s)
    u = primes ** (-s / 2.0)
    kernel_error = np.max(np.abs(omega @ u))
    normalizers = 1.0 - primes ** (-s)

    lhs = 0.0
    rhs = 0.0
    conservation_error = 0.0
    for exponents in itertools.product(range(cutoff + 1), repeat=3):
        exponents_array = np.asarray(exponents, dtype=int)
        probability = float(np.prod(normalizers * primes ** (-s * exponents_array)))
        x = float(exponents_array @ logs)

        jg = 0.0
        j1 = 0.0
        for p_index in range(3):
            for q_index in range(3):
                if p_index == q_index or exponents_array[q_index] == 0:
                    continue
                coefficient = omega[p_index, q_index] * (
                    primes[q_index] / primes[p_index]
                ) ** (s / 2.0)
                shifted_x = x + logs[p_index] - logs[q_index]
                jg += coefficient * g(shifted_x)
                j1 += coefficient
        lhs += probability * f(x) * jg
        conservation_error = max(conservation_error, abs(j1))

        pair_sum = 0.0
        for p_index in range(3):
            for q_index in range(3):
                if p_index == q_index:
                    continue
                pair_sum += (
                    omega[p_index, q_index]
                    / (primes[p_index] * primes[q_index]) ** (s / 2.0)
                    * f(x + logs[q_index])
                    * g(x + logs[p_index])
                )
        rhs += probability * pair_sum

    return lhs, rhs, max(kernel_error, conservation_error)


def main() -> None:
    previous_error = None
    for cutoff in (6, 10, 14, 18, 22):
        lhs, rhs, conservation_error = evaluate(cutoff)
        error = abs(lhs - rhs)
        print(
            f"K={cutoff:2d} lhs={lhs:+.15e} rhs={rhs:+.15e} "
            f"error={error:.3e} conservation={conservation_error:.3e}"
        )
        if previous_error is not None:
            assert error < previous_error
        previous_error = error
        assert conservation_error < 1e-12
    assert previous_error is not None and previous_error < 1e-12
    print("PASS: triangle exchange-Mecke identity")


if __name__ == "__main__":
    main()
