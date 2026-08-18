#!/usr/bin/env python3
"""Finite checks for the Laurent normal-form reduction in 114.a.26."""

from fractions import Fraction
from itertools import combinations

from sympy import Matrix, primerange


def check(label, condition):
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s}  {label}")
    if not condition:
        raise AssertionError(label)


def valuations(value, primes):
    value = Fraction(value)
    exponents = []
    for prime in primes:
        exponent = 0
        while value.numerator % prime == 0:
            value = Fraction(value.numerator // prime, value.denominator)
            exponent += 1
        while value.denominator % prime == 0:
            value = Fraction(value.numerator, value.denominator // prime)
            exponent -= 1
        exponents.append(exponent)
    return tuple(exponents), value


print("A. Unique Laurent encoding of positive rationals")
primes = list(primerange(2, 30))
round_trips = []
for numerator in range(1, 31):
    for denominator in range(1, 31):
        rational = Fraction(numerator, denominator)
        exponents, remainder = valuations(rational, primes)
        rebuilt = Fraction(1)
        for prime, exponent in zip(primes, exponents):
            rebuilt *= Fraction(prime) ** exponent
        round_trips.append(remainder == 1 and rebuilt == rational)
check("A(1..30) all factorization round trips", all(round_trips))

print("\nB. Power characters separate finite Laurent supports")
support = [Fraction(1, 6), Fraction(1, 2), Fraction(1),
           Fraction(3, 2), Fraction(5), Fraction(14)]
full_ranks = []
for size in range(1, len(support) + 1):
    for subset in combinations(support, size):
        # Positive integer powers sigma=1,...,size give a Vandermonde matrix
        # times an invertible diagonal matrix.
        matrix = Matrix([[item**sigma for item in subset]
                         for sigma in range(1, size + 1)])
        full_ranks.append(matrix.det() != 0)
check("B all nonempty subsets have full positive-character rank",
      all(full_ranks))

print("\nC. Factor-through criterion in finite models")
# A linear family of characters descends through a quotient precisely when
# the relation space lies in every character kernel.  Full-rank Vandermonde
# separation makes their common kernel zero.
for size in range(1, 8):
    bases = [Fraction(index + 1, index + 2) for index in range(size)]
    character_matrix = Matrix([[base**sigma for base in bases]
                               for sigma in range(size)])
    common_kernel_dimension = size - character_matrix.rank()
    check(f"C({size}) common kernel is zero",
          common_kernel_dimension == 0)

print("\n" + "=" * 72)
print("VERDICT: ALL CHECKS PASS")
