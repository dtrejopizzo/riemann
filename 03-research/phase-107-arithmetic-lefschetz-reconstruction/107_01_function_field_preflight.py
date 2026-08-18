#!/usr/bin/env python3
"""Exact preflight for the fixed Phase 107 function-field control.

This checks arithmetic consequences of the proposed calibration.  It is
not a proof of the geometric intersection identities or of Hodge index.
It also does not test methodological falsifiers such as F8 ("no
prescribed trace"), because those concern how the Lefschetz package is
constructed, not the arithmetic values verified here.
"""

from fractions import Fraction


Q = 5
MAX_N = 16


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def count_base_curve() -> int:
    squares = {y * y % Q for y in range(Q)}
    affine = 0
    for x in range(Q):
        rhs = (x**3 + x + 1) % Q
        affine += sum(1 for y in range(Q) if y * y % Q == rhs)
        assert (rhs in squares) == any(y * y % Q == rhs for y in range(Q))
    return affine + 1


def main() -> None:
    assert count_base_curve() == 9

    a = [0] * (MAX_N + 1)
    point_count = [0] * (MAX_N + 1)
    closed_points = [0] * (MAX_N + 1)
    a[0] = 2
    a[1] = -3

    print(" n       a_n       N_n       B_n       det(G_n^0)")
    for n in range(1, MAX_N + 1):
        if n >= 2:
            a[n] = -3 * a[n - 1] - Q * a[n - 2]

        point_count[n] = Q**n + 1 - a[n]
        previous = sum(d * closed_points[d] for d in divisors(n) if d < n)
        b_n = Fraction(point_count[n] - previous, n)
        assert b_n.denominator == 1
        closed_points[n] = b_n.numerator
        assert closed_points[n] >= 0

        determinant = 4 * Q**n - a[n] ** 2
        assert determinant >= 0
        assert point_count[n] == sum(
            d * closed_points[d] for d in divisors(n)
        )

        print(
            f"{n:2d} {a[n]:9d} {point_count[n]:9d} "
            f"{closed_points[n]:9d} {determinant:18d}"
        )

    assert (closed_points[1], closed_points[2], closed_points[3]) == (9, 9, 33)
    print("All exact preflight checks passed.")


if __name__ == "__main__":
    main()
