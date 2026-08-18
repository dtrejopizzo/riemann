#!/usr/bin/env python3
"""Exact finite-dimensional audit of the compressed-moment correction."""
from fractions import Fraction as Q


def mm(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return [list(x) for x in zip(*a)]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def power(a, n):
    out = [[Q(int(i == j)) for j in range(len(a))] for i in range(len(a))]
    for _ in range(n):
        out = mm(out, a)
    return out


def main():
    # P projects onto the first two coordinates; M does not preserve Ran P.
    P = [[Q(1), Q(0), Q(0)], [Q(0), Q(1), Q(0)], [Q(0), Q(0), Q(0)]]
    M = [[Q(2), Q(1), Q(1)], [Q(1), Q(3), Q(2)], [Q(1), Q(2), Q(5)]]
    S = [[Q(1), Q(0)], [Q(0), Q(1)], [Q(0), Q(0)]]
    A = mm(mm(P, M), P)
    st = tr(S)
    ambient2 = mm(mm(st, power(M, 2)), S)
    compressed2 = mm(mm(st, power(A, 2)), S)
    defect = sub(ambient2, compressed2)
    rhs = mm(mm(mm(mm(st, M), sub(
        [[Q(int(i == j)) for j in range(3)] for i in range(3)], P)), M), S)
    assert defect == rhs
    # Here the defect is vv^t for v=(1,2), hence positive and nonzero.
    assert defect == [[Q(1), Q(2)], [Q(2), Q(4)]]
    for j in range(1, 5):
        lhs = mm(mm(st, power(A, j)), S)
        recursive = mm(mm(st, M), S) if j == 1 else mm(
            mm(st, M), mm(power(mm(P, M), j - 1), S))
        assert lhs == recursive
    print("D165 compressed moment identities: PASS")


if __name__ == "__main__":
    main()
