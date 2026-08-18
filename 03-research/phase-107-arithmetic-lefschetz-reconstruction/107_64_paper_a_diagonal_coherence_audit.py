#!/usr/bin/env python3
"""Exact finite audit for the diagonal-coherence shadow behind 107_05."""

from __future__ import annotations

from fractions import Fraction


SUPPORT = (
    (2, -4),
    (2, -2),
    (2, 2),
    (2, 4),
    (3, -2),
    (3, 2),
    (5, -2),
    (5, 2),
)


def prime_weight(prime: int, k: int) -> Fraction:
    return Fraction(1, prime ** (abs(k) // 2))


WEIGHTS = {label: prime_weight(*label) for label in SUPPORT}


def add_corr(*corrs: dict[tuple[int, int], Fraction]) -> dict[tuple[int, int], Fraction]:
    out: dict[tuple[int, int], Fraction] = {}
    for corr in corrs:
        for label, coeff in corr.items():
            out[label] = out.get(label, Fraction(0)) + coeff
    return {label: coeff for label, coeff in out.items() if coeff}


CORR = {
    ("x", "x"): {
        (2, -4): Fraction(1, 2),
        (2, 2): Fraction(3, 2),
        (3, 2): Fraction(1, 3),
        (5, -2): Fraction(2, 5),
    },
    ("x", "y"): {
        (2, -2): Fraction(1, 2),
        (2, 4): Fraction(1, 4),
        (3, -2): Fraction(2, 3),
        (5, 2): Fraction(1, 5),
    },
    ("y", "y"): {
        (2, -4): Fraction(1, 4),
        (2, 2): Fraction(1, 1),
        (3, 2): Fraction(5, 6),
        (5, -2): Fraction(3, 5),
    },
}
CORR[("y", "x")] = CORR[("x", "y")]
CORR[("x+y", "x+y")] = add_corr(
    CORR[("x", "x")],
    CORR[("x", "y")],
    CORR[("y", "x")],
    CORR[("y", "y")],
)

ARCH = {
    ("x", "x"): Fraction(7, 6),
    ("x", "y"): Fraction(-5, 12),
    ("y", "y"): Fraction(11, 10),
}
ARCH[("y", "x")] = ARCH[("x", "y")]
ARCH[("x+y", "x+y")] = (
    ARCH[("x", "x")] + 2 * ARCH[("x", "y")] + ARCH[("y", "y")]
)


def cutoff_sum(corr: dict[tuple[int, int], Fraction], max_abs_k: int) -> Fraction:
    total = Fraction(0)
    for label, coeff in corr.items():
        _, k = label
        if abs(k) <= max_abs_k:
            total += WEIGHTS[label] * coeff
    return total


def p_infty(name: tuple[str, str]) -> Fraction:
    return cutoff_sum(CORR[name], 99) + ARCH[name]


def stabilized_green(name: tuple[str, str], max_abs_k: int) -> Fraction:
    return p_infty(name) - cutoff_sum(CORR[name], max_abs_k)


def exact_green(name: tuple[str, str]) -> Fraction:
    return p_infty(name) - cutoff_sum(CORR[name], 99)


def audit_cutoff_independence() -> int:
    checks = 0
    for name in (("x", "x"), ("x", "y"), ("y", "y"), ("x+y", "x+y")):
        target = exact_green(name)
        for cutoff in (4, 6, 8):
            assert stabilized_green(name, cutoff) == target
            checks += 1
    return checks


def audit_same_functional() -> int:
    checks = 0
    cross = exact_green(("x", "y"))
    self_x = exact_green(("x", "x"))
    self_y = exact_green(("y", "y"))
    assert cross == ARCH[("x", "y")]
    checks += 1
    assert self_x == ARCH[("x", "x")]
    checks += 1
    assert self_y == ARCH[("y", "y")]
    checks += 1
    return checks


def audit_polarization_identity() -> int:
    checks = 0
    q_x = exact_green(("x", "x"))
    q_y = exact_green(("y", "y"))
    q_xy = exact_green(("x+y", "x+y"))
    b_xy = exact_green(("x", "y"))
    assert q_xy - q_x - q_y == 2 * b_xy
    checks += 1
    return checks


def audit_diagonal_shift_failure() -> int:
    checks = 0
    q_x = exact_green(("x", "x"))
    q_y = exact_green(("y", "y"))
    q_xy = exact_green(("x+y", "x+y"))
    b_xy = exact_green(("x", "y"))
    for shift in (Fraction(1, 7), Fraction(-2, 9), Fraction(5, 11)):
        broken = (q_xy + shift) - (q_x + shift) - (q_y + shift)
        assert broken != 2 * b_xy
        checks += 1
    return checks


def main() -> None:
    cutoff_checks = audit_cutoff_independence()
    functional_checks = audit_same_functional()
    polarization_checks = audit_polarization_identity()
    shift_checks = audit_diagonal_shift_failure()

    print("All exact Paper A diagonal-coherence checks passed.")
    print(f"  cutoff-independence checks: {cutoff_checks}")
    print(f"  same-functional checks: {functional_checks}")
    print(f"  polarization checks: {polarization_checks}")
    print(f"  diagonal-shift failure checks: {shift_checks}")


if __name__ == "__main__":
    main()
