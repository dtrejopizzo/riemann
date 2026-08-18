#!/usr/bin/env python3
"""Real local witness for additive IV fibers and Frobenius action."""

from __future__ import annotations

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


ROWS = (
    {
        "label": "20.a1",
        "prime": 2,
        "kodaira": "IV",
        "cp": 1,
        "reduction": "additive",
        "frobenius_action": "3-cycle",
    },
    {
        "label": "36.a4",
        "prime": 2,
        "kodaira": "IV",
        "cp": 3,
        "reduction": "additive",
        "frobenius_action": "trivial",
    },
)


def affine_a2_intersection_matrix() -> sp.Matrix:
    return sp.Matrix(
        [
            [-2, 1, 1],
            [1, -2, 1],
            [1, 1, -2],
        ]
    )


def reduced_cartan_a2() -> sp.Matrix:
    return sp.Matrix(
        [
            [2, -1],
            [-1, 2],
        ]
    )


def geometric_component_group_order() -> int:
    snf = smith_normal_form(reduced_cartan_a2())
    diag = [int(snf[i, i]) for i in range(snf.rows)]
    torsion = [d for d in diag if d not in (0, 1)]
    assert torsion == [3]
    return torsion[0]


def frobenius_fixed_size(action: str) -> int:
    if action == "trivial":
        return 3
    if action == "3-cycle":
        return 1
    raise ValueError(f"Unsupported Frobenius action: {action}")


def audit_affine_iv_geometry() -> int:
    checks = 0
    matrix = affine_a2_intersection_matrix()
    ones = sp.Matrix([1, 1, 1])
    assert matrix * ones == sp.zeros(3, 1)
    checks += 1
    assert matrix.rank() == 2
    checks += 1
    assert matrix == matrix.T
    checks += 1
    return checks


def audit_geometric_component_group() -> int:
    checks = 0
    assert geometric_component_group_order() == 3
    checks += 1
    return checks


def audit_frobenius_models() -> int:
    checks = 0
    assert frobenius_fixed_size("trivial") == 3
    checks += 1
    assert frobenius_fixed_size("3-cycle") == 1
    checks += 1
    return checks


def audit_real_rows() -> int:
    checks = 0
    for row in ROWS:
        assert row["kodaira"] == "IV"
        checks += 1
        assert row["reduction"] == "additive"
        checks += 1
        assert row["cp"] == frobenius_fixed_size(row["frobenius_action"])
        checks += 1
    return checks


def main() -> None:
    geometry_checks = audit_affine_iv_geometry()
    component_checks = audit_geometric_component_group()
    frobenius_checks = audit_frobenius_models()
    row_checks = audit_real_rows()

    print("All real additive IV Frobenius checks passed.")
    print(f"  affine-IV geometry checks: {geometry_checks}")
    print(f"  geometric-component checks: {component_checks}")
    print(f"  Frobenius-model checks: {frobenius_checks}")
    print(f"  real-row checks: {row_checks}")
    for row in ROWS:
        print(
            f"  {row['label']} @ p={row['prime']}: "
            f"Kodaira={row['kodaira']}, action={row['frobenius_action']}, "
            f"fixed_size={frobenius_fixed_size(row['frobenius_action'])}, "
            f"c_p={row['cp']}, reduction={row['reduction']}"
        )


if __name__ == "__main__":
    main()
