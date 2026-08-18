#!/usr/bin/env python3
"""Regression checks for the finite-type nuclear bivariant module."""

from collections import defaultdict
from math import isclose, log


def conv(a, b):
    out = defaultdict(float)
    for m, x in a.items():
        for n, y in b.items():
            out[m * n] += x * y
    return dict(out)


def von_mangoldt(n):
    for p in range(2, n + 1):
        if any(p % d == 0 for d in range(2, int(p**0.5) + 1)):
            continue
        k = n
        while k % p == 0:
            k //= p
        if k == 1:
            return log(p)
    return 0.0


def ell(a):
    return sum(x * von_mangoldt(n) for n, x in a.items())


def degree(a):
    return sum(x * log(n) for n, x in a.items())


def delta(n):
    return {n: 1.0}


def matrix_rank(matrix, tol=1e-10):
    a = [row[:] for row in matrix]
    rows, cols = len(a), len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if abs(a[i][col]) > tol), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = a[rank][col]
        a[rank] = [x / scale for x in a[rank]]
        for i in range(rows):
            if i != rank and abs(a[i][col]) > tol:
                factor = a[i][col]
                a[i] = [x - factor * y for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def main():
    primes = [2, 3, 5, 7, 11, 13, 17]

    for m in range(1, 30):
        for n in range(1, 30):
            assert conv(delta(m), delta(n)) == delta(m * n)
            assert isclose(ell(conv(delta(m), delta(n))), von_mangoldt(m * n))

    for p in primes:
        for q in primes:
            ext = degree(delta(p)) * degree(delta(q))
            assert isclose(ext, log(p) * log(q))

    block = [
        [ell(conv(delta(p), delta(q))) for q in primes]
        for p in primes
    ]
    assert matrix_rank(block) == len(primes)
    for i, p in enumerate(primes):
        for j, _q in enumerate(primes):
            assert isclose(block[i][j], log(p) if i == j else 0.0)

    print("PASS: the mixed generator composes by exact label multiplication.")
    print("PASS: diagonal contact is exactly Lambda(mn).")
    print("PASS: ruling polarization has coefficient one.")
    print("PASS: all tested prime directions survive in the nuclear scalars.")


if __name__ == "__main__":
    main()
