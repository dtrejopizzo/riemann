#!/usr/bin/env python3
"""Checks for the horizontal excess in Witt graph/diagonal intersections."""

from math import prod

from sympy import Matrix, totient


def relation_matrix(p, a):
    """Columns are F_p(e_j)-e_j, j=1,...,a, in basis e_0,...,e_a."""
    matrix = [[0 for _ in range(a)] for _ in range(a + 1)]
    matrix[0][0] = p - 1
    matrix[1][0] = -1
    for j in range(2, a + 1):
        matrix[j - 1][j - 1] = p
        matrix[j][j - 1] = -1
    return Matrix(matrix)


print("A. Relation matrices have free rank one and no torsion")
for p in (2, 3, 5, 7, 11, 13, 17, 19):
    for a in range(1, 16):
        matrix = relation_matrix(p, a)
        assert matrix.rank() == a
        unit_minor = matrix[1:a + 1, 0:a].det()
        assert abs(int(unit_minor)) == 1
print("  all checked cokernels are torsion-free of rank one")

print("\nB. Relations reduce every basis vector to phi_1")
for p in (2, 3, 5, 11):
    for a in range(1, 20):
        coefficients = [1]
        if a >= 1:
            coefficients.append(p - 1)
        for _ in range(2, a + 1):
            coefficients.append(p * coefficients[-1])
        assert coefficients == [int(totient(p**j)) for j in range(a + 1)]
print("  e_j=varphi(p^j)e_0 after F_p=id")

print("\nC. F_0 coequalizes F_p and the identity")
for p in (2, 3, 5, 7, 11):
    for a in range(1, 20):
        phi = [int(totient(p**j)) for j in range(a + 1)]
        assert (p - 1) * phi[0] == phi[1]
        for j in range(2, a + 1):
            assert p * phi[j - 1] == phi[j]
        assert phi[0] == 1
print("  the free generator maps to 1 in Z")

print("\nVERDICT: I7 WITT GRAPH HORIZONTAL-EXCESS CHECKS PASS")
