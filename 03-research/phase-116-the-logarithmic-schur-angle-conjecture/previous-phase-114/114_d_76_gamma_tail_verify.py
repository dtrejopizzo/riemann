#!/usr/bin/env python3
"""Exact symbolic checks for the D.76 Gamma-tail comparison."""

import sympy as sp

B, b, x = sp.symbols("B b x", positive=True)
e_b = 2*x/(b*(b**2+x))
e_B = 2*x/(B*(B**2+x))
difference = sp.factor(e_b/e_B-(B/b)**3)
expected = B*x*(b**2-B**2)/(b**3*(b**2+x))
assert sp.simplify(difference-expected) == 0

N = sp.symbols("N", nonnegative=True)
u = sp.symbols("u", real=True)
B_N = 2*N+sp.Rational(1, 2)
integral = sp.integrate((2*u+sp.Rational(1, 2))**-3, (u, N, sp.oo))
assert sp.simplify(integral-1/(4*B_N**2)) == 0
assert sp.simplify(B_N**3*integral-B_N/4) == 0

print("PASS E_b >= (B/b)^3 E_B for b>=B")
print("PASS complete Gamma tail >= (B/4) E_B")
