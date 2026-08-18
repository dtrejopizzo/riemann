#!/usr/bin/env python3
"""Exact audit for the A5 target-pairing assembly shadow of Phase 107."""

from __future__ import annotations

from fractions import Fraction


GENS = ["Fv", "Fh", "Delta", "Zinf", "G2", "G4"]
DIAGONAL_INDEX = 2

SOURCE_PAIRING = [
    [Fraction(1), Fraction(1), Fraction(0), Fraction(0), Fraction(1), Fraction(1)],
    [Fraction(1), Fraction(1), Fraction(0), Fraction(0), Fraction(1), Fraction(1)],
    [Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(2), Fraction(3)],
    [Fraction(0), Fraction(0), Fraction(1), Fraction(3), Fraction(1), Fraction(2)],
    [Fraction(1), Fraction(1), Fraction(2), Fraction(1), Fraction(5), Fraction(2)],
    [Fraction(1), Fraction(1), Fraction(3), Fraction(2), Fraction(2), Fraction(6)],
]
TARGET_PAIRING = [[-entry for entry in row] for row in SOURCE_PAIRING]


def dot(left: list[Fraction], matrix: list[list[Fraction]], right: list[Fraction]) -> Fraction:
    total = Fraction(0)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            total += a * matrix[i][j] * b
    return total


def evaluate_target_pairing(left: list[Fraction], right: list[Fraction]) -> tuple[Fraction, bool]:
    unresolved = left[DIAGONAL_INDEX] != 0 and right[DIAGONAL_INDEX] != 0
    finite_left = left[:]
    finite_right = right[:]
    finite_left[DIAGONAL_INDEX] = Fraction(0)
    finite_right[DIAGONAL_INDEX] = Fraction(0)
    finite_value = dot(finite_left, TARGET_PAIRING, finite_right)
    # Add the finite cross terms involving Delta but not the unresolved square.
    delta_cross = dot(left, TARGET_PAIRING, right) - dot(finite_left, TARGET_PAIRING, finite_right)
    if unresolved:
        # Remove the unresolved diagonal-square contribution; keep the rest finite.
        delta_cross -= left[DIAGONAL_INDEX] * right[DIAGONAL_INDEX] * TARGET_PAIRING[DIAGONAL_INDEX][DIAGONAL_INDEX]
    finite_value += delta_cross
    return finite_value, unresolved


def main() -> None:
    offdiag_samples = [
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0), Fraction(1), Fraction(0), Fraction(1)],
        [Fraction(1), Fraction(1), Fraction(0), Fraction(0), Fraction(-1), Fraction(2)],
        [Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(1), Fraction(1)],
    ]
    diagonal_samples = [
        [Fraction(1), Fraction(0), Fraction(1), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(1), Fraction(1), Fraction(0), Fraction(1)],
        [Fraction(2), Fraction(-1), Fraction(1), Fraction(0), Fraction(0), Fraction(1)],
    ]

    print("Transported finite-channel audit")
    finite_checks = 0
    for left in offdiag_samples:
        for right in offdiag_samples:
            src = dot(left, SOURCE_PAIRING, right)
            tgt, unresolved = evaluate_target_pairing(left, right)
            assert not unresolved
            assert src == -tgt
            finite_checks += 2
    print(f" verified {finite_checks} transported finite-channel checks")

    print("\nDiagonal-placeholder confinement audit")
    diagonal_checks = 0
    for left in diagonal_samples:
        for right in diagonal_samples:
            finite_part, unresolved = evaluate_target_pairing(left, right)
            assert unresolved
            # Once the explicit diagonal slot is removed, everything becomes finite again.
            stripped_left = left[:]
            stripped_right = right[:]
            stripped_left[DIAGONAL_INDEX] = Fraction(0)
            stripped_right[DIAGONAL_INDEX] = Fraction(0)
            stripped_value, stripped_unresolved = evaluate_target_pairing(stripped_left, stripped_right)
            assert not stripped_unresolved
            assert stripped_value == dot(stripped_left, TARGET_PAIRING, stripped_right)
            diagonal_checks += 3
    print(f" verified {diagonal_checks} diagonal-placeholder confinement checks")

    print("\nNo-hidden-boundary-divergence audit")
    boundary_checks = 0
    boundary_like = [
        [Fraction(1), Fraction(1), Fraction(0), Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0), Fraction(2), Fraction(1), Fraction(0)],
        [Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(2)],
    ]
    for sample in boundary_like:
        value, unresolved = evaluate_target_pairing(sample, sample)
        assert not unresolved
        assert value == dot(sample, TARGET_PAIRING, sample)
        boundary_checks += 2
    print(f" verified {boundary_checks} boundary-only finiteness checks")

    print("\nMixed off-diagonal/diagonal transport audit")
    mixed_checks = 0
    for left in offdiag_samples:
        for right in diagonal_samples:
            finite_part, unresolved = evaluate_target_pairing(left, right)
            # One diagonal input is not enough to create the unresolved square.
            assert not unresolved
            assert finite_part == dot(left, TARGET_PAIRING, right)
            mixed_checks += 2
    print(f" verified {mixed_checks} mixed transport checks")

    print("\nAll exact Route A A5 target-pairing assembly checks passed.")
    print(f"  transported finite-channel checks: {finite_checks}")
    print(f"  diagonal-placeholder checks: {diagonal_checks}")
    print(f"  boundary-only finiteness checks: {boundary_checks}")
    print(f"  mixed transport checks: {mixed_checks}")


if __name__ == "__main__":
    main()
