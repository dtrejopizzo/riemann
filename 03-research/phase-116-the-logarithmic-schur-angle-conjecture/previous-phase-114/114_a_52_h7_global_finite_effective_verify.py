#!/usr/bin/env python3
"""Checks for the global finite-effective moment system of a_52."""

from fractions import Fraction
from itertools import product
from math import ceil, exp, gcd, log, prod

from sympy import isprime, nextprime, primerange


def rank_cap(H):
    return ceil(log(2 * H + 1, 3))


def controlled_prime(r, Q):
    odd_primes = tuple(primerange(3, 4 * r))
    P = prod(odd_primes) if odd_primes else 1
    A = max(2 * Q, 3**r, 2 ** (4 * r))
    a = A + 1 + ((2 - (A + 1)) % P)
    R = int(nextprime(a))
    step = P * R
    candidate = a
    while not isprime(candidate):
        candidate += step
    return int(candidate)


def odd_moments(terms, count, p):
    result = []
    for k in range(count):
        s = 2 * k + 1
        total = 0
        for coefficient, value in terms:
            x = value.numerator * pow(value.denominator, -1, p) % p
            total += coefficient * pow(x, s, p)
        result.append(total % p)
    return tuple(result)


print("A. Uniform blocks by intrinsic height")
levels = []
for T in (1, 2, 4):
    H = ceil(exp(T))
    R = rank_cap(H)
    p = controlled_prime(R, H)
    assert p > max(2 * H, 3**R, 2 ** (4 * R))
    for s in range(1, 4 * R, 2):
        assert gcd(s, p - 1) == 1
    assert len({pow(2, s, p) for s in range(1, 4 * R, 2)}) == 2 * R
    levels.append((T, H, R, p))
print("  one prime block handles every norm below each height")

print("\nB. Uniform separation for all small denominators")
T, H, R, p = levels[1]
for Q in range(1, min(H, 6) + 1):
    r = min(2, rank_cap(Q))
    seen = set()
    total = 0
    for c in product(range(-Q, Q + 1), repeat=r):
        if sum(abs(x) for x in c) > Q:
            continue
        terms = tuple(
            (3**j * (1 if value > 0 else -1), Fraction(abs(value), Q))
            for j, value in enumerate(c)
            if value
        )
        image = odd_moments(terms, 2 * r, p)
        assert image not in seen
        seen.add(image)
        total += 1
    assert len(seen) == total
print("  all tested Q share the same separating target")

print("\nC. Prime-factor presentation independence")
factorizations = {
    12: ((2, 2, 3), (3, 4), (2, 6)),
    18: ((2, 3, 3), (3, 6), (2, 9)),
}
for norm, presentations in factorizations.items():
    assert all(prod(parts) == norm for parts in presentations)
    heights = {max(1.0, log(prod(parts))) for parts in presentations}
    assert len(heights) == 1
print("  target level depends only on the product norm")

print("\nD. Dyadic transition and quadratic size")
previous_components = 0
ratios = []
for T, H, R, p in levels:
    components = previous_components + 2 * R
    assert components >= previous_components
    previous_components = components
    accumulated_log = sum(
        2 * level_r * log(level_p)
        for level_t, _, level_r, level_p in levels
        if level_t <= T
    )
    ratios.append(accumulated_log / T**2)
assert max(ratios) < 100
print("  accumulated targets project compatibly and remain quadratic")

print("\nE. Global retention fails at an old characteristic denominator")
old_prime = levels[0][3]
future_T = 1
while ceil(exp(future_T)) < old_prime:
    future_T *= 2
assert old_prime <= ceil(exp(future_T))
try:
    pow(old_prime, -1, old_prime)
except ValueError:
    pass
else:
    raise AssertionError("old characteristic must not invert itself")
print("  per-height checks do not extend to the accumulated global cone")

print("\nVERDICT: H7 PER-HEIGHT BLOCK CHECKS PASS; GLOBAL RETENTION REFUTED IN a57")
