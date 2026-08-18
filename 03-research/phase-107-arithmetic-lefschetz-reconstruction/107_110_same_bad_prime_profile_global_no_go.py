#!/usr/bin/env python3
"""Exact global no-go for coarse bad-prime support profiles."""

from __future__ import annotations


CURVES = (
    {
        "label": "14.a1",
        "conductor": 14,
        "bad_primes": (2, 7),
        "p2_signature": ("I9", 1, "nonsplit multiplicative"),
    },
    {
        "label": "14.a5",
        "conductor": 14,
        "bad_primes": (2, 7),
        "p2_signature": ("I2", 2, "nonsplit multiplicative"),
    },
)


def bad_prime_profile(curve: dict[str, object]) -> tuple[int, ...]:
    return tuple(curve["bad_primes"])


def audit_same_global_profile() -> int:
    checks = 0
    left, right = CURVES
    assert left["conductor"] == right["conductor"] == 14
    checks += 1
    assert bad_prime_profile(left) == bad_prime_profile(right) == (2, 7)
    checks += 1
    return checks


def audit_local_target_difference() -> int:
    checks = 0
    left, right = CURVES
    assert left["p2_signature"] != right["p2_signature"]
    checks += 1
    return checks


def audit_no_go() -> int:
    checks = 0
    left, right = CURVES
    assert bad_prime_profile(left) == bad_prime_profile(right)
    checks += 1
    assert left["p2_signature"] != right["p2_signature"]
    checks += 1
    return checks


def main() -> None:
    profile_checks = audit_same_global_profile()
    local_checks = audit_local_target_difference()
    nogo_checks = audit_no_go()

    print("All same bad-prime profile global no-go checks passed.")
    print(f"  same-profile checks: {profile_checks}")
    print(f"  local-difference checks: {local_checks}")
    print(f"  no-go checks: {nogo_checks}")


if __name__ == "__main__":
    main()
