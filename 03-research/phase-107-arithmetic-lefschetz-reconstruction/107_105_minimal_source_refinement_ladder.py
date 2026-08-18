#!/usr/bin/env python3
"""Exact ladder of minimal source refinements on the pinned local atlas."""

from __future__ import annotations

import sympy as sp


ROWS = (
    {
        "label": "14.a1",
        "prime": 2,
        "kodaira": "I9",
        "cp": 1,
        "reduction": "nonsplit multiplicative",
    },
    {
        "label": "14.a5",
        "prime": 2,
        "kodaira": "I2",
        "cp": 2,
        "reduction": "nonsplit multiplicative",
    },
    {
        "label": "489762.dv3",
        "prime": 2,
        "kodaira": "I2",
        "cp": 2,
        "reduction": "split multiplicative",
    },
    {
        "label": "20.a1",
        "prime": 2,
        "kodaira": "IV",
        "cp": 1,
        "reduction": "additive",
    },
    {
        "label": "36.a4",
        "prime": 2,
        "kodaira": "IV",
        "cp": 3,
        "reduction": "additive",
    },
    {
        "label": "36.a4",
        "prime": 3,
        "kodaira": "III",
        "cp": 2,
        "reduction": "additive",
    },
    {
        "label": "4225.m2",
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


def class_count(signature) -> int:
    return len({signature(row) for row in ROWS})


def audit_counts() -> int:
    checks = 0
    assert class_count(s0) == 3
    checks += 1
    assert class_count(s1) == 5
    checks += 1
    assert class_count(s2) == 6
    checks += 1
    assert class_count(s3) == 7
    checks += 1
    return checks


def audit_strict_refinement_chain() -> int:
    checks = 0
    counts = [class_count(sig) for sig in (s0, s1, s2, s3)]
    assert counts == sorted(counts)
    checks += 1
    assert counts[0] < counts[1]
    checks += 1
    assert counts[1] < counts[2]
    checks += 1
    assert counts[2] < counts[3]
    checks += 1
    return checks


def audit_specific_separations() -> int:
    checks = 0
    i2_split = ROWS[2]
    i2_nonsplit = ROWS[1]
    iv_low = ROWS[3]
    iv_high = ROWS[4]

    assert s1(i2_split) == s1(i2_nonsplit)
    checks += 1
    assert s2(iv_low) != s2(iv_high)
    checks += 1
    assert s2(i2_split) == s2(i2_nonsplit)
    checks += 1
    assert s3(i2_split) != s3(i2_nonsplit)
    checks += 1
    return checks


def main() -> None:
    count_checks = audit_counts()
    chain_checks = audit_strict_refinement_chain()
    separation_checks = audit_specific_separations()

    print("All minimal source refinement ladder checks passed.")
    print(f"  class-count checks: {count_checks}")
    print(f"  strict-chain checks: {chain_checks}")
    print(f"  specific-separation checks: {separation_checks}")


if __name__ == "__main__":
    main()
