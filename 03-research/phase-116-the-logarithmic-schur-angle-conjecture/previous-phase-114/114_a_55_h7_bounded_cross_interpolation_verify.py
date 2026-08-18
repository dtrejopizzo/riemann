#!/usr/bin/env python3
"""Exact checks for the bounded cross-interpolation no-go of a_55."""

from fractions import Fraction
from itertools import product
from math import gcd, log


def solve_mod(matrix, rhs, p):
    """Solve a square nonsingular linear system over F_p."""
    n = len(rhs)
    aug = [list(row) + [value % p] for row, value in zip(matrix, rhs)]
    for column in range(n):
        pivot = next(row for row in range(column, n)
                     if aug[row][column] % p)
        aug[column], aug[pivot] = aug[pivot], aug[column]
        inverse = pow(aug[column][column] % p, -1, p)
        aug[column] = [(inverse * value) % p
                       for value in aug[column]]
        for row in range(n):
            if row == column:
                continue
            factor = aug[row][column] % p
            aug[row] = [
                (left - factor * right) % p
                for left, right in zip(aug[row], aug[column])
            ]
    return [aug[row][-1] for row in range(n)]


def centered(value, p):
    value %= p
    return value - p if value > p // 2 else value


def interpolate(target, m, p):
    exponents = tuple(2 * j + 1 for j in range(m))
    nodes = tuple(pow(2, exponent, p) for exponent in exponents)
    scale = m * (p - 1)
    matrix = [[pow(node, k, p) for k in range(m)] for node in nodes]
    rhs = [scale * pow(2, m * exponent, p) * value
           for exponent, value in zip(exponents, target)]
    residues = solve_mod(matrix, rhs, p)
    return tuple(centered(value, p) for value in residues)


def moment_image(coefficients, m, p):
    scale = m * (p - 1)
    image = []
    for j in range(m):
        exponent = 2 * j + 1
        # Written directly to mirror equation (2.6).
        polynomial = sum(
            coefficient * pow(pow(2, exponent, p), k, p)
            for k, coefficient in enumerate(coefficients)
        ) % p
        value = (pow(scale, -1, p)
                 * pow(pow(2, m, p), -exponent, p)
                 * polynomial) % p
        image.append(value)
    return tuple(image)


print("A. Distinct odd-power nodes and invertible Vandermonde systems")
blocks = ((2, 17), (4, 257))
for m, p in blocks:
    assert p > 2 ** (2 * m)
    exponents = tuple(2 * j + 1 for j in range(m))
    assert all(gcd(exponent, p - 1) == 1 for exponent in exponents)
    nodes = tuple(pow(2, exponent, p) for exponent in exponents)
    assert len(set(nodes)) == m
print("  all interpolation nodes are distinct")

print("\nB. Exact real norm and finite-denominator bounds")
for m, p in blocks:
    scale = m * (p - 1)
    alpha_bound = Fraction(m * (p - 1) ** 2, 4 * scale**2)
    beta_norm = sum(Fraction(4**k, 4**m) for k in range(m))
    assert alpha_bound == Fraction(1, 4 * m) < 1
    assert beta_norm == Fraction(4**m - 1, 3 * 4**m) < 1
    assert scale % p and pow(2, m, p)
print("  both vectors are strict Euclidean contractions")

print("\nC. Every target in the m=2 block has a bounded lift")
m, p = blocks[0]
images = set()
for target in product(range(p), repeat=m):
    coefficients = interpolate(target, m, p)
    assert all(abs(value) <= (p - 1) // 2 for value in coefficients)
    image = moment_image(coefficients, m, p)
    assert image == target
    images.add(image)
assert len(images) == p**m
print("  the bounded family maps onto F_p^m exactly")

print("\nD. Higher-rank deterministic interpolation checks")
m, p = blocks[1]
targets = [
    (0,) * m,
    (1,) * m,
    tuple(range(m)),
    tuple((17 * j * j + 3) % p for j in range(m)),
    (p - 1, 0, 1, p // 2),
]
for target in targets:
    coefficients = interpolate(target, m, p)
    assert moment_image(coefficients, m, p) == target
    assert all(abs(value) <= (p - 1) // 2 for value in coefficients)
print("  all selected F_257^4 targets lift exactly")

print("\nE. The RR coefficient has a positive quadratic deficit")
gap = 1 - log(2) / (2 * log(3))
assert gap > 0.68
for m in (10, 100, 1000):
    # Any controlled p with log p=Theta(m) has the same limiting ratio.
    synthetic_log_p = 3 * m
    degree_1 = synthetic_log_p + log(m)
    degree_2 = m * log(2)
    full_block = m * synthetic_log_p
    code_lead = degree_1 * degree_2 / (2 * log(3))
    assert full_block - code_lead > 0
print("  bounded block entropy exceeds the universal code coefficient")

print("\nVERDICT: H7 BOUNDED CROSS-INTERPOLATION NO-GO CHECKS PASS")
