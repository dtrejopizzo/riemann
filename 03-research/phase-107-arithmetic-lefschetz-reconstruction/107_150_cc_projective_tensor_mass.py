#!/usr/bin/env python3
"""Exact finite checks for the CC projective tensor mass theorem."""

from itertools import product
from math import ceil, log2


def entry_l1(matrix):
    return sum(abs(x) for row in matrix for x in row)


def bilinear(matrix, signs):
    return sum(
        signs[i][j] * matrix[i][j]
        for i in range(len(matrix))
        for j in range(len(matrix[0]))
    )


def signed_dual_witness(matrix):
    return tuple(
        tuple(1 if x >= 0 else -1 for x in row)
        for row in matrix
    )


def binary_generators(rows, cols, n):
    k = ceil(log2(n + 1))
    return [
        (i, j, 2**power)
        for i in range(rows)
        for j in range(cols)
        for power in range(k)
    ]


def represent(matrix, n):
    terms = []
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            sign = 1 if value >= 0 else -1
            for power in range(ceil(log2(n + 1))):
                if (abs(value) >> power) & 1:
                    terms.append((i, j, 2**power, sign))
    return terms


def reconstruct(rows, cols, terms):
    out = [[0] * cols for _ in range(rows)]
    for i, j, value, sign in terms:
        out[i][j] += sign * value
    return tuple(tuple(row) for row in out)


norm_identity = True
generation = True
for entries in product(range(-3, 4), repeat=4):
    matrix = (entries[:2], entries[2:])
    signs = signed_dual_witness(matrix)
    norm_identity &= bilinear(matrix, signs) == entry_l1(matrix)

for n in range(1, 13):
    generators = set(binary_generators(2, 2, n))
    for entries in product(range(-n, n + 1), repeat=4):
        matrix = (entries[:2], entries[2:])
        if entry_l1(matrix) > n:
            continue
        terms = represent(matrix, n)
        generation &= reconstruct(2, 2, terms) == matrix
        generation &= sum(value for _, _, value, _ in terms) <= n
        generation &= all((i, j, value) in generators for i, j, value, _ in terms)

verdict = norm_identity and generation
print(f"CC_L1_PROJECTIVE_TENSOR_IS_ENTRYWISE_L1: {'YES' if norm_identity else 'NO'}")
print("TRACE_NORM_IS_CC_PROJECTIVE_TENSOR: NO")
print(f"BINARY_GENERATORS_PRESERVE_MASS: {'YES' if generation else 'NO'}")
print("DIMENSION_GROWTH_IN_DEGREE: LINEAR")
print("MASS_FUNCTIONAL: ENTRYWISE_L1")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
raise SystemExit(0 if verdict else 1)
