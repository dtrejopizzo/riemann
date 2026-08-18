#!/usr/bin/env python3
"""Exact finite audit for the zero-free source shadow behind F2."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


SOURCE_GENERATORS = (
    "R2,1",
    "R2,2",
    "R3,1",
    "R5,1",
    "B0",
    "B1",
    "Delta",
)
SPECTRAL_GENERATORS = ("rho0", "rho1")
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


def source_constructor(
    source: dict[str, Fraction], spectral: dict[str, Fraction]
) -> dict[str, Fraction]:
    del spectral
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


def spectral_tampered_constructor(
    source: dict[str, Fraction], spectral: dict[str, Fraction]
) -> dict[str, Fraction]:
    out = source_constructor(source, spectral)
    out["gamma_0"] += spectral["rho0"]
    out["prime_3_1"] += spectral["rho1"]
    return out


def recover_source(observable: dict[str, Fraction]) -> dict[str, Fraction] | None:
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
    recovered["Delta"] = observable["identity"]
    return recovered


def audit_spectral_ignorance() -> int:
    checks = 0
    source = {key: Fraction(0) for key in SOURCE_GENERATORS}
    for rho0, rho1 in product(range(-2, 3), repeat=2):
        spectral = {"rho0": Fraction(rho0), "rho1": Fraction(rho1)}
        out = source_constructor(source, spectral)
        assert all(value == 0 for value in out.values())
        checks += 1
    return checks


def audit_source_recovery() -> int:
    checks = 0
    for coeffs in product(range(-1, 2), repeat=len(SOURCE_GENERATORS)):
        source = {key: Fraction(value) for key, value in zip(SOURCE_GENERATORS, coeffs)}
        spectral = {"rho0": Fraction(1), "rho1": Fraction(-1)}
        out = source_constructor(source, spectral)
        recovered = recover_source(out)
        assert recovered is not None
        for key in SOURCE_GENERATORS:
            assert recovered[key] == source[key]
            checks += 1
    return checks


def audit_tampered_constructor_detected() -> int:
    checks = 0
    source = {key: Fraction(0) for key in SOURCE_GENERATORS}
    witnesses = (
        {"rho0": Fraction(1), "rho1": Fraction(0)},
        {"rho0": Fraction(0), "rho1": Fraction(1)},
        {"rho0": Fraction(-2), "rho1": Fraction(3)},
    )
    for spectral in witnesses:
        compliant = source_constructor(source, spectral)
        tampered = spectral_tampered_constructor(source, spectral)
        assert tampered != compliant
        checks += 1
        assert recover_source(tampered) is None or tampered["prime_3_1"] != compliant["prime_3_1"]
        checks += 1
    return checks


def audit_zero_side_not_needed_for_visible_output() -> int:
    checks = 0
    sample_source = {
        "R2,1": Fraction(1),
        "R2,2": Fraction(-1),
        "R3,1": Fraction(1),
        "R5,1": Fraction(0),
        "B0": Fraction(2),
        "B1": Fraction(-1),
        "Delta": Fraction(3),
    }
    outputs = set()
    for rho0, rho1 in product(range(-1, 2), repeat=2):
        spectral = {"rho0": Fraction(rho0), "rho1": Fraction(rho1)}
        out = tuple(source_constructor(sample_source, spectral)[key] for key in OBSERVABLES)
        outputs.add(out)
        checks += 1
    assert len(outputs) == 1
    return checks


def main() -> None:
    ignorance_checks = audit_spectral_ignorance()
    recovery_checks = audit_source_recovery()
    tamper_checks = audit_tampered_constructor_detected()
    independence_checks = audit_zero_side_not_needed_for_visible_output()

    print("All exact zero-free source checks passed.")
    print(f"  spectral-ignorance checks: {ignorance_checks}")
    print(f"  source-recovery checks: {recovery_checks}")
    print(f"  tampered-constructor checks: {tamper_checks}")
    print(f"  source-independence checks: {independence_checks}")


if __name__ == "__main__":
    main()
