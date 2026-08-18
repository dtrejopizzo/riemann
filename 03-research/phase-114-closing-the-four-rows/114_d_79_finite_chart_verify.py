#!/usr/bin/env python3
"""Exact finite-dimensional certificates for D.79."""

from fractions import Fraction


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))]
            for i in range(len(a))]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def main():
    # A nonpositive 2x2 matrix with zero QQ corner cannot have a cross term.
    # The test corner has one positive direction, certified by det < 0.
    D = Fraction(-1, 2)
    B = Fraction(1, 4)
    det_corner = D * 0 - B * B
    assert det_corner == Fraction(-1, 16) < 0

    # Exact positive Schur channel after eliminating D.
    S = -B * (1 / D) * B
    assert S == Fraction(1, 8) > 0

    # Completing the square: q(p,q)=D(p+Xq)^2+S q^2.
    X = (1 / D) * B
    assert X == Fraction(-1, 2)
    for p, q in ((Fraction(2), Fraction(3)),
                 (Fraction(-1), Fraction(5)),
                 (Fraction(7, 3), Fraction(-2))):
        lhs = D * p * p + 2 * B * p * q
        rhs = D * (p + X * q) ** 2 + S * q * q
        assert lhs == rhs

    # Two real Clifford generators: cross terms cancel, square stays positive.
    one = Fraction(1)
    zero = Fraction(0)
    gamma1 = [[one, zero], [zero, -one]]
    gamma2 = [[zero, one], [one, zero]]
    ident = [[one, zero], [zero, one]]
    anti = add(matmul(gamma1, gamma2), matmul(gamma2, gamma1))
    assert anti == [[zero, zero], [zero, zero]]
    assert matmul(gamma1, gamma1) == ident
    assert matmul(gamma2, gamma2) == ident

    a = Fraction(2, 3)
    b = Fraction(5, 7)
    dirac = add(scale(a, gamma1), scale(b, gamma2))
    square = matmul(dirac, dirac)
    expected = scale(a * a + b * b, ident)
    assert square == expected
    assert square[0][0] > 0 and square[1][1] > 0

    # Supertrace can have either sign; it is not an ordered trace.
    supertrace_pos = Fraction(3) - Fraction(1)
    supertrace_neg = Fraction(1) - Fraction(3)
    assert supertrace_pos > 0 and supertrace_neg < 0

    print("D79 finite-chart/Clifford certificates: PASS")
    print("corner determinant, positive Schur channel:", det_corner, S)
    print("Clifford square scalar:", a * a + b * b)


if __name__ == "__main__":
    main()
