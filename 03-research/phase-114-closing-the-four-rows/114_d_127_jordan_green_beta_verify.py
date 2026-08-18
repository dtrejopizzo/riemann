#!/usr/bin/env python3
"""Exact certificates for D.127 Jordan--Green--beta construction."""

from fractions import Fraction
import sympy as sp


def main() -> None:
    rho = Fraction(1, 2)
    contact = Fraction(3)
    size = 4
    green = [[rho**abs(i-j) for j in range(size)] for i in range(size)]
    completed = [[contact*green[i][j] for j in range(size)]
                 for i in range(size)]
    assert sp.Matrix(green).is_positive_definite
    assert sp.Matrix(completed).is_positive_definite
    assert completed[0][3] == contact*rho**3

    t, s = sp.symbols('t s')
    log_ratio = ((t/2)*sp.log(sp.pi)
                 + sp.loggamma((s-t)/2)-sp.loggamma(s/2))
    derivative = sp.diff(log_ratio, t).subs(t, 0)
    expected = (sp.log(sp.pi)-sp.polygamma(0, s/2))/2
    assert sp.simplify(derivative-expected) == 0

    polar = sp.diff(
        sp.log((s-t)*(s-t-1)/(s*(s-1))), t).subs(t, 0)
    assert sp.simplify(polar+1/s+1/(s-1)) == 0

    prep_energy = Fraction(5)
    boundary_energy = Fraction(4)
    assert prep_energy > 0 and boundary_energy > 0
    assert not prep_energy <= boundary_energy

    print("D127 Jordan-Green-beta certificates: PASS")
    print("completed prime depth corner:", completed[0][3])
    print("Gamma derivative:", derivative)
    print("polar derivative:", polar)
    print("positive factors do not force contraction:",
          prep_energy, boundary_energy)


if __name__ == "__main__":
    main()
