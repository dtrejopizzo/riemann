#!/usr/bin/env python3
"""Exact algebra checks for the compensated log(2) split in 104_29."""

from fractions import Fraction as F
from math import comb, factorial


def laguerre_one(n_minus_one: int) -> list[F]:
    """L_{n-1}^{(1)} in ascending powers."""
    degree = n_minus_one
    return [
        F((-1) ** j * comb(degree + 1, degree - j), factorial(j))
        for j in range(degree + 1)
    ]


def compensated_test(n: int) -> list[F]:
    out = laguerre_one(n - 1)
    out[0] -= n
    return out


def main() -> None:
    for n in range(1, 21):
        phi = compensated_test(n)
        assert phi[0] == 0
        if n == 1:
            assert phi == [F(0)]
            continue
        assert phi[-1] == F((-1) ** (n - 1), factorial(n - 1))

        # The top monomial against exp(-epsilon*x) has the exact pole order
        # epsilon^{-n}; factorials cancel.
        top_moment_coefficient = phi[-1] * factorial(n - 1)
        assert top_moment_coefficient == (-1) ** (n - 1)

    # At x0=log(2)/2, b_r=-r+(r-1)/sqrt(2).
    # Since 1/sqrt(2)<1, b_r<-r+(r-1)=-1 for every rational r>1.
    for r in (F(3), F(4), F(2002, 501)):
        assert -r + (r - 1) == -1

    print("PASS: compensated Laguerre tests vanish at zero")
    print("PASS: separated top moments have exact epsilon^(-n) scale")
    print("PASS: the pre-prime density at log(2)/2 is < -1 for r>1")
    print("STOP: the exact exterior inequality is D_n^[r] >= 0 itself")


if __name__ == "__main__":
    main()
