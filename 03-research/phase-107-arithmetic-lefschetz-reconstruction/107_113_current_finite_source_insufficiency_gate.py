#!/usr/bin/env python3
"""Unified insufficiency gate for the current finite source package."""

from __future__ import annotations

import sympy as sp


LOCAL_ROWS = (
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

GLOBAL_CURVES = (
    {
        "label": "14.a1",
        "bad_primes": (2, 7),
        "local_signature_p2": ("I9", 1, "nonsplit multiplicative"),
    },
    {
        "label": "14.a5",
        "bad_primes": (2, 7),
        "local_signature_p2": ("I2", 2, "nonsplit multiplicative"),
    },
)


def target_signature(row: dict[str, object]) -> tuple[object, ...]:
    return (row["kodaira"], row["cp"], row["reduction"])


def s0(row: dict[str, object]) -> object:
    return sp.log(int(row["prime"]))


def s1(row: dict[str, object]) -> tuple[object, ...]:
    return (row["prime"], row["kodaira"])


def s2(row: dict[str, object]) -> tuple[object, ...]:
    return (row["prime"], row["kodaira"], row["cp"])


def collision_count(signature) -> int:
    groups: dict[object, set[tuple[object, ...]]] = {}
    for row in LOCAL_ROWS:
        groups.setdefault(signature(row), set()).add(target_signature(row))
    return sum(1 for targets in groups.values() if len(targets) > 1)


def g0(curve: dict[str, object]) -> tuple[int, ...]:
    return tuple(curve["bad_primes"])


def g1(curve: dict[str, object]) -> tuple[sp.Expr, ...]:
    return tuple(sp.log(p) for p in curve["bad_primes"])


def audit_local_insufficiency() -> int:
    checks = 0
    assert collision_count(s0) > 0
    checks += 1
    assert collision_count(s1) > 0
    checks += 1
    assert collision_count(s2) > 0
    checks += 1
    return checks


def audit_global_insufficiency() -> int:
    checks = 0
    left, right = GLOBAL_CURVES
    assert g0(left) == g0(right)
    checks += 1
    assert left["local_signature_p2"] != right["local_signature_p2"]
    checks += 1
    assert g1(left) == g1(right)
    checks += 1
    assert left["local_signature_p2"] != right["local_signature_p2"]
    checks += 1
    return checks


def audit_unified_gate() -> int:
    checks = 0
    assert all(collision_count(sig) > 0 for sig in (s0, s1, s2))
    checks += 1
    left, right = GLOBAL_CURVES
    assert g0(left) == g0(right) and g1(left) == g1(right)
    checks += 1
    assert left["local_signature_p2"] != right["local_signature_p2"]
    checks += 1
    return checks


def main() -> None:
    local_checks = audit_local_insufficiency()
    global_checks = audit_global_insufficiency()
    unified_checks = audit_unified_gate()

    print("All current finite source insufficiency gate checks passed.")
    print(f"  local insufficiency checks: {local_checks}")
    print(f"  global insufficiency checks: {global_checks}")
    print(f"  unified gate checks: {unified_checks}")


if __name__ == "__main__":
    main()
