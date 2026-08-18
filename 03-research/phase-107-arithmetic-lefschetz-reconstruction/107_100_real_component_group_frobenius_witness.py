#!/usr/bin/env python3
"""Real local witness for multiplicative component groups and Frobenius."""

from __future__ import annotations

from math import gcd

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


ROWS = (
    {
        "label": "14.a1",
        "prime": 2,
        "n": 9,
        "kodaira": "I9",
        "reduction": "nonsplit multiplicative",
        "cp": 1,
    },
    {
        "label": "14.a1",
        "prime": 7,
        "n": 2,
        "kodaira": "I2",
        "reduction": "split multiplicative",
        "cp": 2,
    },
    {
        "label": "14.a5",
        "prime": 2,
        "n": 2,
        "kodaira": "I2",
        "reduction": "nonsplit multiplicative",
        "cp": 2,
    },
    {
        "label": "489762.dv3",
        "prime": 2,
        "n": 2,
        "kodaira": "I2",
        "reduction": "split multiplicative",
        "cp": 2,
    },
)


def reduced_cartan_a(n: int) -> sp.Matrix:
    if n < 2:
        raise ValueError("I_n requires n >= 2")
    size = n - 1
    matrix = sp.zeros(size)
    for i in range(size):
        matrix[i, i] = 2
        if i > 0:
            matrix[i, i - 1] = -1
        if i + 1 < size:
            matrix[i, i + 1] = -1
    return matrix


def geometric_component_group_order(n: int) -> int:
    matrix = reduced_cartan_a(n)
    snf = smith_normal_form(matrix)
    diag = [int(snf[i, i]) for i in range(snf.rows)]
    torsion = [d for d in diag if d not in (0, 1)]
    assert torsion == [n]
    return torsion[0]


def frobenius_fixed_size(n: int, reduction: str) -> int:
    if reduction == "split multiplicative":
        return n
    if reduction == "nonsplit multiplicative":
        return gcd(2, n)
    raise ValueError(f"Unsupported reduction type: {reduction}")


def audit_geometric_component_groups() -> int:
    checks = 0
    assert geometric_component_group_order(2) == 2
    checks += 1
    assert geometric_component_group_order(9) == 9
    checks += 1
    return checks


def audit_split_examples() -> int:
    checks = 0
    for row in ROWS:
        if row["reduction"] == "split multiplicative":
            assert frobenius_fixed_size(row["n"], row["reduction"]) == row["n"]
            checks += 1
            assert row["cp"] == row["n"]
            checks += 1
    return checks


def audit_nonsplit_examples() -> int:
    checks = 0
    for row in ROWS:
        if row["reduction"] == "nonsplit multiplicative":
            expected = gcd(2, row["n"])
            assert frobenius_fixed_size(row["n"], row["reduction"]) == expected
            checks += 1
            assert row["cp"] == expected
            checks += 1
    return checks


def audit_real_snapshot_matches_frobenius_model() -> int:
    checks = 0
    for row in ROWS:
        geom_order = geometric_component_group_order(row["n"])
        assert geom_order == row["n"]
        checks += 1
        fixed = frobenius_fixed_size(row["n"], row["reduction"])
        assert row["cp"] == fixed
        checks += 1
        assert fixed <= geom_order
        checks += 1
    return checks


def main() -> None:
    geom_checks = audit_geometric_component_groups()
    split_checks = audit_split_examples()
    nonsplit_checks = audit_nonsplit_examples()
    snapshot_checks = audit_real_snapshot_matches_frobenius_model()

    print("All real component-group Frobenius checks passed.")
    print(f"  geometric-group checks: {geom_checks}")
    print(f"  split Frobenius checks: {split_checks}")
    print(f"  nonsplit Frobenius checks: {nonsplit_checks}")
    print(f"  real-snapshot checks: {snapshot_checks}")
    for row in ROWS:
        fixed = frobenius_fixed_size(row["n"], row["reduction"])
        print(
            f"  {row['label']} @ p={row['prime']}: "
            f"Kodaira={row['kodaira']}, geometric_order={row['n']}, "
            f"fixed_size={fixed}, c_p={row['cp']}, reduction={row['reduction']}"
        )


if __name__ == "__main__":
    main()
