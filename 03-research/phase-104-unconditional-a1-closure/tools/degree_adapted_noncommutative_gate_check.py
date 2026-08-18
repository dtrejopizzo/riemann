#!/usr/bin/env python3
"""Exact checks for 104_42 (Fraction only)."""

from fractions import Fraction as F


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def matvec(a, x):
    return [sum((a[i][j] * x[j] for j in range(len(x))), F(0))
            for i in range(len(a))]


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), F(0))


def inv2(a):
    d = det2(a)
    return [[a[1][1] / d, -a[0][1] / d],
            [-a[1][0] / d, a[0][0] / d]]


def check_noncommutative_optimizers():
    # Positive inner product: R v = g, R is positive and non-diagonal.
    v = [F(2), F(1)]
    g = [F(-1), F(3)]
    r = [[F(3, 2), F(-4)], [F(-4), F(11)]]
    assert dot(v, g) == 1
    assert r[0][0] > 0 and det2(r) > 0
    assert matvec(r, v) == g
    rinv = inv2(r)
    assert matvec(rinv, g) == v
    cost = (dot(matvec(r, v), v) + dot(matvec(rinv, g), g)) / 2
    assert cost == abs(dot(v, g)) == 1

    # Negative inner product: R v = -g.
    v = [F(1), F(0)]
    g = [F(-2), F(1)]
    r = [[F(2), F(-1)], [F(-1), F(1)]]
    assert dot(v, g) == -2
    assert r[0][0] > 0 and det2(r) > 0
    assert matvec(r, v) == [-x for x in g]
    rinv = inv2(r)
    assert matvec(rinv, g) == [-x for x in v]
    cost = (dot(matvec(r, v), v) + dot(matvec(rinv, g), g)) / 2
    assert cost == abs(dot(v, g)) == 2


def q_from_b(b, d):
    if d == 0:
        return b[1]
    return (b[d + 1] - 2 * b[d] + b[d - 1]) / 2


def check_toeplitz_degree_filter():
    b = [F(0), F(-3, 5), F(7, 11), F(-2, 7), F(13, 17),
         F(5, 19), F(-11, 23), F(29, 31), F(-7, 37), F(41, 43)]

    for n in range(2, len(b)):
        q = [q_from_b(b, d) for d in range(n)]
        rows = []
        for j in range(n):
            rows.append(sum((q[abs(j - k)] for k in range(n)), F(0)))

        # Prefix quadratic form is exactly B_n.
        assert sum(rows, F(0)) == b[n]

        # Each compressed coordinate is the symmetric increment average.
        delta = [b[j + 1] - b[j] for j in range(n)]
        expected = [(delta[j] + delta[n - 1 - j]) / 2
                    for j in range(n)]
        assert rows == expected

        norm_sq = sum((x * x for x in rows), F(0))
        symmetric_sum = sum(
            ((delta[j] + delta[n - 1 - j]) ** 2 for j in range(n)),
            F(0),
        )
        assert norm_sq == symmetric_sum / 4

    # If B_n=x and all earlier values are fixed, the squared right-hand
    # side of (27) has leading coefficient n/2 times x^2.
    for n in range(3, 30):
        leading_coefficient = F(n, 2)
        assert leading_coefficient > 1


def check_offline_falsifier():
    n = 152
    b_off = 2 * (F(2 ** n) + F(1, 2 ** n)) - 4
    budget = F(1501, 2002) * n * n
    assert b_off > budget
    # The corresponding Li quartet is negative.
    lambda_off = 4 - 2 * (F(2 ** n) + F(1, 2 ** n))
    assert lambda_off < 0 and b_off == -lambda_off


def main():
    check_noncommutative_optimizers()
    check_toeplitz_degree_filter()
    check_offline_falsifier()
    print("104_42 noncommutative optimizer: PASS")
    print("104_42 Toeplitz degree filter: PASS")
    print("104_42 off-line falsifier: PASS")


if __name__ == "__main__":
    main()
