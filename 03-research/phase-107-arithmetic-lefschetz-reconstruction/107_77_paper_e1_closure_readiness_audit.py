#!/usr/bin/env python3
"""Exact audit for the E1 closure-readiness shadow of 107_12/107_13."""

from __future__ import annotations

from dataclasses import dataclass


ROUTE_A_ITEMS = ("A1", "A2", "A3", "A4", "A5", "A6")
ROUTE_B_ITEMS = ("B1", "B2", "B3", "B4")
FAILURE_FLAGS = (
    "nonproper_cutoff_model",
    "nonintegrable_metric",
    "source_only_degree_zero",
    "continuous_completion",
    "no_theorem_available",
    "kernel_mismatch",
)


@dataclass(frozen=True)
class ClosureState:
    route_a: dict[str, bool]
    route_b: dict[str, bool]
    published_theorem: bool
    new_theorem: bool
    failure_flags: dict[str, bool]
    terminal_identity_exact: bool
    exact_kernel: bool


def route_a_applicable(state: ClosureState) -> bool:
    return (
        all(state.route_a[item] for item in ROUTE_A_ITEMS)
        and state.published_theorem
        and not state.new_theorem
        and not any(state.failure_flags.values())
    )


def route_b_applicable(state: ClosureState) -> bool:
    return (
        all(state.route_b[item] for item in ROUTE_B_ITEMS)
        and state.new_theorem
        and not state.published_theorem
        and not any(state.failure_flags.values())
    )


def applicability(state: ClosureState) -> bool:
    return route_a_applicable(state) or route_b_applicable(state)


def closure_ready(state: ClosureState) -> bool:
    return applicability(state) and state.terminal_identity_exact and state.exact_kernel


def good_route_a_state() -> ClosureState:
    return ClosureState(
        route_a={item: True for item in ROUTE_A_ITEMS},
        route_b={item: False for item in ROUTE_B_ITEMS},
        published_theorem=True,
        new_theorem=False,
        failure_flags={flag: False for flag in FAILURE_FLAGS},
        terminal_identity_exact=True,
        exact_kernel=True,
    )


def good_route_b_state() -> ClosureState:
    return ClosureState(
        route_a={item: False for item in ROUTE_A_ITEMS},
        route_b={item: True for item in ROUTE_B_ITEMS},
        published_theorem=False,
        new_theorem=True,
        failure_flags={flag: False for flag in FAILURE_FLAGS},
        terminal_identity_exact=True,
        exact_kernel=True,
    )


def audit_good_closure_states() -> int:
    checks = 0
    for state in (good_route_a_state(), good_route_b_state()):
        assert applicability(state)
        checks += 1
        assert closure_ready(state)
        checks += 1
    return checks


def audit_missing_applicability_blocks_closure() -> int:
    checks = 0
    for missing in ROUTE_A_ITEMS:
        state = ClosureState(
            route_a={item: item != missing for item in ROUTE_A_ITEMS},
            route_b={item: False for item in ROUTE_B_ITEMS},
            published_theorem=True,
            new_theorem=False,
            failure_flags={flag: False for flag in FAILURE_FLAGS},
            terminal_identity_exact=True,
            exact_kernel=True,
        )
        assert not closure_ready(state)
        checks += 1
    for missing in ROUTE_B_ITEMS:
        state = ClosureState(
            route_a={item: False for item in ROUTE_A_ITEMS},
            route_b={item: item != missing for item in ROUTE_B_ITEMS},
            published_theorem=False,
            new_theorem=True,
            failure_flags={flag: False for flag in FAILURE_FLAGS},
            terminal_identity_exact=True,
            exact_kernel=True,
        )
        assert not closure_ready(state)
        checks += 1
    return checks


def audit_terminal_identity_and_kernel_are_mandatory() -> int:
    checks = 0
    base = good_route_a_state()
    variants = (
        ClosureState(**{**base.__dict__, "terminal_identity_exact": False}),
        ClosureState(**{**base.__dict__, "exact_kernel": False}),
        ClosureState(
            **{
                **base.__dict__,
                "terminal_identity_exact": False,
                "exact_kernel": False,
            }
        ),
    )
    for state in variants:
        assert applicability(state)
        checks += 1
        assert not closure_ready(state)
        checks += 1
    return checks


def audit_failure_flags_block_closure() -> int:
    checks = 0
    for flag in FAILURE_FLAGS:
        failure_flags = {name: False for name in FAILURE_FLAGS}
        failure_flags[flag] = True
        state = ClosureState(
            route_a={item: True for item in ROUTE_A_ITEMS},
            route_b={item: False for item in ROUTE_B_ITEMS},
            published_theorem=True,
            new_theorem=False,
            failure_flags=failure_flags,
            terminal_identity_exact=True,
            exact_kernel=True,
        )
        assert not applicability(state)
        checks += 1
        assert not closure_ready(state)
        checks += 1
    return checks


def audit_hybrid_and_weakened_states_fail() -> int:
    checks = 0
    cases = [
        ClosureState(
            route_a={item: True for item in ROUTE_A_ITEMS},
            route_b={item: True for item in ROUTE_B_ITEMS},
            published_theorem=True,
            new_theorem=True,
            failure_flags={flag: False for flag in FAILURE_FLAGS},
            terminal_identity_exact=True,
            exact_kernel=True,
        ),
        ClosureState(
            route_a={item: True for item in ROUTE_A_ITEMS},
            route_b={item: False for item in ROUTE_B_ITEMS},
            published_theorem=True,
            new_theorem=False,
            failure_flags={flag: False for flag in FAILURE_FLAGS},
            terminal_identity_exact=False,
            exact_kernel=True,
        ),
        ClosureState(
            route_a={item: True for item in ROUTE_A_ITEMS},
            route_b={item: False for item in ROUTE_B_ITEMS},
            published_theorem=True,
            new_theorem=False,
            failure_flags={flag: False for flag in FAILURE_FLAGS},
            terminal_identity_exact=True,
            exact_kernel=False,
        ),
    ]
    for state in cases:
        assert not closure_ready(state)
        checks += 1
    return checks


def audit_current_phase_not_ready() -> int:
    checks = 0
    current = ClosureState(
        route_a={item: False for item in ROUTE_A_ITEMS},
        route_b={item: False for item in ROUTE_B_ITEMS},
        published_theorem=True,
        new_theorem=False,
        failure_flags={
            "nonproper_cutoff_model": False,
            "nonintegrable_metric": False,
            "source_only_degree_zero": True,
            "continuous_completion": False,
            "no_theorem_available": False,
            "kernel_mismatch": True,
        },
        terminal_identity_exact=False,
        exact_kernel=False,
    )
    assert not applicability(current)
    checks += 1
    assert not closure_ready(current)
    checks += 1
    return checks


def main() -> None:
    good_checks = audit_good_closure_states()
    missing_checks = audit_missing_applicability_blocks_closure()
    identity_kernel_checks = audit_terminal_identity_and_kernel_are_mandatory()
    failure_checks = audit_failure_flags_block_closure()
    hybrid_checks = audit_hybrid_and_weakened_states_fail()
    current_checks = audit_current_phase_not_ready()

    print("All exact Paper E1 closure-readiness checks passed.")
    print(f"  good-closure checks: {good_checks}")
    print(f"  missing-applicability checks: {missing_checks}")
    print(f"  terminal-identity/kernel checks: {identity_kernel_checks}")
    print(f"  hard-failure checks: {failure_checks}")
    print(f"  hybrid-or-weakened checks: {hybrid_checks}")
    print(f"  current-phase checks: {current_checks}")


if __name__ == "__main__":
    main()
