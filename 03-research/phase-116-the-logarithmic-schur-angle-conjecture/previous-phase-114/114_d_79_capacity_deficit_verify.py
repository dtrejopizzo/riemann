#!/usr/bin/env python3
"""Exact rational audit of the D.79 positive-deficit capacity formula."""

from fractions import Fraction

g = Fraction(1, 5000)
ell = Fraction(7, 4_000_000)  # 1.75e-6
delta = Fraction(46, 1)       # safely above the exact threshold

a = 1 / g - delta
capacity_direct = 1 / a - g
capacity_deficit = g * g * delta / (1 - g * delta)
threshold = ell / (g * (g + ell))

assert capacity_direct == capacity_deficit
assert delta > threshold
assert capacity_deficit > ell
assert 0 < g * delta < 1

print("D.79 capacity-deficit certificate: PASS")
print("threshold:", threshold)
print("capacity:", capacity_deficit)
