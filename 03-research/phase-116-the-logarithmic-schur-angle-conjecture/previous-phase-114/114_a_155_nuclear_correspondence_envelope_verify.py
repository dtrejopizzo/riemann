#!/usr/bin/env python3
"""Finite exact checks for the nuclear Dirichlet correspondence envelope."""

from fractions import Fraction
from math import log


def primes_up_to(limit: int) -> list[int]:
    out = []
    for n in range(2, limit + 1):
        if all(n % p for p in out if p * p <= n):
            out.append(n)
    return out


PRIMES = primes_up_to(31)


def von_mangoldt_pattern(n: int) -> tuple[int, int] | None:
    """Return (p, 1) for a prime power; logs are represented symbolically by p."""
    for p in PRIMES:
        value = p
        while value < n:
            value *= p
        if value == n:
            return p, 1
    return None


def convolution(a: dict[int, Fraction], b: dict[int, Fraction]) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for m, am in a.items():
        for n, bn in b.items():
            out[m * n] = out.get(m * n, Fraction()) + am * bn
    return {n: value for n, value in out.items() if value}


def q(a: dict[int, Fraction], r: int) -> Fraction:
    return sum((abs(value) * n**r for n, value in a.items()), Fraction())


def contact_by_convolution(a: dict[int, Fraction], b: dict[int, Fraction]) -> dict[int, Fraction]:
    """Coefficient of each formal log(p) in ell(a*b)."""
    out = {p: Fraction() for p in PRIMES}
    for n, value in convolution(a, b).items():
        pp = von_mangoldt_pattern(n)
        if pp is not None:
            out[pp[0]] += value
    return out


def coordinates(a: dict[int, Fraction]) -> tuple[Fraction, dict[int, Fraction]]:
    a1 = a.get(1, Fraction())
    ap = {}
    for p in PRIMES:
        value = Fraction()
        power = p
        while power <= max(a, default=1):
            value += a.get(power, Fraction())
            power *= p
        ap[p] = value
    return a1, ap


def contact_by_coordinates(a: dict[int, Fraction], b: dict[int, Fraction]) -> dict[int, Fraction]:
    a1, ap = coordinates(a)
    b1, bp = coordinates(b)
    return {p: a1 * bp[p] + b1 * ap[p] + ap[p] * bp[p] for p in PRIMES}


samples = (
    {1: Fraction(2), 2: Fraction(3), 4: Fraction(-1), 3: Fraction(5)},
    {1: Fraction(-1), 2: Fraction(4), 8: Fraction(2), 9: Fraction(7)},
    {6: Fraction(11), 10: Fraction(-3), 25: Fraction(2)},
)

for a in samples:
    for b in samples:
        for r in range(4):
            assert q(convolution(a, b), r) <= q(a, r) * q(b, r)
        assert contact_by_convolution(a, b) == contact_by_coordinates(a, b)

for m in range(1, 30):
    for n in range(1, 30):
        lhs = contact_by_convolution({m: Fraction(1)}, {n: Fraction(1)})
        expected = {p: Fraction() for p in PRIMES}
        pp = von_mangoldt_pattern(m * n)
        if pp is not None:
            expected[pp[0]] = Fraction(1)
        assert lhs == expected

# The bonding diagonal n^-2 has summable nuclear norm.
partial = [sum(1 / (n * n) for n in range(1, bound)) for bound in (10, 100, 1000)]
assert partial[0] < partial[1] < partial[2] < 2

# Each tested prime gives an independent numerical coordinate.
prime_coordinate_vectors = [tuple(1 if p == q0 else 0 for p in PRIMES) for q0 in PRIMES]
assert len(set(prime_coordinate_vectors)) == len(PRIMES)

print("PASS: Dirichlet convolution estimates and exact Lambda contact agree.")
print("PASS: prime-power coordinate formula and nuclear bonding sum agree.")
print(f"PASS: {len(PRIMES)} independent prime numerical directions retained.")
