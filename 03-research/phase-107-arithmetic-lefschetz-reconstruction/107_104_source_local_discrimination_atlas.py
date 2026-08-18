#!/usr/bin/env python3
"""Exact source-side discrimination atlas for pinned real local states."""

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


def source_signature(prime: int) -> sp.Expr:
    return sp.log(prime)


def target_signature(row: dict[str, object]) -> tuple[object, ...]:
    return (row["kodaira"], row["cp"], row["reduction"])


def audit_fixed_prime_collapse() -> int:
    checks = 0
    p2_rows = [row for row in ROWS if row["prime"] == 2]
    assert len(p2_rows) == 5
    checks += 1
    source_classes = {source_signature(row["prime"]) for row in p2_rows}
    assert source_classes == {sp.log(2)}
    checks += 1
    target_classes = {target_signature(row) for row in p2_rows}
    assert len(target_classes) == 5
    checks += 1
    return checks


def audit_prime_separation_is_coarse() -> int:
    checks = 0
    source_classes = {source_signature(row["prime"]) for row in ROWS}
    assert source_classes == {sp.log(2), sp.log(3), sp.log(5)}
    checks += 1
    target_classes = {target_signature(row) for row in ROWS}
    assert len(target_classes) == 6
    checks += 1
    assert len(source_classes) < len(target_classes)
    checks += 1
    return checks


def audit_explicit_p2_non_discrimination() -> int:
    checks = 0
    labels = {(row["label"], row["kodaira"], row["cp"], row["reduction"]) for row in ROWS if row["prime"] == 2}
    assert len(labels) == 5
    checks += 1
    assert all(source_signature(2) == sp.log(2) for _ in labels)
    checks += 1
    return checks


def audit_source_changes_only_with_prime() -> int:
    checks = 0
    by_prime = {}
    for row in ROWS:
        by_prime.setdefault(row["prime"], set()).add(source_signature(row["prime"]))
    for prime, classes in by_prime.items():
        assert classes == {sp.log(prime)}
        checks += 1
    return checks


def main() -> None:
    collapse_checks = audit_fixed_prime_collapse()
    coarse_checks = audit_prime_separation_is_coarse()
    p2_checks = audit_explicit_p2_non_discrimination()
    prime_checks = audit_source_changes_only_with_prime()

    print("All source local discrimination atlas checks passed.")
    print(f"  fixed-prime collapse checks: {collapse_checks}")
    print(f"  coarse prime-separation checks: {coarse_checks}")
    print(f"  explicit p=2 nondiscrimination checks: {p2_checks}")
    print(f"  source-by-prime checks: {prime_checks}")


if __name__ == "__main__":
    main()
