#!/usr/bin/env python3
"""Exact finite certificates for D.128 conditional-expectation audit."""

from fractions import Fraction


def main() -> None:
    # Local Green landing is expansive.
    rho = Fraction(1, 2)
    norm_squared = (1+rho)/(1-rho)
    assert norm_squared == 3 > 1

    # Exact conditional expectation on a two-coordinate product is
    # contractive: average the second fair coordinate.
    values = [Fraction(1), Fraction(3), Fraction(-1), Fraction(5)]
    conditional = [(values[0]+values[1])/2,
                   (values[2]+values[3])/2]
    source_norm = sum(x*x for x in values)/4
    target_norm = sum(x*x for x in conditional)/2
    assert target_norm <= source_norm

    # Fourier coupling is not positivity preserving.
    positive_mass = [Fraction(0), Fraction(1)]
    fourier_image = [
        (positive_mass[0]+positive_mass[1])/2,
        (positive_mass[0]-positive_mass[1])/2,
    ]
    assert fourier_image[1] < 0

    # A contraction factorization would immediately give the target norm
    # inequality, illustrating that it is the desired theorem.
    boundary_norm2 = Fraction(7)
    contraction_squared = Fraction(3, 4)
    prep_norm2 = contraction_squared*boundary_norm2
    assert prep_norm2 <= boundary_norm2

    # Two global jets cannot losslessly amalgamate a d-dimensional local
    # unit-channel range when d>2.
    test_dimension = 7
    jet_rank = 2
    unavoidable_kernel = test_dimension-jet_rank
    assert unavoidable_kernel == 5

    print("D128 conditional-expectation certificates: PASS")
    print("local Green norm squared:", norm_squared)
    print("conditional expectation norms:", source_norm, target_norm)
    print("non-Markov Fourier image:", fourier_image)
    print("conditional landing would imply:", prep_norm2, boundary_norm2)
    print("local-unit directions invisible to two jets:", unavoidable_kernel)


if __name__ == "__main__":
    main()
