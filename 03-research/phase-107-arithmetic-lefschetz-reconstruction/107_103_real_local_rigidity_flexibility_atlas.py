#!/usr/bin/env python3
"""Exact atlas of rigid and flexible real local sectors."""

from __future__ import annotations

from math import gcd


def multiplicative_cp(n: int, reduction: str) -> int:
    if reduction == "split multiplicative":
        return n
    if reduction == "nonsplit multiplicative":
        return gcd(2, n)
    raise ValueError(f"Unsupported multiplicative reduction: {reduction}")


def additive_iv_cp(action: str) -> int:
    if action == "trivial":
        return 3
    if action == "3-cycle":
        return 1
    raise ValueError(f"Unsupported IV action: {action}")


def additive_iii_cp() -> int:
    return 2


MULTIPLICATIVE_ROWS = (
    {"label": "14.a1", "prime": 2, "n": 9, "reduction": "nonsplit multiplicative", "cp": 1},
    {"label": "14.a1", "prime": 7, "n": 2, "reduction": "split multiplicative", "cp": 2},
    {"label": "14.a5", "prime": 2, "n": 2, "reduction": "nonsplit multiplicative", "cp": 2},
    {"label": "489762.dv3", "prime": 2, "n": 2, "reduction": "split multiplicative", "cp": 2},
)

IV_ROWS = (
    {"label": "20.a1", "prime": 2, "action": "3-cycle", "cp": 1},
    {"label": "36.a4", "prime": 2, "action": "trivial", "cp": 3},
)

III_ROWS = (
    {"label": "36.a4", "prime": 3, "cp": 2},
    {"label": "4225.m2", "prime": 5, "cp": 2},
)


def audit_i9_cp_flexibility() -> int:
    checks = 0
    assert multiplicative_cp(9, "split multiplicative") == 9
    checks += 1
    assert multiplicative_cp(9, "nonsplit multiplicative") == 1
    checks += 1
    assert multiplicative_cp(9, "split multiplicative") != multiplicative_cp(9, "nonsplit multiplicative")
    checks += 1
    row = MULTIPLICATIVE_ROWS[0]
    assert row["cp"] == multiplicative_cp(row["n"], row["reduction"])
    checks += 1
    return checks


def audit_i2_cp_rigidity_but_label_flexibility() -> int:
    checks = 0
    split_cp = multiplicative_cp(2, "split multiplicative")
    nonsplit_cp = multiplicative_cp(2, "nonsplit multiplicative")
    assert split_cp == nonsplit_cp == 2
    checks += 1
    split_rows = [r for r in MULTIPLICATIVE_ROWS if r["n"] == 2 and r["reduction"] == "split multiplicative"]
    nonsplit_rows = [r for r in MULTIPLICATIVE_ROWS if r["n"] == 2 and r["reduction"] == "nonsplit multiplicative"]
    assert split_rows and nonsplit_rows
    checks += 1
    assert all(r["cp"] == 2 for r in split_rows + nonsplit_rows)
    checks += 1
    assert {r["reduction"] for r in split_rows + nonsplit_rows} == {
        "split multiplicative",
        "nonsplit multiplicative",
    }
    checks += 1
    return checks


def audit_iv_cp_flexibility() -> int:
    checks = 0
    assert additive_iv_cp("trivial") == 3
    checks += 1
    assert additive_iv_cp("3-cycle") == 1
    checks += 1
    assert additive_iv_cp("trivial") != additive_iv_cp("3-cycle")
    checks += 1
    for row in IV_ROWS:
        assert row["cp"] == additive_iv_cp(row["action"])
        checks += 1
    return checks


def audit_iii_rigidity() -> int:
    checks = 0
    assert additive_iii_cp() == 2
    checks += 1
    for row in III_ROWS:
        assert row["cp"] == 2
        checks += 1
    return checks


def audit_sector_classification() -> int:
    checks = 0
    # I9: flexible already at the cp level.
    assert multiplicative_cp(9, "split multiplicative") != multiplicative_cp(9, "nonsplit multiplicative")
    checks += 1
    # I2: rigid at cp, flexible at finer local label level.
    assert multiplicative_cp(2, "split multiplicative") == multiplicative_cp(2, "nonsplit multiplicative")
    checks += 1
    # IV: flexible at cp.
    assert additive_iv_cp("trivial") != additive_iv_cp("3-cycle")
    checks += 1
    # III: rigid at cp.
    assert additive_iii_cp() == 2
    checks += 1
    return checks


def main() -> None:
    i9_checks = audit_i9_cp_flexibility()
    i2_checks = audit_i2_cp_rigidity_but_label_flexibility()
    iv_checks = audit_iv_cp_flexibility()
    iii_checks = audit_iii_rigidity()
    atlas_checks = audit_sector_classification()

    print("All real local rigidity/flexibility atlas checks passed.")
    print(f"  I9 cp-flexibility checks: {i9_checks}")
    print(f"  I2 mixed-rigidity checks: {i2_checks}")
    print(f"  IV cp-flexibility checks: {iv_checks}")
    print(f"  III rigidity checks: {iii_checks}")
    print(f"  atlas-classification checks: {atlas_checks}")


if __name__ == "__main__":
    main()
