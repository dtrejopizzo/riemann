#!/usr/bin/env python3
"""Exact and diagnostic checks for 104_69.

The limiting theorems are proved in the document.  Floating-point rows only
show the predicted scales.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, exp, log


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


def quartet_term(n: int) -> float:
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
    return logistic(qn + log(n + 1.0))


def quartet_mean(xmax: int) -> float:
    numerator = 0.0
    harmonic = 0.0
    for n in range(1, xmax + 1):
        inv = 1.0 / n
        harmonic += inv
        numerator += inv * quartet_term(n)
    return numerator / harmonic


def main() -> None:
    for eps in (Fraction(1, 3), Fraction(2, 5), Fraction(3, 7)):
        for n in range(1, 13):
            assert p_binomial(n, eps) == p_closed(n, eps)
    print("exact polar identity: PASS")

    c = 0.01
    eta = c - log(200.0 / 199.0)
    assert eta > 0.0
    assert exp(-70.0 / 100.0) < 0.5
    assert exp(-69.0 / 100.0) > 0.5
    print(f"C={c:.12f} eta={eta:.12f}; epsilon_X<=1/2 starts at X=70")

    print("\nquartet finite logarithmic mean (target 0.25)")
    for xmax in (100, 1000, 10000, 100000):
        print(f"  X={xmax:6d} value={quartet_mean(xmax):.9f}")

    print("\nCauchy uniform envelope (factor 2M omitted)")
    for xmax in (500, 1000, 2000, 5000):
        envelope = xmax * exp(-eta * xmax)
        print(f"  X={xmax:5d} X exp(-eta X)={envelope:.9e}")

    print("\npolar scale at n=X (target log|p_X-1| ~ X^2/100)")
    for xmax in (100, 500, 1000, 2000):
        eps = exp(-xmax / 100.0)
        log_p = xmax * (xmax / 100.0 + log(1.0 - eps))
        reference = xmax * xmax / 100.0
        print(
            f"  X={xmax:5d} eps={eps:.4e} "
            f"logp/reference={log_p/reference:.9f}"
        )

    # Exact harmonic identity for the bad residue class.
    for xmax in (4, 20, 100, 400):
        lhs = sum(Fraction(1, n) for n in range(4, xmax + 1, 4))
        rhs = Fraction(1, 4) * sum(
            Fraction(1, k) for k in range(1, xmax // 4 + 1)
        )
        assert lhs == rhs

    print("\nPASS")


if __name__ == "__main__":
    main()
