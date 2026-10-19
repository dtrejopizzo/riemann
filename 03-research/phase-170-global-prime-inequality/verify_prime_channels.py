#!/usr/bin/env python3
"""Checks for R170_201–202. Algebra checks, not a certificate of RH.

Standard library only. Exact rational checks verify cleared Laurent
coefficients; floating checks exercise the actual prime parameters.
"""

from fractions import Fraction as Q
import cmath
import math
import random


def check_cleared_factorization():
    count = 0
    for r in [Q(1, 2), Q(2, 3), Q(3, 7), Q(9, 10)]:
        for ell in [Q(1), Q(7, 3), Q(11, 5)]:
            c = 2 * ell * r / (1 - r)
            b = ell * r * (1 + r) / (1 - r)
            assert c * (1 + r * r) + 2 * ell * r * r == 2 * b
            assert -r * (c + ell) == -b
            # A smaller constant fails at the trivial character U=1.
            assert (c - Q(1, 100)) - 2 * ell * r / (1 - r) < 0
            count += 1
    return count


def check_ratio_channels():
    # Formal shift group: U_m^* U_n is indexed by the rational n/m.
    # Rational weights are probes of the algebra, not substitutes for Λ.
    towers = {2: {2: Q(2), 4: Q(3)}, 3: {3: Q(5), 9: Q(7)}}
    scalar = {}
    separated = {}
    entries = [(p, n, a) for p, tower in towers.items() for n, a in tower.items()]
    for p, m, a in entries:
        for q, n, b in entries:
            ratio = Q(n, m)
            scalar[ratio] = scalar.get(ratio, Q(0)) + a * b
            if p == q:
                separated[ratio] = separated.get(ratio, Q(0)) + a * b
    assert scalar[Q(3, 2)] == 10
    assert Q(3, 2) not in separated
    assert all(r.denominator == 1 or r.numerator == 1 for r in separated)
    assert separated[Q(2)] == 6  # Same-prime current is not deleted.
    return len(scalar), len(separated)


def check_prime_symbols():
    rng = random.Random(170)
    primes = [2, 3, 5, 7, 11, 13]
    max_error = 0.0
    for tau in [0.0, 1e-5, 1.0, 14.0] + [rng.uniform(-100, 100) for _ in range(100)]:
        norm = 0.0
        remainder = 0.0
        for p in primes:
            r, ell = p ** -0.5, math.log(p)
            z = cmath.exp(1j * tau * ell)
            c = 2 * ell * r / (1 - r)
            b = ell * r * (1 + r) / (1 - r)
            d = math.sqrt(b) * (1 - z) / (1 - r * z)
            v = ell * r * z / (1 - r * z)
            norm += abs(d) ** 2
            remainder += c - 2 * v.real
        error = abs(norm - remainder) / max(1.0, abs(norm), abs(remainder))
        max_error = max(max_error, error)
        assert error < 1e-12, (tau, error)
    return max_error


def check_polar_witness():
    # Normalize h(log x) by sqrt(1/x). This is rational for rational x.
    x = Q(3, 2)
    normalized_h = x + 1 - 1 / (1 - 1 / (x * x))
    assert normalized_h == Q(7, 10)
    assert 1 < x < 2  # No prime shift in a sufficiently small neighborhood.
    # Entire neighborhood of endpoint differences stays in a positive region.
    # x^3-x-1 is increasing for x >= 1 and positive at 7/5.
    lower, upper = Q(7, 5), Q(8, 5)
    assert lower ** 3 - lower - 1 > 0
    assert 1 < lower < x < upper < 2
    return normalized_h


if __name__ == '__main__':
    print('Exact cleared-factor checks:', check_cleared_factorization())
    print('Scalar/separated rational supports:', check_ratio_channels())
    print('Maximum relative floating symbol error:', check_prime_symbols())
    print('Exact normalized polar witness:', check_polar_witness())
    print('PASS. These checks do not certify W_T >= 0.')
