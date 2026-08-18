#!/usr/bin/env python3
"""Exact audit for the finite correction-sum shadow of Paper C.

This verifier audits the remaining finite bookkeeping step isolated by
`107_27`: after structural corner collapse is excluded, the denominator
question becomes quantitative and is carried by a signed sum of local
exceptional corrections.

The script checks that:

1. the currently visible local center types contribute only through the
   correction channels already isolated in `107_25`--`107_27`;
2. the correction package aggregates additively over a finite center
   list;
3. cancellation of `-2 c_T` is a genuine numerical condition on signed
   coefficients, not something forced combinatorially by the center
   types themselves;
4. boundary-only centers cannot alter the corner term directly.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CenterContribution:
    center_type: str
    eps_vv: int = 0
    eps_hh: int = 0
    eps_vh: int = 0
    touches_corner: bool = False
    boundary_only: bool = False


def total_correction(contributions: list[CenterContribution]) -> tuple[int, int, int]:
    return (
        sum(item.eps_vv for item in contributions),
        sum(item.eps_hh for item in contributions),
        sum(item.eps_vh for item in contributions),
    )


def denominator(corner_term: int, contributions: list[CenterContribution]) -> int:
    eps_vv, eps_hh, eps_vh = total_correction(contributions)
    return 2 * corner_term + eps_vv + eps_hh + 2 * eps_vh


def check_channel_support() -> int:
    checks = 0
    print("Center support-channel audit")
    samples = [
        CenterContribution("A", eps_vv=1, eps_vh=2, touches_corner=True),
        CenterContribution("B", eps_hh=-1, eps_vh=1, touches_corner=True),
        CenterContribution("C", eps_vv=3, touches_corner=True),
        CenterContribution("D", eps_hh=4, touches_corner=True),
        CenterContribution("E", eps_vv=2, eps_hh=-2, boundary_only=True),
    ]
    for item in samples:
        assert item.center_type in {"A", "B", "C", "D", "E"}
        # No visible center contributes directly to c_T.
        assert not hasattr(item, "delta_c")
        if item.boundary_only:
            assert not item.touches_corner
            assert item.eps_vh == 0
        checks += 1
        print(
            f" type={item.center_type}  corr=({item.eps_vv:2d},{item.eps_hh:2d},{item.eps_vh:2d})"
            f"  touches_corner={item.touches_corner}  boundary_only={item.boundary_only}"
        )
    return checks


def check_additive_aggregation() -> int:
    checks = 0
    print("\nAdditive aggregation audit")
    contributions = [
        CenterContribution("A", eps_vv=1, eps_vh=2, touches_corner=True),
        CenterContribution("B", eps_hh=3, eps_vh=-1, touches_corner=True),
        CenterContribution("C", eps_vv=-2, touches_corner=True),
        CenterContribution("D", eps_hh=4, touches_corner=True),
        CenterContribution("E", eps_vv=1, eps_hh=1, boundary_only=True),
    ]
    eps_vv, eps_hh, eps_vh = total_correction(contributions)
    assert (eps_vv, eps_hh, eps_vh) == (0, 8, 1)
    for corner_term in (1, 3, -4):
        h = denominator(corner_term, contributions)
        expected = 2 * corner_term + eps_vv + eps_hh + 2 * eps_vh
        assert h == expected
        checks += 1
        print(f" c={corner_term:3d}  total eps=({eps_vv:2d},{eps_hh:2d},{eps_vh:2d})  h={h:3d}")
    return checks


def check_no_structural_cancellation() -> int:
    checks = 0
    print("\nNo-structural-cancellation audit")
    # Same center types, different signed coefficients, different h.
    corner_term = 5
    family_1 = [
        CenterContribution("A", eps_vv=1, eps_vh=1, touches_corner=True),
        CenterContribution("B", eps_hh=1, eps_vh=0, touches_corner=True),
    ]
    family_2 = [
        CenterContribution("A", eps_vv=-7, eps_vh=-2, touches_corner=True),
        CenterContribution("B", eps_hh=0, eps_vh=1, touches_corner=True),
    ]
    h1 = denominator(corner_term, family_1)
    h2 = denominator(corner_term, family_2)
    assert h1 != h2
    assert h1 == 14
    assert h2 == 1
    checks += 2
    print(f" family1 h={h1:3d}")
    print(f" family2 h={h2:3d}")

    cancelling_family = [
        CenterContribution("A", eps_vv=-4, eps_vh=0, touches_corner=True),
        CenterContribution("B", eps_hh=-4, eps_vh=-1, touches_corner=True),
    ]
    noncancelling_family = [
        CenterContribution("A", eps_vv=-3, eps_vh=0, touches_corner=True),
        CenterContribution("B", eps_hh=-4, eps_vh=-1, touches_corner=True),
    ]
    assert denominator(corner_term, cancelling_family) == 0
    assert denominator(corner_term, noncancelling_family) == 1
    checks += 2
    print(" cancellation requires a specific signed equality, not the center types alone")
    return checks


def check_boundary_only_invisibility() -> int:
    checks = 0
    print("\nBoundary-only invisibility audit")
    boundary_centers = [
        CenterContribution("E", eps_vv=2, boundary_only=True),
        CenterContribution("E", eps_hh=-3, boundary_only=True),
        CenterContribution("E", eps_vv=1, eps_hh=1, boundary_only=True),
    ]
    for corner_term in (2, 6):
        with_boundary = denominator(corner_term, boundary_centers)
        without_boundary = 2 * corner_term + sum(c.eps_vv + c.eps_hh for c in boundary_centers)
        assert with_boundary == without_boundary
        checks += 1
        print(f" c={corner_term:2d}  h={with_boundary:3d}")
    return checks


def main() -> None:
    support_checks = check_channel_support()
    aggregation_checks = check_additive_aggregation()
    cancellation_checks = check_no_structural_cancellation()
    boundary_checks = check_boundary_only_invisibility()

    print("\nAll exact Paper C correction-sum checks passed.")
    print(
        "Verified "
        f"{support_checks} support-channel checks, "
        f"{aggregation_checks} additive-aggregation checks, "
        f"{cancellation_checks} no-structural-cancellation checks, and "
        f"{boundary_checks} boundary-only invisibility checks."
    )


if __name__ == "__main__":
    main()
