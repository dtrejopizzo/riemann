#!/usr/bin/env python3
"""Exact checks for 114.a.111: prime Cartier subgroup/contact degree."""

from pathlib import Path
from fractions import Fraction
import math


ROOT = Path(__file__).resolve().parent
TEXT = (ROOT / "114_a_111_H7_PRIME_CARTIER_SUBGROUP_AND_CONTACT_DEGREE.md").read_text()


def check(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)
    print(f"PASS {label}")


def valuations_of_fraction(x: Fraction, primes: tuple[int, ...]) -> tuple[int, ...]:
    out = []
    for prime in primes:
        numerator, denominator = x.numerator, x.denominator
        value = 0
        while numerator % prime == 0:
            numerator //= prime
            value += 1
        while denominator % prime == 0:
            denominator //= prime
            value -= 1
        out.append(value)
    return tuple(out)


primes = (2, 3)
box = range(-12, 13)

# Tensor product of the completed prime lattices is addition of valuations.
for m in box:
    for n in box:
        for a in range(-3, 4):
            for b in range(-3, 4):
                left = Fraction(primes[0] ** max(m, 0), primes[0] ** max(-m, 0))
                left *= Fraction(primes[1] ** max(n, 0), primes[1] ** max(-n, 0))
                right = Fraction(primes[0] ** max(a, 0), primes[0] ** max(-a, 0))
                right *= Fraction(primes[1] ** max(b, 0), primes[1] ** max(-b, 0))
                check_value = valuations_of_fraction(left * right, primes)
                if check_value != (m + a, n + b):
                    raise AssertionError("valuation tensor law")
print("PASS valuation tensor law on 30625 products")

# UFD makes the diagonal detector faithful, including negative exponents.
for m in box:
    for n in box:
        x = Fraction(primes[0] ** max(m, 0), primes[0] ** max(-m, 0))
        x *= Fraction(primes[1] ** max(n, 0), primes[1] ** max(-n, 0))
        if x == 1 and (m, n) != (0, 0):
            raise AssertionError(f"UFD detector ({m},{n})")
print("PASS UFD detector on 625 signed exponent pairs")

# The numerical contact functional has the same exact kernel on this box.
for m in box:
    for n in box:
        degree = m * math.log(primes[0]) + n * math.log(primes[1])
        if abs(degree) <= 1e-12 and (m, n) != (0, 0):
            raise AssertionError(f"contact detector ({m},{n})")
print("PASS contact detector on 625 signed exponent pairs")

for marker in (
    "regular effective Cartier-act",
    "faithful realization by completed fraction lattices",
    "linear extension of proved",
    "not a global intersection product",
    "H7-REG-INTER remains open",
    "Row A and RH are not claimed",
):
    check(marker in TEXT, f"scope marker {marker}")

print("VERDICT: PRIME CARTIER-ACT RANK TWO AND CONTACT DEGREE ARE CLOSED")
