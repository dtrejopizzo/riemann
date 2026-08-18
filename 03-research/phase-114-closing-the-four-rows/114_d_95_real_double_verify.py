#!/usr/bin/env python3
"""Exact block certificates for D.95 functional-equation Real double."""

from fractions import Fraction


def mat_vec(a, v):
    return [sum(a[i][j] * v[j] for j in range(len(v)))
            for i in range(len(a))]


def dot(v, w):
    return sum(v[i] * w[i] for i in range(len(v)))


def main() -> None:
    m = Fraction(7, 3)
    swap = [[Fraction(0), m], [m, Fraction(0)]]
    determinant = swap[0][0] * swap[1][1] - swap[0][1] * swap[1][0]
    assert determinant == -(m * m) < 0

    symmetric = [Fraction(1), Fraction(1)]
    antisymmetric = [Fraction(1), Fraction(-1)]
    q_plus = dot(symmetric, mat_vec(swap, symmetric))
    q_minus = dot(antisymmetric, mat_vec(swap, antisymmetric))
    assert q_plus == 2 * m > 0
    assert q_minus == -2 * m < 0

    # Spectral projectors of the bare swap: both are nonzero and idempotent.
    identity = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    bare_swap = [[Fraction(0), Fraction(1)], [Fraction(1), Fraction(0)]]
    p_plus = [[(identity[i][j] + bare_swap[i][j]) / 2 for j in range(2)]
              for i in range(2)]
    p_minus = [[(identity[i][j] - bare_swap[i][j]) / 2 for j in range(2)]
               for i in range(2)]

    for projector in (p_plus, p_minus):
        square = [[sum(projector[i][k] * projector[k][j] for k in range(2))
                   for j in range(2)] for i in range(2)]
        assert square == projector
        assert any(entry != 0 for row in projector for entry in row)

    # A fixed orbit is a positive one-dimensional block.
    fixed_value = Fraction(5, 4)
    fixed_q = m * fixed_value * fixed_value
    assert fixed_q > 0

    print("D95 Real-double block certificates: PASS")
    print("free-orbit determinant:", determinant)
    print("symmetric/antisymmetric values:", q_plus, q_minus)
    print("fixed-orbit value:", fixed_q)


if __name__ == "__main__":
    main()
