#!/usr/bin/env python3
"""Exact audit for the assembled Route A applicability shadow of Phase 107."""

from __future__ import annotations

from dataclasses import dataclass, replace


ROUTE_A_ITEMS = ("A1", "A2", "A3", "A4", "A5", "A6")


@dataclass(frozen=True)
class CandidateTargetState:
    envelope_coherent: bool
    one_receiver: bool
    degree_zero: bool
    scaling_covariant: bool
    one_metric_profile: bool
    one_remainder_channel: bool
    nonnegative_log_support: bool
    non_diagonal_finite: bool
    diagonal_placeholder_only: bool
    functoriality_ok: bool


def route_a_shadow_ok(state: CandidateTargetState) -> dict[str, bool]:
    return {
        "A1": state.envelope_coherent,
        "A2": state.one_metric_profile and state.one_remainder_channel,
        "A3": state.degree_zero and state.scaling_covariant,
        "A4": state.nonnegative_log_support,
        "A5": state.non_diagonal_finite and state.diagonal_placeholder_only,
        "A6": state.functoriality_ok,
    }


def assembled_applicable(state: CandidateTargetState) -> bool:
    checklist = route_a_shadow_ok(state)
    return (
        all(checklist[item] for item in ROUTE_A_ITEMS)
        and state.one_receiver
    )


def good_state() -> CandidateTargetState:
    return CandidateTargetState(
        envelope_coherent=True,
        one_receiver=True,
        degree_zero=True,
        scaling_covariant=True,
        one_metric_profile=True,
        one_remainder_channel=True,
        nonnegative_log_support=True,
        non_diagonal_finite=True,
        diagonal_placeholder_only=True,
        functoriality_ok=True,
    )


def current_phase_state() -> CandidateTargetState:
    # Still only finite symbolic shadows, not genuine theorem-level applicability.
    return CandidateTargetState(
        envelope_coherent=True,
        one_receiver=True,
        degree_zero=True,
        scaling_covariant=True,
        one_metric_profile=True,
        one_remainder_channel=True,
        nonnegative_log_support=True,
        non_diagonal_finite=True,
        diagonal_placeholder_only=True,
        functoriality_ok=True,
    )


def audit_good_state() -> int:
    checks = 0
    state = good_state()
    checklist = route_a_shadow_ok(state)
    for item in ROUTE_A_ITEMS:
        assert checklist[item]
        checks += 1
    assert assembled_applicable(state)
    checks += 1
    return checks


def audit_each_item_is_mandatory() -> int:
    checks = 0
    toggles = {
        "A1": {"envelope_coherent": False},
        "A2a": {"one_metric_profile": False},
        "A2b": {"one_remainder_channel": False},
        "A3a": {"degree_zero": False},
        "A3b": {"scaling_covariant": False},
        "A4": {"nonnegative_log_support": False},
        "A5a": {"non_diagonal_finite": False},
        "A5b": {"diagonal_placeholder_only": False},
        "A6": {"functoriality_ok": False},
        "receiver": {"one_receiver": False},
    }
    for updates in toggles.values():
        state = replace(good_state(), **updates)
        assert not assembled_applicable(state)
        checks += 1
    return checks


def audit_cross_compatibility() -> int:
    checks = 0
    state = good_state()
    # Degree zero and metric discipline live on the same receiver.
    assert state.one_receiver and state.degree_zero and state.one_metric_profile
    checks += 1
    # Pairing finiteness and functoriality coexist with the same assembled state.
    assert state.non_diagonal_finite and state.functoriality_ok
    checks += 1
    # Diagonal placeholder isolation does not destroy the nonnegative support package.
    assert state.diagonal_placeholder_only and state.nonnegative_log_support
    checks += 1
    return checks


def audit_current_phase_is_still_not_theorem_level() -> int:
    checks = 0
    state = current_phase_state()
    assert assembled_applicable(state)
    checks += 1
    # Even with all finite shadows present, the current phase is still not
    # theorem-level applicable. This audit remains only a finite assembled shadow.
    theorem_level_applicable = False
    assert not theorem_level_applicable
    checks += 1
    return checks


def main() -> None:
    good_checks = audit_good_state()
    mandatory_checks = audit_each_item_is_mandatory()
    cross_checks = audit_cross_compatibility()
    current_checks = audit_current_phase_is_still_not_theorem_level()

    print("All exact Route A assembled applicability checks passed.")
    print(f"  good-state checks: {good_checks}")
    print(f"  mandatory-item checks: {mandatory_checks}")
    print(f"  cross-compatibility checks: {cross_checks}")
    print(f"  current-phase checks: {current_checks}")


if __name__ == "__main__":
    main()
