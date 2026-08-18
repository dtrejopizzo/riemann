#!/usr/bin/env python3
"""Exact certificates for the D.82 unitary-Hankel audit."""

from fractions import Fraction


def matmul(a, b):
    n, m, q = len(a), len(b), len(b[0])
    return [[sum(a[i][k] * b[k][j] for k in range(m))
             for j in range(q)] for i in range(n)]


def matsub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def matadd(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def main():
    # Single-prime factor v_r at r=1/2 has both Hardy orientations.
    r = Fraction(1, 2)
    negative_coeff = -r
    positive = [(1 - r * r) * r ** n for n in range(8)]
    assert negative_coeff != 0
    assert all(c != 0 for c in positive)

    # Exact infinite Hilbert--Schmidt norms of the two rank-one Hankels.
    lower_hs2 = r * r
    # (1-r^2)^2 r^2 (sum r^(2n))^2 = r^2.
    upper_hs2 = ((1 - r * r) ** 2 * r * r
                 / (1 - r * r) ** 2)
    assert lower_hs2 == upper_hs2 == Fraction(1, 4)

    # The phase derivative P_r-1 has both signs.
    phase_at_one = 2 * r / (1 - r)
    phase_at_minus_one = -2 * r / (1 + r)
    assert phase_at_one == 2 > 0
    assert phase_at_minus_one == Fraction(-2, 3) < 0

    # Finite exact model of the windowed Hankel commutator (3.5).
    # U and W are commuting powers of the cyclic shift; P is a window.
    z = Fraction(0)
    o = Fraction(1)
    U = [[z, z, z, o],
         [o, z, z, z],
         [z, o, z, z],
         [z, z, o, z]]
    W = matmul(U, U)
    P = [[o, z, z, z],
         [z, o, z, z],
         [z, z, z, z],
         [z, z, z, z]]
    I = [[o if i == j else z for j in range(4)] for i in range(4)]
    Q = matsub(I, P)

    H = matmul(matmul(Q, U), P)
    Wp = matmul(matmul(P, W), P)
    Wm = matmul(matmul(Q, W), Q)
    lhs = matsub(matmul(H, Wp), matmul(Wm, H))
    rhs = matadd(
        [[-x for x in row]
         for row in matmul(matmul(matmul(Q, U), Q), matmul(W, P))],
        matmul(matmul(matmul(Q, W), P), matmul(U, P)),
    )
    assert lhs == rhs

    toeplitz_edge = matmul(matmul(matmul(Q, W), P), matmul(U, P))
    assert any(x != 0 for row in toeplitz_edge for x in row)

    print("D82 unitary-Hankel certificates: PASS")
    print("two Hankel HS squares:", lower_hs2, upper_hs2)
    print("local phase signs:", phase_at_one, phase_at_minus_one)


if __name__ == "__main__":
    main()
