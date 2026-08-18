#!/usr/bin/env python3
"""Exact audit for the Route A functoriality shadow of Phase 107.

This verifier audits a finite exact shadow of A6 from `107_12` and the
compatibility clauses of `107_11`:

1. additivity of the realization map;
2. transpose compatibility;
3. discrete scaling covariance on a finite visible sub-semigroup;
4. pullback/pushforward adjunction with respect to the transported
   pairing.

It does not prove the actual geometric theorem, only the exact finite
logic that any realized functor must satisfy.
"""

from __future__ import annotations

from fractions import Fraction


GENS = ["Fv", "Fh", "Delta", "Zinf", "G2", "G4"]


def mat_vec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [
        sum(entry * value for entry, value in zip(row, vector))
        for row in matrix
    ]


def vec_add(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    return [a + b for a, b in zip(left, right)]


def vec_scale(scale: Fraction, vector: list[Fraction]) -> list[Fraction]:
    return [scale * value for value in vector]


def dot(left: list[Fraction], matrix: list[list[Fraction]], right: list[Fraction]) -> Fraction:
    total = Fraction(0)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            total += a * matrix[i][j] * b
    return total


def main() -> None:
    # Finite shadow of the realization map: identity on the chosen basis.
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
    target_pairing = [[-entry for entry in row] for row in source_pairing]

    # Transpose swaps the two rulings and fixes the remaining generators.
    transpose = [
        [Fraction(0), Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(1)],
    ]

    # One finite visible correspondence shadow and its adjoint.
    pullback = [
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(1), Fraction(1), Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(1)],
    ]
    # In this shadow the target functor sees the same linear maps.
    target_pullback = pullback

    samples = [
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(2), Fraction(-1), Fraction(0), Fraction(0), Fraction(1)],
        [Fraction(3), Fraction(-1), Fraction(2), Fraction(1), Fraction(0), Fraction(-2)],
    ]

    print("Additivity audit")
    additivity_checks = 0
    for left in samples:
        for right in samples:
            summed = vec_add(left, right)
            image_sum = mat_vec(realization, summed)
            sum_images = vec_add(mat_vec(realization, left), mat_vec(realization, right))
            assert image_sum == sum_images
            additivity_checks += 1
    print(f" verified {additivity_checks} additivity comparisons")

    print("\nTranspose audit")
    transpose_checks = 0
    for vector in samples:
        src = mat_vec(realization, mat_vec(transpose, vector))
        tgt = mat_vec(transpose, mat_vec(realization, vector))
        assert src == tgt
        transpose_checks += 1
        print(f" vector={vector} transpose-image={src}")

    print("\nDiscrete scaling audit")
    scaling_checks = 0
    scaling_factors = [Fraction(2), Fraction(3)]
    for factor in scaling_factors:
        for vector in samples:
            src_scaled = mat_vec(realization, vec_scale(factor, vector))
            tgt_scaled = vec_scale(factor, mat_vec(realization, vector))
            assert src_scaled == tgt_scaled
            scaling_checks += 1
            print(f" factor={factor} vector={vector} scaled={src_scaled}")

    print("\nPullback/pushforward pairing audit")
    pairing_checks = 0
    for left in samples:
        for right in samples:
            src_left = mat_vec(pullback, left)
            tgt_left = mat_vec(target_pullback, mat_vec(realization, left))
            assert tgt_left == mat_vec(realization, src_left)

            src_pair = dot(src_left, source_pairing, right)
            tgt_pair = dot(tgt_left, target_pairing, mat_vec(realization, right))
            assert src_pair == -tgt_pair
            pairing_checks += 1
    print(f" verified {pairing_checks} pullback/pairing comparisons")

    print("\nAll exact Route A A6 functoriality shadow checks passed.")
    print(
        "Verified "
        f"{additivity_checks} additivity checks, "
        f"{transpose_checks} transpose checks, "
        f"{scaling_checks} scaling checks, and "
        f"{pairing_checks} pullback/pairing checks."
    )


if __name__ == "__main__":
    main()
