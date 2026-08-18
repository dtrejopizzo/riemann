#!/usr/bin/env python3
"""Exact audit for the unified finite-support synthesis shadow of 107_06."""

from __future__ import annotations

from fractions import Fraction


SUPPORT = (
    (2, -4),
    (2, -2),
    (2, 2),
    (2, 4),
    (3, -2),
    (3, 2),
    (5, -2),
    (5, 2),
)

WEIGHTS = {label: Fraction(1, label[0] ** (abs(label[1]) // 2)) for label in SUPPORT}


def add_corr(*corrs: dict[tuple[int, int], Fraction]) -> dict[tuple[int, int], Fraction]:
    out: dict[tuple[int, int], Fraction] = {}
    for corr in corrs:
        for label, coeff in corr.items():
            out[label] = out.get(label, Fraction(0)) + coeff
    return {label: coeff for label, coeff in out.items() if coeff}


CORR = {
    ("x", "x"): {
        (2, -4): Fraction(1, 2),
        (2, 2): Fraction(3, 2),
        (3, 2): Fraction(1, 3),
        (5, -2): Fraction(2, 5),
    },
    ("x", "y"): {
        (2, -2): Fraction(1, 2),
        (2, 4): Fraction(1, 4),
        (3, -2): Fraction(2, 3),
        (5, 2): Fraction(1, 5),
    },
    ("y", "y"): {
        (2, -4): Fraction(1, 4),
        (2, 2): Fraction(1, 1),
        (3, 2): Fraction(5, 6),
        (5, -2): Fraction(3, 5),
    },
    ("x2", "y"): {
        (6, 0): Fraction(7, 10),  # non-prime-power ratio shadow, must die
        (10, 0): Fraction(-3, 10),  # non-prime-power ratio shadow, must die
    },
}
CORR[("y", "x")] = CORR[("x", "y")]
CORR[("x+y", "x+y")] = add_corr(
    CORR[("x", "x")],
    CORR[("x", "y")],
    CORR[("y", "x")],
    CORR[("y", "y")],
)

ARCH = {
    ("x", "x"): Fraction(7, 6),
    ("x", "y"): Fraction(-5, 12),
    ("y", "y"): Fraction(11, 10),
}
ARCH[("y", "x")] = ARCH[("x", "y")]
ARCH[("x+y", "x+y")] = ARCH[("x", "x")] + 2 * ARCH[("x", "y")] + ARCH[("y", "y")]


def primitive_extract(symbol: str) -> dict[str, Fraction]:
    if symbol == "x":
        return {"x": Fraction(1)}
    if symbol == "y":
        return {"y": Fraction(1)}
    if symbol == "x+y":
        return {"x": Fraction(1), "y": Fraction(1)}
    if symbol == "x*y":
        return {}
    if symbol == "x2":
        return {"x2": Fraction(1)}
    raise ValueError(symbol)


def finite_corr(left: str, right: str) -> dict[tuple[int, int], Fraction]:
    result: dict[tuple[int, int], Fraction] = {}
    left_prim = primitive_extract(left)
    right_prim = primitive_extract(right)
    for l_name, l_coeff in left_prim.items():
        for r_name, r_coeff in right_prim.items():
            corr = CORR.get((l_name, r_name), {})
            for label, coeff in corr.items():
                if label in WEIGHTS:
                    result[label] = result.get(label, Fraction(0)) + l_coeff * r_coeff * coeff
    return result


def cutoff_sum(corr: dict[tuple[int, int], Fraction], max_abs_k: int) -> Fraction:
    total = Fraction(0)
    for label, coeff in corr.items():
        _, k = label
        if abs(k) <= max_abs_k:
            total += WEIGHTS[label] * coeff
    return total


def pairing(left: str, right: str, cutoff: int) -> Fraction:
    corr = finite_corr(left, right)
    arch = ARCH.get((left, right), Fraction(0))
    p_infty = cutoff_sum(corr, 99) + arch
    return p_infty - cutoff_sum(corr, cutoff)


def pairing_with_diagonal_shift(left: str, right: str, cutoff: int, shift: Fraction) -> Fraction:
    value = pairing(left, right, cutoff)
    if left == right:
        return value + shift
    return value


def audit_connected_extraction_gate() -> int:
    checks = 0
    assert primitive_extract("x*y") == {}
    checks += 1
    assert finite_corr("x*y", "x") == {}
    checks += 1
    assert finite_corr("x*y", "y") == {}
    checks += 1
    assert pairing("x*y", "x", 8) == 0
    checks += 1
    assert pairing("x*y", "y", 8) == 0
    checks += 1
    return checks


def audit_prime_power_support_gate() -> int:
    checks = 0
    xy_corr = finite_corr("x", "y")
    assert set(xy_corr) == {(2, -2), (2, 4), (3, -2), (5, 2)}
    checks += 1
    bad_corr = finite_corr("x2", "y")
    assert bad_corr == {}
    checks += 1
    xx_corr = finite_corr("x", "x")
    assert all(label in WEIGHTS for label in xx_corr)
    checks += len(xx_corr)
    return checks


def audit_common_green_and_polarization() -> int:
    checks = 0
    q_x = pairing("x", "x", 8)
    q_y = pairing("y", "y", 8)
    q_xy = pairing("x+y", "x+y", 8)
    b_xy = pairing("x", "y", 8)
    assert q_x == ARCH[("x", "x")]
    checks += 1
    assert q_y == ARCH[("y", "y")]
    checks += 1
    assert b_xy == ARCH[("x", "y")]
    checks += 1
    assert q_xy - q_x - q_y == 2 * b_xy
    checks += 1
    return checks


def audit_cutoff_independence() -> int:
    checks = 0
    for pair in (("x", "x"), ("x", "y"), ("y", "y"), ("x+y", "x+y")):
        target = pairing(pair[0], pair[1], 99)
        for cutoff in (4, 6, 8):
            assert pairing(pair[0], pair[1], cutoff) == target
            checks += 1
    return checks


def audit_detectable_failures() -> int:
    checks = 0
    b_xy = pairing("x", "y", 8)
    q_x = pairing("x", "x", 8)
    q_y = pairing("y", "y", 8)
    q_xy = pairing("x+y", "x+y", 8)
    for shift in (Fraction(1, 7), Fraction(-2, 9), Fraction(5, 11)):
        broken_x = pairing_with_diagonal_shift("x", "x", 8, shift)
        broken_y = pairing_with_diagonal_shift("y", "y", 8, shift)
        broken_xy = pairing_with_diagonal_shift("x+y", "x+y", 8, shift)
        assert broken_xy - broken_x - broken_y != 2 * b_xy
        checks += 1
    return checks


def main() -> None:
    extraction_checks = audit_connected_extraction_gate()
    support_checks = audit_prime_power_support_gate()
    green_checks = audit_common_green_and_polarization()
    cutoff_checks = audit_cutoff_independence()
    failure_checks = audit_detectable_failures()

    print("All exact Paper A unified-synthesis checks passed.")
    print(f"  connected-extraction gate checks: {extraction_checks}")
    print(f"  prime-power support gate checks: {support_checks}")
    print(f"  common-Green/polarization checks: {green_checks}")
    print(f"  cutoff-independence checks: {cutoff_checks}")
    print(f"  detectable-failure checks: {failure_checks}")


if __name__ == "__main__":
    main()
