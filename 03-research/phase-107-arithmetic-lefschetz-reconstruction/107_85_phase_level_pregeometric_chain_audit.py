#!/usr/bin/env python3
"""Exact audit for the phase-level pregeometric chain shadow of Phase 107."""

from __future__ import annotations

from dataclasses import dataclass, replace


@dataclass(frozen=True)
class PhaseChainState:
    candidate_target_assembled: bool
    route_a_assembled: bool
    terminal_identity_exact: bool
    exact_kernel: bool
    geometric_realization: bool


def closure_ready(state: PhaseChainState) -> bool:
    return (
        state.route_a_assembled
        and state.terminal_identity_exact
        and state.exact_kernel
    )


def pregeometric_chain_ok(state: PhaseChainState) -> bool:
    return (
        state.candidate_target_assembled
        and state.route_a_assembled
        and state.terminal_identity_exact
        and state.exact_kernel
        and closure_ready(state)
        and (not state.route_a_assembled or state.candidate_target_assembled)
    )


def good_state() -> PhaseChainState:
    return PhaseChainState(
        candidate_target_assembled=True,
        route_a_assembled=True,
        terminal_identity_exact=True,
        exact_kernel=True,
        geometric_realization=False,
    )


def audit_good_chain_state() -> int:
    checks = 0
    state = good_state()
    assert state.candidate_target_assembled
    checks += 1
    assert state.route_a_assembled
    checks += 1
    assert state.terminal_identity_exact
    checks += 1
    assert state.exact_kernel
    checks += 1
    assert closure_ready(state)
    checks += 1
    assert pregeometric_chain_ok(state)
    checks += 1
    return checks


def audit_mandatory_blocks() -> int:
    checks = 0
    variants = (
        replace(good_state(), candidate_target_assembled=False),
        replace(good_state(), route_a_assembled=False),
        replace(good_state(), terminal_identity_exact=False),
        replace(good_state(), exact_kernel=False),
    )
    for state in variants:
        assert not pregeometric_chain_ok(state)
        checks += 1
    return checks


def audit_chain_compatibility() -> int:
    checks = 0
    state = good_state()
    # Route A may not float free of the assembled target.
    assert state.route_a_assembled <= state.candidate_target_assembled
    checks += 1
    # Closure may not activate before the Route A and terminal layers coexist.
    assert closure_ready(state)
    assert state.route_a_assembled and state.terminal_identity_exact and state.exact_kernel
    checks += 2
    # The same state carries the target-side assembly and the E1 bridge data.
    assert state.candidate_target_assembled and closure_ready(state)
    checks += 1
    return checks


def audit_bypass_rejection() -> int:
    checks = 0
    variants = (
        PhaseChainState(False, True, True, True, False),
        PhaseChainState(False, True, False, True, False),
        PhaseChainState(True, False, True, True, False),
    )
    for state in variants:
        assert not pregeometric_chain_ok(state)
        checks += 1
    return checks


def audit_current_phase_still_not_geometric_completion() -> int:
    checks = 0
    state = good_state()
    assert pregeometric_chain_ok(state)
    checks += 1
    assert not state.geometric_realization
    checks += 1
    return checks


def main() -> None:
    good_checks = audit_good_chain_state()
    mandatory_checks = audit_mandatory_blocks()
    compatibility_checks = audit_chain_compatibility()
    bypass_checks = audit_bypass_rejection()
    current_checks = audit_current_phase_still_not_geometric_completion()

    print("All exact phase-level pregeometric chain checks passed.")
    print(f"  good-chain checks: {good_checks}")
    print(f"  mandatory-block checks: {mandatory_checks}")
    print(f"  chain-compatibility checks: {compatibility_checks}")
    print(f"  bypass-rejection checks: {bypass_checks}")
    print(f"  current-phase checks: {current_checks}")


if __name__ == "__main__":
    main()
