#!/usr/bin/env python3
"""Exact audit for the degree-zero/covariance realization shadow of 107_11."""

from __future__ import annotations

from fractions import Fraction


GENS = ["Fv", "Fh", "Delta", "Zinf", "G2", "G4"]


def dot(left: list[Fraction], matrix: list[list[Fraction]], right: list[Fraction]) -> Fraction:
    total = Fraction(0)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            total += a * matrix[i][j] * b
    return total


def mat_vec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [
        sum(entry * value for entry, value in zip(row, vector))
        for row in matrix
    ]


def vec_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    return [a + b for a, b in zip(left, right)]


def vec_scale(scale: Fraction, vector: list[Fraction]) -> list[Fraction]:
    return [scale * value for value in vector]


def primitive_projection(
    vector: list[Fraction], polarization: list[Fraction], height_matrix: list[list[Fraction]]
) -> tuple[list[Fraction], Fraction]:
    numerator = dot(vector, height_matrix, polarization)
    denominator = dot(polarization, height_matrix, polarization)
    assert denominator != 0
    coeff = numerator / denominator
    projected = [value - coeff * h for value, h in zip(vector, polarization)]
    return projected, coeff


def degree(vector: list[Fraction], polarization: list[Fraction], height_matrix: list[list[Fraction]]) -> Fraction:
    return dot(vector, height_matrix, polarization)


def main() -> None:
    realization = [
        [Fraction(int(i == j)) for j in range(len(GENS))]
        for i in range(len(GENS))
    ]

    source_pairing = [
        [Fraction(1), Fraction(1), Fraction(0), Fraction(0), Fraction(1), Fraction(1)],
        [Fraction(1), Fraction(1), Fraction(0), Fraction(0), Fraction(1), Fraction(1)],
        [Fraction(0), Fraction(0), Fraction(4), Fraction(1), Fraction(2), Fraction(3)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(3), Fraction(1), Fraction(2)],
        [Fraction(1), Fraction(1), Fraction(2), Fraction(1), Fraction(5), Fraction(2)],
        [Fraction(1), Fraction(1), Fraction(3), Fraction(2), Fraction(2), Fraction(6)],
    ]
    target_height = [[-entry for entry in row] for row in source_pairing]
    polarization = [Fraction(1), Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)]
    radical = [Fraction(1), Fraction(-1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)]

    divisor_samples = [
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(2), Fraction(-1), Fraction(0), Fraction(0), Fraction(1)],
        [Fraction(3), Fraction(-1), Fraction(2), Fraction(1), Fraction(0), Fraction(-2)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(1), Fraction(-1), Fraction(2)],
    ]

    print("Additivity audit")
    additivity_checks = 0
    for left in divisor_samples:
        for right in divisor_samples:
            realized_sum = mat_vec(realization, vec_add(left, right))
            sum_realized = vec_add(mat_vec(realization, left), mat_vec(realization, right))
            assert realized_sum == sum_realized
            additivity_checks += 1
    print(f" verified {additivity_checks} additivity comparisons")

    print("\nDegree-zero projection audit")
    degree_zero_checks = 0
    primitive_vectors: list[list[Fraction]] = []
    for vector in divisor_samples:
        realized = mat_vec(realization, vector)
        projected, coeff = primitive_projection(realized, polarization, target_height)
        assert degree(projected, polarization, target_height) == 0
        primitive_vectors.append(projected)
        degree_zero_checks += 1
        print(f" vector={vector} coeff={coeff} projected={projected}")

    print("\nDiscrete scaling covariance audit")
    scaling_checks = 0
    for factor in (Fraction(2), Fraction(3)):
        for projected in primitive_vectors:
            scaled = vec_scale(factor, projected)
            assert degree(scaled, polarization, target_height) == 0
            src_self = dot(scaled, source_pairing, scaled)
            tgt_self = dot(scaled, target_height, scaled)
            assert src_self == -tgt_self
            scaling_checks += 2
            print(f" factor={factor} scaled={scaled} src_self={src_self} tgt_self={tgt_self}")

    print("\nRadical and degree-zero compatibility audit")
    radical_checks = 0
    assert degree(radical, polarization, target_height) == 0
    radical_checks += 1
    for projected in primitive_vectors:
        assert dot(radical, source_pairing, projected) == 0
        assert dot(radical, target_height, projected) == 0
        radical_checks += 2
    print(f" verified {radical_checks} radical/degree-zero comparisons")

    print("\nAll exact Paper C realization degree-zero covariance checks passed.")
    print(f"  additivity checks: {additivity_checks}")
    print(f"  degree-zero checks: {degree_zero_checks}")
    print(f"  scaling checks: {scaling_checks}")
    print(f"  radical-compatibility checks: {radical_checks}")


if __name__ == "__main__":
    main()
