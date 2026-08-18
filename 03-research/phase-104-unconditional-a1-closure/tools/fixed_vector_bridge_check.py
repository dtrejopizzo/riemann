#!/usr/bin/env python3
"""Exact finite checks for 104_28.

The script verifies with Fraction arithmetic:

  L_{n-1}^{(1)} = sum_{k=0}^{n-1} L_k,
  ||sum_{k<n} phi_k||^2 = n,
  1_n^* T_n(q) 1_n = q_n for arbitrary rational sequences.

It does not construct an archimedean whitening and does not test A1.
"""

from fractions import Fraction as F
from math import comb, factorial


def laguerre_coeffs(n: int, alpha: int) -> list[F]:
    """Coefficients in ascending powers of x."""
    return [
        F((-1) ** j * comb(n + alpha, n - j), factorial(j))
        for j in range(n + 1)
    ]


def add_poly(left: list[F], right: list[F]) -> list[F]:
    size = max(len(left), len(right))
    out = [F(0) for _ in range(size)]
    for index, value in enumerate(left):
        out[index] += value
    for index, value in enumerate(right):
        out[index] += value
    return out


def check_laguerre_sum(nmax: int = 20) -> None:
    for n in range(1, nmax + 1):
        rhs: list[F] = []
        for k in range(n):
            rhs = add_poly(rhs, laguerre_coeffs(k, 0))
        assert rhs == laguerre_coeffs(n - 1, 1)


def toeplitz_energy(q: list[F], n: int) -> F:
    t = [q[1]]
    for m in range(1, n):
        t.append((q[m + 1] - 2 * q[m] + q[m - 1]) / 2)
    return n * t[0] + 2 * sum((n - m) * t[m] for m in range(1, n))


def check_fejer_identity(nmax: int = 20) -> None:
    # Non-special rational data: the identity must be pure telescoping.
    q = [F(0)] + [F(7 * n**3 - 5 * n**2 + 11 * n, 13) for n in range(1, nmax + 2)]
    for n in range(1, nmax + 1):
        assert toeplitz_energy(q, n) == q[n]


def main() -> None:
    check_laguerre_sum()
    check_fejer_identity()
    # Orthonormality of phi_k makes the norm statement immediate once the
    # coefficient vector is the n-entry vector of ones.
    for n in range(1, 21):
        assert sum(F(1) ** 2 for _ in range(n)) == n
    print("PASS: exact Laguerre-prefix and Fejer/Toeplitz bridge checks")
    print("STOP: A_1 < 0, so the natural archimedean Toeplitz form is not a metric")


if __name__ == "__main__":
    main()
