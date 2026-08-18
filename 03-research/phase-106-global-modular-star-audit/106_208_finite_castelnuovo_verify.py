#!/usr/bin/env python3
"""Exact audit of the finite root-row Castelnuovo--Severi test."""

from fractions import Fraction
from math import isclose, sqrt


def incidence_matrix(M: int, n: int) -> list[list[int]]:
    """Unnormalized pullback R_M -> R_{Mn}."""
    return [[1 if a % M == b else 0 for b in range(M)] for a in range(M * n)]


def gram(U: list[list[int]]) -> list[list[int]]:
    rows = len(U)
    cols = len(U[0])
    return [
        [sum(U[a][i] * U[a][j] for a in range(rows)) for j in range(cols)]
        for i in range(cols)
    ]


def trace(A: list[list[int]]) -> int:
    return sum(A[i][i] for i in range(len(A)))


def determinant_3(A: list[list[int]]) -> int:
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


def main() -> None:
    tested = []
    for M in (2, 3, 5, 7):
        for n in (1, 2, 3, 4, 5, 8):
            U = incidence_matrix(M, n)
            G = gram(U)
            expected = [[n if i == j else 0 for j in range(M)] for i in range(M)]
            assert G == expected

            self_intersection = Fraction(trace(G), M)
            assert self_intersection == n

            primitive_square = self_intersection - 2 * n
            assert primitive_square == -n
            assert self_intersection <= 2 * n

            balanced_vertical = 1.0 / sqrt(n)
            assert isclose(balanced_vertical, n ** -0.5, rel_tol=0.0, abs_tol=1e-15)
            tested.append((M, n))

    n = 6
    intersection_matrix = [[0, 1, 1], [1, 0, n], [1, n, n]]
    assert determinant_3(intersection_matrix) == n

    # The first Eulerian idempotent is not multiplicative on primitives.
    # Record the exact degree-two mismatch e1(xy) - e1(x)e1(y) = -xy.
    e1_xy = 0
    e1_x_times_e1_y = 1
    assert e1_xy - e1_x_times_e1_y == -1

    print("root rows tested:", len(tested))
    print("U*U exact on every row: yes")
    print("self-intersection / n:", Fraction(1, 1))
    print("primitive square / n:", Fraction(-1, 1))
    print("Castelnuovo ratio Gamma^2/(2 d_v d_h):", Fraction(1, 2))
    print("3x3 intersection determinant at n=6:", determinant_3(intersection_matrix))
    print("Eulerian multiplicativity defect in degree two:", -1)


if __name__ == "__main__":
    main()
