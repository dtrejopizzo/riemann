#!/usr/bin/env python3
"""Exact finite audit for the sharp equality-case gate behind F10."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


BASIS = ("r", "u", "v", "w")
PRIMITIVE_BASIS = ("r", "u", "v")


def q_source(vec: tuple[int, int, int, int]) -> Fraction:
    r, u, v, w = map(Fraction, vec)
    return u * u + v * v + 2 * w * w


def q_target_good(vec: tuple[int, int, int, int]) -> Fraction:
    return -q_source(vec)


def q_target_bad_extra_kernel(vec: tuple[int, int, int, int]) -> Fraction:
    r, u, v, w = map(Fraction, vec)
    return -(v * v + 2 * w * w)


def primitive_projection(vec: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    r, u, v, _w = vec
    return (r, u, v, 0)


def quotient_repr(vec: tuple[int, int, int, int]) -> tuple[int, int, int]:
    r, u, v, _w = primitive_projection(vec)
    return (u, v, 0) if r != 0 else (u, v, 0)


def radical_span(vec: tuple[int, int, int, int]) -> bool:
    _r, u, v, w = primitive_projection(vec)
    return u == 0 and v == 0 and w == 0


def audit_exact_kernel_good_model() -> int:
    checks = 0
    for vec in product(range(-2, 3), repeat=4):
        prim = primitive_projection(vec)
        if q_source(prim) == 0:
            assert radical_span(prim)
            checks += 1
        else:
            assert not radical_span(prim)
            checks += 1
        assert q_target_good(prim) == -q_source(prim)
        checks += 1
    return checks


def audit_extra_kernel_detected() -> int:
    checks = 0
    witnesses = [
        (0, 1, 0, 0),
        (1, 1, 0, 0),
        (2, -1, 0, 0),
    ]
    for vec in witnesses:
        prim = primitive_projection(vec)
        assert q_source(prim) > 0
        checks += 1
        assert q_target_bad_extra_kernel(prim) == 0
        checks += 1
        assert not radical_span(prim)
        checks += 1
    return checks


def audit_quotient_identity_good_vs_bad() -> int:
    checks = 0
    for vec in product(range(-1, 2), repeat=4):
        prim = primitive_projection(vec)
        if radical_span(prim):
            continue
        u, v, _ = quotient_repr(prim)
        assert -(Fraction(u) * u + Fraction(v) * v) == q_target_good((0, u, v, 0))
        checks += 1
        if u != 0:
            assert q_target_bad_extra_kernel((0, u, v, 0)) != q_target_good((0, u, v, 0))
            checks += 1
    return checks


def audit_inclusion_not_enough() -> int:
    checks = 0
    bad_kernel_vectors = []
    for vec in product(range(-1, 2), repeat=4):
        prim = primitive_projection(vec)
        if q_target_bad_extra_kernel(prim) == 0 and not radical_span(prim):
            bad_kernel_vectors.append(prim)
    assert bad_kernel_vectors
    checks += 1
    for vec in bad_kernel_vectors[:5]:
        assert q_target_good(vec) != 0
        checks += 1
    return checks


def main() -> None:
    kernel_checks = audit_exact_kernel_good_model()
    extra_checks = audit_extra_kernel_detected()
    quotient_checks = audit_quotient_identity_good_vs_bad()
    inclusion_checks = audit_inclusion_not_enough()

    print("All exact equality-case exactness checks passed.")
    print(f"  exact-kernel checks: {kernel_checks}")
    print(f"  extra-kernel witness checks: {extra_checks}")
    print(f"  quotient-identity checks: {quotient_checks}")
    print(f"  inclusion-not-enough checks: {inclusion_checks}")


if __name__ == "__main__":
    main()
