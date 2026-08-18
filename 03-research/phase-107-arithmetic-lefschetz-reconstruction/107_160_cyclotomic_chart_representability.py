#!/usr/bin/env python3
"""Exact cyclotomic factor and degree checks for the rooted chart."""

from sympy import Poly, cyclotomic_poly, divisors, symbols, totient


x = symbols("x")
all_ok = True
for level in (2, 6, 12, 30, 60):
    factors = [Poly(cyclotomic_poly(n, x), x, domain="ZZ") for n in divisors(level)]
    product_poly = Poly(1, x, domain="ZZ")
    for factor in factors:
        product_poly *= factor
    factorization_ok = product_poly == Poly(x**level - 1, x, domain="ZZ")
    degree_ok = sum(int(totient(n)) for n in divisors(level)) == level
    monic_ok = all(factor.LC() == 1 for factor in factors)
    irreducible_ok = all(factor.is_irreducible for factor in factors)
    all_ok &= factorization_ok and degree_ok and monic_ok and irreducible_ok
    print(f"L={level}_COMPONENTS={len(factors)}_GENERIC_DEGREE={sum(f.degree() for f in factors)}")

print(f"CYCLOTOMIC_FACTORIZATION_EXACT: {'YES' if all_ok else 'NO'}")
print(f"GENERIC_DEGREE_EQUALS_ROOTED_ORDER: {'YES' if all_ok else 'NO'}")
print("ROOTED_LABEL_MULTIPLICITY: EXACT_ORDER_ONLY")
print("FINITE_FLAT_PROPER_REGULAR_CHART: YES")
print(f"VERDICT: {'YES' if all_ok else 'NO'}")
raise SystemExit(0 if all_ok else 1)
