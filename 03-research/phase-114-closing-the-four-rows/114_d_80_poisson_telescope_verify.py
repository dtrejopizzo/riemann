#!/usr/bin/env python3
"""Exact scalar certificates for the D.80 Poisson/Schur telescopes."""

from fractions import Fraction


def main():
    # Choose R=2 log 2.  Then cosh(R/2)=5/4 and eta=4/5.
    eta = Fraction(4, 5)

    # Tate characters of A_R: (2/5)(2+1/2)=1.
    chi_plus = Fraction(2, 5) * (Fraction(2) + Fraction(1, 2))
    chi_minus = chi_plus
    assert chi_plus == chi_minus == 1
    assert 1 - chi_plus == 0  # E_R is primitive.

    # Linear telescope 1=sum_{j<N}(1-a)a^j+a^N.
    for a in (Fraction(-2, 5), Fraction(1, 3), Fraction(4, 5)):
        for n in (1, 2, 5, 12):
            bulk = sum((1 - a) * a ** j for j in range(n))
            assert bulk + a ** n == 1

    # Gamma graph contraction.
    gamma_bounds = [eta ** (2 * n) for n in range(1, 8)]
    assert all(gamma_bounds[j + 1] < gamma_bounds[j]
               for j in range(len(gamma_bounds) - 1))

    # Scalar angle telescope and exact Schur residual.
    lambdas = (Fraction(1, 5), Fraction(1, 2), Fraction(4, 5))
    for lam in lambdas:
        schur = lam / 4
        for n in (1, 2, 5, 10):
            layers = sum((lam ** j) * (1 - lam) / 4
                         for j in range(1, n + 1))
            residual = lam ** (n + 1) / 4
            assert layers + residual == schur

    # A finite trace-class model: every eigenvalue is <1, so Tr(C^N)->0.
    eig = (Fraction(1, 2), Fraction(1, 3), Fraction(1, 5), Fraction(1, 7))
    trace_powers = [sum(x ** n for x in eig) for n in range(1, 10)]
    assert all(trace_powers[j + 1] < trace_powers[j]
               for j in range(len(trace_powers) - 1))
    assert trace_powers[-1] < Fraction(1, 250)

    print("D80 primitive Poisson/Schur telescope certificates: PASS")
    print("Gamma residual bounds:", gamma_bounds)
    print("finite trace powers first/last:", trace_powers[0], trace_powers[-1])


if __name__ == "__main__":
    main()
