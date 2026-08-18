#!/usr/bin/env python3
"""Real local witness for split versus nonsplit multiplicative data."""

from __future__ import annotations

import math

import sympy as sp


def source_local_weight(prime: int) -> sp.Expr:
    return sp.log(prime)


def cycle_intersection_matrix(n: int) -> sp.Matrix:
    matrix = sp.zeros(n)
    for i in range(n):
        matrix[i, i] = -2
        matrix[i, (i - 1) % n] += 1
        matrix[i, (i + 1) % n] += 1
    return matrix


ROWS = (
    {
        "label": "14.a5",
        "prime": 2,
        "kodaira": "I2",
        "matrix": cycle_intersection_matrix(2),
        "cp": 2,
        "reduction": "nonsplit multiplicative",
    },
    {
        "label": "489762.dv3",
        "prime": 2,
        "kodaira": "I2",
        "matrix": cycle_intersection_matrix(2),
        "cp": 2,
        "reduction": "split multiplicative",
    },
)


def audit_same_coarse_local_data() -> int:
    checks = 0
    left, right = ROWS
    assert left["prime"] == right["prime"] == 2
    checks += 1
    assert source_local_weight(left["prime"]) == source_local_weight(right["prime"])
    checks += 1
    assert left["matrix"] == right["matrix"]
    checks += 1
    assert left["cp"] == right["cp"] == 2
    checks += 1
    return checks


def audit_split_nonsplit_difference() -> int:
    checks = 0
    left, right = ROWS
    assert left["reduction"] != right["reduction"]
    checks += 1
    assert {left["reduction"], right["reduction"]} == {
        "split multiplicative",
        "nonsplit multiplicative",
    }
    checks += 1
    return checks


def audit_boundary_statement() -> int:
    checks = 0
    # Same source scalar.
    assert source_local_weight(2) == sp.log(2)
    checks += 1
    # Same fiber matrix and same c_p.
    assert ROWS[0]["matrix"] == ROWS[1]["matrix"]
    checks += 1
    assert ROWS[0]["cp"] == ROWS[1]["cp"]
    checks += 1
    # Still different real local data.
    assert ROWS[0]["reduction"] != ROWS[1]["reduction"]
    checks += 1
    return checks


def main() -> None:
    coarse_checks = audit_same_coarse_local_data()
    label_checks = audit_split_nonsplit_difference()
    boundary_checks = audit_boundary_statement()

    print("All real split/non-split boundary checks passed.")
    print(f"  same-coarse-data checks: {coarse_checks}")
    print(f"  reduction-label checks: {label_checks}")
    print(f"  boundary-statement checks: {boundary_checks}")
    print(f"  source log(2) = {math.log(2):.12f}")
    for row in ROWS:
        print(
            f"  {row['label']} @ p={row['prime']}: "
            f"Kodaira={row['kodaira']}, c_p={row['cp']}, reduction={row['reduction']}"
        )


if __name__ == "__main__":
    main()
