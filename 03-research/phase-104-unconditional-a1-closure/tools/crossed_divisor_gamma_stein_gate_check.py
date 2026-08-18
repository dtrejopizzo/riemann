#!/usr/bin/env python3
"""Exact checks for 104_45 (integers/Fraction only).

This is an algebraic checker.  It does not evaluate zeta, zeros, A1 or RH.
"""

from fractions import Fraction
from math import comb, factorial


def poly_eval(coeffs, x):
    out = Fraction(0)
    for c in reversed(coeffs):
        out = out * x + c
    return out


def poly_derivative(coeffs):
    return [Fraction(j) * coeffs[j] for j in range(1, len(coeffs))]


def laguerre(m, alpha, scale=Fraction(1)):
    """Coefficients of L_m^(alpha)(scale*x)."""
    return [
        Fraction((-1) ** j * comb(m + alpha, m - j), factorial(j))
        * scale**j
        for j in range(m + 1)
    ]


def oriented_segment_identity():
    tests = [
        (Fraction(7, 3), Fraction(2, 5)),
        (Fraction(1, 7), Fraction(9, 4)),
        (Fraction(5), Fraction(5)),
    ]
    polys = [
        [Fraction(3), Fraction(-2), Fraction(5, 7)],
        [Fraction(-1), Fraction(0), Fraction(4), Fraction(-3, 2)],
    ]
    for a, b in tests:
        for coeffs in polys:
            # Integral_b^a f'(x) dx, evaluated monomial by monomial.
            deriv = poly_derivative(coeffs)
            integral = sum(
                deriv[j] * (a ** (j + 1) - b ** (j + 1)) / (j + 1)
                for j in range(len(deriv))
            )
            assert integral == poly_eval(coeffs, a) - poly_eval(coeffs, b)


def laguerre_derivative_identity():
    scales = [Fraction(1), Fraction(3, 2), Fraction(7, 5)]
    for n in range(2, 31):
        for scale in scales:
            lhs = poly_derivative(laguerre(n - 1, 1, scale))
            rhs = [-scale * c for c in laguerre(n - 2, 2, scale)]
            assert lhs == rhs


def crossed_symbol_identity():
    # A is the intermediate selector/uniform symbol; it must cancel for
    # arbitrary values, not just for values coming from zeta.
    rows = [
        (Fraction(5, 3), Fraction(7, 4), Fraction(-2, 9), Fraction(11, 6)),
        (Fraction(13, 8), Fraction(3, 2), Fraction(1, 7), Fraction(19, 10)),
    ]
    for ell_shift, pole_shift, r0, a_mid in rows:
        selector = ell_shift - a_mid
        total = a_mid - r0 - pole_shift
        assert r0 + selector + total == ell_shift - pole_shift


def rational_sign_implications():
    gamma_lo = Fraction(1, 2)
    gamma_hi = Fraction(3, 5)
    log2_lo = Fraction(2, 3)
    log2_hi = Fraction(1)
    assert log2_lo - gamma_hi == Fraction(1, 15) > 0
    assert log2_hi / 2 - gamma_lo <= 0
    # The strict source bounds make the second implication strict.

    # Elementary rational certificates quoted in the text.
    h6 = sum(Fraction(1, k) for k in range(1, 7))
    exp_lower = sum(Fraction(39, 20) ** k / factorial(k) for k in range(7))
    assert exp_lower == Fraction(35844308849, 5120000000) > 7
    # Hence log(7)<39/20 and H_6-log(7)>1/2.
    assert h6 - Fraction(39, 20) == Fraction(1, 2)

    h25 = sum(Fraction(1, k) for k in range(1, 26))
    y = Fraction(12, 13)
    log25_lower = 2 * sum(y ** (2 * j + 1) / (2 * j + 1) for j in range(27))
    assert log25_lower > h25 - Fraction(3, 5)
    # Hence gamma < H_25-log(25) < 3/5.


def complete_monotonicity_obstruction():
    # Rigorous rational upper bound e < 68/25.  After k=7, successive
    # exponential-series terms have ratio at most 1/8.
    e_upper = sum(Fraction(1, factorial(k)) for k in range(7))
    e_upper += Fraction(8, 7 * factorial(7))
    assert e_upper == Fraction(31967, 11760) < Fraction(68, 25)

    # At j=32 and q=32/log(2), log(2)^33 cancels.  This exact integer
    # inequality proves that the m=2 atom alone exceeds 32!/q^33.
    assert 32**33 * 25**32 > 2 * factorial(32) * 68**32


def generalized_von_mangoldt_convolution():
    # Formal finite Dirichlet convolution: if b and Lambda satisfy
    # c = Lambda*b, then -Z' = (-Z'/Z)Z coefficientwise.  We check the
    # divisor indexing exactly on arbitrary rational data.
    limit = 40
    b = [Fraction(0)] + [Fraction((n % 7) + 1, (n % 5) + 1) for n in range(1, limit + 1)]
    lam = [Fraction(0)] + [Fraction((n % 11) - 3, (n % 4) + 1) for n in range(1, limit + 1)]
    lam[1] = Fraction(0)  # von Mangoldt-type convention
    for n in range(1, limit + 1):
        direct = sum(lam[d] * b[n // d] for d in range(1, n + 1) if n % d == 0)
        pairs = sum(lam[d] * b[k] for d in range(1, n + 1) for k in range(1, n + 1) if d * k == n)
        assert direct == pairs


def main():
    oriented_segment_identity()
    laguerre_derivative_identity()
    crossed_symbol_identity()
    rational_sign_implications()
    complete_monotonicity_obstruction()
    generalized_von_mangoldt_convolution()
    print("104_45 crossed divisor-Gamma Stein gate: exact checks passed")


if __name__ == "__main__":
    main()
