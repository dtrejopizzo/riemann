#!/usr/bin/env python3
"""Exact audit for the assembled Hodge pre-applicability shadow of Phase 107."""

from __future__ import annotations

from dataclasses import dataclass, replace


@dataclass(frozen=True)
class HodgeState:
    route_a_selected: bool
    route_b_selected: bool
    route_a_finite_assembled: bool
    route_a_theorem_level: bool
    route_b_theorem_level: bool
    published_hodge_theorem_available: bool


def genuinely_applicable(state: HodgeState) -> bool:
    route_a_ok = (
        state.route_a_selected
        and (not state.route_b_selected)
        and state.route_a_theorem_level
        and state.published_hodge_theorem_available
    )
    route_b_ok = (
        state.route_b_selected
        and (not state.route_a_selected)
        and state.route_b_theorem_level
    )
    return route_a_ok or route_b_ok


def preapplicable_current_state(state: HodgeState) -> bool:
    return (
        state.route_a_selected
        and (not state.route_b_selected)
        and state.route_a_finite_assembled
        and (not state.route_a_theorem_level)
        and (not genuinely_applicable(state))
    )


def good_state() -> HodgeState:
    return HodgeState(
        route_a_selected=True,
        route_b_selected=False,
        route_a_finite_assembled=True,
        route_a_theorem_level=False,
        route_b_theorem_level=False,
        published_hodge_theorem_available=True,
    )


def audit_good_state() -> int:
    checks = 0
    state = good_state()
    assert state.route_a_selected and not state.route_b_selected
    checks += 1
    assert state.route_a_finite_assembled
    checks += 1
    assert not state.route_a_theorem_level
    checks += 1
    assert not state.route_b_theorem_level
    checks += 1
    assert not genuinely_applicable(state)
    checks += 1
    assert preapplicable_current_state(state)
    checks += 1
    return checks


def audit_hybrid_or_fake_promotions_fail() -> int:
    checks = 0
    variants = (
        replace(good_state(), route_b_selected=True),
        replace(good_state(), route_a_selected=False, route_b_selected=True, route_b_theorem_level=False),
        replace(good_state(), route_a_theorem_level=True, route_b_selected=True),
        replace(good_state(), route_a_finite_assembled=False),
        replace(good_state(), route_a_theorem_level=True, published_hodge_theorem_available=False),
    )
    for state in variants:
        assert not preapplicable_current_state(state)
        checks += 1
    return checks


def audit_true_applicability_requires_theorem_level() -> int:
    checks = 0
    route_a_true = replace(good_state(), route_a_theorem_level=True)
    assert genuinely_applicable(route_a_true)
    checks += 1
    assert not preapplicable_current_state(route_a_true)
    checks += 1

    route_b_true = HodgeState(
        route_a_selected=False,
        route_b_selected=True,
        route_a_finite_assembled=False,
        route_a_theorem_level=False,
        route_b_theorem_level=True,
        published_hodge_theorem_available=False,
    )
    assert genuinely_applicable(route_b_true)
    checks += 1
    return checks


def audit_cross_compatibility() -> int:
    checks = 0
    state = good_state()
    assert state.route_a_selected and state.route_a_finite_assembled
    checks += 1
    assert state.published_hodge_theorem_available and not state.route_a_theorem_level
    checks += 1
    assert not state.route_b_selected and not state.route_b_theorem_level
    checks += 1
    assert preapplicable_current_state(state)
    checks += 1
    return checks


def main() -> None:
    good_checks = audit_good_state()
    hybrid_checks = audit_hybrid_or_fake_promotions_fail()
    theorem_checks = audit_true_applicability_requires_theorem_level()
    compatibility_checks = audit_cross_compatibility()

    print("All exact Paper D assembled Hodge pre-applicability checks passed.")
    print(f"  good-state checks: {good_checks}")
    print(f"  hybrid-promotion checks: {hybrid_checks}")
    print(f"  theorem-level checks: {theorem_checks}")
    print(f"  cross-compatibility checks: {compatibility_checks}")


if __name__ == "__main__":
    main()
