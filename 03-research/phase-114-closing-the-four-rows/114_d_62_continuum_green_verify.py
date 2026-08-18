#!/usr/bin/env python3
"""Symbolic checks for the D.62 continuum Green identity."""

import sympy as sp

x, y = sp.symbols("x y", real=True)

# Away from the diagonal the kernel solves the homogeneous equation.
k_plus = sp.exp(x / 2)
k_minus = sp.exp(-x / 2)
assert sp.simplify(sp.diff(k_plus, x, 2) - k_plus / 4) == 0
assert sp.simplify(sp.diff(k_minus, x, 2) - k_minus / 4) == 0

# Its first derivative jumps by one at zero, producing delta_0.
jump = sp.diff(k_plus, x).subs(x, 0) - sp.diff(k_minus, x).subs(x, 0)
assert jump == 1

# For x above/below the support, the two kernel branches factor through the
# corresponding Tate moments.
assert sp.simplify(sp.exp((x - y) / 2) - sp.exp(x / 2) * sp.exp(-y / 2)) == 0
assert sp.simplify(sp.exp((y - x) / 2) - sp.exp(-x / 2) * sp.exp(y / 2)) == 0

# Integration by parts has the strict negative-square coefficients.
tau = sp.symbols("tau", real=True)
green_symbol = -1 / (tau**2 + sp.Rational(1, 4))
assert green_symbol.subs(tau, 0) == -4
assert sp.limit(green_symbol, tau, sp.oo) == 0

print("PASS continuum kernel homogeneous equation and unit derivative jump")
print("PASS exterior branches factor through the two Tate moments")
print("PASS primitive Green symbol is strictly negative and noncoercive at high frequency")

