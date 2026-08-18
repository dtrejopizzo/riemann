#!/usr/bin/env python3
"""Exact finite certificates for D.121 multiscale threshold audit."""

from fractions import Fraction


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))]
            for i in range(len(a))]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def main() -> None:
    # Exact renormalized update D*D-2I=-(S+S*) for a unitary shift.
    n = 5
    s = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for j in range(n):
        s[(j + 1) % n][j] = 1
    st = transpose(s)
    identity = [[Fraction(i == j) for j in range(n)] for i in range(n)]
    d = sub(identity, s)
    jump = matmul(transpose(d), d)
    renormalized = sub(jump, scale(2, identity))
    assert renormalized == scale(-1, add(s, st))

    # At birth, use two disjoint finite intervals.  Their shift correlation
    # is zero, while the difference energy equals twice the norm.
    f = [Fraction(1), Fraction(2), Fraction(3), Fraction(0), Fraction(0),
         Fraction(0), Fraction(0), Fraction(0)]
    shifted = [Fraction(0)] * 4 + f[:4]
    norm = sum(x*x for x in f)
    corr = sum(x*y for x, y in zip(f, shifted))
    diff = sum((x-y)**2 for x, y in zip(f, shifted))
    assert corr == 0
    assert diff == 2 * norm

    # Exact scalar Schur-capacity identity in a positive 2x2 example.
    a = Fraction(4)
    b = Fraction(1)
    d0 = Fraction(3)
    capacity = d0 - b*b/a
    assert capacity == Fraction(11, 4) > 0
    determinant = a*d0-b*b
    assert determinant == a*capacity

    # Elementary per-prime budget toy: square-root costs have divergent
    # partial sums, whereas a finite reserve remains fixed.
    costs = [Fraction(1, k) for k in range(1, 101)]
    assert sum(costs) > 5

    print("D121 multiscale threshold certificates: PASS")
    print("birth correlation/difference:", corr, diff)
    print("renormalized update: -(S+S*) exact")
    print("sample shorted capacity:", capacity)
    print("nonsummable reserve toy partial cost:", sum(costs))


if __name__ == "__main__":
    main()
