#!/usr/bin/env python3
"""Exact audit for the assembled equality-case gate of Phase 107."""

from __future__ import annotations

from dataclasses import dataclass, replace


@dataclass(frozen=True)
class EqualityCaseState:
    radical_only_kernel: bool
    nonradical_survival: bool
    primitive_quotient_identity: bool
    exact_kernel_minimality: bool
    extra_kernel_present: bool


def equality_case_gate_ok(state: EqualityCaseState) -> bool:
    return (
        state.radical_only_kernel
        and state.nonradical_survival
        and state.primitive_quotient_identity
        and state.exact_kernel_minimality
        and not state.extra_kernel_present
    )


def good_state() -> EqualityCaseState:
    return EqualityCaseState(
        radical_only_kernel=True,
        nonradical_survival=True,
        primitive_quotient_identity=True,
        exact_kernel_minimality=True,
        extra_kernel_present=False,
    )


def audit_good_state() -> int:
    checks = 0
    state = good_state()
    assert state.radical_only_kernel
    checks += 1
    assert state.nonradical_survival
    checks += 1
    assert state.primitive_quotient_identity
    checks += 1
    assert state.exact_kernel_minimality
    checks += 1
    assert not state.extra_kernel_present
    checks += 1
    assert equality_case_gate_ok(state)
    checks += 1
    return checks


def audit_gate_failures() -> int:
    checks = 0
    variants = (
        replace(good_state(), radical_only_kernel=False),
        replace(good_state(), nonradical_survival=False),
        replace(good_state(), primitive_quotient_identity=False),
        replace(good_state(), exact_kernel_minimality=False),
        replace(good_state(), extra_kernel_present=True),
    )
    for state in variants:
        assert not equality_case_gate_ok(state)
        checks += 1
    return checks


def audit_extra_kernel_is_detected() -> int:
    checks = 0
    weakened = replace(good_state(), nonradical_survival=False, extra_kernel_present=True)
    assert not equality_case_gate_ok(weakened)
    checks += 1
    weakened = replace(good_state(), primitive_quotient_identity=True, extra_kernel_present=True)
    assert not equality_case_gate_ok(weakened)
    checks += 1
    return checks


def audit_cross_compatibility() -> int:
    checks = 0
    state = good_state()
    assert state.radical_only_kernel and state.exact_kernel_minimality
    checks += 1
    assert state.nonradical_survival and state.primitive_quotient_identity
    checks += 1
    assert equality_case_gate_ok(state)
    checks += 1
    return checks


def main() -> None:
    good_checks = audit_good_state()
    failure_checks = audit_gate_failures()
    extra_kernel_checks = audit_extra_kernel_is_detected()
    compatibility_checks = audit_cross_compatibility()

    print("All exact assembled equality-case gate checks passed.")
    print(f"  good-state checks: {good_checks}")
    print(f"  gate-failure checks: {failure_checks}")
    print(f"  extra-kernel checks: {extra_kernel_checks}")
    print(f"  cross-compatibility checks: {compatibility_checks}")


if __name__ == "__main__":
    main()
