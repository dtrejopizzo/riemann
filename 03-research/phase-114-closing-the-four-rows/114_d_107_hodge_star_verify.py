#!/usr/bin/env python3
"""Exact block certificates for D.107 periodic Hodge-star audit."""

from fractions import Fraction


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def main() -> None:
    # Free character pair: R=diag(r,1/r), Q=swap is invariant.
    r = Fraction(3, 2)
    scaling = [[r, Fraction(0)], [Fraction(0), 1 / r]]
    swap = [[Fraction(0), Fraction(1)],
            [Fraction(1), Fraction(0)]]
    invariant = matmul(matmul(scaling, swap), scaling)
    assert invariant == swap  # real diagonal, so R^*=R

    # The algebraically positive star=swap does not commute with scaling.
    star_positive = swap
    left = matmul(star_positive, scaling)
    right = matmul(scaling, star_positive)
    assert left != right
    h_positive = matmul(swap, star_positive)
    assert h_positive == [[1, 0], [0, 1]]

    # Equivariant Q-self-adjoint diagonal involutions are +/-I and leave
    # the Hodge metric hyperbolic.
    for sign in (Fraction(1), Fraction(-1)):
        star = [[sign, 0], [0, sign]]
        hodge = matmul(swap, star)
        determinant = hodge[0][0] * hodge[1][1] - hodge[0][1] * hodge[1][0]
        assert determinant == -1 < 0

    # Lyapunov equation for a nilpotent Jordan block forces h_11=0.
    # N=[[0,1],[0,0]], H=[[x,y],[y,z]] gives HN+N^T H=[[0,x],[x,2y]].
    x = Fraction(0)
    y = Fraction(0)
    z = Fraction(5)
    determinant_h = x * z - y * y
    assert determinant_h == 0  # cannot be positive definite

    print("D107 periodic Hodge-star certificates: PASS")
    print("Krein scaling invariance:", invariant)
    print("positive star commutator nonzero:", left, right)
    print("nilpotent Lyapunov forced determinant:", determinant_h)


if __name__ == "__main__":
    main()
