#!/usr/bin/env python3
"""Residual ambiguity matrix for the minimal source refinement ladder."""

from __future__ import annotations

import sympy as sp


ROWS = (
    {
        "name": "14.a1@2:I9:cp1:nonsplit",
        "prime": 2,
        "kodaira": "I9",
        "cp": 1,
        "reduction": "nonsplit multiplicative",
    },
    {
        "name": "14.a5@2:I2:cp2:nonsplit",
        "prime": 2,
        "kodaira": "I2",
        "cp": 2,
        "reduction": "nonsplit multiplicative",
    },
    {
        "name": "489762.dv3@2:I2:cp2:split",
        "prime": 2,
        "kodaira": "I2",
        "cp": 2,
        "reduction": "split multiplicative",
    },
    {
        "name": "20.a1@2:IV:cp1:additive",
        "prime": 2,
        "kodaira": "IV",
        "cp": 1,
        "reduction": "additive",
    },
    {
        "name": "36.a4@2:IV:cp3:additive",
        "prime": 2,
        "kodaira": "IV",
        "cp": 3,
        "reduction": "additive",
    },
    {
        "name": "36.a4@3:III:cp2:additive",
        "prime": 3,
        "kodaira": "III",
        "cp": 2,
        "reduction": "additive",
    },
    {
        "name": "4225.m2@5:III:cp2:additive",
        "prime": 5,
        "kodaira": "III",
        "cp": 2,
        "reduction": "additive",
    },
)


def s0(row: dict[str, object]) -> object:
    return sp.log(int(row["prime"]))


def s1(row: dict[str, object]) -> tuple[object, ...]:
    return (row["prime"], row["kodaira"])


def s2(row: dict[str, object]) -> tuple[object, ...]:
    return (row["prime"], row["kodaira"], row["cp"])


def s3(row: dict[str, object]) -> tuple[object, ...]:
    return (row["prime"], row["kodaira"], row["cp"], row["reduction"])


def collisions(signature) -> list[set[str]]:
    groups: dict[object, set[str]] = {}
    for row in ROWS:
        groups.setdefault(signature(row), set()).add(str(row["name"]))
    return [names for names in groups.values() if len(names) > 1]


def audit_s0_collision() -> int:
    checks = 0
    groups = collisions(s0)
    assert len(groups) == 1
    checks += 1
    assert len(groups[0]) == 5
    checks += 1
    expected = {
        "14.a1@2:I9:cp1:nonsplit",
        "14.a5@2:I2:cp2:nonsplit",
        "489762.dv3@2:I2:cp2:split",
        "20.a1@2:IV:cp1:additive",
        "36.a4@2:IV:cp3:additive",
    }
    assert groups[0] == expected
    checks += 1
    return checks


def audit_s1_collision() -> int:
    checks = 0
    groups = collisions(s1)
    assert len(groups) == 2
    checks += 1
    expected_iv = {
        "20.a1@2:IV:cp1:additive",
        "36.a4@2:IV:cp3:additive",
    }
    expected_i2 = {
        "14.a5@2:I2:cp2:nonsplit",
        "489762.dv3@2:I2:cp2:split",
    }
    group_set = {frozenset(group) for group in groups}
    assert group_set == {frozenset(expected_iv), frozenset(expected_i2)}
    checks += 1
    return checks


def audit_s2_collision() -> int:
    checks = 0
    groups = collisions(s2)
    assert len(groups) == 1
    checks += 1
    expected = {
        "14.a5@2:I2:cp2:nonsplit",
        "489762.dv3@2:I2:cp2:split",
    }
    assert groups[0] == expected
    checks += 1
    return checks


def audit_s3_no_collision() -> int:
    checks = 0
    groups = collisions(s3)
    assert groups == []
    checks += 1
    return checks


def main() -> None:
    s0_checks = audit_s0_collision()
    s1_checks = audit_s1_collision()
    s2_checks = audit_s2_collision()
    s3_checks = audit_s3_no_collision()

    print("All source refinement residual ambiguity checks passed.")
    print(f"  S0 collision checks: {s0_checks}")
    print(f"  S1 collision checks: {s1_checks}")
    print(f"  S2 collision checks: {s2_checks}")
    print(f"  S3 no-collision checks: {s3_checks}")


if __name__ == "__main__":
    main()
