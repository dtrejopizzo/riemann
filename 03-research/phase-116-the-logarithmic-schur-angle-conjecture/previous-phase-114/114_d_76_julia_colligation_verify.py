#!/usr/bin/env python3
"""Exact finite certificates for the D.76 Julia gate."""

from fractions import Fraction


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return [list(r) for r in zip(*a)]


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def main():
    # Rational diagonal contraction C=diag(3/5,4/5); both defect square
    # roots are rational and the Julia matrix is exactly unitary.
    C = [[Fraction(3, 5), 0], [0, Fraction(4, 5)]]
    D = [[Fraction(4, 5), 0], [0, Fraction(3, 5)]]
    U = [
        [C[0][0], 0, D[0][0], 0],
        [0, C[1][1], 0, D[1][1]],
        [D[0][0], 0, -C[0][0], 0],
        [0, D[1][1], 0, -C[1][1]],
    ]
    assert mm(tr(U), U) == eye(4)

    # Pullback on the first summand is C*C-I, exactly the norm defect.
    P = [[Fraction(int(i == j and i < 2)) for j in range(4)]
         for i in range(4)]
    UtPU = mm(mm(tr(U), P), U)
    defect = [[UtPU[i][j] - P[i][j] for j in range(4)]
              for i in range(4)]
    assert defect[0][0] == Fraction(9, 25) - 1
    assert defect[1][1] == Fraction(16, 25) - 1

    # A scalar expansive corner cannot be the corner of a Hilbert unitary.
    expansive = Fraction(6, 5)
    assert expansive * expansive > 1

    # Bounded transform changes the requested defect.
    bt_sq = expansive * expansive / (1 + expansive * expansive)
    transformed_defect = bt_sq - 1
    requested_defect = expansive * expansive - 1
    assert transformed_defect != requested_defect

    print("D76 Julia-colligation certificates: PASS")
    print("contractive defects:", defect[0][0], defect[1][1])
    print("expansive requested / transformed:",
          requested_defect, transformed_defect)


if __name__ == "__main__":
    main()
