#!/usr/bin/env python3
"""Exact necessity gate for future local source upgrades."""

from __future__ import annotations

import sympy as sp


ROWS = {
    "i9": {
        "prime": 2,
        "kodaira": "I9",
        "cp": 1,
        "reduction": "nonsplit multiplicative",
    },
    "i2_ns": {
        "prime": 2,
        "kodaira": "I2",
        "cp": 2,
        "reduction": "nonsplit multiplicative",
    },
    "i2_sp": {
        "prime": 2,
        "kodaira": "I2",
        "cp": 2,
        "reduction": "split multiplicative",
    },
    "iv_1": {
        "prime": 2,
        "kodaira": "IV",
        "cp": 1,
        "reduction": "additive",
    },
    "iv_3": {
        "prime": 2,
        "kodaira": "IV",
        "cp": 3,
        "reduction": "additive",
    },
}


def s0(row: dict[str, object]) -> object:
    return sp.log(int(row["prime"]))


def s1(row: dict[str, object]) -> tuple[object, ...]:
    return (row["prime"], row["kodaira"])


def s2(row: dict[str, object]) -> tuple[object, ...]:
    return (row["prime"], row["kodaira"], row["cp"])


def s3(row: dict[str, object]) -> tuple[object, ...]:
    return (row["prime"], row["kodaira"], row["cp"], row["reduction"])


SIGNATURES = (s0, s1, s2, s3)


def separates(signature, left: str, right: str) -> bool:
    return signature(ROWS[left]) != signature(ROWS[right])


def audit_geometry_gate() -> int:
    checks = 0
    assert not separates(s0, "i9", "i2_ns")
    checks += 1
    assert separates(s1, "i9", "i2_ns")
    checks += 1
    assert separates(s2, "i9", "i2_ns")
    checks += 1
    assert separates(s3, "i9", "i2_ns")
    checks += 1
    return checks


def audit_cp_gate() -> int:
    checks = 0
    assert not separates(s0, "iv_1", "iv_3")
    checks += 1
    assert not separates(s1, "iv_1", "iv_3")
    checks += 1
    assert separates(s2, "iv_1", "iv_3")
    checks += 1
    assert separates(s3, "iv_1", "iv_3")
    checks += 1
    return checks


def audit_fine_label_gate() -> int:
    checks = 0
    assert not separates(s0, "i2_ns", "i2_sp")
    checks += 1
    assert not separates(s1, "i2_ns", "i2_sp")
    checks += 1
    assert not separates(s2, "i2_ns", "i2_sp")
    checks += 1
    assert separates(s3, "i2_ns", "i2_sp")
    checks += 1
    return checks


def main() -> None:
    geometry_checks = audit_geometry_gate()
    cp_checks = audit_cp_gate()
    fine_checks = audit_fine_label_gate()

    print("All local source upgrade necessity gate checks passed.")
    print(f"  geometry-gate checks: {geometry_checks}")
    print(f"  cp-gate checks: {cp_checks}")
    print(f"  fine-label-gate checks: {fine_checks}")


if __name__ == "__main__":
    main()
