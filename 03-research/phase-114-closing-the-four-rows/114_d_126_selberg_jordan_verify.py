#!/usr/bin/env python3
"""Exact finite certificates for D.126 Selberg--Jordan capacity."""

import sympy as sp


def main() -> None:
    # Local Jordan moments for x=p^t: a0=1, ak=(x-1)x^(k-1).
    x = sp.Rational(2)
    moments = [sp.Integer(1)] + [(x-1)*x**(k-1) for k in range(1, 7)]
    hankel = sp.Matrix(3, 3, lambda i, j: moments[i+j])
    assert all(minor >= 0 for minor in (
        hankel[:1, :1].det(), hankel[:2, :2].det(), hankel.det()))

    # Shorting the unit gives a positive covariance on p,p^2.
    covariance = hankel[1:, 1:] - hankel[1:, :1]*hankel[:1, 1:]
    assert covariance.is_positive_semidefinite

    # First and second Taylor coefficients at a prime power.
    t, ell = sp.symbols('t ell', positive=True)
    j_pk = sp.exp(3*t*ell) - sp.exp(2*t*ell)  # p^3
    first = sp.diff(j_pk, t).subs(t, 0)
    second = sp.diff(j_pk, t, 2).subs(t, 0)
    assert sp.simplify(first - ell) == 0
    assert sp.simplify(second - 5*ell**2) == 0  # (2k-1)ell^2

    # At pq, first derivative vanishes and second is 2 logp logq.
    a, b = sp.symbols('a b', positive=True)
    j_pq = (sp.exp(t*a)-1)*(sp.exp(t*b)-1)
    assert sp.diff(j_pq, t).subs(t, 0) == 0
    assert sp.simplify(sp.diff(j_pq, t, 2).subs(t, 0)-2*a*b) == 0

    # Raw Selberg derivative at {1,p} is indefinite.
    raw = sp.Matrix([[0, ell**2], [ell**2, 3*ell**2]])
    assert sp.factor(raw.det()) == -ell**4

    print("D126 Selberg-Jordan capacity certificates: PASS")
    print("local Jordan Hankel/covariance PSD: exact")
    print("prime-power derivatives:", first, second)
    print("mixed-prime second derivative:", 2*a*b)
    print("raw second-order determinant:", sp.factor(raw.det()))


if __name__ == "__main__":
    main()
