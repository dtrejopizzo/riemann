#!/usr/bin/env python3
"""Exact bookkeeping checks for 104_25; no floating-point sign decisions."""

from fractions import Fraction


def q_coeff(a, m, u=Fraction(1)):
    conv = sum(Fraction(m - k + 1) * a[k] for k in range(m + 1))
    return (Fraction(m + 1) - conv) / u


def main():
    # Exact local-disk witness: R=1/2, N=4, a=0, M=6.
    radius = Fraction(1, 2)
    degree = 4
    amplitude = Fraction(6)
    coeffs = [Fraction(0)] * (degree + 1)
    coeffs[degree] = amplitude

    disk_bound = amplitude * radius**degree
    qn = q_coeff(coeffs, degree)

    assert disk_bound == Fraction(3, 8) <= 1
    assert qn == -1
    assert radius ** (-degree) == 16 > degree + 1

    # Direct convolution check for a nontrivial rational polynomial.
    test = [Fraction(1, 3), Fraction(2, 5), Fraction(-1, 7)]
    for m in range(len(test)):
        direct = q_coeff(test, m, Fraction(3, 2))
        sigma = sum(
            (Fraction(1) - Fraction(k, m + 1)) * test[k]
            for k in range(m + 1)
        )
        fejer_form = Fraction(m + 1, 1) * (1 - sigma) / Fraction(3, 2)
        assert direct == fejer_form

    print("PASS: exact coefficient/Fejer bookkeeping")
    print("PASS: R=1/2, Phi=6 z^4 has disk norm 3/8 but q_4=-1")
    print("No floating-point sign decision was used.")


if __name__ == "__main__":
    main()
