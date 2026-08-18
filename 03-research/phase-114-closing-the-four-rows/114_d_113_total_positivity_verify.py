#!/usr/bin/env python3
"""Exact certificates for D.113 total-positivity/reflection audit."""

from itertools import combinations
from sympy import Matrix, Rational, diag, kronecker_product, sqrt


def main() -> None:
    rho = Rational(1, 2)

    # One-chain K is totally nonnegative through six depths.
    n = 6
    k = Matrix([[rho ** abs(i - j) for j in range(n)] for i in range(n)])
    for order in range(1, n + 1):
        for rows in combinations(range(n), order):
            for cols in combinations(range(n), order):
                assert k.extract(rows, cols).det() >= 0

    # Kunneth exact negative minor.
    k2 = Matrix([[1, rho], [rho, 1]])
    tensor = kronecker_product(k2, k2)
    kunneth_minor = tensor.extract((0, 1), (1, 2)).det()
    assert kunneth_minor == Rational(-3, 8)

    # Two-jet projected kernel has positive and negative order-two minors
    # even after its entrywise-positive diagonal sign gauge.
    n = 4
    k4 = Matrix([[rho ** abs(i - j) for j in range(n)] for i in range(n)])
    hminus = Matrix([rho**i for i in range(n)])
    hplus = Matrix([rho ** (n - 1 - i) for i in range(n)])
    h = Matrix.hstack(hminus, hplus)
    projection = Matrix.eye(n) - h * (h.T * h).inv() * h.T
    gauged = diag(1, -1, -1, 1) * projection * k4 * projection * diag(1, -1, -1, 1)
    positive_minor = gauged.extract((0, 1), (0, 1)).det()
    negative_minor = gauged.extract((0, 1), (0, 2)).det()
    assert positive_minor == Rational(3024, 474721) > 0
    assert negative_minor == Rational(-7560, 474721) < 0

    # Actual p=3 local primitive counterdirection.
    rho3 = 1 / sqrt(3)
    n = 6
    k3 = Matrix([[rho3 ** abs(i - j) for j in range(n)] for i in range(n)])
    z = Matrix.zeros(n, n - 2)
    stencil = [1, -(rho3 + 1 / rho3), 1]
    for j in range(n - 2):
        for a, value in enumerate(stencil):
            z[j + a, j] = value
    y = Matrix([-2, -3, -3, -2])
    x = z * y
    assert sum(x[i] * rho3**i for i in range(n)).simplify() == 0
    assert sum(x[i] * rho3**(-i) for i in range(n)).simplify() == 0
    local_q = (x.T * (k3 - Matrix.eye(n)) * x)[0].simplify()
    assert local_q == Rational(4, 3) * (-109 + 63 * sqrt(3))
    assert local_q > 0

    # Two positive heat modes: principal and cross minors have opposite sign.
    r1, r2 = Rational(1, 2), Rational(1, 3)
    f0, f1, f2 = 2, r1 + r2, r1 * r1 + r2 * r2
    heat_principal = f0 * f0 - f1 * f1
    heat_cross = f1 * f1 - f0 * f2
    assert heat_principal > 0
    assert heat_cross == Rational(-1, 36) < 0

    print("D113 total-positivity certificates: PASS")
    print("Kunneth counterminor:", kunneth_minor)
    print("projected positive/negative minors:", positive_minor, negative_minor)
    print("p=3 primitive local form:", local_q)
    print("Gamma two-mode principal/cross minors:", heat_principal, heat_cross)


if __name__ == "__main__":
    main()
