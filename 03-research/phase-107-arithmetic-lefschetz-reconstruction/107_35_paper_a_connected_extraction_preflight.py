#!/usr/bin/env python3
"""Exact audit for Paper A connected extraction.

This script checks two exact pieces behind `107_03`.

1. On a truncated symmetric Hopf algebra on primitive generators, the
   first Eulerian idempotent `e_1 = log^*(I)` fixes degree-1 generators
   and annihilates decomposable monomials.
2. For the fixed control curve `E/F_5`, the Euler-product logarithm
   built from primitive closed-point counts recovers the point-count
   sequence exactly in a finite window.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb


Q = 5
MAX_N = 16
NUM_GENERATORS = 3
MAX_TOTAL_DEGREE = 4


Monomial = tuple[int, ...]
Polynomial = dict[Monomial, Fraction]


def add_poly(left: Polynomial, right: Polynomial) -> Polynomial:
    out = dict(left)
    for mono, coeff in right.items():
        out[mono] = out.get(mono, Fraction(0)) + coeff
        if out[mono] == 0:
            del out[mono]
    return out


def scale_poly(poly: Polynomial, scalar: Fraction) -> Polynomial:
    if scalar == 0:
        return {}
    return {mono: scalar * coeff for mono, coeff in poly.items() if coeff != 0}


def total_degree(mono: Monomial) -> int:
    return sum(mono)


def unit_monomial() -> Monomial:
    return (0,) * NUM_GENERATORS


def monomial_basis(max_total_degree: int) -> list[Monomial]:
    basis: list[Monomial] = []

    def rec(idx: int, remaining: int, prefix: list[int]) -> None:
        if idx == NUM_GENERATORS - 1:
            basis.append(tuple(prefix + [remaining]))
            return
        for value in range(remaining + 1):
            rec(idx + 1, remaining - value, prefix + [value])

    for degree in range(max_total_degree + 1):
        rec(0, degree, [])
    return basis


def coproduct(mono: Monomial) -> list[tuple[Fraction, Monomial, Monomial]]:
    terms: list[tuple[Fraction, Monomial, Monomial]] = []

    def rec(
        idx: int,
        left_prefix: list[int],
        right_prefix: list[int],
        coeff: int,
    ) -> None:
        if idx == NUM_GENERATORS:
            terms.append((Fraction(coeff), tuple(left_prefix), tuple(right_prefix)))
            return
        exponent = mono[idx]
        for split in range(exponent + 1):
            rec(
                idx + 1,
                left_prefix + [split],
                right_prefix + [exponent - split],
                coeff * comb(exponent, split),
            )

    rec(0, [], [], 1)
    return terms


def f_map(mono: Monomial) -> Polynomial:
    if total_degree(mono) == 0:
        return {}
    return {mono: Fraction(1)}


def poly_mul(left: Polynomial, right: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for mono_left, coeff_left in left.items():
        for mono_right, coeff_right in right.items():
            mono = tuple(a + b for a, b in zip(mono_left, mono_right))
            out[mono] = out.get(mono, Fraction(0)) + coeff_left * coeff_right
            if out[mono] == 0:
                del out[mono]
    return out


def convolution_power_on_monomial(mono: Monomial, power: int) -> Polynomial:
    if power == 1:
        return f_map(mono)

    out: Polynomial = {}
    for coeff, left, right in coproduct(mono):
        left_poly = f_map(left)
        if not left_poly:
            continue
        right_poly = convolution_power_on_monomial(right, power - 1)
        if not right_poly:
            continue
        out = add_poly(out, scale_poly(poly_mul(left_poly, right_poly), coeff))
    return out


def eulerian_idempotent_on_monomial(mono: Monomial) -> Polynomial:
    degree = total_degree(mono)
    if degree == 0:
        return {}
    out: Polynomial = {}
    for power in range(1, degree + 1):
        term = convolution_power_on_monomial(mono, power)
        out = add_poly(out, scale_poly(term, Fraction((-1) ** (power - 1), power)))
    return out


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def point_counts_and_closed_points() -> tuple[list[int], list[int]]:
    a = [0] * (MAX_N + 1)
    point_count = [0] * (MAX_N + 1)
    closed_points = [0] * (MAX_N + 1)
    a[0] = 2
    a[1] = -3

    for n in range(1, MAX_N + 1):
        if n >= 2:
            a[n] = -3 * a[n - 1] - Q * a[n - 2]
        point_count[n] = Q**n + 1 - a[n]
        previous = sum(d * closed_points[d] for d in divisors(n) if d < n)
        b_n = Fraction(point_count[n] - previous, n)
        assert b_n.denominator == 1
        closed_points[n] = b_n.numerator
    return point_count, closed_points


def series_mul(left: list[Fraction], right: list[Fraction], max_degree: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(max_degree + 1)]
    for i, a in enumerate(left):
        if a == 0:
            continue
        for j, b in enumerate(right):
            if b == 0 or i + j > max_degree:
                continue
            out[i + j] += a * b
    return out


def series_log(one_plus_h: list[Fraction]) -> list[Fraction]:
    assert one_plus_h[0] == 1
    max_degree = len(one_plus_h) - 1
    h = one_plus_h[:]
    h[0] = 0
    out = [Fraction(0) for _ in range(max_degree + 1)]
    power = h[:]
    for r in range(1, max_degree + 1):
        coeff = Fraction((-1) ** (r - 1), r)
        for degree in range(1, max_degree + 1):
            out[degree] += coeff * power[degree]
        power = series_mul(power, h, max_degree)
    return out


def euler_factor(d: int, multiplicity: int, max_degree: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(max_degree + 1)]
    for j in range(0, max_degree // d + 1):
        coeff = Fraction(1)
        for t in range(j):
            coeff *= Fraction(multiplicity + t, t + 1)
        out[d * j] = coeff
    return out


def main() -> None:
    print("Hopf-algebra primitive extraction audit")
    basis = monomial_basis(MAX_TOTAL_DEGREE)
    primitive_count = 0
    decomposable_count = 0
    for mono in basis:
        degree = total_degree(mono)
        if degree == 0:
            continue
        image = eulerian_idempotent_on_monomial(mono)
        if degree == 1:
            assert image == {mono: Fraction(1)}
            primitive_count += 1
            print(f" mono={mono}  e1(mono)=mono")
        else:
            assert image == {}
            decomposable_count += 1
            print(f" mono={mono}  e1(mono)=0")

    print("\nFunction-field Euler extraction audit")
    point_count, closed_points = point_counts_and_closed_points()
    zeta_series = [Fraction(0) for _ in range(MAX_N + 1)]
    zeta_series[0] = 1
    for d in range(1, MAX_N + 1):
        factor = euler_factor(d, closed_points[d], MAX_N)
        zeta_series = series_mul(zeta_series, factor, MAX_N)
    log_series = series_log(zeta_series)

    print(" n       N_n       B_n    coeff(log Z)")
    for n in range(1, MAX_N + 1):
        expected = Fraction(point_count[n], n)
        assert log_series[n] == expected
        reconstructed = Fraction(1, n) * sum(
            d * closed_points[d] for d in divisors(n)
        )
        assert reconstructed == expected
        print(
            f"{n:2d} {point_count[n]:9d} {closed_points[n]:9d}"
            f" {str(log_series[n]):>14}"
        )

    print(
        f"\nPrimitive extraction passed on {primitive_count} degree-1 monomials"
        f" and {decomposable_count} decomposable monomials."
    )
    print(f"Euler-product logarithm audit passed through n={MAX_N}.")


if __name__ == "__main__":
    main()
