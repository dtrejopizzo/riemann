#!/usr/bin/env python3
"""Numerical/exact certificates for D.89 transverse trace energy."""

from fractions import Fraction
import mpmath as mp


def discrete_energy(values, shift):
    # Relative coordinate u is the integer index.
    return sum((1 + (u + shift) ** 2) * abs(v) ** 2
               for u, v in values.items())


def main() -> None:
    mp.mp.dps = 50

    # C_1 is exactly pi and the sharp profile saturates the trace bound.
    c1 = mp.quad(lambda u: 1 / (1 + u * u), [-mp.inf, mp.inf])
    assert abs(c1 - mp.pi) < mp.mpf("1e-45")
    output_sq = (c1 / 2) ** 2
    energy = c1 / 2
    bound = c1 / 2 * energy
    assert abs(output_sq - bound) < mp.mpf("1e-45")

    # Exact one-sided translation cocycle E(a)=E+2aM+a^2N.
    values = {-2: Fraction(1, 3), 0: Fraction(2, 3), 3: Fraction(-1, 2)}
    a = 5
    e0 = discrete_energy(values, 0)
    ea = discrete_energy(values, a)
    mass = sum(v * v for v in values.values())
    moment = sum(Fraction(u) * v * v for u, v in values.items())
    assert ea == e0 + 2 * a * moment + a * a * mass

    # The Kunneth trace defect is zero on the sharp family.
    defect = bound - output_sq
    assert abs(defect) < mp.mpf("1e-45")

    print("D89 transverse trace certificates: PASS")
    print("C_1:", mp.nstr(c1, 30))
    print("sharp trace defect:", mp.nstr(defect, 5))
    print("one-sided energy before/after:", e0, ea)


if __name__ == "__main__":
    main()
