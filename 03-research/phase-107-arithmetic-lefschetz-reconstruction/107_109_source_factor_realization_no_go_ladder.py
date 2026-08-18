#!/usr/bin/env python3
"""Exact no-go ladder for source-factored local realizations."""

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


def target_signature(row: dict[str, object]) -> tuple[object, ...]:
    return (row["kodaira"], row["cp"], row["reduction"])


def collision_count(signature) -> int:
    groups: dict[object, set[tuple[object, ...]]] = {}
    for row in ROWS:
        groups.setdefault(signature(row), set()).add(target_signature(row))
    return sum(1 for targets in groups.values() if len(targets) > 1)


def audit_s0_no_go() -> int:
    checks = 0
    assert collision_count(s0) >= 1
    checks += 1
    p2_targets = {
        target_signature(row)
        for row in ROWS
        if s0(row) == sp.log(2)
    }
    assert len(p2_targets) == 5
    checks += 1
    return checks


def audit_s1_no_go() -> int:
    checks = 0
    assert collision_count(s1) == 2
    checks += 1
    return checks


def audit_s2_no_go() -> int:
    checks = 0
    assert collision_count(s2) == 1
    checks += 1
    return checks


def audit_s3_escape_point() -> int:
    checks = 0
    assert collision_count(s3) == 0
    checks += 1
    return checks


def main() -> None:
    s0_checks = audit_s0_no_go()
    s1_checks = audit_s1_no_go()
    s2_checks = audit_s2_no_go()
    s3_checks = audit_s3_escape_point()

    print("All source-factor realization no-go ladder checks passed.")
    print(f"  S0 no-go checks: {s0_checks}")
    print(f"  S1 no-go checks: {s1_checks}")
    print(f"  S2 no-go checks: {s2_checks}")
    print(f"  S3 escape-point checks: {s3_checks}")


if __name__ == "__main__":
    main()
