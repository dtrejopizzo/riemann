#!/usr/bin/env python3
"""Exact and diagnostic checks for 104_70."""

from __future__ import annotations

from fractions import Fraction
from math import comb, exp, log, sqrt


def p_binomial(n: int, eps: Fraction) -> Fraction:
    total = Fraction(0)
    for k in range(1, n + 1):
        total += (
            Fraction(n * comb(n - 1, k - 1) * (-1) ** (k - 1), k)
            / eps**k
        )
    return total


def p_closed(n: int, eps: Fraction) -> Fraction:
    return 1 + (-1) ** (n - 1) * ((1 - eps) / eps) ** n


def logistic(y: float) -> float:
    if y >= 40.0:
        return exp(-y)
    if y <= -40.0:
        return 1.0 - exp(y)
    return 1.0 / (1.0 + exp(y))


def quartet_variable_term(n: int) -> float:
    root = sqrt(n)
    temperature = exp(-root)
    barrier = exp(2.0 * root)
    residue = n % 4
    if residue in (1, 3):
        qn = 4.0
    elif n > 500:
        return 1.0 if residue == 0 else 0.0
    else:
        power = float(1 << n)
        if residue == 0:
            qn = 4.0 - 2.0 * (power + 1.0 / power)
        else:
            qn = 4.0 + 2.0 * (power + 1.0 / power)
    return logistic(temperature * (qn + barrier))


def quartet_mean(xmax: int) -> float:
    numerator = 0.0
    harmonic = 0.0
    for n in range(1, xmax + 1):
        inv = 1.0 / n
        harmonic += inv
        numerator += inv * quartet_variable_term(n)
    return numerator / harmonic


def main() -> None:
    for eps in (Fraction(1, 3), Fraction(2, 5), Fraction(3, 7)):
        for n in range(1, 13):
            assert p_binomial(n, eps) == p_closed(n, eps)
    print("exact polar identity: PASS")

    print("\nminimum epsilon for t_n |p_n-1| <= 1")
    for n in (100, 1000, 10000, 100000):
        eps_min = 1.0 / (1.0 + exp(1.0 / sqrt(n)))
        print(f"  n={n:6d} epsilon_min={eps_min:.12f}")
        assert eps_min < 0.5
    print("  limit = 0.5, not 0")

    print("\npolar divergence for epsilon_n=1/n")
    for n in (100, 500, 1000, 5000):
        eps = 1.0 / n
        log_scaled_p = -sqrt(n) + n * log((1.0 - eps) / eps)
        print(f"  n={n:5d} log(t_n |p_n-1|)={log_scaled_p:.6e}")
        assert log_scaled_p > 0.0

    print("\ndetector retains every fixed exponential rate")
    for rate in (1.01, 1.1, 2.0):
        values = [n * log(rate) - sqrt(n) for n in (1000, 10000, 100000)]
        print(
            f"  R={rate:.2f} log(t_n R^n): "
            + " ".join(f"{value:.3f}" for value in values)
        )
        assert values[-1] > values[0]

    print("\nvariable-temperature quartet mean (target 0.25)")
    for xmax in (100, 1000, 10000, 100000):
        print(f"  X={xmax:6d} value={quartet_mean(xmax):.9f}")

    print("\ndiagonal absolute polar phase at n=X")
    for xmax in (100, 500, 1000, 2000):
        eps = exp(-xmax / 100.0)
        log_scaled_p = (
            -sqrt(xmax)
            + xmax * (xmax / 100.0 + log(1.0 - eps))
        )
        reference = xmax * xmax / 100.0 - sqrt(xmax)
        print(
            f"  X={xmax:5d} log(t_X|p_X-1|)={log_scaled_p:.6e} "
            f"reference={reference:.6e}"
        )

    print("\nPASS")


if __name__ == "__main__":
    main()
