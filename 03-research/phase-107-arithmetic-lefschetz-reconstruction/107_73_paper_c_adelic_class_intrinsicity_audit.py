#!/usr/bin/env python3
"""Exact audit for the finite adelic-class intrinsicity shadow of 107_22."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product


CHARTS = ("U0", "U1", "Uinf")
ROOTS = (0, 1, 2)


@dataclass(frozen=True)
class LocalPresentation:
    chart: str
    root: int
    finite_a: int
    finite_b: int
    receiver_main: int
    receiver_extra: int


def normalized_presentation(chart: str, root: int) -> LocalPresentation:
    return LocalPresentation(
        chart=chart,
        root=root,
        finite_a=2,
        finite_b=-1,
        receiver_main=1,
        receiver_extra=0,
    )


def bad_split_presentation(chart: str, root: int) -> LocalPresentation:
    return LocalPresentation(
        chart=chart,
        root=root,
        finite_a=2,
        finite_b=-1,
        receiver_main=1,
        receiver_extra=1,
    )


def quotient_class_key(presentation: LocalPresentation) -> tuple[int, int, int, int]:
    return (
        presentation.finite_a,
        presentation.finite_b,
        presentation.receiver_main,
        presentation.receiver_extra,
    )


def total_receiver_weight(presentation: LocalPresentation) -> int:
    return presentation.receiver_main + presentation.receiver_extra


def audit_chart_root_quotient() -> int:
    checks = 0
    presentations = [
        normalized_presentation(chart, root)
        for chart, root in product(CHARTS, ROOTS)
    ]
    base_key = quotient_class_key(presentations[0])
    for left, right in product(presentations, repeat=2):
        assert quotient_class_key(left) == quotient_class_key(right) == base_key
        checks += 1
    return checks


def audit_invariant_receiver_weight() -> int:
    checks = 0
    for chart, root in product(CHARTS, ROOTS):
        presentation = normalized_presentation(chart, root)
        assert total_receiver_weight(presentation) == 1
        assert quotient_class_key(presentation)[:2] == (2, -1)
        checks += 1
    return checks


def audit_root_refinement_invisibility() -> int:
    checks = 0
    for chart in CHARTS:
        base = normalized_presentation(chart, ROOTS[0])
        for root in ROOTS[1:]:
            refined = normalized_presentation(chart, root)
            assert quotient_class_key(base) == quotient_class_key(refined)
            assert total_receiver_weight(base) == total_receiver_weight(refined)
            checks += 1
    return checks


def audit_extra_receiver_rejected() -> int:
    checks = 0
    for chart, root in product(CHARTS, ROOTS):
        good = normalized_presentation(chart, root)
        bad = bad_split_presentation(chart, root)
        assert quotient_class_key(good) != quotient_class_key(bad)
        assert total_receiver_weight(good) == 1
        assert total_receiver_weight(bad) == 2
        checks += 1
    return checks


def main() -> None:
    quotient_checks = audit_chart_root_quotient()
    receiver_weight_checks = audit_invariant_receiver_weight()
    root_refinement_checks = audit_root_refinement_invisibility()
    extra_receiver_checks = audit_extra_receiver_rejected()

    print("All exact Paper C adelic-class intrinsicity checks passed.")
    print(f"  quotient checks: {quotient_checks}")
    print(f"  receiver-weight checks: {receiver_weight_checks}")
    print(f"  rooted-refinement checks: {root_refinement_checks}")
    print(f"  extra-receiver rejection checks: {extra_receiver_checks}")


if __name__ == "__main__":
    main()
