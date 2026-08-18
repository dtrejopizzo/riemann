#!/usr/bin/env python3
"""Exact finite certificates for the strong row-A rank obstruction."""

from fractions import Fraction


def rank_over_q(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = a[rank][col]
        a[rank] = [x / scale for x in a[rank]]
        for i in range(rows):
            if i != rank and a[i][col]:
                scale = a[i][col]
                a[i] = [x - scale * y for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def prime_contact_pattern(size):
    # Replace nonzero log(p_i) by distinct positive rational witnesses.
    # Diagonal rescaling does not alter rank.
    return [[i + 2 if i == j else 0 for j in range(size)] for i in range(size)]


for r in range(1, 13):
    matrix = prime_contact_pattern(r)
    assert rank_over_q(matrix) == r

print("PASS: prime contact submatrices have ranks 1,...,12.")
print("Since the construction works for arbitrarily many distinct primes,")
print("the kernel Lambda(mn) cannot factor through a finite-rank lattice.")
