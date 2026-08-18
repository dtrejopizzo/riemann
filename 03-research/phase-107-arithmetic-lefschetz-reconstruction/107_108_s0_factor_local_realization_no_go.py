#!/usr/bin/env python3
"""Exact no-go for local realization maps factoring through S0."""

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


def target_signature(row: dict[str, object]) -> tuple[object, ...]:
    return (row["kodaira"], row["cp"], row["reduction"])


def audit_p2_collapse_under_s0() -> int:
    checks = 0
    p2_rows = [row for row in ROWS if row["prime"] == 2]
    assert len(p2_rows) == 5
    checks += 1
    assert {s0(row) for row in p2_rows} == {sp.log(2)}
    checks += 1
    assert len({target_signature(row) for row in p2_rows}) == 5
    checks += 1
    return checks


def audit_no_s0_factor_faithfulness() -> int:
    checks = 0
    # Any factor-through-S0 map is constant on each S0 fiber.
    p2_rows = [row for row in ROWS if row["prime"] == 2]
    s0_fiber = {row["name"] for row in p2_rows}
    assert len(s0_fiber) == 5
    checks += 1
    target_fiber = {target_signature(row) for row in p2_rows}
    assert len(target_fiber) == 5
    checks += 1
    # Therefore identity on target signatures cannot factor through S0 on this fiber.
    assert len(s0_fiber) == len(target_fiber) and len(s0_fiber) > 1
    checks += 1
    return checks


def audit_global_nonfaithfulness_on_pinned_atlas() -> int:
    checks = 0
    source_classes = {}
    for row in ROWS:
        source_classes.setdefault(s0(row), set()).add(row["name"])
    # Faithfulness fails because one source class has more than one distinct target state.
    assert any(len(names) > 1 for names in source_classes.values())
    checks += 1
    assert any(
        len({target_signature(row) for row in ROWS if row["name"] in names}) > 1
        for names in source_classes.values()
    )
    checks += 1
    return checks


def main() -> None:
    p2_checks = audit_p2_collapse_under_s0()
    factor_checks = audit_no_s0_factor_faithfulness()
    global_checks = audit_global_nonfaithfulness_on_pinned_atlas()

    print("All S0-factor local realization no-go checks passed.")
    print(f"  p=2 collapse checks: {p2_checks}")
    print(f"  factor-faithfulness checks: {factor_checks}")
    print(f"  global nonfaithfulness checks: {global_checks}")


if __name__ == "__main__":
    main()
