#!/usr/bin/env python3
"""Exact finite audit for the route-exclusivity shadow behind F9."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


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
class RouteState:
    route_a: dict[str, bool]
    route_b: dict[str, bool]
    published_theorem: bool
    new_theorem: bool
    failure_flags: dict[str, bool]


def route_a_applicable(state: RouteState) -> bool:
    return (
        all(state.route_a[item] for item in ROUTE_A_ITEMS)
        and state.published_theorem
        and not state.new_theorem
        and not any(state.failure_flags.values())
    )


def route_b_applicable(state: RouteState) -> bool:
    return (
        all(state.route_b[item] for item in ROUTE_B_ITEMS)
        and state.new_theorem
        and not state.published_theorem
        and not any(state.failure_flags.values())
    )


def applicability(state: RouteState) -> bool:
    return route_a_applicable(state) or route_b_applicable(state)


def audit_route_exclusivity() -> int:
    checks = 0
    good_a = RouteState(
        route_a={item: True for item in ROUTE_A_ITEMS},
        route_b={item: False for item in ROUTE_B_ITEMS},
        published_theorem=True,
        new_theorem=False,
        failure_flags={flag: False for flag in FAILURE_FLAGS},
    )
    assert route_a_applicable(good_a)
    assert applicability(good_a)
    checks += 2

    good_b = RouteState(
        route_a={item: False for item in ROUTE_A_ITEMS},
        route_b={item: True for item in ROUTE_B_ITEMS},
        published_theorem=False,
        new_theorem=True,
        failure_flags={flag: False for flag in FAILURE_FLAGS},
    )
    assert route_b_applicable(good_b)
    assert applicability(good_b)
    checks += 2

    hybrid = RouteState(
        route_a={item: True for item in ROUTE_A_ITEMS},
        route_b={item: True for item in ROUTE_B_ITEMS},
        published_theorem=True,
        new_theorem=True,
        failure_flags={flag: False for flag in FAILURE_FLAGS},
    )
    assert not applicability(hybrid)
    checks += 1
    return checks


def audit_incomplete_routes_fail() -> int:
    checks = 0
    for missing_a in ROUTE_A_ITEMS:
        state = RouteState(
            route_a={item: item != missing_a for item in ROUTE_A_ITEMS},
            route_b={item: False for item in ROUTE_B_ITEMS},
            published_theorem=True,
            new_theorem=False,
            failure_flags={flag: False for flag in FAILURE_FLAGS},
        )
        assert not applicability(state)
        checks += 1

    for missing_b in ROUTE_B_ITEMS:
        state = RouteState(
            route_a={item: False for item in ROUTE_A_ITEMS},
            route_b={item: item != missing_b for item in ROUTE_B_ITEMS},
            published_theorem=False,
            new_theorem=True,
            failure_flags={flag: False for flag in FAILURE_FLAGS},
        )
        assert not applicability(state)
        checks += 1
    return checks


def audit_failure_flags_are_hard_failures() -> int:
    checks = 0
    for flag in FAILURE_FLAGS:
        failure_flags = {name: False for name in FAILURE_FLAGS}
        failure_flags[flag] = True
        state = RouteState(
            route_a={item: True for item in ROUTE_A_ITEMS},
            route_b={item: False for item in ROUTE_B_ITEMS},
            published_theorem=True,
            new_theorem=False,
            failure_flags=failure_flags,
        )
        assert not applicability(state)
        checks += 1
    return checks


def audit_hybrid_analogy_failures() -> int:
    checks = 0
    cases = [
        RouteState(
            route_a={item: True for item in ROUTE_A_ITEMS},
            route_b={item: False for item in ROUTE_B_ITEMS},
            published_theorem=False,
            new_theorem=False,
            failure_flags={flag: False for flag in FAILURE_FLAGS},
        ),
        RouteState(
            route_a={item: False for item in ROUTE_A_ITEMS},
            route_b={item: True for item in ROUTE_B_ITEMS},
            published_theorem=False,
            new_theorem=False,
            failure_flags={flag: False for flag in FAILURE_FLAGS},
        ),
        RouteState(
            route_a={item: True for item in ROUTE_A_ITEMS},
            route_b={item: False for item in ROUTE_B_ITEMS},
            published_theorem=False,
            new_theorem=True,
            failure_flags={flag: False for flag in FAILURE_FLAGS},
        ),
        RouteState(
            route_a={item: False for item in ROUTE_A_ITEMS},
            route_b={item: True for item in ROUTE_B_ITEMS},
            published_theorem=True,
            new_theorem=False,
            failure_flags={flag: False for flag in FAILURE_FLAGS},
        ),
    ]
    for state in cases:
        assert not applicability(state)
        checks += 1
    return checks


def audit_current_phase_state() -> int:
    checks = 0
    current = RouteState(
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
    )
    assert not applicability(current)
    checks += 1
    return checks


def main() -> None:
    exclusivity_checks = audit_route_exclusivity()
    incomplete_checks = audit_incomplete_routes_fail()
    failure_checks = audit_failure_flags_are_hard_failures()
    hybrid_checks = audit_hybrid_analogy_failures()
    current_checks = audit_current_phase_state()

    print("All exact Hodge-route exclusivity checks passed.")
    print(f"  exclusivity checks: {exclusivity_checks}")
    print(f"  incomplete-route checks: {incomplete_checks}")
    print(f"  hard-failure checks: {failure_checks}")
    print(f"  hybrid-analogy checks: {hybrid_checks}")
    print(f"  current-phase checks: {current_checks}")


if __name__ == "__main__":
    main()
