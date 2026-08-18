#!/usr/bin/env python3
"""Finite exact checks for full-tree twisted-bio odd moments."""

from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import gcd, prod

from sympy import isprime, primerange, nextprime


def controlled_prime(r, Q):
    small_odd = tuple(primerange(3, 4 * r))
    P = prod(small_odd) if small_odd else 1
    A = max(2 * Q, 3**r, 2 ** (4 * r))
    a = A + 1 + ((2 - (A + 1)) % P)
    R = int(nextprime(a))
    modulus = P * R
    candidate = a
    while not isprime(candidate):
        candidate += modulus
    return int(candidate), small_odd


@lru_cache(maxsize=None)
def transported_add(x, y, s, p):
    inverse = pow(s, -1, p - 1)
    tx = pow(x, inverse, p) if x else 0
    ty = pow(y, inverse, p) if y else 0
    return pow((tx + ty) % p, s, p)


def odd_moments(terms, r, p):
    values = []
    for k in range(2 * r):
        s = 2 * k + 1
        total = 0
        for coefficient, label in terms:
            x = label.numerator * pow(label.denominator, -1, p) % p
            total += coefficient * pow(x, s, p)
        values.append(total % p)
    return tuple(values)


print("A. Controlled primes and invertible odd exponents")
examples = []
for r, Q in ((1, 3), (2, 5), (3, 7)):
    p, small_odd = controlled_prime(r, Q)
    assert p > max(2 * Q, 3**r, 2 ** (4 * r))
    for ell in small_odd:
        assert (p - 1) % ell != 0
    for s in range(1, 4 * r, 2):
        assert gcd(s, p - 1) == 1
    assert len({pow(2, s, p) for s in range(1, 4 * r, 2)}) == 2 * r
    examples.append((r, Q, p))
print("  every required power is a multiplicative permutation")

print("\nB. Transported field laws and integer power map")
p = examples[0][2]
for s in range(1, 4 * examples[0][0], 2):
    for x, y, z in product(range(p), repeat=3):
        add = lambda a, b: transported_add(a, b, s, p)
        assert add(add(x, y), z) == add(x, add(y, z))
        assert add(x, y) == add(y, x)
        assert z * add(x, y) % p == add(z * x % p, z * y % p)
    value = 0
    for _ in range(7):
        value = transported_add(value, 1, s, p)
    assert value == pow(7, s, p)
print("  field laws and n -> n^s hold exactly")

print("\nC. Alternating full-tree operations remain homogeneous")
r, Q, p = examples[0]
s = 3
add_s = lambda x, y: transported_add(x, y, s, p)
trees = (
    lambda x, y, z: (add_s(x, y) + z) % p,
    lambda x, y, z: add_s((x + y) % p, z),
    lambda x, y, z: add_s(x, (add_s(y, z) + x) % p),
)
grid = range(min(p, 13))
for f in trees:
    for scalar, xyz in product(grid, product(grid, repeat=3)):
        scaled = tuple(scalar * x % p for x in xyz)
        assert f(*scaled) == scalar * f(*xyz) % p
print("  every tested alternating tree defines a unary scalar action")

print("\nD. Odd-Vandermonde determinant")
for r, Q, p in examples:
    labels = [Fraction(a, Q) for a in range(1, min(Q, 2 * r) + 1)]
    xs = [x.numerator * pow(x.denominator, -1, p) % p for x in labels]
    determinant = 1
    for x in xs:
        determinant = determinant * x % p
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            determinant = determinant * (xs[j] ** 2 - xs[i] ** 2) % p
    assert determinant != 0
print("  product(x_i) product(x_j^2-x_i^2) is nonzero")

print("\nE. Exhaustive balanced-code separation")
for r, Q, p in examples[:2]:
    images = set()
    total = 0
    for c in product(range(-Q, Q + 1), repeat=r):
        if sum(abs(x) for x in c) > Q:
            continue
        terms = tuple(
            (3**j * (1 if value > 0 else -1), Fraction(abs(value), Q))
            for j, value in enumerate(c)
            if value
        )
        image = odd_moments(terms, r, p)
        assert image not in images
        images.add(image)
        total += 1
    assert len(images) == total
print("  complete small balanced codes are separated")

print("\nVERDICT: H7 FULL-TREE FINITE-BIO MOMENT CHECKS PASS")
