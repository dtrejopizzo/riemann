#!/usr/bin/env python3
"""Exact finite certificates for D.119 supersymmetric killing audit."""

from fractions import Fraction


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))]
            for i in range(len(a))]


def main() -> None:
    # Two-dimensional cohomology with an arbitrary positive gap eps^2.
    eps = Fraction(3, 7)
    q = [[Fraction(0), Fraction(0), eps]]
    even = matmul(transpose(q), q)
    odd = matmul(q, transpose(q))
    assert [even[i][i] for i in range(3)] == [0, 0, eps * eps]
    assert odd == [[eps * eps]]
    assert sum(even[i][i] for i in range(3)) - odd[0][0] == 0
    assert eps * eps == Fraction(9, 49)  # freely variable positive gap

    # Hilbert enlargement adds the mass; Krein enlargement subtracts it.
    partial = [[Fraction(1), Fraction(0)],
               [Fraction(0), Fraction(2)]]
    lap = matmul(transpose(partial), partial)  # diag(1,4)
    mass = Fraction(1)
    hilbert = [[lap[i][j] + mass * Fraction(i == j)
                for j in range(2)] for i in range(2)]
    krein = [[lap[i][j] - mass * Fraction(i == j)
              for j in range(2)] for i in range(2)]
    assert [hilbert[i][i] for i in range(2)] == [2, 5]
    assert [krein[i][i] for i in range(2)] == [0, 3]

    # A larger subtraction creates a negative direction: Krein
    # factorization alone does not prove primitive positivity.
    larger_mass = Fraction(2)
    indefinite = [[lap[i][j] - larger_mass * Fraction(i == j)
                    for j in range(2)] for i in range(2)]
    assert [indefinite[i][i] for i in range(2)] == [-1, 2]

    # The crossed two-jet metric is hyperbolic.
    crossed = [[Fraction(0), Fraction(1)],
               [Fraction(1), Fraction(0)]]
    positive_vector = [Fraction(1), Fraction(1)]
    negative_vector = [Fraction(1), Fraction(-1)]
    def quad(a, x):
        return sum(x[i] * a[i][j] * x[j]
                   for i in range(len(x)) for j in range(len(x)))
    assert quad(crossed, positive_vector) == 2
    assert quad(crossed, negative_vector) == -2

    print("D119 supersymmetric killing certificates: PASS")
    print("two-class arbitrary gap:", eps * eps)
    print("Hilbert/Krein mass signs:",
          [hilbert[i][i] for i in range(2)],
          [krein[i][i] for i in range(2)])
    print("unproved negative direction:", indefinite[0][0])
    print("crossed jet inertia witnesses:",
          quad(crossed, positive_vector), quad(crossed, negative_vector))


if __name__ == "__main__":
    main()
