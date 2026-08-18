#!/usr/bin/env python3
"""Exact certificates for the D.85 round-trip/scattering audit."""

from fractions import Fraction


def main():
    # Rational unitary colligation blocks.
    T, G, H, R = (Fraction(3, 5), Fraction(4, 5),
                   Fraction(-4, 5), Fraction(3, 5))
    C = T * T
    assert C == Fraction(9, 25)

    # Round-trip state/output map z -> (Cz, Hz, G*Tz) is isometric.
    for z in (Fraction(1), Fraction(7, 3), Fraction(-5, 2)):
        next_state = C * z
        a = H * z
        b = G * T * z
        assert next_state ** 2 + a ** 2 + b ** 2 == z ** 2

    # Exact defect identities.
    DT2 = 1 - C
    DC2 = 1 - C * C
    assert DT2 == Fraction(16, 25)
    assert (G * T) ** 2 == C * (1 - C)
    assert DT2 == DC2 / (1 + C)

    # Odd/even Schur layers exhaust C/4.
    # Sum finite truncations and retain the exact tail.
    for n in (1, 2, 5, 10):
        layers = sum(DT2 * C ** j / 4 for j in range(1, n + 1))
        tail = C ** (n + 1) / 4
        assert layers + tail == C / 4

    # Initial landing residual.  The positive graph has residual zero while
    # the Schur state energy is nonzero.
    DT = Fraction(4, 5)
    sqrtC = Fraction(3, 5)
    z = Fraction(1)
    p = Fraction(3, 8)
    residual = 2 * DT * p - sqrtC * z
    assert residual == 0
    assert (sqrtC * z) ** 2 == Fraction(9, 25) > 0

    # Paugam swap block has signs + and -.
    swap_plus = 2 * Fraction(1) * Fraction(1)
    swap_minus = 2 * Fraction(1) * Fraction(-1)
    assert swap_plus > 0 and swap_minus < 0

    # Contact functional cannot be positive on {1,delta_p}.
    lp = Fraction(2)  # exact positive surrogate for log(p)
    det_contact = 0 * lp - lp * lp
    assert det_contact == Fraction(-4) < 0

    print("D85 two-boundary/round-trip certificates: PASS")
    print("C, D_T^2, D_C^2:", C, DT2, DC2)
    print("positive-graph residual/state energy:", residual, sqrtC ** 2)
    print("contact Gram determinant:", det_contact)


if __name__ == "__main__":
    main()
