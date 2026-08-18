#!/usr/bin/env python3
"""Exact scalar-angle certificates for D.78."""

from fractions import Fraction


def main():
    # Scalar generic two-projection angle: alpha=1/2, beta=1/2.
    alpha = Fraction(1, 2)
    beta = Fraction(1, 2)
    D = alpha - 1
    B = beta / 2  # Hermitian corner off-diagonal.

    # Minimal solution DX=B and its unavoidable bottom block.
    X = B / D
    assert X == Fraction(-1, 2)
    bottom = X * D * X
    assert bottom == Fraction(-1, 8)
    assert bottom != 0

    # Positive Schur remainder of [[D,B],[B,0]].
    schur = -B * (1 / D) * B
    assert schur == Fraction(1, 8) > 0
    determinant = D * 0 - B * B
    assert determinant < 0  # one positive and one negative direction

    # Rational angle family lambda=n^2/(n^2+1).  Formula (4.3) is n^2/4.
    angle_norm_sq = []
    for n in (1, 2, 4, 8, 16):
        lam = Fraction(n * n, n * n + 1)
        val = lam / (4 * (1 - lam))
        assert val == Fraction(n * n, 4)
        angle_norm_sq.append(val)
    assert all(angle_norm_sq[i + 1] > angle_norm_sq[i]
               for i in range(len(angle_norm_sq) - 1))

    print("D78 triangular/Schur certificates: PASS")
    print("transport X, diagonal cost, positive Schur:", X, bottom, schur)
    print("cofinal angle norms squared:", angle_norm_sq)


if __name__ == "__main__":
    main()
