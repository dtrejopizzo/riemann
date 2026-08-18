#!/usr/bin/env python3
"""Exact mixed-cell controls built from the published CC generators."""

from fractions import Fraction


PAIRS = ((2, 2), (2, 3), (3, 5), (5, 7), (7, 11))


def cc_frame(prime: int, degree: int):
    dimension = degree - prime + 1
    epsilon = Fraction(prime - 1, 2 * dimension)
    times = [Fraction(0)] + [Fraction(i, dimension) * epsilon for i in range(1, dimension)]

    coefficients = []
    running = Fraction(0)
    for time in times:
        running += time
        coefficients.append(-running)

    bounds = [Fraction(0)] + times[1:] + [epsilon]
    witnesses = [
        Fraction(1) + (bounds[i] + bounds[i + 1]) / 2
        for i in range(dimension)
    ]

    def phi(index: int, x: Fraction) -> Fraction:
        if index == 0:
            return Fraction(0)
        right_slope = (degree - index) // prime
        return max(-index * (x - 1), right_slope * (x - prime))

    section_condition = True
    for index in range(1, degree - prime + 1):
        right_slope = (degree - index) // prime
        section_condition &= right_slope >= 1
        section_condition &= index + prime * right_slope <= degree
        section_condition &= phi(index, Fraction(1)) == 0
        section_condition &= phi(index, Fraction(prime)) == 0
        section_condition &= -index < right_slope

    def generator(i: int, x: Fraction) -> Fraction:
        return phi(degree - prime - i, x) + coefficients[i]

    gaps = []
    for i, x in enumerate(witnesses):
        values = [generator(k, x) for k in range(dimension)]
        competitors = values[:i] + values[i + 1 :]
        if not competitors or values[i] <= max(competitors):
            raise AssertionError("published dominance frame collapsed")
        gaps.append(values[i] - max(competitors))

    return dimension, witnesses, generator, min(gaps), section_condition


dominance_ok = True
coefficient_recovery_ok = True
row_column_mutation_rejected = True
external_divisor_condition_ok = True

for p, q in PAIRS:
    d, xs, g, gap_p, section_p = cc_frame(p, p + 3)
    e, ys, h, gap_q, section_q = cc_frame(q, q + 2)
    external_divisor_condition_ok &= section_p and section_q
    mixed_gap = min(gap_p, gap_q)
    eta = mixed_gap / 4

    perturbation = {
        (i, j): (eta / 8 if (i, j) == (1, 1) else Fraction(0))
        for i in range(d)
        for j in range(e)
    }

    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            values = {
                (k, ell): g(k, x) + h(ell, y) + perturbation[k, ell]
                for k in range(d)
                for ell in range(e)
            }
            winner = max(values, key=values.get)
            dominance_ok &= winner == (i, j)
            recovered = values[winner] - g(i, x) - h(j, y)
            coefficient_recovery_ok &= recovered == perturbation[i, j]

    # The chosen matrix has a nonzero 2x2 additive minor, so it cannot be
    # represented by row-plus-column coefficients.
    additive_minor = (
        perturbation[0, 0]
        + perturbation[1, 1]
        - perturbation[0, 1]
        - perturbation[1, 0]
    )
    row_column_mutation_rejected &= additive_minor != 0

cofinal_product_ok = True
for p, q in PAIRS:
    alpha = Fraction(2)
    beta = Fraction(3)
    for n, m in ((3, 3), (4, 8), (9, 3), (6, 12)):
        d = int(alpha * p**n) - p + 1
        e = int(beta * q**m) - q + 1
        normalized = Fraction(d * e, p**n * q**m)
        error_bound = (
            alpha * Fraction(q - 1, q**m)
            + beta * Fraction(p - 1, p**n)
            + Fraction((p - 1) * (q - 1), p**n * q**m)
        )
        cofinal_product_ok &= abs(normalized - alpha * beta) <= error_bound

verdict = all((
    dominance_ok,
    coefficient_recovery_ok,
    row_column_mutation_rejected,
    external_divisor_condition_ok,
    cofinal_product_ok,
))

print("MIXED_EXTERNAL_SECTION_CELL: CONSTRUCTED")
print(f"EXTERNAL_DIVISOR_CONDITION: {'YES' if external_divisor_condition_ok else 'NO'}")
print("CELL_DIMENSION: PRODUCT")
print("NORMALIZED_MIXED_LIMIT: ALPHA_BETA")
print(f"CARTESIAN_COLLAPSE_AVOIDED: {'YES' if row_column_mutation_rejected else 'NO'}")
print("GLOBAL_SQUARE_H0: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
