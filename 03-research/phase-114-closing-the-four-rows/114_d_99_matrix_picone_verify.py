#!/usr/bin/env python3
"""Certificates for D.99 matrix Picone/total-positivity audit."""

from fractions import Fraction

import mpmath as mp


def mat_vec(a, v):
    return [sum(a[i][j] * v[j] for j in range(len(v)))
            for i in range(len(a))]


def det3(columns):
    a = [[columns[j][i] for j in range(3)] for i in range(3)]
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def main() -> None:
    # Prime jump ordered minor.
    prime_minor = Fraction(0) * 0 - Fraction(1) * 1
    assert prime_minor == -1

    # Tate span is not invariant in the minimal path model.
    lap = [
        [Fraction(1), Fraction(-1), Fraction(0)],
        [Fraction(-1), Fraction(2), Fraction(-1)],
        [Fraction(0), Fraction(-1), Fraction(1)],
    ]
    h_plus = [Fraction(1, 2), Fraction(1), Fraction(2)]
    h_minus = [Fraction(2), Fraction(1), Fraction(1, 2)]
    l_h_plus = mat_vec(lap, h_plus)
    invariant_det = det3([h_plus, h_minus, l_h_plus])
    assert l_h_plus == [Fraction(-1, 2), Fraction(-1, 2), Fraction(1)]
    assert invariant_det == Fraction(-21, 8) != 0

    # Gamma density has a negative ordered TP2 minor.
    mp.mp.dps = 50

    def w(r):
        return mp.e ** (-r / 2) / (1 - mp.e ** (-2 * r))

    radius = mp.mpf(2)
    eps = mp.mpf("0.25")
    gamma_minor = w(radius) ** 2 - w(radius - eps) * w(radius + eps)
    assert gamma_minor < 0

    # Direct strict log-convexity certificate.
    log_second = (
        4 * mp.e ** (-2 * radius) /
        (1 - mp.e ** (-2 * radius)) ** 2
    )
    assert log_second > 0

    print("D99 matrix Picone certificates: PASS")
    print("prime TP2 minor:", prime_minor)
    print("Tate-span invariance determinant:", invariant_det)
    print("Gamma TP2 minor:", gamma_minor)
    print("Gamma log-second derivative:", log_second)


if __name__ == "__main__":
    main()
