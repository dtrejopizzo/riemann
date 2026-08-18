#!/usr/bin/env python3
"""Exact and numerical checks for the D.159 endpoint-flat tail theorem."""

from fractions import Fraction
import math


def derivative(poly: list[Fraction]) -> list[Fraction]:
    return [Fraction(k) * poly[k] for k in range(1, len(poly))]


def multiply(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


m = 20
factor = [Fraction(1)]
for _ in range(m):
    factor = multiply(factor, [Fraction(1), Fraction(0), Fraction(-1)])

q = [Fraction(3), Fraction(-2), Fraction(5), Fraction(1)]
f = multiply(factor, q)
current = f
for r in range(m):
    at_plus = sum(current, Fraction(0))
    at_minus = sum((c * ((-1) ** k) for k, c in enumerate(current)), Fraction(0))
    assert at_plus == 0 and at_minus == 0, r
    current = derivative(current)

assert 170 - 2 * m - 2 == 128


def integral_closed(a: int, j: int, r: float) -> float:
    ell = math.log(r) + 5.0
    return r ** (1 - a) * sum(
        math.comb(j, k) * ell ** (j - k) * math.factorial(k) / (a - 1) ** (k + 1)
        for k in range(j + 1)
    )


# Differentiate the right side numerically: its negative derivative is the
# integrand, which certifies the elementary antiderivative formula.
for j in range(5):
    r = 231.0
    h = 1.0e-3
    deriv = (integral_closed(2 * m, j, r + h) - integral_closed(2 * m, j, r - h)) / (2 * h)
    expected = -(math.log(r) + 5) ** j / r ** (2 * m)
    assert abs(deriv - expected) <= 2.0e-8 * max(abs(expected), 1.0e-300)

# Floating scale quoted in the note; the directed script will replace this
# diagnostic norm by an Arb upper endpoint.
t = 0.5 * math.log(5)
norm2 = 10 ** 111.30307634368016
bound_j4 = 2 * t * norm2 / math.pi * integral_closed(40, 4, 4096.0)
assert bound_j4 < 1.1e-27

print("D159 endpoint-flat dimension, jets, and Fourier tail: PASS")
print(f"floating j=4 tail scale at R=4096 = {bound_j4:.6e}")
