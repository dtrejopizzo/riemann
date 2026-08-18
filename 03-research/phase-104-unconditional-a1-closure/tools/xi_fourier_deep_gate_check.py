#!/usr/bin/env python3
"""Checks for 104_83.  Float calculations are diagnostic only."""

from fractions import Fraction
from math import exp, log, pi, sqrt

import numpy as np


def poly_derivative(p):
    return [j * p[j] for j in range(1, len(p))]


def next_polynomial(p, a):
    """If D^k exp(a*u-x*exp(2u))=base*P_k(x exp(2u))."""
    q = [0.0] * (len(p) + 1)
    for j, value in enumerate(p):
        q[j] += a * value
        q[j + 1] -= 2.0 * value
    for j, value in enumerate(poly_derivative(p)):
        q[j + 1] += 2.0 * value
    return q


def evaluate_polynomial(p, x):
    value = 0.0
    for coefficient in reversed(p):
        value = value * x + coefficient
    return value


def mode_derivatives_at_zero(m, order):
    x = pi * m * m
    values = [0.0] * (order + 1)
    pieces = ((2.0 * pi * pi * m**4, 4.5), (-3.0 * pi * m * m, 2.5))
    for coefficient, a in pieces:
        base = coefficient * exp(-x)
        polynomial = [1.0]
        for k in range(order + 1):
            values[k] += base * evaluate_polynomial(polynomial, x)
            polynomial = next_polynomial(polynomial, a)
    return values


def theta_mode(u, m):
    x = pi * m * m * np.exp(2.0 * u)
    return (
        2.0 * pi * pi * m**4 * np.exp(4.5 * u)
        - 3.0 * pi * m * m * np.exp(2.5 * u)
    ) * np.exp(-x)


def main():
    # g(22/7)=13/98 is the exact lower certificate for g(pi).
    x = Fraction(22, 7)
    g = 15 * x - 4 * x * x - Fraction(15, 2)
    assert g == Fraction(13, 98) and g > 0

    total = [0.0] * 8
    first = mode_derivatives_at_zero(1, 7)
    for m in range(1, 20):
        values = mode_derivatives_at_zero(m, 7)
        for k, value in enumerate(values):
            total[k] += value
    assert first[1] > 0.0
    for k in (1, 3, 5, 7):
        scale = max(1.0, abs(first[k]))
        assert abs(total[k]) < 2e-13 * scale

    # Exact translate formula, checked away from underflow.
    for m in (2, 3, 5):
        for value in (0.0, 0.2, 0.7):
            left = float(theta_mode(np.array([value]), m)[0])
            right = float(theta_mode(np.array([value + log(m)]), 1)[0]) / sqrt(m)
            assert abs(left - right) <= 2e-13 * max(abs(left), abs(right), 1e-300)

    # Diagnostic only: at known critical zeros the higher modes cancel f_1.
    u = np.linspace(0.0, 3.0, 300001)
    first_values = theta_mode(u, 1)
    full_values = sum(theta_mode(u, m) for m in range(1, 9))
    zeros = (14.134725141734695, 21.022039638771556, 25.01085758014569)
    ratios = []
    for zero in zeros:
        phase = np.cos(zero * u)
        c1 = np.trapz(first_values * phase, u)
        tail = np.trapz((full_values - first_values) * phase, u)
        ratios.append(tail / c1)
        assert abs(tail / c1 + 1.0) < 2e-8

    print("PASS: g(22/7) = 13/98 > 0, hence f_1'(0) > 0")
    print("PASS: theta odd boundary jets 1,3,5,7 cancel (float diagnostic)")
    print("PASS: f_m(u) = m^(-1/2) f_1(u+log m) (float diagnostic)")
    print("PASS: tail/first at first three critical zeros =", ratios)
    print("NOTE: Fourier quadrature is diagnostic; the theorem uses integration by parts")


if __name__ == "__main__":
    main()
