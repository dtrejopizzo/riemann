#!/usr/bin/env python3
"""Real local information hierarchy witness for Phase 107."""

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
        "matrix": cycle_intersection_matrix(2),
        "cp": 2,
        "reduction": "nonsplit multiplicative",
    },
    {
        "label": "489762.dv3",
        "prime": 2,
        "matrix": cycle_intersection_matrix(2),
        "cp": 2,
        "reduction": "split multiplicative",
    },
    {
        "label": "14.a1",
        "prime": 2,
        "matrix": cycle_intersection_matrix(9),
        "cp": 1,
        "reduction": "nonsplit multiplicative",
    },
    {
        "label": "102.a1",
        "prime": 3,
        "matrix": cycle_intersection_matrix(2),
        "cp": 2,
        "reduction": "nonsplit multiplicative",
    },
)


def audit_source_vs_geometry() -> int:
    checks = 0
    a, _b, c, _d = ROWS
    assert source_local_weight(a["prime"]) == source_local_weight(c["prime"])
    checks += 1
    assert a["matrix"].rows != c["matrix"].rows
    checks += 1
    return checks


def audit_geometry_vs_full_label() -> int:
    checks = 0
    a, b, _c, _d = ROWS
    assert a["matrix"] == b["matrix"]
    checks += 1
    assert a["cp"] == b["cp"] == 2
    checks += 1
    assert a["reduction"] != b["reduction"]
    checks += 1
    return checks


def audit_cp_is_intermediate() -> int:
    checks = 0
    a, b, c, _d = ROWS
    assert c["cp"] != a["cp"]
    checks += 1
    assert c["cp"] != b["cp"]
    checks += 1
    assert a["cp"] == b["cp"]
    checks += 1
    return checks


def audit_repeated_i2_different_prime() -> int:
    checks = 0
    a, _b, _c, d = ROWS
    assert a["matrix"] == d["matrix"]
    checks += 1
    assert a["cp"] == d["cp"] == 2
    checks += 1
    assert source_local_weight(a["prime"]) != source_local_weight(d["prime"])
    checks += 1
    return checks


def main() -> None:
    source_geom_checks = audit_source_vs_geometry()
    geom_label_checks = audit_geometry_vs_full_label()
    cp_checks = audit_cp_is_intermediate()
    repeated_checks = audit_repeated_i2_different_prime()

    print("All real local information hierarchy checks passed.")
    print(f"  source-vs-geometry checks: {source_geom_checks}")
    print(f"  geometry-vs-label checks: {geom_label_checks}")
    print(f"  cp-intermediate checks: {cp_checks}")
    print(f"  repeated-I2 checks: {repeated_checks}")
    print(f"  source log(2) = {math.log(2):.12f}")
    print(f"  source log(3) = {math.log(3):.12f}")
    for row in ROWS:
        print(
            f"  {row['label']} @ p={row['prime']}: "
            f"matrix_size={row['matrix'].rows}, c_p={row['cp']}, reduction={row['reduction']}"
        )


if __name__ == "__main__":
    main()
