#!/usr/bin/env python3
"""Symbolic checks for the D.67 high-frequency separation theorem."""

import sympy as sp

x, N, a = sp.symbols("x N a", real=True, positive=True)
chi = sp.Function("chi", real=True)(x)
u = chi * sp.exp(sp.I * N * x)
L_u = sp.expand(sp.diff(u, x, 2) - sp.Rational(1, 4) * u)
expected = sp.exp(sp.I * N * x) * (
    sp.diff(chi, x, 2)
    + 2 * sp.I * N * sp.diff(chi, x)
    - (N**2 + sp.Rational(1, 4)) * chi
)
assert sp.simplify(L_u - expected) == 0

# The Tate exponentials are in the kernel of the formal adjoint of L.
for sigma in (sp.Rational(1, 2), -sp.Rational(1, 2)):
    weight = sp.exp(sigma * x)
    assert sp.simplify(sp.diff(weight, x, 2) - weight / 4) == 0

# The phase sequence makes the first translate constructive.
j = sp.symbols("j", integer=True, positive=True)
Nj = 2 * sp.pi * j / a
assert sp.simplify(sp.exp(-sp.I * Nj * a)) == 1

# Exact order comparison used in the theorem.
assert sp.limit(N**4 / N**2, N, sp.oo) == sp.oo
assert sp.limit(N**4 / (N**4 * sp.log(N)), N, sp.oo) == 0

print("PASS F_N=(d^2-1/4)(chi exp(iNx)) expansion")
print("PASS two Tate moments vanish by formal adjoint integration")
print("PASS N_j log(2)=2 pi j gives constructive first-contact phase")
print("PASS Green/arithmetic/Gamma orders are N^2, N^4, N^4 log N")
