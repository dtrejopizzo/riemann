#!/usr/bin/env python3
"""Compare real repeated Kodaira types across different primes."""

from __future__ import annotations

import math
from dataclasses import dataclass

import sympy as sp


@dataclass(frozen=True)
class LocalRow:
    label: str
    prime: int
    kodaira: str
    reduction_type: str
    tamagawa: int
    ord_disc: int


SNAPSHOT = (
    LocalRow("14.a5", 2, "I_{2}", "nonsplit multiplicative", 2, 2),
    LocalRow("102.a1", 2, "I_{2}", "nonsplit multiplicative", 2, 2),
    LocalRow("102.a1", 3, "I_{2}", "nonsplit multiplicative", 2, 2),
    LocalRow("14.a1", 2, "I_{9}", "nonsplit multiplicative", 1, 9),
)


def cycle_intersection_matrix(n: int) -> sp.Matrix:
    matrix = sp.zeros(n)
    for i in range(n):
        matrix[i, i] = -2
        matrix[i, (i - 1) % n] += 1
        matrix[i, (i + 1) % n] += 1
    return matrix


def matrix_for_kodaira(symbol: str) -> sp.Matrix:
    if symbol == "I_{2}":
        return cycle_intersection_matrix(2)
    if symbol == "I_{9}":
        return cycle_intersection_matrix(9)
    raise ValueError(symbol)


def audit_repeated_i2_geometry() -> int:
    checks = 0
    i2_rows = [row for row in SNAPSHOT if row.kodaira == "I_{2}"]
    base = matrix_for_kodaira("I_{2}")
    for row in i2_rows:
        assert matrix_for_kodaira(row.kodaira) == base
        checks += 1
        assert row.ord_disc == 2
        checks += 1
        assert row.tamagawa == 2
        checks += 1
    return checks


def audit_log_weight_scaling() -> int:
    checks = 0
    base = matrix_for_kodaira("I_{2}")
    weighted_2 = sp.log(2) * base
    weighted_3 = sp.log(3) * base
    assert weighted_2 != weighted_3
    checks += 1
    ratio = weighted_3[0, 0] / weighted_2[0, 0]
    assert sp.simplify(ratio - sp.log(3) / sp.log(2)) == 0
    checks += 1
    assert weighted_2 / sp.log(2) == base
    checks += 1
    assert weighted_3 / sp.log(3) == base
    checks += 1
    return checks


def audit_type_change_changes_geometry() -> int:
    checks = 0
    i2 = matrix_for_kodaira("I_{2}")
    i9 = matrix_for_kodaira("I_{9}")
    assert i2.rows != i9.rows
    checks += 1
    assert i2 != i9[:2, :2]
    checks += 1
    return checks


def main() -> None:
    geometry_checks = audit_repeated_i2_geometry()
    scaling_checks = audit_log_weight_scaling()
    type_checks = audit_type_change_changes_geometry()

    print("All real Kodaira-type log-weight comparison checks passed.")
    print(f"  repeated-I2 geometry checks: {geometry_checks}")
    print(f"  log-weight scaling checks: {scaling_checks}")
    print(f"  type-change checks: {type_checks}")
    for row in SNAPSHOT:
        print(
            f"  {row.label} @ p={row.prime}: "
            f"Kodaira={row.kodaira}, reduction={row.reduction_type}, "
            f"c_p={row.tamagawa}, ord_p(Delta)={row.ord_disc}, "
            f"log(p)={math.log(row.prime):.12f}"
        )


if __name__ == "__main__":
    main()
