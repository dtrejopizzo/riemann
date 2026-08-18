#!/usr/bin/env python3
"""Finite certificates for D.74.

The script checks two exact finite-section facts used in the note:

1. the singular values of D_N=diag(1,...,1/N) and its Moore--Penrose
   inverse, displaying inverse norm N;
2. the projection-commutator trace is a difference of two off-diagonal
   squares, not a negative square.

It does not certify the Frechet range theorem or the global trace formula.
"""

from fractions import Fraction


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def frob_sq(a):
    return sum(x * x for row in a for x in row)


def main():
    # Dense/nonclosed-range model: inverse norms of finite sections diverge.
    inverse_norms = []
    for n in (4, 8, 16, 32):
        singular = [Fraction(1, k) for k in range(1, n + 1)]
        inverse = [1 / s for s in singular]
        inverse_norms.append(max(inverse))
        assert inverse_norms[-1] == n
    assert inverse_norms == [4, 8, 16, 32]

    # Exact commutator certificate with rational matrices.
    # P projects onto the first two coordinates.
    P = [[Fraction(int(i == j and i < 2)) for j in range(4)]
         for i in range(4)]
    I = [[Fraction(int(i == j)) for j in range(4)] for i in range(4)]
    Q = sub(I, P)
    A = [
        [Fraction(1), Fraction(0), Fraction(2), Fraction(-1)],
        [Fraction(0), Fraction(1), Fraction(1), Fraction(3)],
        [Fraction(4), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(1), Fraction(-2), Fraction(0), Fraction(1)],
    ]
    At = transpose(A)
    comm = sub(matmul(P, At), matmul(At, P))
    lhs = trace(matmul(A, comm))
    qap = matmul(matmul(Q, A), P)
    paq = matmul(matmul(P, A), Q)
    rhs = frob_sq(qap) - frob_sq(paq)
    assert lhs == rhs
    assert frob_sq(qap) > 0 and frob_sq(paq) > 0

    print("D74 finite certificates: PASS")
    print("Moore--Penrose finite inverse norms:", inverse_norms)
    print("commutator trace = lower square - upper square =", lhs)


if __name__ == "__main__":
    main()
