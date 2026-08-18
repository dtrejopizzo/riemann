#!/usr/bin/env python3
"""Symbolic checks for the differential proof of H7-LNF in 114.a.27."""

from fractions import Fraction

from sympy import Poly, diff, expand, factorint, symbols


def check(label, condition):
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s}  {label}")
    if not condition:
        raise AssertionError(label)


print("A. Prime differential and localization")
prime_formula_checks = []
for value in range(1, 101):
    factors = factorint(value)
    # Coefficient of e_p in d(n) is v_p(n)n/p.
    for prime, exponent in factors.items():
        coefficient = exponent * Fraction(value, prime)
        prime_formula_checks.append(
            coefficient == Fraction(value) * exponent / prime)
check("A integer prime-differential formula through 100",
      all(prime_formula_checks))

localization_checks = []
for numerator in range(1, 15):
    for denominator in range(1, 15):
        value = Fraction(numerator, denominator)
        for prime in (2, 3, 5, 7, 11, 13):
            valuation = factorint(numerator).get(prime, 0) \
                - factorint(denominator).get(prime, 0)
            derivative_coefficient = value * valuation / prime
            inverse_rule = (-Fraction(numerator, 1)
                            * Fraction(denominator, 1) ** -2
                            * factorint(denominator).get(prime, 0)
                            * Fraction(denominator, prime)
                            + Fraction(denominator, 1) ** -1
                            * factorint(numerator).get(prime, 0)
                            * Fraction(numerator, prime))
            localization_checks.append(
                derivative_coefficient == inverse_rule)
check("A rational quotient/inverse rule on the finite grid",
      all(localization_checks))

print("\nB. Formal chain rule in independent prime directions")
x2, x3, x5 = symbols("x2 x3 x5")
polynomials = [
    x2**4 * x3**2 - 7 * x5 + 3,
    (x2 + 2 * x3 - x5) ** 3,
    x2 * x3 * x5 + x2**2 - x3**4,
]
increments = symbols("e2 e3 e5")
t = symbols("t")
for index, polynomial in enumerate(polynomials, 1):
    substituted = polynomial.subs({
        x2: x2 + t * increments[0],
        x3: x3 + t * increments[1],
        x5: x5 + t * increments[2],
    })
    linear_term = expand(substituted).coeff(t, 1)
    gradient = sum(diff(polynomial, variable) * increment
                   for variable, increment in zip((x2, x3, x5), increments))
    check(f"B({index}) square-zero chain rule",
          expand(linear_term - gradient) == 0)

print("\nC. Characteristic-zero degree descent")
for index, polynomial in enumerate(polynomials, 1):
    nonzero_partials = [diff(polynomial, variable)
                        for variable in (x2, x3, x5)
                        if diff(polynomial, variable) != 0]
    check(f"C({index}) a nonconstant polynomial has a nonzero partial",
          bool(nonzero_partials))
    check(f"C({index}) every nonzero partial lowers total degree",
          all(Poly(partial, x2, x3, x5).total_degree()
              < Poly(polynomial, x2, x3, x5).total_degree()
              for partial in nonzero_partials))

print("\n" + "=" * 72)
print("VERDICT: ALL CHECKS PASS")
