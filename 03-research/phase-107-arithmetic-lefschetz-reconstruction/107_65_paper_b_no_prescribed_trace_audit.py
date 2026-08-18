#!/usr/bin/env python3
"""Exact finite audit for the no-prescribed-trace shadow behind 107_09."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


RETURN_GENERATORS = ("R2,1", "R2,2", "R3,1", "R5,1")
BOUNDARY_GENERATORS = ("B0", "B1")
SOURCE_GENERATORS = RETURN_GENERATORS + BOUNDARY_GENERATORS + ("Delta",)
OBSERVABLES = (
    "prime_2_1",
    "prime_2_2",
    "prime_3_1",
    "prime_5_1",
    "gamma_0",
    "pole_0",
    "gamma_1",
    "pole_1",
    "identity",
)


def zero_vector(keys: tuple[str, ...]) -> dict[str, Fraction]:
    return {key: Fraction(0) for key in keys}


def evaluate_raw(source: dict[str, Fraction]) -> dict[str, Fraction]:
    out = zero_vector(OBSERVABLES)
    out["prime_2_1"] = -Fraction(1, 2) * source["R2,1"]
    out["prime_2_2"] = -Fraction(1, 4) * source["R2,2"]
    out["prime_3_1"] = -Fraction(1, 3) * source["R3,1"]
    out["prime_5_1"] = -Fraction(1, 5) * source["R5,1"]
    out["gamma_0"] = Fraction(3, 2) * source["B0"]
    out["pole_0"] = Fraction(3, 2) * source["B0"]
    out["gamma_1"] = -Fraction(5, 4) * source["B1"]
    out["pole_1"] = -Fraction(5, 4) * source["B1"]
    out["identity"] = source["Delta"]
    return out


def renormalize(source: dict[str, Fraction], c_f: Fraction) -> dict[str, Fraction]:
    shifted = dict(source)
    shifted["Delta"] -= c_f
    return evaluate_raw(shifted)


def recover_source(observable: dict[str, Fraction]) -> dict[str, Fraction] | None:
    if observable["identity"] != 0:
        return None
    if observable["gamma_0"] != observable["pole_0"]:
        return None
    if observable["gamma_1"] != observable["pole_1"]:
        return None

    recovered = zero_vector(SOURCE_GENERATORS)
    recovered["R2,1"] = -2 * observable["prime_2_1"]
    recovered["R2,2"] = -4 * observable["prime_2_2"]
    recovered["R3,1"] = -3 * observable["prime_3_1"]
    recovered["R5,1"] = -5 * observable["prime_5_1"]
    recovered["B0"] = Fraction(2, 3) * observable["gamma_0"]
    recovered["B1"] = -Fraction(4, 5) * observable["gamma_1"]
    recovered["Delta"] = Fraction(0)
    return recovered


def audit_diagonal_cleanup() -> int:
    checks = 0
    samples = (
        {"R2,1": 1, "R2,2": 0, "R3,1": 1, "R5,1": 0, "B0": 1, "B1": 0, "Delta": 2},
        {"R2,1": 0, "R2,2": 1, "R3,1": 0, "R5,1": 1, "B0": 0, "B1": -1, "Delta": -3},
    )
    for sample in samples:
        source = {key: Fraction(sample.get(key, 0)) for key in SOURCE_GENERATORS}
        raw = evaluate_raw(source)
        ren = renormalize(source, source["Delta"])
        assert ren["identity"] == 0
        checks += 1
        for key in OBSERVABLES:
            if key != "identity":
                assert ren[key] == raw[key]
                checks += 1
    return checks


def audit_boundary_coupling() -> int:
    checks = 0
    for b0, b1 in product(range(-2, 3), repeat=2):
        source = zero_vector(SOURCE_GENERATORS)
        source["B0"] = Fraction(b0)
        source["B1"] = Fraction(b1)
        obs = renormalize(source, Fraction(0))
        assert obs["gamma_0"] == obs["pole_0"]
        checks += 1
        assert obs["gamma_1"] == obs["pole_1"]
        checks += 1
    return checks


def audit_trivial_kernel() -> int:
    checks = 0
    for coeffs in product(range(-1, 2), repeat=len(SOURCE_GENERATORS)):
        source = {key: Fraction(value) for key, value in zip(SOURCE_GENERATORS, coeffs)}
        ren = renormalize(source, source["Delta"])
        if all(value == 0 for value in ren.values()):
            assert all(source[key] == 0 for key in RETURN_GENERATORS + BOUNDARY_GENERATORS)
        else:
            recovered = recover_source(ren)
            assert recovered is not None
            for key in RETURN_GENERATORS + BOUNDARY_GENERATORS:
                assert recovered[key] == source[key]
                checks += 1
    return checks


def audit_invalid_prescribed_perturbations() -> int:
    checks = 0
    invalid_observables = (
        {
            "prime_2_1": Fraction(0),
            "prime_2_2": Fraction(0),
            "prime_3_1": Fraction(0),
            "prime_5_1": Fraction(0),
            "gamma_0": Fraction(1),
            "pole_0": Fraction(0),
            "gamma_1": Fraction(0),
            "pole_1": Fraction(0),
            "identity": Fraction(0),
        },
        {
            "prime_2_1": Fraction(0),
            "prime_2_2": Fraction(0),
            "prime_3_1": Fraction(0),
            "prime_5_1": Fraction(0),
            "gamma_0": Fraction(0),
            "pole_0": Fraction(0),
            "gamma_1": Fraction(0),
            "pole_1": Fraction(0),
            "identity": Fraction(1),
        },
        {
            "prime_2_1": Fraction(0),
            "prime_2_2": Fraction(0),
            "prime_3_1": Fraction(0),
            "prime_5_1": Fraction(0),
            "gamma_0": Fraction(0),
            "pole_0": Fraction(0),
            "gamma_1": Fraction(2),
            "pole_1": Fraction(-2),
            "identity": Fraction(0),
        },
    )
    for observable in invalid_observables:
        assert recover_source(observable) is None
        checks += 1
    return checks


def main() -> None:
    diagonal_checks = audit_diagonal_cleanup()
    boundary_checks = audit_boundary_coupling()
    kernel_checks = audit_trivial_kernel()
    invalid_checks = audit_invalid_prescribed_perturbations()

    print("All exact Paper B no-prescribed-trace checks passed.")
    print(f"  diagonal-cleanup checks: {diagonal_checks}")
    print(f"  boundary-coupling checks: {boundary_checks}")
    print(f"  trivial-kernel checks: {kernel_checks}")
    print(f"  invalid-perturbation checks: {invalid_checks}")


if __name__ == "__main__":
    main()
