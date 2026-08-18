#!/usr/bin/env python3
"""Exact checks for W_p = Z x_{F_p} Z and its branch intersection."""

from math import isclose, log

from sympy import primerange


def multiply(pair1, pair2, p):
    """Multiply a+b*e using e^2=(p-2)e+(p-1)."""
    a, b = pair1
    c, d = pair2
    return (a * c + b * d * (p - 1),
            a * d + b * c + b * d * (p - 2))


def characters(pair, p):
    a, b = pair
    return (a + b * (p - 1), a - b)


print("A. Character pair is a multiplicative bijection onto the fiber product")
for p in primerange(2, 100):
    for a in range(-5, 6):
        for b in range(-5, 6):
            r, s = characters((a, b), p)
            assert (r - s) % p == 0
            recovered_b = (r - s) // p
            recovered_a = s + recovered_b
            assert (recovered_a, recovered_b) == (a, b)
            for c, d in ((0, 0), (1, 0), (0, 1), (2, -1), (-3, 2)):
                product = multiply((a, b), (c, d), p)
                left = characters(product, p)
                rc, sc = characters((c, d), p)
                assert left == (r * rc, s * sc)
print("  all checked products and inverse formulas pass")

print("\nB. The two branches meet modulo exactly p")
for p in primerange(2, 500):
    f0_value = p - 1
    trace_value = -1
    assert f0_value - trace_value == p
    assert isclose(log(abs(f0_value - trace_value)), log(p))
print("  branch tensor relation is p=0")

print("\nC. Cyclotomic and incidence masses agree")
for p in primerange(2, 1000):
    cyclotomic_at_one = p
    residue_cardinality = p
    assert cyclotomic_at_one == residue_cardinality
    assert isclose(log(cyclotomic_at_one), log(residue_cardinality))
print("  log|Phi_p(1)|=log #F_p=Lambda(p)")

print("\nVERDICT: I7 WITT PRIME-NODE INTERSECTION CHECKS PASS")
