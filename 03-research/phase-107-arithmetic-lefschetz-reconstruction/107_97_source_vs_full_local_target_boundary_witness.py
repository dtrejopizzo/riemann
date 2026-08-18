#!/usr/bin/env python3
"""Assemble the local real boundaries between source, geometry, and arithmetic."""

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


REAL_ROWS = (
    {"label": "14.a5", "prime": 2, "kodaira": "I2", "matrix": cycle_intersection_matrix(2), "cp": 2},
    {"label": "14.a1", "prime": 2, "kodaira": "I9", "matrix": cycle_intersection_matrix(9), "cp": 1},
    {"label": "102.a1", "prime": 3, "kodaira": "I2", "matrix": cycle_intersection_matrix(2), "cp": 2},
)


def audit_same_prime_source_is_too_coarse() -> int:
    checks = 0
    row_i2 = REAL_ROWS[0]
    row_i9 = REAL_ROWS[1]
    assert source_local_weight(row_i2["prime"]) == source_local_weight(row_i9["prime"])
    checks += 1
    assert row_i2["matrix"].rows != row_i9["matrix"].rows
    checks += 1
    assert row_i2["cp"] != row_i9["cp"]
    checks += 1
    return checks


def audit_same_geometry_different_primes() -> int:
    checks = 0
    row_2 = REAL_ROWS[0]
    row_3 = REAL_ROWS[2]
    assert row_2["matrix"] == row_3["matrix"]
    checks += 1
    assert row_2["cp"] == row_3["cp"] == 2
    checks += 1
    assert source_local_weight(2) != source_local_weight(3)
    checks += 1
    return checks


def audit_nested_boundary() -> int:
    checks = 0
    # Source sees only the prime.
    assert source_local_weight(2) == sp.log(2)
    checks += 1
    # Geometry sees Kodaira type.
    assert cycle_intersection_matrix(2) != cycle_intersection_matrix(9)[:2, :2]
    checks += 1
    # Full local target can still distinguish cp.
    assert REAL_ROWS[0]["cp"] != REAL_ROWS[1]["cp"]
    checks += 1
    return checks


def main() -> None:
    coarse_checks = audit_same_prime_source_is_too_coarse()
    repeated_checks = audit_same_geometry_different_primes()
    boundary_checks = audit_nested_boundary()

    print("All source-vs-full-local-target boundary checks passed.")
    print(f"  same-prime source-coarseness checks: {coarse_checks}")
    print(f"  repeated-geometry checks: {repeated_checks}")
    print(f"  nested-boundary checks: {boundary_checks}")
    print(f"  source log(2) = {math.log(2):.12f}")
    print(f"  source log(3) = {math.log(3):.12f}")
    for row in REAL_ROWS:
        print(
            f"  {row['label']} @ p={row['prime']}: "
            f"Kodaira={row['kodaira']}, matrix_size={row['matrix'].rows}, c_p={row['cp']}"
        )


if __name__ == "__main__":
    main()
