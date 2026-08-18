#!/usr/bin/env python3
"""Real local witness separating fiber geometry from Tamagawa data."""

from __future__ import annotations

import sympy as sp


SNAPSHOT = (
    {"label": "14.a1", "prime": 2, "kodaira": "I_{9}", "reduction": "nonsplit multiplicative", "cp": 1},
    {"label": "14.a1", "prime": 7, "kodaira": "I_{2}", "reduction": "split multiplicative", "cp": 2},
    {"label": "14.a5", "prime": 2, "kodaira": "I_{2}", "reduction": "nonsplit multiplicative", "cp": 2},
)


def cycle_intersection_matrix(n: int) -> sp.Matrix:
    matrix = sp.zeros(n)
    for i in range(n):
        matrix[i, i] = -2
        matrix[i, (i - 1) % n] += 1
        matrix[i, (i + 1) % n] += 1
    return matrix


def reduced_cofactor(matrix: sp.Matrix) -> int:
    minor = matrix[1:, 1:]
    return abs(int(minor.det()))


def audit_i2_examples() -> int:
    checks = 0
    matrix = cycle_intersection_matrix(2)
    cof = reduced_cofactor(matrix)
    assert cof == 2
    checks += 1
    for row in SNAPSHOT:
        if row["kodaira"] == "I_{2}":
            assert row["cp"] == cof
            checks += 1
    return checks


def audit_i9_boundary() -> int:
    checks = 0
    matrix = cycle_intersection_matrix(9)
    cof = reduced_cofactor(matrix)
    assert cof == 9
    checks += 1
    row = next(r for r in SNAPSHOT if r["kodaira"] == "I_{9}")
    assert row["cp"] == 1
    checks += 1
    assert cof != row["cp"]
    checks += 1
    return checks


def audit_same_geometry_different_reduction_labels() -> int:
    checks = 0
    i2_rows = [r for r in SNAPSHOT if r["kodaira"] == "I_{2}"]
    assert len(i2_rows) == 2
    checks += 1
    reductions = {r["reduction"] for r in i2_rows}
    assert reductions == {"split multiplicative", "nonsplit multiplicative"}
    checks += 1
    assert all(r["cp"] == 2 for r in i2_rows)
    checks += 1
    return checks


def main() -> None:
    i2_checks = audit_i2_examples()
    i9_checks = audit_i9_boundary()
    label_checks = audit_same_geometry_different_reduction_labels()

    print("All real component-group boundary checks passed.")
    print(f"  I2 cofactor checks: {i2_checks}")
    print(f"  I9 boundary checks: {i9_checks}")
    print(f"  reduction-label checks: {label_checks}")
    for row in SNAPSHOT:
        print(
            f"  {row['label']} @ p={row['prime']}: "
            f"Kodaira={row['kodaira']}, reduction={row['reduction']}, c_p={row['cp']}"
        )


if __name__ == "__main__":
    main()
