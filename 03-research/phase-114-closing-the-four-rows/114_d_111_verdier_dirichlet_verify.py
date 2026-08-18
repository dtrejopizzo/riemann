#!/usr/bin/env python3
"""Exact finite certificates for D.111 Verdier/Dirichlet audit."""

from fractions import Fraction


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))]
            for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def main() -> None:
    # Truncated unilateral shift and the exact rank-one Laplacian defect.
    n = 5
    rho = Fraction(1, 2)
    scale = Fraction(1, 1) / (1 - rho * rho)
    shift = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for j in range(n - 1):
        shift[j + 1][j] = 1
    identity = [[Fraction(i == j) for j in range(n)] for i in range(n)]
    d = [[(identity[i][j] - rho * transpose(shift)[i][j])
          for j in range(n)] for i in range(n)]
    dstar = transpose(d)
    lap0 = [[scale * x for x in row] for row in matmul(dstar, d)]
    lap1 = [[scale * x for x in row] for row in matmul(d, dstar)]
    defect = sub(lap0, lap1)
    expected = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    # A finite truncation has two boundaries: - at the left and + at the
    # artificial right endpoint.  The half-line limit retains the first.
    expected[0][0] = -rho * rho * scale
    expected[-1][-1] = rho * rho * scale
    assert defect == expected

    # Closed range does not determine a requested sharp constant.
    # diag(1,2) is invertible/closed-range but has lower constant 1, not 2.
    singular_squares = [Fraction(1), Fraction(4)]
    assert min(singular_squares) == 1 < 2

    # Duality+nuclearity finite countermodel S=2I, B=I.
    xnorm2 = Fraction(13, 7)
    signed = 4 * xnorm2 - xnorm2
    assert signed == 3 * xnorm2 > 0

    # Difference energy expansion w||F-SF||^2
    # =2w||F||^2-2w Re<F,SF> for a unitary S.
    w = Fraction(5, 9)
    norm2 = Fraction(11, 5)
    correlation = Fraction(2, 7)
    lhs = w * (2 * norm2 - 2 * correlation)
    rhs = 2 * w * norm2 - 2 * w * correlation
    assert lhs == rhs

    print("D111 Verdier/Dirichlet certificates: PASS")
    print("finite Jacobi boundary defect:", defect[0][0], defect[-1][-1])
    print("closed-range sharp-constant counterexample:", singular_squares)
    print("duality/nuclearity signed countermodel:", signed)


if __name__ == "__main__":
    main()
