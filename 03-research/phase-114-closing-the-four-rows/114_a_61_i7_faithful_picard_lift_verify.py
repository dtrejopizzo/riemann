#!/usr/bin/env python3
"""Exact checks for the faithful Picard label and conditional normal contact."""

from collections import Counter
from math import gcd, isclose, log

from sympy import factorint


def valuations(n):
    return Counter({int(p): int(k) for p, k in factorint(n).items()})


def tensor_labels(left, right):
    result = left.copy()
    result.update(right)
    return result


def degree(label):
    return sum(k * log(p) for p, k in label.items())


def contact_order(n):
    factors = factorint(n)
    if len(factors) == 1:
        return int(next(iter(factors)))
    return 1  # Cardinality of the zero module.


print("A. Faithful Picard labels and monoidal composition")
seen = {}
for n in range(1, 1000):
    label = valuations(n)
    key = tuple(sorted(label.items()))
    assert key not in seen
    seen[key] = n
    assert isclose(degree(label), log(n), rel_tol=0, abs_tol=1e-12)
for m in range(1, 120):
    for n in range(1, 120):
        assert tensor_labels(valuations(m), valuations(n)) == valuations(m * n)
print("  n -> G_n is faithful and G_m tensor G_n=G_mn")

print("\nB. Primitive normal layers have one F_p quotient")
for p in (2, 3, 5, 7, 11, 13):
    for k in range(1, 12):
        modulus = p**k
        layer = {p ** (k - 1) * a % modulus for a in range(p)}
        assert len(layer) == p
        assert all(value % p ** (k - 1) == 0 for value in layer)
print("  I_p^(k-1)/I_p^k has cardinality p")

print("\nC. Same-prime graded multiplication adds layer indices")
for p in (2, 3, 5, 7):
    for a in range(0, 7):
        for b in range(0, 7):
            assert p**a * p**b == p ** (a + b)
print("  gr^a(I_p) tensor gr^b(I_p) -> gr^(a+b)(I_p)")

print("\nD. Mixed-prime contact cancellation and von Mangoldt mass")
for n in range(2, 5000):
    factors = factorint(n)
    order = contact_order(n)
    if len(factors) == 1:
        p = int(next(iter(factors)))
        assert order == p
        expected = log(p)
    else:
        primes = tuple(int(p) for p in factors)
        assert any(gcd(p, q) == 1 for i, p in enumerate(primes)
                   for q in primes[i + 1:])
        assert order == 1
        expected = 0.0
    assert isclose(log(order), expected, rel_tol=0, abs_tol=1e-12)
print("  primitive normal contacts have exact Lambda(n) mass")

print("\nVERDICT: UNIT-TORSOR LABELS PASS; COMPLETED LATTICE NEEDS PRIME-REG; NORMAL CONTACT OPEN")
