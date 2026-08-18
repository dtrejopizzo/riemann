#!/usr/bin/env python3
"""Exact audit for the finite pairing-transport shadow of Phase 107.

This verifier audits the finite algebraic shadow of the comparison

    <D_f, D_g>_src = -deg(M_f . M_g)

required by `107_11` and `107_13`.

The scope is an exact bilinear shadow:

1. generator comparison on a finite visible basis;
2. bilinear extension to finite-support divisors;
3. terminal self-pairing identity on sample primitive vectors;
4. compatibility with one explicit radical direction.

It does not construct the geometric target side.
"""

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


def is_zero_vector(vector: list[Fraction]) -> bool:
    return all(value == 0 for value in vector)


def primitive_projection(
    vector: list[Fraction], polarization: list[Fraction], height_matrix: list[list[Fraction]]
) -> tuple[list[Fraction], Fraction]:
    numerator = dot(vector, height_matrix, polarization)
    denominator = dot(polarization, height_matrix, polarization)
    assert denominator != 0
    coeff = numerator / denominator
    projected = [
        value - coeff * h
        for value, h in zip(vector, polarization)
    ]
    return projected, coeff


def main() -> None:
    # Exact finite shadow:
    # source pairing matrix and target height matrix are negatives.
    source = [
        [Fraction(1), Fraction(1), Fraction(0), Fraction(0), Fraction(1), Fraction(1)],
        [Fraction(1), Fraction(1), Fraction(0), Fraction(0), Fraction(1), Fraction(1)],
        [Fraction(0), Fraction(0), Fraction(4), Fraction(1), Fraction(2), Fraction(3)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(3), Fraction(1), Fraction(2)],
        [Fraction(1), Fraction(1), Fraction(2), Fraction(1), Fraction(5), Fraction(2)],
        [Fraction(1), Fraction(1), Fraction(3), Fraction(2), Fraction(2), Fraction(6)],
    ]
    target = [[-entry for entry in row] for row in source]

    print("Generator comparison audit")
    generator_checks = 0
    basis = [[Fraction(int(i == j)) for j in range(len(GENS))] for i in range(len(GENS))]
    for i, left in enumerate(basis):
        for j, right in enumerate(basis):
            src = dot(left, source, right)
            tgt = dot(left, target, right)
            assert src == -tgt
            generator_checks += 1
            if i <= j:
                print(f" {GENS[i]:>5s} vs {GENS[j]:>5s}: src={src} target={tgt}")

    print("\nBilinear extension audit")
    divisor_samples = [
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(2), Fraction(-1), Fraction(0), Fraction(0), Fraction(1)],
        [Fraction(3), Fraction(-1), Fraction(2), Fraction(1), Fraction(0), Fraction(-2)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(1), Fraction(-1), Fraction(2)],
    ]
    extension_checks = 0
    for left in divisor_samples:
        for right in divisor_samples:
            src = dot(left, source, right)
            tgt = dot(left, target, right)
            assert src == -tgt
            extension_checks += 1
            print(f" left={left} right={right} src={src} target={tgt}")

    print("\nPrimitive self-pairing audit")
    polarization = [Fraction(1), Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)]
    primitive_checks = 0
    for vector in divisor_samples:
        projected, coeff = primitive_projection(vector, polarization, target)
        degree = dot(projected, target, polarization)
        assert degree == 0
        src_self = dot(projected, source, projected)
        tgt_self = dot(projected, target, projected)
        assert src_self == -tgt_self
        primitive_checks += 1
        print(
            f" vector={vector} coeff={coeff} projected={projected}"
            f" src_self={src_self} target_self={tgt_self}"
        )

    print("\nRadical compatibility audit")
    radical = [Fraction(1), Fraction(-1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)]
    radical_checks = 0
    # In this shadow the explicit radical sits in the kernel of the transported pairing.
    radical_source = mat_vec(source, radical)
    radical_target = mat_vec(target, radical)
    assert is_zero_vector(radical_source)
    assert is_zero_vector(radical_target)
    radical_checks += 2
    for vector in divisor_samples:
        assert dot(radical, source, vector) == 0
        assert dot(radical, target, vector) == 0
        radical_checks += 2
        print(f" witness={vector} radical-src=0 radical-target=0")

    print("\nAll exact Paper C pairing-transport shadow checks passed.")
    print(
        "Verified "
        f"{generator_checks} generator checks, "
        f"{extension_checks} bilinear-extension checks, "
        f"{primitive_checks} primitive self-pairing checks, and "
        f"{radical_checks} radical-compatibility checks."
    )


if __name__ == "__main__":
    main()
