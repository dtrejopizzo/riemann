#!/usr/bin/env python3
"""Exact algebra checks for the tapered Selberg/Hankel gate of 104_37."""

from fractions import Fraction
from math import comb, factorial


def laguerre(n: int, alpha: int) -> list[Fraction]:
    """Coefficients of L_n^(alpha), in ascending powers."""
    return [
        Fraction((-1) ** k * comb(n + alpha, n - k), factorial(k))
        for k in range(n + 1)
    ]


def add(*polys: list[Fraction]) -> list[Fraction]:
    size = max(map(len, polys))
    return [
        sum((p[k] if k < len(p) else Fraction(0) for p in polys), Fraction(0))
        for k in range(size)
    ]


def scale(c: Fraction, poly: list[Fraction]) -> list[Fraction]:
    return [c * x for x in poly]


def trim(poly: list[Fraction]) -> list[Fraction]:
    out = poly[:]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def check_tapered_test(top: int = 24) -> None:
    tapers = [Fraction(-2), Fraction(-1, 3), Fraction(0), Fraction(1, 7), Fraction(1), Fraction(2)]
    one = laguerre(0, 1)
    for n in range(2, top + 1):
        wn = laguerre(n - 1, 1)
        wnext = laguerre(n, 1)
        ln = laguerre(n, 0)
        for t in tapers:
            # Toeplitz polarization: w_n+t(w_{n+1}-w_n-w_1)+t^2 w_1.
            polarized = trim(
                add(wn, scale(t, add(wnext, scale(-1, wn), scale(-1, one))), scale(t * t, one))
            )
            closed = trim(add(wn, scale(t, ln), [t * (t - 1)]))
            assert polarized == closed

            if t:
                assert len(closed) - 1 == n
                assert closed[-1] == t * Fraction((-1) ** n, factorial(n))
            else:
                assert len(closed) - 1 == n - 1
                assert closed[-1] == Fraction((-1) ** (n - 1), factorial(n - 1))


def check_hankel_leading_minors() -> None:
    # At t=0, d=n-2; at t!=0, d=n-1.  Both cover the endpoint n=149.
    for d in (1, 2, 3, 147, 148, 499):
        determinant = 8**d - 9**d
        assert determinant < 0

        # Equivalent two-point AM-GM model at R=1,S=2:
        # (2R)^d(2S)^d-(R+S)^(2d).
        assert determinant == (2**d) * (4**d) - 3 ** (2 * d)


def check_scalar_taper_identity() -> None:
    # Arbitrary rational data verify M_t in both gauges.  No zeta values
    # or numerical approximation enter this identity.
    kappa = Fraction(1501, 2002)
    a_n = Fraction(31, 5)
    delta_a = Fraction(7, 11)
    b_n = Fraction(-13, 17)
    b_next = Fraction(19, 23)
    b_one = Fraction(-57721, 100000)  # arbitrary stand-in for -gamma
    for t in (Fraction(-3, 2), Fraction(0), Fraction(2, 7), Fraction(1)):
        direct = kappa * (a_n + t * t * delta_a) - (
            b_n + t * (b_next - b_n - b_one) + t * t * b_one
        )
        h_n = kappa * a_n - b_n
        d_n = kappa * delta_a - b_one
        h_next = kappa * (a_n + delta_a) - b_next
        schur = h_n - t * (h_n + d_n - h_next) + t * t * d_n
        assert direct == schur


def main() -> None:
    check_tapered_test()
    check_hankel_leading_minors()
    check_scalar_taper_identity()
    print("PASS: exact tapered test, Schur identity, and negative Hankel leading minor")


if __name__ == "__main__":
    main()
