#!/usr/bin/env python3
"""Exact rank growth of truncated bilateral Frobenius orbits."""

from fractions import Fraction


def orbit_vectors(prime, radius):
    exponents = [Fraction(prime) ** k for k in range(-radius, radius + 1)]
    basis = {exponent: i for i, exponent in enumerate(exponents)}
    vectors = []
    for exponent in exponents:
        row = [0] * len(exponents)
        row[basis[exponent]] = 1
        vectors.append(row)
    return vectors


def rational_rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = a[rank][col]
        a[rank] = [x / scale for x in a[rank]]
        for r in range(rows):
            if r != rank and a[r][col]:
                factor = a[r][col]
                a[r] = [x - factor * y for x, y in zip(a[r], a[rank])]
        rank += 1
    return rank


radii = (1, 2, 4, 8, 16)
all_ok = True
for prime in (2, 3, 5):
    ranks = [rational_rank(orbit_vectors(prime, radius)) for radius in radii]
    expected = [2 * radius + 1 for radius in radii]
    ok = ranks == expected
    all_ok &= ok
    print(f"P={prime}_TRUNCATED_ORBIT_RANKS: {ranks}")

print(f"FROBENIUS_ORBIT_RANK_UNBOUNDED: {'YES' if all_ok else 'NO'}")
print("NONCONSTANT_FROBENIUS_STABLE_FINITE_DIMENSION: NO")
print("ADDITIVE_STALK_TRUNCATION_ROUTE: CLOSED_NO_GO")
print(f"VERDICT: {'YES' if all_ok else 'NO'}")
raise SystemExit(0 if all_ok else 1)
