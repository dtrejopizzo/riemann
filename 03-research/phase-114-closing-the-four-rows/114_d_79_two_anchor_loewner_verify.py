#!/usr/bin/env python3
"""Exact certificate for the D.79 two-anchor Gamma-tail lemma."""

import sympy as sp

B, b, C, x = sp.symbols("B b C x", positive=True)

alpha = B**3 * (C**2 - b**2) / (b**3 * (C**2 - B**2))
beta = C**3 * (b**2 - B**2) / (b**3 * (C**2 - B**2))

lhs = 1 / (b * (b**2 + x))
rhs = alpha / (B * (B**2 + x)) + beta / (C * (C**2 + x))
expected = x * (b**2 - B**2) * (C**2 - b**2) / (
    b**3 * (B**2 + x) * (b**2 + x) * (C**2 + x)
)

assert sp.factor(lhs - rhs - expected) == 0
assert sp.factor(alpha.subs(b, B) - 1) == 0
assert sp.factor(beta.subs(b, B)) == 0
assert sp.factor(alpha.subs(b, C)) == 0
assert sp.factor(beta.subs(b, C) - 1) == 0
assert sp.factor(1 / b**3 - alpha / B**3 - beta / C**3) == 0
assert sp.factor(1 / b - alpha / B - beta / C) == 0

# A rational interior specialization checks the strict sign without floats.
special = sp.factor(expected.subs({B: 2, b: 3, C: 5, x: 7}))
assert special > 0

print("D.79 two-anchor Gamma-tail Loewner certificate: PASS")
print("strict rational specialization:", special)
