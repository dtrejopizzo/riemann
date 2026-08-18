#!/usr/bin/env python3
"""Exact finite analogue of the homogeneous-endobio H7-UEMB proof."""

from itertools import product


P = 5
R = 3
R_INV = 3  # 3*3 = 1 mod 4


def T(x):
    return pow(x, R, P)


def T_inv(x):
    return pow(x, R_INV, P)


def add_1(x, y):
    return (x + y) % P


def add_u(x, y):
    return T_inv((T(x) + T(y)) % P)


def linear(coeffs, values, add):
    out = 0
    for a, x in zip(coeffs, values):
        out = add(out, a * x % P)
    return out


print("A. Two distinct transported fields with common multiplication")
assert add_1(1, 1) == 2
assert add_u(1, 1) == 3
for x, y, z in product(range(P), repeat=3):
    assert add_u(add_u(x, y), z) == add_u(x, add_u(y, z))
    assert add_u(x, y) == add_u(y, x)
    assert z * add_u(x, y) % P == add_u(z * x % P, z * y % P)
print("  field laws and common distributive multiplication pass")

print("\nB. Ordinary, twisted and mixed operations are homogeneous")
operations = [
    lambda xs: linear((1, 2, 3), xs, add_1),
    lambda xs: linear((1, 2, 3), xs, add_u),
    lambda xs: add_1(add_u(xs[0], xs[1]), xs[2]),
    lambda xs: add_u(add_1(xs[0], xs[1]), xs[2]),
]
for f in operations:
    for t, xs in product(range(P), product(range(P), repeat=3)):
        scaled = tuple(t * x % P for x in xs)
        assert f(scaled) == t * f(xs) % P
print("  f(t x)=t f(x) for the complete finite grid")

print("\nC. Haran commutativity move through every scalar column")
for f in operations:
    for g in operations:
        for b in product(range(P), repeat=3):
            for xs in product(range(P), repeat=3):
                gx = g(xs)
                left = f(tuple(bi * gx % P for bi in b))
                right = f(tuple(g(tuple(bi * x % P for x in xs)) for bi in b))
                assert left == right
print("  column/operation interchange follows exactly from homogeneity")

print("\nD. Common unary action separates scalars")
signatures = {a: tuple(a * x % P for x in range(P)) for a in range(P)}
assert len(set(signatures.values())) == P
for a in range(P):
    assert signatures[a][1] == a
print("  evaluation at 1 recovers every unary scalar")

print("\nVERDICT: H7 HOMOGENEOUS-ENDOBIO UNARY EMBEDDING CHECKS PASS")
