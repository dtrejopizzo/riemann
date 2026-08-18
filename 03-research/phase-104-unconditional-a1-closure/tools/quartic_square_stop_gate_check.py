#!/usr/bin/env python3
"""Exact arithmetic checks for 104_26; no floating-point sign decisions."""

from fractions import Fraction as F


def main():
    # (11 - 8 sqrt(2))/8 < 0 iff 11^2 < (8 sqrt(2))^2.
    assert 11 * 11 < 8 * 8 * 2

    # Minimal quartet witness: cosh(2 log 2)=17/8, cos(5pi/3)=1/2.
    quartet_lambda_2 = 4 - 4 * F(17, 8) * F(1, 2)
    assert quartet_lambda_2 == F(-1, 4)

    r_star = F(2002, 501)
    delta = 4 - r_star
    assert delta == F(2, 501)

    # D_r = (1001 D_4 - A)/1002, checked symbolically on rational probes.
    for lam, arch in [(F(7, 3), F(5, 2)), (F(-2, 7), F(11, 5))]:
        d4 = 4 * lam - arch
        dr = r_star * lam - arch
        assert dr == (1001 * d4 - arch) / 1002

    # n=150 phase: 150*(74/75)=148, an even integer.
    assert F(150 * 74, 75) == 148

    print("PASS: quartic PF2 radical sign certificate 121 < 128")
    print("PASS: exact quartet witness lambda_2 = -1/4")
    print("PASS: D_[r*] = (1001 D_[4] - A)/1002")
    print("PASS: n=150 off-line phase is 148*pi")
    print("No floating-point sign decision was used.")


if __name__ == "__main__":
    main()
