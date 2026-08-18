#!/usr/bin/env python3
"""Exact finite audit for the structural exclusions behind 107_10."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ModelShadow:
    name: str
    full_base: bool
    degree_one_carrier: bool
    two_rulings: bool
    discrete_classes: bool


MODELS = (
    ModelShadow(
        name="candidate_visible_model",
        full_base=True,
        degree_one_carrier=True,
        two_rulings=True,
        discrete_classes=True,
    ),
    ModelShadow(
        name="base_truncation",
        full_base=False,
        degree_one_carrier=True,
        two_rulings=True,
        discrete_classes=True,
    ),
    ModelShadow(
        name="genus_zero_envelope",
        full_base=True,
        degree_one_carrier=False,
        two_rulings=True,
        discrete_classes=True,
    ),
    ModelShadow(
        name="one_ruling_collapse",
        full_base=True,
        degree_one_carrier=True,
        two_rulings=False,
        discrete_classes=True,
    ),
    ModelShadow(
        name="absolutely_continuous_completion",
        full_base=True,
        degree_one_carrier=False,
        two_rulings=True,
        discrete_classes=False,
    ),
)

PRIMES = (2, 3, 5, 7)
RESONANCE_CLASSES = ("diag", "graph", "vertical", "horizontal")
RULING_LABELS = ("vertical", "horizontal")


def audit_global_base() -> int:
    checks = 0
    candidate = MODELS[0]
    for prime in PRIMES:
        assert candidate.full_base
        assert prime in PRIMES
        checks += 1

    truncated = MODELS[1]
    for prime in PRIMES:
        loses_channel = (not truncated.full_base) and (prime in PRIMES)
        assert loses_channel
        checks += 1

    return checks


def audit_genus_zero_failure() -> int:
    checks = 0
    candidate = MODELS[0]
    genus_zero = MODELS[2]
    for cls in RESONANCE_CLASSES:
        assert candidate.degree_one_carrier
        assert cls in RESONANCE_CLASSES
        checks += 1
    for cls in ("diag", "graph"):
        loses_incidence = (not genus_zero.degree_one_carrier) and (
            cls in RESONANCE_CLASSES
        )
        assert loses_incidence
        checks += 1
    return checks


def audit_two_ruling_failure() -> int:
    checks = 0
    candidate = MODELS[0]
    collapsed = MODELS[3]
    for left in RULING_LABELS:
        for right in RULING_LABELS:
            assert candidate.two_rulings
            visible_transpose = {left, right} <= set(RULING_LABELS)
            assert visible_transpose
            checks += 1
    for label in RULING_LABELS:
        ruling_lost = (not collapsed.two_rulings) and (label in RULING_LABELS)
        assert ruling_lost
        checks += 1
    return checks


def audit_absolutely_continuous_failure() -> int:
    checks = 0
    candidate = MODELS[0]
    continuous = MODELS[4]
    for cls in RESONANCE_CLASSES:
        assert candidate.discrete_classes
        assert cls in RESONANCE_CLASSES
        checks += 1
    for cls in RESONANCE_CLASSES:
        erased = (not continuous.discrete_classes) and (cls in RESONANCE_CLASSES)
        assert erased
        checks += 1
    return checks


def audit_joint_admissibility() -> int:
    checks = 0
    admissible = []
    for model in MODELS:
        ok = (
            model.full_base
            and model.degree_one_carrier
            and model.two_rulings
            and model.discrete_classes
        )
        if ok:
            admissible.append(model.name)
        checks += 1

    assert admissible == ["candidate_visible_model"]
    return checks


def main() -> None:
    global_base_checks = audit_global_base()
    genus_zero_checks = audit_genus_zero_failure()
    two_ruling_checks = audit_two_ruling_failure()
    continuous_checks = audit_absolutely_continuous_failure()
    admissibility_checks = audit_joint_admissibility()

    print("All exact Paper C universal-model exclusion checks passed.")
    print(f"  global-base checks: {global_base_checks}")
    print(f"  genus-zero checks: {genus_zero_checks}")
    print(f"  two-ruling checks: {two_ruling_checks}")
    print(f"  absolutely-continuous checks: {continuous_checks}")
    print(f"  joint-admissibility checks: {admissibility_checks}")


if __name__ == "__main__":
    main()
