#!/usr/bin/env python3
"""Exact finite audit for the load-bearing shadow of 107_00 §20."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


VISIBLE_TESTS = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
    (1, 1, 0, 0),
    (0, 1, 1, 0),
)
RADICAL = (1, -1, 0, 0)


def is_radical(vec: tuple[int, int, int, int]) -> bool:
    return vec == RADICAL or vec == tuple(-x for x in RADICAL)


def algebraic_part(vec: tuple[int, int, int, int]) -> tuple[Fraction, Fraction]:
    a, b, c, d = map(Fraction, vec)
    return (a + b, c + d)


def green_part_full(
    vec: tuple[int, int, int, int]
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    return tuple(Fraction(x) for x in vec)


def green_part_truncated(
    vec: tuple[int, int, int, int]
) -> tuple[Fraction, Fraction]:
    a, b, _c, _d = map(Fraction, vec)
    return (a - b, a + 2 * b)


def combined_full(vec: tuple[int, int, int, int]) -> tuple[Fraction, ...]:
    return algebraic_part(vec) + green_part_full(vec)


def combined_truncated(vec: tuple[int, int, int, int]) -> tuple[Fraction, ...]:
    return algebraic_part(vec) + green_part_truncated(vec)


def audit_algebraic_collisions() -> int:
    checks = 0
    collisions = []
    for left, right in product(VISIBLE_TESTS, repeat=2):
        if left >= right:
            continue
        if algebraic_part(left) == algebraic_part(right):
            diff = tuple(l - r for l, r in zip(left, right))
            if not is_radical(diff):
                collisions.append((left, right, diff))
    assert collisions
    for left, right, diff in collisions:
        assert not is_radical(diff)
        checks += 1
    return checks


def audit_full_green_separates() -> int:
    checks = 0
    for left, right in product(VISIBLE_TESTS, repeat=2):
        if left == right:
            continue
        assert combined_full(left) != combined_full(right)
        checks += 1
    return checks


def audit_truncated_green_collides() -> int:
    checks = 0
    collisions = []
    for left, right in product(VISIBLE_TESTS, repeat=2):
        if left >= right:
            continue
        if combined_truncated(left) == combined_truncated(right):
            diff = tuple(l - r for l, r in zip(left, right))
            collisions.append((left, right, diff))
    assert collisions
    for left, right, diff in collisions:
        assert not is_radical(diff)
        checks += 1
    return checks


def audit_nonradical_collision_witness() -> int:
    checks = 0
    left = (1, 0, 0, 1)
    right = (0, 1, 1, 0)
    assert algebraic_part(left) == algebraic_part(right)
    checks += 1
    diff = tuple(l - r for l, r in zip(left, right))
    assert not is_radical(diff)
    checks += 1
    assert combined_full(left) != combined_full(right)
    checks += 1
    return checks


def main() -> None:
    algebraic_checks = audit_algebraic_collisions()
    full_green_checks = audit_full_green_separates()
    truncated_checks = audit_truncated_green_collides()
    witness_checks = audit_nonradical_collision_witness()

    print("All exact archimedean load-bearing checks passed.")
    print(f"  algebraic-collision checks: {algebraic_checks}")
    print(f"  full-green separation checks: {full_green_checks}")
    print(f"  truncated-green collision checks: {truncated_checks}")
    print(f"  nonradical witness checks: {witness_checks}")


if __name__ == "__main__":
    main()
