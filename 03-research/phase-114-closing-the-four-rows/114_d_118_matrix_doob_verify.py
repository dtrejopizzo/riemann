#!/usr/bin/env python3
"""Exact algebraic certificates for D.118 matrix Doob audit."""

from fractions import Fraction


def main() -> None:
    # q=e^{a/2}; q=2 is an exact toy central torsor.
    q = Fraction(2)
    eigenvalue = 2 - q - 1 / q
    compensation = -eigenvalue
    assert eigenvalue == Fraction(-1, 2)
    assert compensation == Fraction(1, 2) > 0

    # Conjugated Markov coefficients and zero row sum.
    forward = 1 / q
    backward = q
    diagonal = q + 1 / q
    assert diagonal - forward - backward == 0

    # Source central rate w=Lambda/sqrt(n), q=sqrt(n).  Symbolically choose
    # Lambda=7 and n=q^2=4: the two rates are Lambda/n and Lambda.
    contact = Fraction(7)
    n = q * q
    central = contact / q
    oriented_low = central / q
    oriented_high = central * q
    assert oriented_low == contact / n
    assert oriented_high == contact

    # The forced Doob killing is Lambda(1+1/n-2/sqrt(n)).
    doob_killing = central * (q + 1 / q - 2)
    expected = contact * (1 + 1 / n - 2 / q)
    assert doob_killing == expected == Fraction(7, 4)

    # It proves L >= -C, not the desired L >= +m.
    desired_mass = 2 * central
    assert -doob_killing < 0 < desired_mass

    # At the Gamma jet, the large-r integrand has exact limit one after
    # writing x=e^{-r/2}: 2*x/(1-x^4)*(cosh(r/2)-1)
    # = (1-x)^2/(1-x^4), whose limit at x=0 is 1.
    def gamma_compensation_integrand(x: Fraction) -> Fraction:
        return (1 - x) ** 2 / (1 - x**4)

    values = [gamma_compensation_integrand(Fraction(1, 2**k))
              for k in range(1, 8)]
    assert all(0 < value < 1 for value in values)
    assert values[-1] > Fraction(49, 50)

    print("D118 matrix Doob/Tate-jet certificates: PASS")
    print("jet eigenvalue/forced compensation:", eigenvalue, compensation)
    print("oriented source rates:", oriented_low, oriented_high)
    print("Doob versus desired sign:", doob_killing, desired_mass)
    print("Gamma compensation integrand tends to one:", values[-1])


if __name__ == "__main__":
    main()
