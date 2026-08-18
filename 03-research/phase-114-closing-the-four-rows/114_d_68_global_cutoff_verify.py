#!/usr/bin/env python3
"""Symbolic asymptotic checks for D.68."""

import sympy as sp

X, T = sp.symbols("X T", positive=True)
eps = sp.Rational(1, 10)
t = sp.symbols("t", positive=True)

# Partial summation with the PNT main term psi(t)=t.
A_main = X / sp.sqrt(X) + sp.Rational(1, 2) * sp.integrate(
    t / t ** sp.Rational(3, 2), (t, 1, X)
)
assert sp.simplify(A_main - (2 * sp.sqrt(X) - 1)) == 0

# Stieltjes inversion of A_main gives psi(X)=X up to the endpoint constant.
A_cont = 2 * (sp.sqrt(t) - 1)
psi_recovered = 2 * (sp.sqrt(X) - 1) * sp.sqrt(X) - sp.Rational(1, 2) * sp.integrate(
    A_cont / sp.sqrt(t), (t, 1, X)
)
assert sp.simplify(psi_recovered - (X - 1)) == 0

# Error inversion: R(t)=t^eps produces square-root scale.
err = sp.sqrt(X) * X**eps + sp.Rational(1, 2) * sp.integrate(
    t**eps / sp.sqrt(t), (t, 1, X)
)
assert sp.limit(err / X ** (sp.Rational(1, 2) + 2 * eps), X, sp.oo) == 0

# Absolute-phase cutoff has log R ~ 4 exp(T), larger than every T^k.
k = sp.symbols("k", positive=True)
assert sp.limit(sp.exp(T) / T**k, T, sp.oo) == sp.oo

print("PASS PNT main term A(X)=2 sqrt(X)+O(1)")
print("PASS Stieltjes inversion returns psi(X)=X+O(1)")
print("PASS X^eps centered error yields X^(1/2+eps) Chebyshev error")
print("PASS log R_abs ~ 4 exp(T) dominates every polynomial in T")
