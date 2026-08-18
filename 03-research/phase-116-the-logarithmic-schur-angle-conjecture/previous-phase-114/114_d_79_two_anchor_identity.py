#!/usr/bin/env python3
"""Symbolic Loewner identity behind the D.79 two-anchor tail bound."""
import sympy as sp

B, b, C, x = sp.symbols("B b C x", positive=True)
m = lambda a: 2*x/(a*(a*a+x))
alpha = B**3*(C**2-b**2)/(b**3*(C**2-B**2))
beta = C**3*(b**2-B**2)/(b**3*(C**2-B**2))
difference = sp.factor(m(b)-alpha*m(B)-beta*m(C))
expected = sp.factor(
    -2*x**2*(-B+b)*(B+b)*(-C+b)*(C+b)
    / (b**3*(B**2+x)*(C**2+x)*(b**2+x))
)
assert sp.simplify(difference-expected) == 0
# If B<=b<=C, the two middle signed factors have opposite signs, so the
# displayed leading minus makes the full numerator nonnegative.
print("PASS exact two-anchor multiplier factorisation")
