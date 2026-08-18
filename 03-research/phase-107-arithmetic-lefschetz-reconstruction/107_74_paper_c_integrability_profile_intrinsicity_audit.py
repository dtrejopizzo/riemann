#!/usr/bin/env python3
"""Exact audit for the finite integrability-profile shadow of 107_23."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


CHARTS = ("interior", "lower", "upper", "diagonal", "corner")
ROOTS = (0, 1, 2)
ORDER_PAIRS = ((3, 2), (4, 2), (5, 3), (6, 4))


@dataclass(frozen=True)
class GlobalProfile:
    boundary_v: int
    boundary_h: int
    diagonal: int
    remainder: tuple[int, int]
    extra_direction: int


@dataclass(frozen=True)
class LocalPresentation:
    chart: str
    root: int
    boundary_v: int
    boundary_h: int
    diagonal: int
    remainder: tuple[int, int]
    extra_direction: int


def canonical_profile(order_pair: tuple[int, int]) -> GlobalProfile:
    m, n = order_pair
    return GlobalProfile(
        boundary_v=1,
        boundary_h=1,
        diagonal=1,
        remainder=(m, n),
        extra_direction=0,
    )


def restrict_profile(profile: GlobalProfile, chart: str, root: int) -> LocalPresentation:
    if chart == "interior":
        return LocalPresentation(chart, root, 0, 0, 0, profile.remainder, 0)
    if chart == "lower":
        return LocalPresentation(chart, root, profile.boundary_v, 0, 0, profile.remainder, 0)
    if chart == "upper":
        return LocalPresentation(chart, root, 0, profile.boundary_h, 0, profile.remainder, 0)
    if chart == "diagonal":
        return LocalPresentation(chart, root, 0, 0, profile.diagonal, profile.remainder, 0)
    if chart == "corner":
        return LocalPresentation(
            chart,
            root,
            profile.boundary_v,
            profile.boundary_h,
            profile.diagonal,
            profile.remainder,
            0,
        )
    raise ValueError(chart)


def bad_extra_direction(order_pair: tuple[int, int], chart: str, root: int) -> LocalPresentation:
    presentation = restrict_profile(canonical_profile(order_pair), chart, root)
    return LocalPresentation(
        presentation.chart,
        presentation.root,
        presentation.boundary_v,
        presentation.boundary_h,
        presentation.diagonal,
        presentation.remainder,
        1,
    )


def local_key(presentation: LocalPresentation) -> tuple[int, int, int, tuple[int, int], int]:
    return (
        presentation.boundary_v,
        presentation.boundary_h,
        presentation.diagonal,
        presentation.remainder,
        presentation.extra_direction,
    )


def global_key(profile: GlobalProfile) -> tuple[int, int, int, tuple[int, int], int]:
    return (
        profile.boundary_v,
        profile.boundary_h,
        profile.diagonal,
        profile.remainder,
        profile.extra_direction,
    )


def audit_root_invariance() -> int:
    checks = 0
    for order_pair in ORDER_PAIRS:
        for chart in CHARTS:
            base = restrict_profile(canonical_profile(order_pair), chart, ROOTS[0])
            for root in ROOTS[1:]:
                other = restrict_profile(canonical_profile(order_pair), chart, root)
                assert local_key(base) == local_key(other)
                checks += 1
    return checks


def audit_chart_glue_to_intrinsic_profile() -> int:
    checks = 0
    for order_pair in ORDER_PAIRS:
        profile = canonical_profile(order_pair)
        for chart, root in product(CHARTS, ROOTS):
            presentation = restrict_profile(profile, chart, root)
            if chart == "corner":
                assert local_key(presentation)[:3] == global_key(profile)[:3]
            assert presentation.remainder == profile.remainder
            checks += 2
    return checks


def audit_corner_restrictions() -> int:
    checks = 0
    for order_pair in ORDER_PAIRS:
        profile = canonical_profile(order_pair)
        corner = restrict_profile(profile, "corner", ROOTS[0])
        lower = restrict_profile(profile, "lower", ROOTS[0])
        upper = restrict_profile(profile, "upper", ROOTS[0])
        diagonal = restrict_profile(profile, "diagonal", ROOTS[0])
        interior = restrict_profile(profile, "interior", ROOTS[0])

        assert (corner.boundary_v, 0, 0, corner.remainder, 0) == local_key(lower)
        assert (0, corner.boundary_h, 0, corner.remainder, 0) == local_key(upper)
        assert (0, 0, corner.diagonal, corner.remainder, 0) == local_key(diagonal)
        assert (0, 0, 0, corner.remainder, 0) == local_key(interior)
        checks += 4
    return checks


def audit_extra_direction_rejection() -> int:
    checks = 0
    for order_pair in ORDER_PAIRS:
        for chart, root in product(CHARTS, ROOTS):
            good = restrict_profile(canonical_profile(order_pair), chart, root)
            bad = bad_extra_direction(order_pair, chart, root)
            assert local_key(good) != local_key(bad)
            assert good.extra_direction == 0
            assert bad.extra_direction == 1
            checks += 3
    return checks


def main() -> None:
    root_checks = audit_root_invariance()
    glue_checks = audit_chart_glue_to_intrinsic_profile()
    restriction_checks = audit_corner_restrictions()
    extra_direction_checks = audit_extra_direction_rejection()

    print("All exact Paper C integrability-profile intrinsicity checks passed.")
    print(f"  root-invariance checks: {root_checks}")
    print(f"  chart-to-profile checks: {glue_checks}")
    print(f"  corner-restriction checks: {restriction_checks}")
    print(f"  extra-direction rejection checks: {extra_direction_checks}")


if __name__ == "__main__":
    main()
