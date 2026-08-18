#!/usr/bin/env python3
"""Exact finite-dimensional checks for D.210.

The script verifies typing and identities only.  It is not evidence for
the row-D sign.
"""

from fractions import Fraction as F


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def add(a, b, sign=1):
    return [[x + sign * y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def inv(a):
    n = len(a)
    aug = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(a)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if aug[i][j])
        aug[j], aug[pivot] = aug[pivot], aug[j]
        q = aug[j][j]
        aug[j] = [x / q for x in aug[j]]
        for i in range(n):
            if i != j and aug[i][j]:
                q = aug[i][j]
                aug[i] = [x - q * y for x, y in zip(aug[i], aug[j])]
    return [row[n:] for row in aug]


def block(a, rows, cols):
    return [[a[i][j] for j in cols] for i in rows]


def quadratic_green(a, c):
    return mm(transpose(c), mm(inv(a), c))


# A positive rational matrix, split W={0,1}, Z={2,3}.
A = [
    [F(6), F(1), F(1), F(0)],
    [F(1), F(5), F(0), F(1)],
    [F(1), F(0), F(4), F(1)],
    [F(0), F(1), F(1), F(3)],
]
C = [
    [F(1), F(2)],
    [F(0), F(1)],
    [F(2), F(0)],
    [F(1), F(1)],
]
W, Z = [0, 1], [2, 3]
Aww, Awz = block(A, W, W), block(A, W, Z)
Azw, Azz = block(A, Z, W), block(A, Z, Z)
Cw, Cz = block(C, W, [0, 1]), block(C, Z, [0, 1])
Aww_i = inv(Aww)
S = add(Azz, mm(Azw, mm(Aww_i, Awz)), sign=-1)
R = add(Cz, mm(Azw, mm(Aww_i, Cw)), sign=-1)
Gw = mm(transpose(Cw), mm(Aww_i, Cw))
rhs = add(Gw, mm(transpose(R), mm(inv(S), R)))
lhs = quadratic_green(A, C)
assert lhs == rhs

# Galerkin increment: W1={0}, W2={0,1}.
W1 = [0]
A11 = block(A, W1, W1)
C1 = block(C, W1, [0, 1])
G1 = mm(transpose(C1), mm(inv(A11), C1))
increment = add(Gw, G1, sign=-1)

# Exact 2x2 PSD check: diagonal nonnegative and determinant nonnegative.
assert increment[0][0] >= 0 and increment[1][1] >= 0
assert increment[0][0] * increment[1][1] - increment[0][1] ** 2 >= 0

print("D.210 operator-Green identity: PASS")
print("exact Green =", lhs)
print("captured Green G_W =", Gw)
print("corrected residual R_W =", R)
print("tail Schur S_W =", S)
print("nested Galerkin increment =", increment)
print("Scope: exact finite-dimensional identity only; row-D sign NOT CLAIMED")
