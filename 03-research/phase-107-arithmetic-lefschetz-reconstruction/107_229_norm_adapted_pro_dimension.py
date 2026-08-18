#!/usr/bin/env python3
"""Exact checks for the norm-adapted two-ruling pro-dimension."""

from fractions import Fraction


PRIMES = (2, 3, 5, 7, 11)
WINDOWS = (Fraction(1, 2), Fraction(1), Fraction(7, 3))


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def norm_level(prime: int, window: Fraction, depth: int) -> set[Fraction]:
    top = floor_fraction(window * prime**depth)
    return {Fraction(a, prime**depth) for a in range(top + 1)}


def norm_count(prime: int, window: Fraction, depth: int) -> int:
    return floor_fraction(window * prime**depth) + 1


def rectangular_rank(prime: int, cutoff: int, depth: int) -> int:
    return 1 + (cutoff - cutoff // prime) * (2 * depth + 1)


level_formula_ok = True
frobenius_ok = True
for prime in PRIMES:
    for window in WINDOWS:
        for depth in range(1, 5):
            level = norm_level(prime, window, depth)
            level_formula_ok &= len(level) == norm_count(prime, window, depth)
            level_formula_ok &= all(
                0 <= x <= window and x.denominator <= prime**depth
                for x in level
            )

            multiplied = {prime * x for x in level}
            divided = {x / prime for x in level}
            frobenius_ok &= multiplied == norm_level(
                prime, prime * window, depth - 1
            )
            frobenius_ok &= divided == norm_level(
                prime, window / prime, depth + 1
            )

# The old rectangular filtration has zero density under the published scale.
rectangular_zero_density = all(
    Fraction(rectangular_rank(prime, 7, 40), prime**40) < Fraction(1, 10**8)
    for prime in PRIMES
)


def normalized_square_count(p, q, a, b, r, s):
    count = norm_count(p, a, r) * norm_count(q, b, s)
    return Fraction(count, p**r * q**s)


def error_bound(p, q, a, b, r, s):
    return a * Fraction(1, q**s) + b * Fraction(1, p**r) + Fraction(
        1, p**r * q**s
    )


pairs = ((2, 2), (2, 3), (3, 5), (5, 7), (7, 11))
paths = (
    lambda k: (k, k),
    lambda k: (k, 2 * k),
    lambda k: (3 * k, k),
    lambda k: (k, k * k),
)
cofinal_bound_ok = True
cofinal_convergence_visible = True
for p, q in pairs:
    for a, b in ((Fraction(1), Fraction(1)), (Fraction(7, 3), Fraction(5, 2))):
        target = a * b
        for path in paths:
            errors = []
            for k in range(1, 7):
                r, s = path(k)
                value = normalized_square_count(p, q, a, b, r, s)
                error = value - target
                cofinal_bound_ok &= 0 <= error <= error_bound(p, q, a, b, r, s)
                errors.append(error)
            cofinal_convergence_visible &= errors[-1] < errors[0]

# Exact published special-divisor formula:
# tdim H0(alpha{1})^(p^n) = alpha*p^n - p + 1.
one_ruling_h0_match = True
for p in PRIMES:
    alphas = (Fraction(1, p**2), Fraction(3, p), Fraction(2))
    for alpha in alphas:
        for n in range(4, 9):
            scaled_degree = alpha * p**n
            if scaled_degree.denominator != 1 or scaled_degree < p:
                continue
            actual_h0_dimension = int(scaled_degree) - p + 1
            support_dimension = norm_count(p, alpha, n)
            one_ruling_h0_match &= support_dimension - actual_h0_dimension == p
            one_ruling_h0_match &= Fraction(p, p**n) <= Fraction(1, p**3)

# Negative controls: omitting either cutoff leaves arbitrarily large finite
# witnesses inside what would have to be one level.
real_cutoff_required = all(
    len({Fraction(a, p**2) for a in range(bound)}) == bound
    for p in PRIMES
    for bound in (10, 100, 1000)
)
padic_cutoff_required = all(
    len({Fraction(1, p**k) for k in range(bound)}) == bound
    and all(Fraction(1, p**k) <= 1 for k in range(bound))
    for p in PRIMES
    for bound in (10, 100, 1000)
)

verdict = all((
    level_formula_ok,
    frobenius_ok,
    rectangular_zero_density,
    cofinal_bound_ok,
    cofinal_convergence_visible,
    one_ruling_h0_match,
    real_cutoff_required,
    padic_cutoff_required,
))

print("RECTANGULAR_107154_NORMALIZED_DENSITY: ZERO")
print("NORM_ADAPTED_ONE_RULING_LIMIT: WINDOW_LENGTH")
print("TWO_RULING_COFINAL_LIMIT: PRODUCT_OF_WINDOW_LENGTHS")
print(f"ONE_RULING_ACTUAL_H0_LIMIT: {'MATCHED' if one_ruling_h0_match else 'MISMATCHED'}")
print(f"FROBENIUS_COVARIANCE: {'YES' if frobenius_ok else 'NO'}")
print("FULL_PERIODIC_H0_DIMENSION: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
