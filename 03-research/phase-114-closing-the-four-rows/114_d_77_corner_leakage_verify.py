#!/usr/bin/env python3
"""Exact finite certificates for the D.77 corner/leakage decomposition."""

from fractions import Fraction


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def trp(a):
    return [list(r) for r in zip(*a)]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def main():
    # P and P_hat are noncommuting rank-two orthogonal projections.
    P = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    # Projection onto spans of (e1+e3)/sqrt2 and (e2+e4)/sqrt2.
    H = [
        [Fraction(1, 2), 0, Fraction(1, 2), 0],
        [0, Fraction(1, 2), 0, Fraction(1, 2)],
        [Fraction(1, 2), 0, Fraction(1, 2), 0],
        [0, Fraction(1, 2), 0, Fraction(1, 2)],
    ]
    assert mm(H, H) == H and trp(H) == H
    Q = sub([[Fraction(int(i == j)) for j in range(4)]
             for i in range(4)], P)
    A = [
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [0, 1, 0, 1],
    ]
    At = trp(A)

    corner_op = sub(mm(H, P), P)
    supported_op = sub(mm(mm(P, H), P), P)
    corner = trace(mm(mm(At, corner_op), A))
    supported = trace(mm(mm(At, supported_op), A))
    cross = trace(mm(mm(mm(mm(At, Q), H), P), A))
    assert corner - supported == cross

    # Supported compression is nonpositive: P H P <= P.
    assert supported <= 0
    assert cross != 0

    # Exact primitive three-point frame for q=2.
    coeff = [Fraction(1), Fraction(-5, 2), Fraction(1)]
    m_plus = sum(coeff[n] * 2 ** n for n in range(3))
    m_minus = sum(coeff[n] * Fraction(1, 2 ** n) for n in range(3))
    log_weight = sum(Fraction(n) * coeff[n] ** 2 for n in range(3))
    assert m_plus == 0 and m_minus == 0
    assert log_weight == Fraction(33, 4)

    print("D77 corner/leakage certificates: PASS")
    print("corner, supported, cross:", corner, supported, cross)
    print("primitive logarithmic boundary weight:", log_weight)


if __name__ == "__main__":
    main()
