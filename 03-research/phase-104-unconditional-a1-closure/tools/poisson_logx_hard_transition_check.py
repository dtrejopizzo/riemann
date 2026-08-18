#!/usr/bin/env python3
"""Diagnostic checks for 104_75 (standard library only)."""

from __future__ import annotations

import cmath
import math


def laguerre_n_minus_1_alpha_1(n: int, u: float) -> float:
    """L_{n-1}^{(1)}(u), n >= 1, from its finite expansion."""
    return sum(
        math.comb(n, k + 1) * ((-u) ** k) / math.factorial(k)
        for k in range(n)
    )


def bessel_scaled_series(t: float, u: float, terms: int = 100) -> float:
    """sqrt(t/u) J_1(2 sqrt(tu)), evaluated by its entire series."""
    total = 0.0
    term = t
    total += term
    for j in range(terms - 1):
        term *= -(t * u) / ((j + 1) * (j + 2))
        total += term
        if abs(term) < 1e-18 * max(1.0, abs(total)):
            break
    return total


def poisson_weights(t: float, cutoff: int):
    p = math.exp(-t)
    yield 0, p
    for n in range(cutoff):
        p *= t / (n + 1)
        yield n + 1, p


def quartet(n: int) -> float:
    residue = n % 4
    if residue % 2:
        return 4.0
    amplitude = 2.0**n + 2.0 ** (-n)
    return 4.0 - 2.0 * amplitude if residue == 0 else 4.0 + 2.0 * amplitude


def logistic_from_x(x: float) -> float:
    if x >= 0.0:
        y = math.exp(-x) if x < 745.0 else 0.0
        return y / (1.0 + y)
    y = math.exp(x) if x > -745.0 else 0.0
    return 1.0 / (1.0 + y)


def check_bessel_identity() -> None:
    for t, u in ((0.3, 0.7), (0.8, 1.4), (1.1, 0.2)):
        lhs = sum(
            (t**n) * laguerre_n_minus_1_alpha_1(n, u)
            / math.factorial(n)
            for n in range(1, 45)
        )
        rhs = math.exp(t) * bessel_scaled_series(t, u)
        assert abs(lhs - rhs) < 2e-12, (t, u, lhs, rhs)


def check_pole_identity() -> None:
    for t, eps in ((0.4, 0.7), (0.8, 0.3), (1.2, 0.9)):
        a = 1.0 - 1.0 / eps
        lhs = sum(
            (1.0 - a**n) * t**n / math.factorial(n)
            for n in range(1, 120)
        ) * math.exp(-t)
        rhs = 1.0 - math.exp(-t / eps)
        assert abs(lhs - rhs) < 2e-12, (t, eps, lhs, rhs)


def check_quartet_linear_formula() -> None:
    w = 2j
    for t in (2.0, 5.0, 10.0):
        cutoff = int(t + 16.0 * math.sqrt(t) + 50)
        lhs = sum(p * quartet(n) for n, p in poisson_weights(t, cutoff) if n)
        rhs = 4.0 - 2.0 * (
            cmath.exp((w - 1.0) * t) + cmath.exp((1.0 / w - 1.0) * t)
        ).real
        assert abs(lhs - rhs) < 2e-10, (t, lhs, rhs)


def check_mod_four_and_fermi() -> None:
    values = []
    for t in (20.0, 40.0, 80.0):
        cutoff = int(t + 14.0 * math.sqrt(t) + 80)
        residues = [0.0] * 4
        fermi = 0.0
        total = 0.0
        for n, p in poisson_weights(t, cutoff):
            total += p
            residues[n % 4] += p
            if n:
                x = quartet(n) + math.log(n + 1.0)
                fermi += p * logistic_from_x(x)
        assert abs(total - 1.0) < 2e-12
        assert max(abs(v - 0.25) for v in residues) < 2e-8
        values.append(fermi)
    assert values[0] > values[1] > values[2] > 0.25, values
    assert abs(values[-1] - 0.25) < 2e-4, values


def check_hard_soft_sandwich() -> None:
    xs = [-4.0, -0.2, 0.5, 2.0, 7.0]
    weights = [1.0 / (j + 1) for j in range(len(xs))]
    norm = sum(weights)
    fermi = sum(w * logistic_from_x(x) for w, x in zip(weights, xs)) / norm
    delta0 = sum(w for w, x in zip(weights, xs) if x <= 0.0) / norm
    for b in (0.0, 1.0, 3.0):
        deltab = sum(w for w, x in zip(weights, xs) if x <= b) / norm
        assert 0.5 * delta0 <= fermi + 1e-15
        assert fermi <= deltab + math.exp(-b) + 1e-15


def quartet_crosses_giant_threshold(n: int, x: int) -> bool:
    if n == 0 or n % 4:
        return False
    if n < 500:
        magnitude = 2.0 * (2.0**n + 2.0 ** (-n)) - 4.0 - math.log(n + 1.0)
        if magnitude <= 0.0:
            return False
        log_magnitude = math.log(magnitude)
    else:
        log_magnitude = (n + 1.0) * math.log(2.0)
    return log_magnitude >= math.sqrt(x)


def check_giant_threshold_quartet() -> None:
    ratios = []
    for x in (10_000, 100_000, 1_000_000):
        harmonic = 0.0
        bad = 0.0
        for n in range(1, x + 1):
            inv = 1.0 / n
            harmonic += inv
            if quartet_crosses_giant_threshold(n, x):
                bad += inv
        ratios.append(bad / harmonic)
    assert ratios[0] < ratios[1] < ratios[2] < 0.125, ratios
    assert abs(ratios[-1] - 0.125) < 0.012, ratios


def main() -> None:
    check_bessel_identity()
    check_pole_identity()
    check_quartet_linear_formula()
    check_mod_four_and_fermi()
    check_hard_soft_sandwich()
    check_giant_threshold_quartet()
    print("PASS poisson_logx_hard_transition_check")


if __name__ == "__main__":
    main()
