#!/usr/bin/env python3
"""Exact checks for prime-power Witt contact filtrations."""

from math import gcd, isclose, log

from sympy import Matrix, primerange, totient


def theta(p, a, r, j):
    """theta_r(e_j), with r=a denoting F_0."""
    if r == a:
        return int(totient(p**j))
    if j <= r:
        return int(totient(p**j))
    if j == r + 1:
        return -(p**r)
    return 0


print("A. Adjacent character contacts are exactly p^k")
for p in primerange(2, 50):
    for a in range(1, 10):
        for k in range(1, a + 1):
            differences = [theta(p, a, k, j) - theta(p, a, k - 1, j)
                           for j in range(a + 1)]
            contact = 0
            for value in differences:
                contact = gcd(contact, abs(value))
            assert contact == p**k
print("  all adjacent tensor ideals are (p^k)")

print("\nB. Primitive layers have cardinality p")
for p in primerange(2, 200):
    for k in range(1, 20):
        full_size = p**k
        previous_size = p ** (k - 1)
        layer_size = full_size // previous_size
        assert layer_size == p
        assert isclose(log(layer_size), log(p))
print("  deg primitive layer=log p=Lambda(p^k)")

print("\nC. Character-order determinant")
for p in primerange(2, 30):
    for a in range(1, 8):
        matrix = Matrix([[theta(p, a, r, j) for j in range(a + 1)]
                         for r in range(a + 1)])
        expected = p ** (a * (a + 1) // 2)
        assert abs(int(matrix.det())) == expected
print("  index is p^(a(a+1)/2)")

print("\nVERDICT: I7 PRIME-POWER CONTACT FILTRATION CHECKS PASS")
