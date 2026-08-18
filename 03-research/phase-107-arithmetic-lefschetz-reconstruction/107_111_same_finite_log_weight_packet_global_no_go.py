#!/usr/bin/env python3
"""Exact no-go for coarse global packets of finite log weights."""

from __future__ import annotations

import sympy as sp


CURVES = (
    {
        "label": "14.a1",
        "bad_primes": (2, 7),
        "p2_signature": ("I9", 1, "nonsplit multiplicative"),
    },
    {
        "label": "14.a5",
        "bad_primes": (2, 7),
        "p2_signature": ("I2", 2, "nonsplit multiplicative"),
    },
)


def log_weight_packet(curve: dict[str, object]) -> tuple[sp.Expr, ...]:
    return tuple(sp.log(p) for p in curve["bad_primes"])


def audit_same_log_weight_packet() -> int:
    checks = 0
    left, right = CURVES
    assert log_weight_packet(left) == log_weight_packet(right) == (sp.log(2), sp.log(7))
    checks += 1
    return checks


def audit_local_difference() -> int:
    checks = 0
    left, right = CURVES
    assert left["p2_signature"] != right["p2_signature"]
    checks += 1
    return checks


def audit_no_go() -> int:
    checks = 0
    left, right = CURVES
    assert log_weight_packet(left) == log_weight_packet(right)
    checks += 1
    assert left["p2_signature"] != right["p2_signature"]
    checks += 1
    return checks


def main() -> None:
    packet_checks = audit_same_log_weight_packet()
    local_checks = audit_local_difference()
    nogo_checks = audit_no_go()

    print("All same finite log-weight packet global no-go checks passed.")
    print(f"  same-packet checks: {packet_checks}")
    print(f"  local-difference checks: {local_checks}")
    print(f"  no-go checks: {nogo_checks}")


if __name__ == "__main__":
    main()
