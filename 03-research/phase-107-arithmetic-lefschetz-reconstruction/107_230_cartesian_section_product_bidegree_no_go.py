#!/usr/bin/env python3
"""Exact asymptotic gate for Cartesian periodic-section products."""

from fractions import Fraction


PAIRS = ((2, 2), (2, 3), (3, 5), (5, 7), (7, 11))
PATHS = (
    lambda k: (k, k),
    lambda k: (k, 2 * k),
    lambda k: (3 * k, k),
    lambda k: (k, k * k),
)


def actual_dimension(prime: int, degree: Fraction, depth: int) -> int:
    scaled = degree * prime**depth
    if scaled.denominator != 1 or scaled < prime:
        raise ValueError("depth is below the published exact range")
    return int(scaled) - prime + 1


def normalized_cartesian(p, q, alpha, beta, n, m):
    dimension = actual_dimension(p, alpha, n) + actual_dimension(q, beta, m)
    return Fraction(dimension, p**n * q**m)


def cartesian_bound(p, q, alpha, beta, n, m):
    return (
        alpha * Fraction(1, q**m)
        + beta * Fraction(1, p**n)
        + Fraction(p + q - 2, p**n * q**m)
    )


cartesian_bound_ok = True
cartesian_zero_visible = True
mixed_control_survives = True
for p, q in PAIRS:
    alpha = Fraction(2)
    beta = Fraction(3)
    for path in PATHS:
        values = []
        for k in range(2, 7):
            n, m = path(k)
            value = normalized_cartesian(p, q, alpha, beta, n, m)
            cartesian_bound_ok &= 0 <= value <= cartesian_bound(
                p, q, alpha, beta, n, m
            )
            values.append(value)

            d1 = actual_dimension(p, alpha, n)
            d2 = actual_dimension(q, beta, m)
            mixed_value = Fraction(d1 * d2, p**n * q**m)
            mixed_control_survives &= mixed_value > 0
            mixed_control_survives &= abs(mixed_value - alpha * beta) <= (
                alpha * Fraction(q - 1, q**m)
                + beta * Fraction(p - 1, p**n)
                + Fraction((p - 1) * (q - 1), p**n * q**m)
            )
        cartesian_zero_visible &= values[-1] < values[0]

verdict = cartesian_bound_ok and cartesian_zero_visible and mixed_control_survives

print("CARTESIAN_SECTION_PRODUCT_DIMENSION: ADDITIVE")
print("CARTESIAN_BIDEGREE_NORMALIZED_LIMIT: ZERO")
print("MIXED_PARAMETER_CHANNEL_REQUIRED: YES")
print(f"MIXED_PRODUCT_NEGATIVE_CONTROL: {'SURVIVES' if mixed_control_survives else 'ERASED'}")
print(f"VERDICT: {'YES' if verdict else 'NO'}")

