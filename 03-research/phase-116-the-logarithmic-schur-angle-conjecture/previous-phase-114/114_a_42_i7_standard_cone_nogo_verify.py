#!/usr/bin/env python3
"""Checks for the reduced fixed-cone no-go and cyclotomic replacement."""

from math import isclose, log

from sympy import Matrix, cyclotomic_poly, eye, symbols, zeros


print("A. Reduced Frobenius is nilpotent")
for p in (2, 3, 5, 7, 11, 13):
    for a in range(1, 15):
        f = zeros(a)
        for j in range(1, a):
            f[j - 1, j] = p
        assert f**a == zeros(a)
print("  F_bar^a=0 on all checked prime-power stages")

print("\nB. 1-F_bar is integrally invertible with determinant one")
for p in (2, 3, 5, 7, 11):
    for a in range(1, 13):
        f = zeros(a)
        for j in range(1, a):
            f[j - 1, j] = p
        operator = eye(a) - f
        inverse = sum((f**j for j in range(a)), zeros(a))
        assert operator * inverse == eye(a)
        assert operator.det() == 1
        assert all(entry.q == 1 for entry in inverse)
print("  standard reduced cone is integrally acyclic")

print("\nC. Cyclotomic determinant gives von Mangoldt")
t = symbols("t")
for n in range(2, 501):
    value = int(cyclotomic_poly(n, t).subs(t, 1))
    base = None
    for p in range(2, n + 1):
        if any(p % d == 0 for d in range(2, int(p**0.5) + 1)):
            continue
        power = p
        while power < n:
            power *= p
        if power == n:
            base = p
            break
    expected_value = base if base else 1
    expected_mass = log(base) if base else 0.0
    assert value == expected_value
    assert isclose(log(abs(value)), expected_mass)
print("  log|Norm(1-zeta_n)|=Lambda(n) for 2<=n<=500")

print("\nVERDICT: I7 STANDARD-CONE NO-GO/CYCLOTOMIC CHECKS PASS")
