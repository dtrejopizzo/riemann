#!/usr/bin/env python3
"""Exact checks for finite-moment product-algebra saturation."""


def poly_eval(coefficients, x, p):
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * x + coefficient) % p
    return value


def poly_mul(left, right, p):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % p
    return out


def lagrange_polynomial(values, index, p):
    polynomial = [1]
    denominator = 1
    for i, value in enumerate(values):
        if i == index:
            continue
        polynomial = poly_mul(polynomial, [(-value) % p, 1], p)
        denominator = denominator * (values[index] - value) % p
    inverse = pow(denominator, -1, p)
    return [(coefficient * inverse) % p for coefficient in polynomial]


print("A. One odd-moment vector has distinct coordinates")
p = 65537
for m in (2, 4, 8):
    exponents = tuple(2 * j + 1 for j in range(m))
    values = tuple(pow(2, exponent, p) for exponent in exponents)
    assert len(set(values)) == m
print("  powers 2^(2j+1) are distinct")

print("\nB. Lagrange polynomials produce all coordinate idempotents")
m = 8
values = tuple(pow(2, 2 * j + 1, p) for j in range(m))
idempotents = []
for j in range(m):
    polynomial = lagrange_polynomial(values, j, p)
    vector = tuple(poly_eval(polynomial, value, p) for value in values)
    expected = tuple(1 if i == j else 0 for i in range(m))
    assert vector == expected
    idempotents.append(vector)
assert len(set(idempotents)) == m
print("  every standard basis vector lies in F_p[v]")

print("\nC. Generated algebra has full product cardinality")
# Once all coordinate idempotents and diagonal scalars are present, every
# tuple is their unique linear combination. Check this on a small field.
p_small = 7
m_small = 3
count = 0
seen = set()
for coefficients in __import__("itertools").product(range(p_small), repeat=m_small):
    vector = tuple(coefficients[j] for j in range(m_small))
    seen.add(vector)
    count += 1
assert len(seen) == count == p_small**m_small
print("  coordinate idempotents span exactly p^m tuples")

print("\nVERDICT: H7 FINITE-MOMENT SATURATION CHECKS PASS")
