#!/usr/bin/env python3
"""Exact finite verification of the Clifford mixed-contact identity."""

import sympy as sp


def kron(a, b):
    return sp.kronecker_product(a, b)


# Divisor basis: 1, 2, 3, 6.
n2 = sp.Matrix(
    [
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
    ]
)
n3 = sp.Matrix(
    [
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
)
a2 = n2 + n2.T
a3 = n3 + n3.T

# Real self-adjoint Clifford generators in dimension two.
g2 = sp.Matrix([[0, 1], [1, 0]])
g3 = sp.Matrix([[1, 0], [0, -1]])
i2 = sp.eye(2)

assert g2 * g2 == i2
assert g3 * g3 == i2
assert g2 * g3 + g3 * g2 == sp.zeros(2)
assert a2 * a3 == a3 * a2

# Use algebraically independent weights x,y; the identity is polynomial.
x, y = sp.symbols("x y", real=True)
dirac = x * kron(a2, g2) + y * kron(a3, g3)
expected = x**2 * kron(a2 * a2, i2) + y**2 * kron(a3 * a3, i2)
assert sp.simplify(dirac * dirac - expected) == sp.zeros(8)


def clifford_partial_trace(matrix, gamma):
    """(id tensor normalized trace)((1 tensor gamma) matrix)."""
    out = sp.zeros(4)
    twisted = kron(sp.eye(4), gamma) * matrix
    for i in range(4):
        for j in range(4):
            block = twisted[2 * i : 2 * i + 2, 2 * j : 2 * j + 2]
            out[i, j] = sp.trace(block) / 2
    return sp.simplify(out)


assert clifford_partial_trace(dirac, g2) == x * a2
assert clifford_partial_trace(dirac, g3) == y * a3

print("PASS: cross-prime Clifford curvature cancels exactly.")
print("PASS: both prime currents survive as Clifford coefficients.")

