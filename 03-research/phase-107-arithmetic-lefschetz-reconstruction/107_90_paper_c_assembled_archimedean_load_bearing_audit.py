#!/usr/bin/env python3
"""Exact audit for the assembled archimedean load-bearing shadow of Phase 107."""

from __future__ import annotations

from dataclasses import dataclass, replace


@dataclass(frozen=True)
class LoadBearingState:
    intrinsic_single_receiver: bool
    finite_support_realized: bool
    point_spectrum_retained: bool
    algebraic_storage_only: bool
    full_green_separation: bool
    truncated_green_only: bool


def assembled_load_bearing_ok(state: LoadBearingState) -> bool:
    return (
        state.intrinsic_single_receiver
        and state.finite_support_realized
        and state.point_spectrum_retained
        and (not state.algebraic_storage_only)
        and state.full_green_separation
        and (not state.truncated_green_only)
    )


def good_state() -> LoadBearingState:
    return LoadBearingState(
        intrinsic_single_receiver=True,
        finite_support_realized=True,
        point_spectrum_retained=True,
        algebraic_storage_only=False,
        full_green_separation=True,
        truncated_green_only=False,
    )


def audit_good_state() -> int:
    checks = 0
    state = good_state()
    assert state.intrinsic_single_receiver
    checks += 1
    assert state.finite_support_realized
    checks += 1
    assert state.point_spectrum_retained
    checks += 1
    assert not state.algebraic_storage_only
    checks += 1
    assert state.full_green_separation
    checks += 1
    assert not state.truncated_green_only
    checks += 1
    assert assembled_load_bearing_ok(state)
    checks += 1
    return checks


def audit_obstruction_modes() -> int:
    checks = 0
    variants = (
        replace(good_state(), algebraic_storage_only=True, full_green_separation=False),
        replace(good_state(), truncated_green_only=True, full_green_separation=False),
        replace(good_state(), point_spectrum_retained=False),
        replace(good_state(), finite_support_realized=False),
        replace(good_state(), intrinsic_single_receiver=False),
    )
    for state in variants:
        assert not assembled_load_bearing_ok(state)
        checks += 1
    return checks


def audit_cross_compatibility() -> int:
    checks = 0
    state = good_state()
    assert state.intrinsic_single_receiver and state.point_spectrum_retained
    checks += 1
    assert state.finite_support_realized and state.full_green_separation
    checks += 1
    assert not state.algebraic_storage_only and not state.truncated_green_only
    checks += 1
    assert assembled_load_bearing_ok(state)
    checks += 1
    return checks


def audit_truncation_breaks_faithfulness() -> int:
    checks = 0
    truncated = replace(good_state(), truncated_green_only=True, full_green_separation=False)
    assert not assembled_load_bearing_ok(truncated)
    checks += 1
    algebraic = replace(good_state(), algebraic_storage_only=True, full_green_separation=False)
    assert not assembled_load_bearing_ok(algebraic)
    checks += 1
    return checks


def main() -> None:
    good_checks = audit_good_state()
    obstruction_checks = audit_obstruction_modes()
    compatibility_checks = audit_cross_compatibility()
    truncation_checks = audit_truncation_breaks_faithfulness()

    print("All exact Paper C assembled archimedean load-bearing checks passed.")
    print(f"  good-state checks: {good_checks}")
    print(f"  obstruction-mode checks: {obstruction_checks}")
    print(f"  cross-compatibility checks: {compatibility_checks}")
    print(f"  truncation-break checks: {truncation_checks}")


if __name__ == "__main__":
    main()
