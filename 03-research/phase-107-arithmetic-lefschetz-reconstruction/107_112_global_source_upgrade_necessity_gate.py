#!/usr/bin/env python3
"""Exact necessity gate for future finite global source upgrades."""

from __future__ import annotations

import sympy as sp


CURVES = (
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


def g0(curve: dict[str, object]) -> tuple[int, ...]:
    return tuple(curve["bad_primes"])


def g1(curve: dict[str, object]) -> tuple[sp.Expr, ...]:
    return tuple(sp.log(p) for p in curve["bad_primes"])


def audit_support_profile_failure() -> int:
    checks = 0
    left, right = CURVES
    assert g0(left) == g0(right) == (2, 7)
    checks += 1
    assert left["local_signature_p2"] != right["local_signature_p2"]
    checks += 1
    return checks


def audit_log_weight_packet_failure() -> int:
    checks = 0
    left, right = CURVES
    assert g1(left) == g1(right) == (sp.log(2), sp.log(7))
    checks += 1
    assert left["local_signature_p2"] != right["local_signature_p2"]
    checks += 1
    return checks


def audit_global_upgrade_necessity() -> int:
    checks = 0
    left, right = CURVES
    assert g0(left) == g0(right)
    checks += 1
    assert g1(left) == g1(right)
    checks += 1
    assert left["local_signature_p2"] != right["local_signature_p2"]
    checks += 1
    return checks


def main() -> None:
    support_checks = audit_support_profile_failure()
    packet_checks = audit_log_weight_packet_failure()
    gate_checks = audit_global_upgrade_necessity()

    print("All global source upgrade necessity gate checks passed.")
    print(f"  support-profile checks: {support_checks}")
    print(f"  log-weight-packet checks: {packet_checks}")
    print(f"  necessity-gate checks: {gate_checks}")


if __name__ == "__main__":
    main()
