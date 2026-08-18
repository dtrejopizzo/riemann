#!/usr/bin/env python3
"""Exact checks for a75; contracted two-sided cut data remain open."""

from itertools import product
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


def signed_root(x):
    if x == 0:
        return 0
    return (1 if x > 0 else -1) * abs(x) ** 0.5


def signed_square(x):
    if x == 0:
        return 0
    return (1 if x > 0 else -1) * abs(x) ** 2


def add_twisted(values):
    return signed_square(sum(signed_root(value) for value in values))


# A unary path in either color is the identity; with all other leaves zero,
# every sign is recovered exactly.
for n in range(1, 11):
    for signs in product((-1, 1), repeat=n):
        recovered_ordinary = []
        recovered_twisted = []
        for i in range(n):
            inputs = [0] * n
            inputs[i] = signs[i]
            recovered_ordinary.append(sum(inputs))
            recovered_twisted.append(add_twisted(inputs))
        if tuple(recovered_ordinary) != signs or tuple(recovered_twisted) != signs:
            raise AssertionError(f"sign recovery n={n}, signs={signs}")
    check(f"all sign patterns recovered n={n}", True)


# Exact chain-rule support: a diagonal sign substitution multiplies each
# mixed derivative by eps_i eps_j, which is never zero.
x, y = sp.symbols("x y")
eps_x, eps_y = sp.symbols("eps_x eps_y", nonzero=True)
# SymPy's internal Subs dummy names are version-dependent; verify the robust
# coefficient statement directly by differentiating a generic polynomial.
a, b, c, d = sp.symbols("a b c d")
poly = a * x * y + b * x**2 * y + c * x * y**2 + d
substituted = poly.subs({x: eps_x * x, y: eps_y * y}, simultaneous=True)
lhs = sp.diff(substituted, x, y)
rhs = eps_x * eps_y * sp.diff(poly, x, y).subs(
    {x: eps_x * x, y: eps_y * y}, simultaneous=True
)
check("exact mixed-Hessian sign chain rule", sp.simplify(lhs - rhs) == 0)


# The graph support is invariant for every finite sign pattern because every
# edge multiplier is +/-1.
for n in range(2, 11):
    edges = tuple((i, j) for i in range(n) for j in range(i + 1, n))
    for signs in product((-1, 1), repeat=n):
        multipliers = tuple(signs[i] * signs[j] for i, j in edges)
        if any(value == 0 for value in multipliers):
            raise AssertionError(f"zero Hessian multiplier n={n}")
    check(f"Hessian support invariant for all signs n={n}", True)


doc = (HERE / "114_a_75_H7_SIGNED_READ_ONCE_PRIME_REGULARITY.md").read_text()
for marker in ("H7-RF-BICUT", "does not assert", "genuinely two-sided"):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: SIGNED READ-ONCE PRIME REGULARITY PASS; H7-RF-BICUT OPEN")
