#!/usr/bin/env python3
"""Exact finite-matrix certificate for D.45, Lemma 3.1."""

from fractions import Fraction as Q


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def sub(a, b):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def hs2(a):
    return sum(x * x for row in a for x in row)


def diag(values):
    n = len(values)
    return [[values[i] if i == j else Q(0) for j in range(n)] for i in range(n)]


def check(a, p, label, expected_sign=None):
    n = len(a)
    eye = diag([Q(1)] * n)
    q = sub(eye, p)
    astar = transpose(a)
    comm = sub(matmul(p, astar), matmul(astar, p))
    lhs = trace(matmul(a, comm))
    qap = matmul(matmul(q, a), p)
    paq = matmul(matmul(p, a), q)
    rhs = hs2(qap) - hs2(paq)
    assert lhs == rhs
    if expected_sign == "positive":
        assert lhs > 0
    elif expected_sign == "negative":
        assert lhs < 0
    print(f"PASS {label}: trace={lhs}, lower-upper={rhs}")


P = diag([Q(1), Q(1), Q(0), Q(0)])

# b=P A Q nonzero, c=Q A P zero: negative.
A_upper = [
    [Q(0), Q(0), Q(1), Q(2)],
    [Q(0), Q(0), Q(3), Q(4)],
    [Q(0), Q(0), Q(0), Q(0)],
    [Q(0), Q(0), Q(0), Q(0)],
]

# c=Q A P nonzero, b=P A Q zero: positive.
A_lower = transpose(A_upper)

A_both = [
    [Q(1), Q(2), Q(1), Q(0)],
    [Q(0), Q(1), Q(2), Q(1)],
    [Q(3), Q(0), Q(1), Q(1)],
    [Q(1), Q(1), Q(0), Q(2)],
]

check(A_upper, P, "upper Hankel block", "negative")
check(A_lower, P, "lower Hankel block", "positive")
check(A_both, P, "two-sided Hankel blocks")
print("All exact Meyer commutator certificates passed.")
