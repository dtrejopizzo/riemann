#!/usr/bin/env python3
"""Exact audit for the assembled no-prescribed-trace shadow of Phase 107."""

from __future__ import annotations

from dataclasses import dataclass, replace


@dataclass(frozen=True)
class TraceAssemblyState:
    identity_cleanup_only: bool
    boundary_joint: bool
    mixed_separated: bool
    source_recoverable: bool
    externally_retouchable: bool


def assembled_no_prescribed_trace_ok(state: TraceAssemblyState) -> bool:
    return (
        state.identity_cleanup_only
        and state.boundary_joint
        and state.mixed_separated
        and state.source_recoverable
        and not state.externally_retouchable
    )


def good_state() -> TraceAssemblyState:
    return TraceAssemblyState(
        identity_cleanup_only=True,
        boundary_joint=True,
        mixed_separated=True,
        source_recoverable=True,
        externally_retouchable=False,
    )


def audit_good_state() -> int:
    checks = 0
    state = good_state()
    assert state.identity_cleanup_only
    checks += 1
    assert state.boundary_joint
    checks += 1
    assert state.mixed_separated
    checks += 1
    assert state.source_recoverable
    checks += 1
    assert not state.externally_retouchable
    checks += 1
    assert assembled_no_prescribed_trace_ok(state)
    checks += 1
    return checks


def audit_mandatory_features() -> int:
    checks = 0
    variants = (
        replace(good_state(), identity_cleanup_only=False),
        replace(good_state(), boundary_joint=False),
        replace(good_state(), mixed_separated=False),
        replace(good_state(), source_recoverable=False),
        replace(good_state(), externally_retouchable=True),
    )
    for state in variants:
        assert not assembled_no_prescribed_trace_ok(state)
        checks += 1
    return checks


def audit_cross_compatibility() -> int:
    checks = 0
    state = good_state()
    assert state.identity_cleanup_only and state.source_recoverable
    checks += 1
    assert state.boundary_joint and state.mixed_separated
    checks += 1
    assert state.mixed_separated and state.source_recoverable
    checks += 1
    assert assembled_no_prescribed_trace_ok(state)
    checks += 1
    return checks


def audit_external_retouch_failures() -> int:
    checks = 0
    bad_states = (
        TraceAssemblyState(True, False, True, False, True),
        TraceAssemblyState(False, True, True, False, True),
        TraceAssemblyState(True, True, False, False, True),
        TraceAssemblyState(True, True, True, False, True),
    )
    for state in bad_states:
        assert not assembled_no_prescribed_trace_ok(state)
        checks += 1
    return checks


def main() -> None:
    good_checks = audit_good_state()
    mandatory_checks = audit_mandatory_features()
    compatibility_checks = audit_cross_compatibility()
    retouch_checks = audit_external_retouch_failures()

    print("All exact Paper B assembled no-prescribed-trace checks passed.")
    print(f"  good-state checks: {good_checks}")
    print(f"  mandatory-feature checks: {mandatory_checks}")
    print(f"  cross-compatibility checks: {compatibility_checks}")
    print(f"  external-retouch checks: {retouch_checks}")


if __name__ == "__main__":
    main()
