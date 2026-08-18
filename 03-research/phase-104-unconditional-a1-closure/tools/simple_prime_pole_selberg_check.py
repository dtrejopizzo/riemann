#!/usr/bin/env python3
"""Exact checks for 104_35 (no floating-point arithmetic)."""

from fractions import Fraction
from math import comb, factorial


def laguerre(n: int, alpha: int) -> list[Fraction]:
    """Coefficients of L_n^(alpha)(x), low degree first."""
    return [
        Fraction((-1) ** k * comb(n + alpha, n - k), factorial(k))
        for k in range(n + 1)
    ]


def derivative(poly: list[Fraction]) -> list[Fraction]:
    return [Fraction(k) * poly[k] for k in range(1, len(poly))]


def sub(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    size = max(len(left), len(right))
    return [
        (left[k] if k < len(left) else Fraction(0))
        - (right[k] if k < len(right) else Fraction(0))
        for k in range(size)
    ]


def scale_poly(c: Fraction, poly: list[Fraction]) -> list[Fraction]:
    return [c * coef for coef in poly]


def moment_exp_minus_x(poly: list[Fraction]) -> Fraction:
    """Integral_0^infty exp(-x) poly(x) dx."""
    return sum(coef * factorial(k) for k, coef in enumerate(poly))


def add_measure(*measures: dict[int, Fraction]) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for measure in measures:
        for point, mass in measure.items():
            out[point] = out.get(point, Fraction(0)) + mass
    return {point: mass for point, mass in out.items() if mass}


def scale_measure(c: Fraction, measure: dict[int, Fraction]) -> dict[int, Fraction]:
    return {point: c * mass for point, mass in measure.items() if c * mass}


def coordinate_weight(measure: dict[int, Fraction]) -> dict[int, Fraction]:
    return {point: Fraction(point) * mass for point, mass in measure.items()}


def convolution(
    left: dict[int, Fraction], right: dict[int, Fraction]
) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for x, a in left.items():
        for y, b in right.items():
            out[x + y] = out.get(x + y, Fraction(0)) + a * b
    return {point: mass for point, mass in out.items() if mass}


def check_laguerre_edges(top: int = 30) -> None:
    for n in range(1, top + 1):
        degree = n - 1
        l1 = laguerre(degree, 1)
        l2 = laguerre(degree, 2)

        # d/dx(e^-x L^(1)) = e^-x((L^(1))' - L^(1)) = -e^-x L^(2).
        assert sub(derivative(l1), l1) == scale_poly(Fraction(-1), l2)
        assert moment_exp_minus_x(l2) == n
        assert l1[0] == n
        assert l2[0] == Fraction(n * (n + 1), 2)


def check_centered_selberg_identity() -> None:
    # Arbitrary finite rational measures.  This checks the algebraic core
    # u(alpha-beta)+alpha*alpha-beta*beta
    # = u*r+2 beta*r+r*r without positivity or approximation.
    beta = {0: Fraction(2, 3), 2: Fraction(5, 7), 5: Fraction(3, 11)}
    r = {1: Fraction(4, 9), 3: Fraction(-2, 5), 6: Fraction(7, 13)}
    alpha = add_measure(beta, r)

    left = add_measure(
        coordinate_weight(alpha),
        convolution(alpha, alpha),
        scale_measure(Fraction(-1), coordinate_weight(beta)),
        scale_measure(Fraction(-1), convolution(beta, beta)),
    )
    right = add_measure(
        coordinate_weight(r),
        scale_measure(Fraction(2), convolution(beta, r)),
        convolution(r, r),
    )
    assert left == right


def main() -> None:
    check_laguerre_edges()
    check_centered_selberg_identity()
    print("PASS: Laguerre borders and simple-prime centered Selberg identity")


if __name__ == "__main__":
    main()
