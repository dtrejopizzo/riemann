#!/usr/bin/env python3
"""Exact finite-dimensional certificate for D.46 projection signs."""

from fractions import Fraction as F


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    bt = transpose(b)
    return [[sum(x*y for x, y in zip(r, c)) for c in bt] for r in a]


def sub(a, b):
    return [[x-y for x, y in zip(r, s)] for r, s in zip(a, b)]


def mv(a, x):
    return [sum(u*v for u, v in zip(r, x)) for r in a]


def dot(x, y):
    return sum(u*v for u, v in zip(x, y))


def diag(v):
    return [[v[i] if i == j else F(0) for j in range(len(v))]
            for i in range(len(v))]


# U swaps a 3-dimensional support space with its exterior.
zero = [[F(0)]*3 for _ in range(3)]
eye3 = diag([F(1)]*3)
U = [zero[i] + eye3[i] for i in range(3)] + [eye3[i] + zero[i] for i in range(3)]
P = diag([F(1)]*3 + [F(0)]*3)
Ut = transpose(U)
A = sub(mm(mm(Ut, P), U), P)

# Two jets remove e1 and e4.  Primitive compression still contains
# a negative support vector e2 and a positive exterior vector e5.
e2 = [F(0), F(1), F(0), F(0), F(0), F(0)]
e5 = [F(0), F(0), F(0), F(0), F(1), F(0)]
q2 = dot(e2, mv(A, e2))
q5 = dot(e5, mv(A, e5))
assert q2 == -1 and q5 == 1

# Verify A = (1/2) U^* [2P-I,U].
I = diag([F(1)]*6)
FP = sub([[2*x for x in row] for row in P], I)
comm = sub(mm(FP, U), mm(U, FP))
rhs = [[x/F(2) for x in row] for row in mm(Ut, comm)]
assert rhs == A

print("PASS phase identity A=(1/2)U*[2P-I,U]")
print("PASS two-jet compression remains indefinite:", q2, q5)
