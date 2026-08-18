#!/usr/bin/env python3
"""Exact check of the D.79 one-mode Feshbach formula."""

import sympy as sp

mu = sp.Rational(-1, 100)
g = sp.Rational(2, 1)
eps = sp.Rational(1, 50)

A = sp.Matrix([[mu, eps], [eps, g]])
disc = sp.sqrt((g - mu) ** 2 + 4 * eps**2)
lam_minus = (mu + g - disc) / 2
lam_plus = (mu + g + disc) / 2

char = sp.factor(A.charpoly().as_expr())
assert sp.simplify(char.subs(sp.Symbol("lambda"), lam_minus)) == 0
assert sp.simplify(char.subs(sp.Symbol("lambda"), lam_plus)) == 0
assert lam_minus < lam_plus

coarse = mu - eps**2 / (g - mu)
assert sp.simplify(lam_minus - coarse) >= 0

print("D.79 directed one-mode Feshbach certificate: PASS")
print("exact lower root:", lam_minus)
print("coarse lower bound:", coarse)
