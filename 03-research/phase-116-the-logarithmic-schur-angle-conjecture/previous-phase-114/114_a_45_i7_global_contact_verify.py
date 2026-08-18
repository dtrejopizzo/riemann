#!/usr/bin/env python3
"""Checks for the global primitive contact module system P_n."""

from math import gcd, isclose, log

from sympy import factorint


def contact_modulus(n):
    """None denotes Z; integer d denotes Z/d, so d=1 is the zero module."""
    if n == 1:
        return None
    factors = factorint(n)
    if len(factors) != 1:
        return 1
    return next(iter(factors))


def tensor_modulus(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return gcd(a, b)


print("A. Tensor composition P_m tensor P_n = P_mn")
for m in range(1, 501):
    for n in range(1, 301):
        left = tensor_modulus(contact_modulus(m), contact_modulus(n))
        right = contact_modulus(m * n)
        assert left == right
print("  all labels m<=500, n<=300 compose correctly")

print("\nB. Contact mass equals von Mangoldt")
for n in range(2, 5001):
    factors = factorint(n)
    modulus = contact_modulus(n)
    mass = log(modulus)
    expected = log(next(iter(factors))) if len(factors) == 1 else 0.0
    assert isclose(mass, expected)
print("  log #P_n=Lambda(n) for 2<=n<=5000")

print("\nC. Tensor associativity and symmetry")
labels = [contact_modulus(n) for n in range(1, 80)]
for a in labels:
    for b in labels:
        assert tensor_modulus(a, b) == tensor_modulus(b, a)
        for c in labels:
            left = tensor_modulus(tensor_modulus(a, b), c)
            right = tensor_modulus(a, tensor_modulus(b, c))
            assert left == right
print("  finite contact labels form a symmetric monoidal system")

print("\nVERDICT: I7 GLOBAL PRIMITIVE CONTACT SYSTEM CHECKS PASS")
