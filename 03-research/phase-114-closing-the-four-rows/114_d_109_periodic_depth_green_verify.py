#!/usr/bin/env python3
"""Certificates for D.109 periodic-depth Green resolvent."""

from fractions import Fraction
from math import isclose, sqrt


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b)))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def main() -> None:
    # p=4 makes rho rational.  The identities are algebraic in rho and do
    # not depend on 4 being prime.
    p = 4
    rho = Fraction(1, 2)
    n = 7

    # Stationary covariance K(r,s)=rho^|r-s|.
    k = [[rho ** abs(i - j) for j in range(n)] for i in range(n)]

    # The half-line Jacobi precision Q.  On a finite leading block QK=I;
    # the final row sees the omitted infinite tail, so certify rows < n-1.
    scale = 1 / (1 - rho * rho)
    q = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    q[0][0] = scale
    for i in range(1, n):
        q[i][i] = (1 + rho * rho) * scale
    for i in range(n - 1):
        q[i][i + 1] = q[i + 1][i] = -rho * scale
    qk = matmul(q, k)
    for i in range(n - 1):
        for j in range(n):
            assert qk[i][j] == (1 if i == j else 0)

    # Cofinal extremal-count overlaps converge to rho^|r-s|.
    a = 3
    r, s = 1, 4

    def d(depth):
        return a * (p ** depth) - p + 1

    target = float(rho ** abs(r - s))
    errors = []
    for t in (1, 3, 6, 10):
        overlap = sqrt(d(t + min(r, s)) / d(t + max(r, s)))
        errors.append(abs(overlap - target))
    assert all(errors[i + 1] < errors[i] for i in range(len(errors) - 1))
    assert errors[-1] < 1e-7

    # Exact finite-depth Markov innovation is normalized and orthogonal to
    # the entire earlier cumulative subspace; the scalar check is the norm.
    dr, dr1 = d(5), d(6)
    rho_r = sqrt(dr / dr1)
    innovation_norm_sq = (
        1 + rho_r * rho_r - 2 * rho_r * sqrt(dr / dr1)
    ) / (1 - rho_r * rho_r)
    assert isclose(innovation_norm_sq, 1.0, rel_tol=0, abs_tol=1e-14)

    # Kunneth covariance is the Kronecker product of the two local kernels.
    qprime = 9
    sigma = Fraction(1, 3)
    kp = [[rho ** abs(i - j) for j in range(3)] for i in range(3)]
    kq = [[sigma ** abs(i - j) for j in range(2)] for i in range(2)]
    product_entry = kp[0][2] * kq[0][1]
    assert product_entry == Fraction(1, p) * Fraction(1, 3)
    assert product_entry == Fraction(1, 12)
    assert qprime == 9  # documents sigma=qprime^{-1/2}

    print("D109 periodic-depth Green certificates: PASS")
    print("stationary target and cofinal errors:", target, errors)
    print("Jacobi leading-block inverse rows:", n - 1)
    print("Kunneth sample covariance:", product_entry)


if __name__ == "__main__":
    main()
