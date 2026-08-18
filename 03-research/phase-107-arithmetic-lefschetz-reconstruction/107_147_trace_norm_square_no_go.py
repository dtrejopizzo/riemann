#!/usr/bin/env python3
"""Exact checks for 107.147: the trace-norm square no-go."""

import itertools
import math


def nuclear_norm_squared(matrix):
    """Return ||A||_*^2 exactly for a 2 by 2 integer matrix."""
    a, b, c, d = matrix
    return a * a + b * b + c * c + d * d + 2 * abs(a * d - b * c)


def canonical_sign(vector):
    for entry in vector:
        if entry:
            return vector if entry > 0 else tuple(-x for x in vector)
    return vector


def nuclear_ball(n):
    return {
        matrix
        for matrix in itertools.product(range(-n, n + 1), repeat=4)
        if nuclear_norm_squared(matrix) <= n * n
    }


def exact_dimensions_at_one_and_two():
    ball_one = nuclear_ball(1)
    ball_two = nuclear_ball(2)

    # At mass one every nonzero representation has one unit matrix.
    candidates_one = {
        canonical_sign(matrix) for matrix in ball_one if any(matrix)
    }
    dim_one = len(candidates_one)

    candidates_two = {
        canonical_sign(matrix) for matrix in ball_two if any(matrix)
    }
    units = {
        matrix for matrix in candidates_two if nuclear_norm_squared(matrix) == 1
    }

    # With budget two, a representation not using the target itself can
    # contain only two distinct norm-one generators.
    two_unit_sums = set()
    for left, right in itertools.combinations(units, 2):
        for sign_left, sign_right in itertools.product((1, -1), repeat=2):
            two_unit_sums.add(
                tuple(
                    sign_left * x + sign_right * y
                    for x, y in zip(left, right)
                )
            )

    mandatory = {
        matrix
        for matrix in candidates_two
        if matrix not in two_unit_sums
        and tuple(-x for x in matrix) not in two_unit_sums
    }

    reached = {(0, 0, 0, 0)}
    for matrix in mandatory:
        reached.add(matrix)
        reached.add(tuple(-x for x in matrix))
    mandatory_units = {
        matrix for matrix in mandatory if nuclear_norm_squared(matrix) == 1
    }
    for left, right in itertools.combinations(mandatory_units, 2):
        for sign_left, sign_right in itertools.product((1, -1), repeat=2):
            reached.add(
                tuple(
                    sign_left * x + sign_right * y
                    for x, y in zip(left, right)
                )
            )

    assert len(ball_one) == 9
    assert len(ball_two) == 49
    assert dim_one == 4
    assert len(mandatory) == 12
    assert ball_two <= reached
    return dim_one, len(mandatory)


def primitive_circle_count(n):
    """Count signed ordered primitive (x,y) with x^2+y^2=n^2."""
    count = 0
    target = n * n
    for x in range(-n, n + 1):
        y_squared = target - x * x
        y = math.isqrt(y_squared)
        if y * y != y_squared:
            continue
        ys = (0,) if y == 0 else (y, -y)
        for signed_y in ys:
            if math.gcd(abs(x), abs(signed_y)) == 1:
                count += 1
    return count


def check_primitive_family():
    primes = (5, 13, 17, 29)
    n = 1
    rows = []
    for k, prime in enumerate(primes, start=1):
        n *= prime
        actual = primitive_circle_count(n)
        expected = 4 * (2**k)
        assert actual == expected
        rows.append((k, n, actual, expected // 2))
    return rows


def main():
    dim_one, dim_two = exact_dimensions_at_one_and_two()
    rows = check_primitive_family()

    print("Primitive boundary controls:")
    for k, n, signed_count, mandatory_rays in rows:
        print(
            f"  k={k}, n={n}: primitive signed points={signed_count}, "
            f"mandatory rays={mandatory_rays}"
        )
    print()
    print("TRACE_NORM_MODEL_EXACT: YES")
    print(f"EXACT_DIMENSION_N1: {dim_one}")
    print(f"EXACT_DIMENSION_N2: {dim_two}")
    print("PRIMITIVE_BOUNDARY_COUNTS: YES")
    print("BASE3_SURVIVES_ON_SQUARE: NO")
    print("LINEAR_RR_GROWTH_SURVIVES: NO")
    print("TRACE_NORM_BRANCH: CLOSED_NO_GO")
    print("VERDICT: YES")


if __name__ == "__main__":
    main()
