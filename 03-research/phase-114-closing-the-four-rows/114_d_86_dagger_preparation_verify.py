#!/usr/bin/env python3
"""Exact certificates for the D.86 dagger-preparation audit."""

from fractions import Fraction


def main():
    # Scalar Halmos angle lambda=9/25.
    lam = Fraction(9, 25)
    sqrt_lam = Fraction(3, 5)
    DT = Fraction(4, 5)

    # Krein pullback block Q*JQ.
    a = 4 * (1 - lam)
    b = -2 * DT * sqrt_lam
    d = Fraction(0)
    determinant = a * d - b * b
    assert a == Fraction(64, 25)
    assert b == Fraction(-24, 25)
    assert determinant == Fraction(-576, 625) < 0

    # Positive graph: differential residual zero, boundary nonzero.
    z = Fraction(1)
    p = sqrt_lam / (2 * DT)
    residual = 2 * DT * p - sqrt_lam * z
    boundary = sqrt_lam * z
    assert p == Fraction(3, 8)
    assert residual == 0
    assert boundary * boundary == Fraction(9, 25) > 0
    krein_energy = residual * residual - boundary * boundary
    hilbert_energy = residual * residual + boundary * boundary
    assert krein_energy < 0 < hilbert_energy

    # A finite prime+Gamma multiplier is negative at tau=0.
    # Use exact positive surrogates m0=5, log(p)=1, r=1/2.
    m0 = Fraction(5)
    logp = Fraction(1)
    r = Fraction(1, 2)
    one_minus_poisson_at_zero = -2 * r / (1 - r)
    delta_zero = -m0 + logp * one_minus_poisson_at_zero
    assert one_minus_poisson_at_zero == -2
    assert delta_zero == -7 < 0

    # Contact Gram and minimal scalar diagonal repair.
    ell = Fraction(2)
    contact_det = -ell * ell
    assert contact_det == -4
    # g=ell is enough, g=ell/2 is not; exact golden threshold lies between.
    g_small = ell / 2
    g_large = ell
    det_small = g_small * (g_small + ell) - ell * ell
    det_large = g_large * (g_large + ell) - ell * ell
    assert det_small < 0 < det_large

    print("D86 dagger-preparation certificates: PASS")
    print("Krein block determinant:", determinant)
    print("positive-graph Krein/Hilbert energies:", krein_energy, hilbert_energy)
    print("finite prime+Gamma central defect:", delta_zero)


if __name__ == "__main__":
    main()
