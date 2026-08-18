#!/usr/bin/env python3
"""Exact finite certificates for D.129 Jordan ANOVA audit."""

from fractions import Fraction


def main() -> None:
    # Local two-point Jordan moments at x=2.
    x = Fraction(2)
    mean = x-1
    second = x*(x-1)
    variance = second-mean*mean
    assert variance == x-1 == 1

    # ANOVA coefficients indexed by subsets of three coordinates.
    chaos_norms = {
        (): Fraction(4),
        (0,): Fraction(2),
        (1,): Fraction(3),
        (2,): Fraction(5),
        (0, 1): Fraction(7),
        (0, 2): Fraction(11),
        (0, 1, 2): Fraction(13),
    }
    var = sum(v for s, v in chaos_norms.items() if s)
    es = sum(len(s)*v for s, v in chaos_norms.items() if s)
    assert var <= es

    # Equality on first chaos.
    first_var = sum(v for s, v in chaos_norms.items() if len(s) == 1)
    first_es = sum(len(s)*v for s, v in chaos_norms.items()
                   if len(s) == 1)
    assert first_var == first_es

    # Local physical landing is expansive.
    rho = Fraction(1, 2)
    landing_norm_squared = (1+rho)/(1-rho)
    assert landing_norm_squared == 3 > 1

    # A second-chaos variance t^2 needs t^{-1/2} amplitude to contribute at
    # order t, demonstrating loss of uniform boundedness.
    t = Fraction(1, 100)
    singular_amplitude_squared = 1/t
    assert singular_amplitude_squared*t*t == t

    print("D129 Jordan ANOVA/Efron-Stein certificates: PASS")
    print("variance / Efron-Stein energy:", var, es)
    print("first-chaos equality:", first_var, first_es)
    print("expansive landing norm squared:", landing_norm_squared)
    print("required second-chaos amplitude squared:", singular_amplitude_squared)


if __name__ == "__main__":
    main()
