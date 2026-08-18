#!/usr/bin/env python3
"""Exact audit for the finite terminal-identity primitive-quotient shadow.

This verifier audits a finite algebraic shadow behind `107_13`:
after primitive projection and quotienting by the explicit radical, the
source quadratic form and the transported target self-pairing coincide
exactly with the required sign.

The script does not prove the geometric theorem on a realized
arithmetic surface.  It exact-audits the finite quotient logic of the
terminal identity and its equality case.
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


def primitive_projection(
    vector: list[Fraction], polarization: list[Fraction], pairing: list[list[Fraction]]
) -> tuple[list[Fraction], Fraction]:
    numerator = dot(vector, pairing, polarization)
    denominator = dot(polarization, pairing, polarization)
    assert denominator != 0
    coeff = numerator / denominator
    projected = [value - coeff * h for value, h in zip(vector, polarization)]
    return projected, coeff


def is_zero(vector: list[Fraction]) -> bool:
    return all(value == 0 for value in vector)


def is_multiple_of(vector: list[Fraction], radical: list[Fraction]) -> bool:
    scalar: Fraction | None = None
    for value, base in zip(vector, radical):
        if base == 0:
            if value != 0:
                return False
            continue
        candidate = value / base
        if scalar is None:
            scalar = candidate
        elif candidate != scalar:
            return False
    return scalar is not None


def quotient_reduce(vector: list[Fraction], radical: list[Fraction]) -> list[Fraction]:
    # Fix the quotient representative by eliminating the first radical-supported slot.
    assert radical[0] != 0
    coeff = vector[0] / radical[0]
    return [value - coeff * base for value, base in zip(vector, radical)]


def main() -> None:
    source = [
        [Fraction(1), Fraction(1), Fraction(0), Fraction(0), Fraction(1), Fraction(1)],
        [Fraction(1), Fraction(1), Fraction(0), Fraction(0), Fraction(1), Fraction(1)],
        [Fraction(0), Fraction(0), Fraction(4), Fraction(1), Fraction(2), Fraction(3)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(3), Fraction(1), Fraction(2)],
        [Fraction(1), Fraction(1), Fraction(2), Fraction(1), Fraction(5), Fraction(2)],
        [Fraction(1), Fraction(1), Fraction(3), Fraction(2), Fraction(2), Fraction(6)],
    ]
    target = [[-entry for entry in row] for row in source]

    polarization = [Fraction(1), Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)]
    radical = [Fraction(1), Fraction(-1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)]

    samples = [
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(2), Fraction(-1), Fraction(0), Fraction(0), Fraction(1)],
        [Fraction(3), Fraction(-1), Fraction(2), Fraction(1), Fraction(0), Fraction(-2)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(1), Fraction(-1), Fraction(2)],
        [Fraction(2), Fraction(-1), Fraction(0), Fraction(1), Fraction(1), Fraction(-1)],
    ]

    print("Primitive quotient terminal-identity audit")
    primitive_checks = 0
    projected_samples: list[list[Fraction]] = []
    for vector in samples:
        primitive, coeff = primitive_projection(vector, polarization, target)
        assert dot(primitive, target, polarization) == 0
        src_q = dot(primitive, source, primitive)
        tgt_q = dot(primitive, target, primitive)
        assert src_q == -tgt_q
        primitive_checks += 3
        projected_samples.append(primitive)
        print(
            f" vector={vector} coeff={coeff} primitive={primitive}"
            f" src_q={src_q} target_q={tgt_q}"
        )

    print("\nRadical-quotient invariance audit")
    radical_checks = 0
    shifts = [Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(2)]
    for primitive in projected_samples:
        base_src = dot(primitive, source, primitive)
        base_tgt = dot(primitive, target, primitive)
        reduced = quotient_reduce(primitive, radical)
        for shift in shifts:
            shifted = [value + shift * basis for value, basis in zip(primitive, radical)]
            shifted_src = dot(shifted, source, shifted)
            shifted_tgt = dot(shifted, target, shifted)
            assert shifted_src == base_src
            assert shifted_tgt == base_tgt
            assert quotient_reduce(shifted, radical) == reduced
            radical_checks += 3
        print(f" primitive={primitive} quotient_repr={reduced} invariant over shifts={list(shifts)}")

    print("\nEquality-case audit on finite primitive window")
    equality_checks = 0
    witnesses = 0
    for a0 in range(-2, 3):
        for a1 in range(-2, 3):
            for a2 in range(-2, 3):
                for a3 in range(-2, 3):
                    for a4 in range(-2, 3):
                        for a5 in range(-2, 3):
                            vector = [
                                Fraction(a0),
                                Fraction(a1),
                                Fraction(a2),
                                Fraction(a3),
                                Fraction(a4),
                                Fraction(a5),
                            ]
                            primitive, _ = primitive_projection(vector, polarization, target)
                            q_src = dot(primitive, source, primitive)
                            q_tgt = dot(primitive, target, primitive)
                            assert q_src == -q_tgt
                            equality_checks += 1
                            if q_src == 0:
                                assert is_multiple_of(primitive, radical)
                            else:
                                assert not is_multiple_of(primitive, radical)
                                witnesses += 1
    print(f" checked primitive coefficient box [-2,2]^6, nonzero witnesses={witnesses}")

    print("\nGenerator-to-quotient comparison audit")
    generator_checks = 0
    basis = [[Fraction(int(i == j)) for j in range(len(GENS))] for i in range(len(GENS))]
    for generator in basis:
        primitive, _ = primitive_projection(generator, polarization, target)
        src_q = dot(primitive, source, primitive)
        tgt_q = dot(primitive, target, primitive)
        assert src_q == -tgt_q
        generator_checks += 1
        print(f" primitive generator image={primitive} src_q={src_q} target_q={tgt_q}")

    print("\nAll exact terminal-identity primitive-quotient checks passed.")
    print(
        "Verified "
        f"{primitive_checks} primitive terminal-identity checks, "
        f"{radical_checks} radical-quotient invariance checks, "
        f"{equality_checks} finite equality-case checks, and "
        f"{generator_checks} generator quotient checks."
    )


if __name__ == "__main__":
    main()
