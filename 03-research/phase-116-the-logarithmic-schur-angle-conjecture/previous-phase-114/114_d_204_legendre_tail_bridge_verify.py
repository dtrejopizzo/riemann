#!/usr/bin/env python3
"""Exact arithmetic audit of the m=20 Legendre-tail coefficient.

This checks the coefficient multiplying the weighted derivative integral
and the derivative budget left by a chosen capacity allowance.  It does not
evaluate that derivative integral.
"""
from fractions import Fraction
from math import factorial
from decimal import Decimal


def coefficient(N: int, m: int) -> Fraction:
    return Fraction(factorial(N - m), factorial(N + m))


m = 20
c230 = coefficient(230, m)
c260 = coefficient(260, m)
assert 3.273e-95 < float(c230) < 3.274e-95
assert 2.425e-97 < float(c260) < 2.426e-97

allowance = Fraction(1, 20)  # 0.05
budget230 = allowance / c230
budget260 = allowance / c260
assert float(budget230) > 1.52e93
assert float(budget260) > 2.06e95

# Directed primitive-graph enclosure from the full complement audit.
eta_upper = Decimal("6.58e-505")
assert eta_upper < Decimal("1e-500")

print("D204 Legendre-tail bridge arithmetic: PASS")
print("c_230,20 =", float(c230))
print("c_260,20 =", float(c260))
print("0.05 derivative budgets =", float(budget230), float(budget260))
print("remaining obligation: directed weighted twentieth-derivative trace")
