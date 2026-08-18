#!/usr/bin/env python3
"""Certificates for D.112 Poisson--Calderon contraction audit."""

from fractions import Fraction
from math import sqrt


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))]
            for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def main() -> None:
    # Finite exact analogue of the two-jet orthogonal projection.
    # h_-=(1,1,0), h_+=(0,1,1).
    h = [[Fraction(1), Fraction(0)],
         [Fraction(1), Fraction(1)],
         [Fraction(0), Fraction(1)]]
    gram = matmul(transpose(h), h)
    assert gram == [[2, 1], [1, 2]]
    gram_inv = [[Fraction(2, 3), Fraction(-1, 3)],
                [Fraction(-1, 3), Fraction(2, 3)]]
    hg = matmul(h, gram_inv)
    correction = matmul(hg, transpose(h))
    identity = [[Fraction(i == j) for j in range(3)] for i in range(3)]
    projection = [[identity[i][j] - correction[i][j]
                   for j in range(3)] for i in range(3)]
    assert matmul(projection, projection) == projection
    assert transpose(projection) == projection
    assert matmul(transpose(h), projection) == [[0, 0, 0], [0, 0, 0]]

    # Sharp-norm identity for B=diag(1,3), c=4.
    c = Fraction(4)
    singular_squares = [Fraction(1), Fraction(9)]
    canonical_left_inverse_diagonal = [Fraction(2), Fraction(2, 3)]
    norm_c = max(canonical_left_inverse_diagonal)
    expected = sqrt(float(c / min(singular_squares)))
    assert float(norm_c) == expected == 2.0
    assert norm_c > 1
    # It still satisfies C B=sqrt(c) I.
    assert [canonical_left_inverse_diagonal[0] * 1,
            canonical_left_inverse_diagonal[1] * 3] == [2, 2]

    # Local p=4 Szego block and inverse both have norm sqrt(3)>1.
    rho = Fraction(1, 2)
    norm_sq = (1 + rho) / (1 - rho)
    assert norm_sq == 3 > 1

    # Julia defect is negative in the expanding direction of the toy C.
    defect_first = 1 - norm_c * norm_c
    assert defect_first == -3 < 0

    print("D112 Calderon contraction certificates: PASS")
    print("two-jet projection:", projection)
    print("canonical left-inverse norm:", norm_c)
    print("local Szego norm squared / Julia defect:", norm_sq, defect_first)


if __name__ == "__main__":
    main()
