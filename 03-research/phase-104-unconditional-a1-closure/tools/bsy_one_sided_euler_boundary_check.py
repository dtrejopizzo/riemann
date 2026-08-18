#!/usr/bin/env python3
"""Finite diagnostics for the exact formulas in 104_89."""

from math import atan, cos, log, pi, sqrt


def poisson(r, theta):
    return (1.0 - r * r) / (1.0 - 2.0 * r * cos(theta) + r * r)


def tower(p, theta):
    r = 1.0 / sqrt(p)
    denominator = sqrt(1.0 - 2.0 * r * cos(theta) + r * r)
    return log((1.0 - r * r) / denominator)


def trapezoid_periodic(fn, count=1 << 19):
    return sum(fn(2.0 * pi * j / count) for j in range(count)) / count


def main():
    # Balanced Poisson spike: the positive mass has a closed form.
    for r in (0.5, 0.9, 0.99, 0.999):
        numeric = trapezoid_periodic(
            lambda th: max(poisson(r, th) - poisson(-r, th), 0.0)
        )
        exact = 4.0 / pi * atan((1.0 + r) / (1.0 - r)) - 1.0
        assert abs(numeric - exact) < 2e-8

    # Exact ordinary prime towers have zero mean but both signs.
    for p in (5, 7, 11, 101):
        r = 1.0 / sqrt(p)
        mean = trapezoid_periodic(
            lambda th: tower(p, th) * poisson(r, th)
        )
        positive = trapezoid_periodic(
            lambda th: max(tower(p, th), 0.0) * poisson(r, th)
        )
        negative = trapezoid_periodic(
            lambda th: max(-tower(p, th), 0.0) * poisson(r, th)
        )
        assert abs(mean) < 2e-11
        assert abs(positive - negative) < 2e-11
        assert positive >= 1.0 / (36.0 * sqrt(p))

    print("104_89 checker: PASS")
    print("balanced spike positive mass tends to 1")
    print("ordinary prime towers have equal nonzero positive/negative costs")


if __name__ == "__main__":
    main()
