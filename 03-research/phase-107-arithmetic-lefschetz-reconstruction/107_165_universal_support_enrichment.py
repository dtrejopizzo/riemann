#!/usr/bin/env python3
"""Finite exact checks for the universal support enrichment."""

from collections import defaultdict
from itertools import product


PRIMES = (2, 3, 5, 7, 11)


def normalize(poly):
    return {exponent: coefficient for exponent, coefficient in poly.items() if coefficient}


def add(left, right):
    out = defaultdict(int, left)
    for exponent, coefficient in right.items():
        out[exponent] += coefficient
    return normalize(out)


def multiply(left, right):
    out = defaultdict(int)
    for (a, b), c in left.items():
        for (x, y), d in right.items():
            out[(a + x, b + y)] += c * d
    return normalize(out)


def minimal_support(poly):
    support = set(poly)
    return {
        u
        for u in support
        if not any(v != u and v[0] <= u[0] and v[1] <= u[1] for v in support)
    }


def upper_union(left, right):
    fake = {u: 1 for u in set(left) | set(right)}
    return minimal_support(fake)


def upper_minkowski(left, right):
    fake = {(a + x, b + y): 1 for a, b in left for x, y in right}
    return minimal_support(fake)


def frobenius(poly, vertical, horizontal):
    return {(vertical * a, horizontal * b): c for (a, b), c in poly.items()}


def lambda_map(poly, n, m):
    out = defaultdict(int)
    for (a, b), coefficient in poly.items():
        out[n * a + m * b] += coefficient
    return normalize(out)


def mass(poly):
    return sum(abs(coefficient) for coefficient in poly.values())


samples = [
    {(0, 0): 1, (1, 2): 2},
    {(2, 0): 3, (0, 3): 1, (2, 2): 4},
    {(1, 1): 2, (3, 0): 5},
]

all_ok = True
checks = 0
for left, right in product(samples, repeat=2):
    tropical_add = minimal_support(add(left, right))
    expected_add = upper_union(minimal_support(left), minimal_support(right))
    tropical_mul = minimal_support(multiply(left, right))
    expected_mul = upper_minkowski(minimal_support(left), minimal_support(right))
    all_ok &= tropical_add == expected_add
    all_ok &= tropical_mul == expected_mul

    for prime in PRIMES:
        for vertical, horizontal in ((prime, 1), (1, prime)):
            lhs = minimal_support(frobenius(add(left, right), vertical, horizontal))
            rhs = upper_union(
                minimal_support(frobenius(left, vertical, horizontal)),
                minimal_support(frobenius(right, vertical, horizontal)),
            )
            all_ok &= lhs == rhs
            checks += 1

    for n, m in ((1, 1), (2, 1), (3, 2)):
        image_sum = lambda_map(add(left, right), n, m)
        sum_images = add(lambda_map(left, n, m), lambda_map(right, n, m))
        image_product = lambda_map(multiply(left, right), n, m)
        product_images = {}
        for a, c in lambda_map(left, n, m).items():
            for b, d in lambda_map(right, n, m).items():
                product_images[a + b] = product_images.get(a + b, 0) + c * d
        all_ok &= image_sum == sum_images
        all_ok &= image_product == normalize(product_images)
        all_ok &= mass(lambda_map(add(left, right), n, m)) <= mass(add(left, right))
        checks += 1

# Signed cancellation prevents any additive extension of tropical support.
x = {(0, 1): 1}
y = {(1, 0): 1}
minus_y = {(1, 0): -1}
before = minimal_support(add(x, y))
after = minimal_support(add(add(x, y), minus_y))
cancellation_detected = before == {(0, 1), (1, 0)} and after == {(0, 1)}
all_ok &= cancellation_detected

print(f"REAL_PRIME_ACTIONS: {','.join(map(str, PRIMES))}")
print(f"EXACT_COMPATIBILITY_CHECKS: {checks}")
print(f"POSITIVE_TROPICALIZATION_SEMIRING_MAP: {'YES' if all_ok else 'NO'}")
print(f"TWO_FROBENIUS_RULINGS_EQUIVARIANT: {'YES' if all_ok else 'NO'}")
print(f"LAMBDA_MAP_RING_COMPATIBLE: {'YES' if all_ok else 'NO'}")
print(f"SIGNED_CANCELLATION_CHANGES_NEWTON_SHADOW: {'YES' if cancellation_detected else 'NO'}")
print("ADDITIVE_TROPICALIZATION_OF_GROUP_COMPLETION: NO")
print("ENRICHMENT: N[M]_WITH_GROUP_COMPLETION_Z[M]")
print(f"VERDICT: {'YES' if all_ok else 'NO'}")
raise SystemExit(0 if all_ok else 1)
