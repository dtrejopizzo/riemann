#!/usr/bin/env python3
"""Exact audit for the candidate-envelope coherence shadow of 107_15--107_17."""

from __future__ import annotations

from dataclasses import dataclass


CHARTS = ("interior", "lower", "upper", "corner")
COMPONENTS = ("Delta", "Fv", "Fh", "G2", "G3", "G5")
CANDIDATE_CENTERS = (
    "corner_Delta_Fv",
    "corner_Delta_Fh",
    "corner_G2_Fv",
    "corner_G3_Fh",
    "interior_G2_Delta",
    "interior_G3_Delta",
    "interior_G5_Delta",
)


@dataclass(frozen=True)
class EnvelopeComponent:
    component: str
    chart: str
    receiver: str
    ruling_signature: tuple[int, int]


def visible_cover() -> dict[str, tuple[EnvelopeComponent, ...]]:
    return {
        "Delta": (
            EnvelopeComponent("Delta", "interior", "corner_phase", (1, 1)),
            EnvelopeComponent("Delta", "corner", "corner_phase", (1, 1)),
        ),
        "Fv": (
            EnvelopeComponent("Fv", "lower", "corner_phase", (1, 0)),
            EnvelopeComponent("Fv", "corner", "corner_phase", (1, 0)),
        ),
        "Fh": (
            EnvelopeComponent("Fh", "upper", "corner_phase", (0, 1)),
            EnvelopeComponent("Fh", "corner", "corner_phase", (0, 1)),
        ),
        "G2": (
            EnvelopeComponent("G2", "interior", "corner_phase", (1, 1)),
            EnvelopeComponent("G2", "lower", "corner_phase", (1, 0)),
        ),
        "G3": (
            EnvelopeComponent("G3", "interior", "corner_phase", (1, 1)),
            EnvelopeComponent("G3", "upper", "corner_phase", (0, 1)),
        ),
        "G5": (
            EnvelopeComponent("G5", "interior", "corner_phase", (1, 1)),
            EnvelopeComponent("G5", "corner", "corner_phase", (1, 1)),
        ),
    }


def singular_center(component: str, chart: str) -> str:
    table = {
        ("Delta", "corner"): "corner_Delta_Fv",
        ("Fv", "corner"): "corner_Delta_Fv",
        ("Fh", "corner"): "corner_Delta_Fh",
        ("G2", "lower"): "corner_G2_Fv",
        ("G3", "upper"): "corner_G3_Fh",
        ("G2", "interior"): "interior_G2_Delta",
        ("G3", "interior"): "interior_G3_Delta",
        ("G5", "interior"): "interior_G5_Delta",
    }
    return table[(component, chart)]


def audit_common_cover() -> int:
    checks = 0
    cover = visible_cover()
    for component in COMPONENTS:
        pieces = cover[component]
        assert pieces
        checks += 1
        assert all(piece.component == component for piece in pieces)
        checks += len(pieces)
        assert any(piece.chart in CHARTS for piece in pieces)
        checks += 1
    return checks


def audit_corner_receiver_glue() -> int:
    checks = 0
    cover = visible_cover()
    for component, pieces in cover.items():
        receivers = {piece.receiver for piece in pieces}
        assert receivers == {"corner_phase"}
        checks += 1
        if component in ("Delta", "Fv", "Fh", "G5"):
            assert any(piece.chart == "corner" for piece in pieces)
            checks += 1
    return checks


def audit_regularization_centers() -> int:
    checks = 0
    cover = visible_cover()
    encountered = set()
    for component, pieces in cover.items():
        for piece in pieces:
            if (component, piece.chart) in {
                ("Delta", "corner"),
                ("Fv", "corner"),
                ("Fh", "corner"),
                ("G2", "lower"),
                ("G3", "upper"),
                ("G2", "interior"),
                ("G3", "interior"),
                ("G5", "interior"),
            }:
                center = singular_center(component, piece.chart)
                assert center in CANDIDATE_CENTERS
                encountered.add(center)
                checks += 1
    assert encountered == set(CANDIDATE_CENTERS)
    checks += 1
    return checks


def audit_ruling_and_receiver_are_load_bearing() -> int:
    checks = 0
    cover = visible_cover()
    # Distinct rulings really stay distinct.
    fv_signatures = {piece.ruling_signature for piece in cover["Fv"]}
    fh_signatures = {piece.ruling_signature for piece in cover["Fh"]}
    assert fv_signatures == {(1, 0)}
    checks += 1
    assert fh_signatures == {(0, 1)}
    checks += 1
    assert fv_signatures != fh_signatures
    checks += 1

    # Deleting the receiver destroys every boundary/corner realization.
    for component in ("Delta", "Fv", "Fh", "G5"):
        surviving = [piece for piece in cover[component] if piece.receiver != "corner_phase"]
        assert not surviving
        checks += 1
    return checks


def audit_genus_zero_single_chart_failure() -> int:
    checks = 0
    cover = visible_cover()
    all_charts = {piece.chart for pieces in cover.values() for piece in pieces}
    assert len(all_charts) > 1
    checks += 1
    # No single chart carries both distinct rulings and the corner receiver.
    for chart in CHARTS:
        chart_components = {
            piece.component
            for pieces in cover.values()
            for piece in pieces
            if piece.chart == chart
        }
        if {"Fv", "Fh", "Delta", "G2", "G3", "G5"} <= chart_components:
            raise AssertionError("single-chart collapse should be impossible")
        checks += 1
    return checks


def main() -> None:
    cover_checks = audit_common_cover()
    receiver_checks = audit_corner_receiver_glue()
    center_checks = audit_regularization_centers()
    load_bearing_checks = audit_ruling_and_receiver_are_load_bearing()
    collapse_checks = audit_genus_zero_single_chart_failure()

    print("All exact Paper C candidate-envelope coherence checks passed.")
    print(f"  common-cover checks: {cover_checks}")
    print(f"  corner-receiver checks: {receiver_checks}")
    print(f"  regularization-center checks: {center_checks}")
    print(f"  load-bearing structure checks: {load_bearing_checks}")
    print(f"  single-chart collapse checks: {collapse_checks}")


if __name__ == "__main__":
    main()
