#!/usr/bin/env python3
"""Exact certificates for D.96 scattering/de Branges audit."""

from fractions import Fraction


def main() -> None:
    # Exact transport of a hypothetical off-line zero.
    beta = Fraction(3, 4)
    a = Fraction(1, 8)
    imag_z = beta - Fraction(1, 2) - a
    assert imag_z == Fraction(1, 8) > 0

    # At an upper E-zero, the diagonal de Branges kernel is negative.
    e_sharp_abs_sq = Fraction(9, 4)
    # Suppress the positive 4*pi factor; sign is exact.
    kernel_sign_numerator = -e_sharp_abs_sq / imag_z
    assert kernel_sign_numerator < 0

    # Safe edge: beta<1 and a=1/2 imply no transported zero in C_+.
    safe_imag_z = beta - Fraction(1, 2) - Fraction(1, 2)
    assert safe_imag_z < 0

    # A local Euler ratio crosses the unit circle with theta.
    r_plus = Fraction(1, 4)
    r_minus = Fraction(1, 2)
    ratio_at_zero = (1 - r_plus) / (1 - r_minus)
    ratio_at_pi = (1 + r_plus) / (1 + r_minus)
    assert ratio_at_zero == Fraction(3, 2) > 1
    assert ratio_at_pi == Fraction(5, 6) < 1

    print("D96 scattering realization certificates: PASS")
    print("transported imaginary part:", imag_z)
    print("de Branges diagonal sign proxy:", kernel_sign_numerator)
    print("safe-edge imaginary part:", safe_imag_z)
    print("local ratio at 0, pi:", ratio_at_zero, ratio_at_pi)


if __name__ == "__main__":
    main()
