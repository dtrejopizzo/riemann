#!/usr/bin/env python3
"""Exact certificates for the D.83 feedthrough/Pick audit."""

from fractions import Fraction


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))]
            for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def main():
    # Single-prime v_r at r=1/2.
    r = Fraction(1, 2)
    theta0 = 1 - r * r
    theta_minus1 = -r
    assert theta0 == Fraction(3, 4) != 0

    # Truncated Hardy displacement.  W+ is backward, W- is forward.
    n = 4
    Wp = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    Wm = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for j in range(1, n):
        Wp[j - 1][j] = 1
    for j in range(n - 1):
        Wm[j + 1][j] = 1

    # E maps e0 to f0.  The first Toeplitz row begins (theta0,theta_-1,0,...).
    E = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    E[0][0] = 1
    T = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    first_row = [theta0, theta_minus1] + [Fraction(0)] * (n - 2)
    T[0] = first_row
    rhs = [[-x for x in row] for row in matmul(E, T)]
    assert rhs[0][0] == -theta0 != 0

    # Every displacement Y W+ - W- Y has zero (0,0), for arbitrary Y.
    Y = [[Fraction((i + 1) * (j + 2), 17) for j in range(n)]
         for i in range(n)]
    disp_a = matmul(Y, Wp)
    disp_b = matmul(Wm, Y)
    displacement = [[disp_a[i][j] - disp_b[i][j]
                     for j in range(n)] for i in range(n)]
    assert displacement[0][0] == 0
    assert displacement != rhs

    # The tail psi_-1=r cancels one row entry but creates the opposite column.
    psi = [Fraction(0)] * (2 * n)
    psi[1] = r
    H = [[psi[i + j + 1] for j in range(n)] for i in range(n)]
    ha = matmul(H, Wp)
    hb = matmul(Wm, H)
    hd = [[ha[i][j] - hb[i][j] for j in range(n)] for i in range(n)]
    assert hd[0][1] == r
    assert hd[1][0] == -r

    # Exact energy balance for a rational orthogonal colligation.
    T0, G0, H0, R0 = (Fraction(3, 5), Fraction(4, 5),
                       Fraction(-4, 5), Fraction(3, 5))
    for x, u in ((Fraction(2), Fraction(1)),
                 (Fraction(-3, 2), Fraction(5, 3))):
        x1 = T0 * x + G0 * u
        y = H0 * x + R0 * u
        assert x * x + u * u == x1 * x1 + y * y

    # Gram/Pick criterion: X*X-Y*Y positive in a contractive example.
    X = [[Fraction(1), Fraction(0)],
         [Fraction(0), Fraction(1)]]
    Yc = [[Fraction(1, 2), Fraction(0)],
          [Fraction(0), Fraction(1, 3)]]
    gram_x = matmul(transpose(X), X)
    gram_y = matmul(transpose(Yc), Yc)
    pick = [[gram_x[i][j] - gram_y[i][j] for j in range(2)]
            for i in range(2)]
    assert pick == [[Fraction(3, 4), Fraction(0)],
                    [Fraction(0), Fraction(8, 9)]]

    print("D83 Redheffer/feedthrough/Pick certificates: PASS")
    print("unreachable zero-time coefficient:", rhs[0][0])
    print("tail row/column pair:", hd[0][1], hd[1][0])


if __name__ == "__main__":
    main()
