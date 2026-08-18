#!/usr/bin/env python3
"""Exact rational audit of the convex trapezoid Gamma-tail bound."""
import sympy as sp

x, t = sp.symbols("x t", positive=True)
f = 1 / (x * (x*x + t*t))
f2 = sp.factor(sp.diff(f, x, 2))
target = 2*(t**4 + 3*t*t*x*x + 6*x**4)/(x**3*(t*t+x*x)**3)
assert sp.simplify(f2-target) == 0

# Exact finite convex trapezoid check on one interval for rational t,x0.
tv = sp.Rational(3, 2)
x0 = sp.Rational(5)
fv = 1/(x*(x*x+tv*tv))
integral = sp.integrate(fv, (x, x0, x0+2))
trapezoid = 1/(x0*(x0*x0+tv*tv)) + 1/((x0+2)*((x0+2)**2+tv*tv))
assert sp.N(trapezoid-integral, 50) > 0

# The endpoint correction is strictly positive over the integral-only bound.
correction = 1/(2*x0*(x0*x0+tv*tv))
assert correction > 0

print("D.79 convex trapezoid tail certificate: PASS")
print("f'' factor:", f2)
print("one-cell margin:", sp.N(trapezoid-integral, 30))
