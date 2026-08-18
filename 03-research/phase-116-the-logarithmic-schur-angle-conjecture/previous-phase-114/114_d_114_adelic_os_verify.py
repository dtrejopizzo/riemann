#!/usr/bin/env python3
"""Exact certificates for D.114 adelic reflection positivity."""

from fractions import Fraction


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))]
            for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def main() -> None:
    rho = Fraction(1, 2)
    depths = range(4)

    # Prime OS Hankel contact is an outer product.
    v = [rho**r for r in depths]
    hankel = [[v[r] * v[s] for s in depths] for r in depths]
    assert hankel == matmul([[x] for x in v], [v])
    # Every 2x2 minor vanishes, and the quadratic form is a square.
    for i in range(3):
        for j in range(3):
            assert hankel[i][i] * hankel[j + 1][j + 1] - \
                   hankel[i][j + 1] * hankel[j + 1][i] == 0

    # Minimal dilation covariance is the difference-depth Toeplitz kernel.
    toeplitz = [[rho ** abs(r - s) for s in depths] for r in depths]
    # Positive Jacobi elimination: all leading principal determinants.
    leading = []
    from sympy import Matrix
    for n in range(1, 5):
        det = Matrix([row[:n] for row in toeplitz[:n]]).det()
        leading.append(det)
        assert det > 0

    # Two Gamma heat modes form a positive Hankel Gram.
    rates = [Fraction(1, 2), Fraction(1, 3)]
    gamma_vectors = [[r**t for r in rates] for t in depths]
    gamma_hankel = matmul(gamma_vectors, transpose(gamma_vectors))
    for n in range(1, 3):
        assert Matrix([row[:n] for row in gamma_hankel[:n]]).det() >= 0

    # Kunneth/Schur product of two OS Gram matrices remains a Gram matrix.
    schur = [[hankel[i][j] * gamma_hankel[i][j]
              for j in depths] for i in depths]
    product_vectors = [[v[i] * gamma_vectors[i][a] for a in range(2)]
                       for i in depths]
    assert schur == matmul(product_vectors, transpose(product_vectors))

    # A local p=4 Szego block is expanding, so cannot itself be a
    # conditional expectation.
    local_norm_sq = (1 + rho) / (1 - rho)
    assert local_norm_sq == 3 > 1

    # Finite toy: Y_+=I, Y_-=2I.  The induced assignment is not a
    # contraction and its Pick defect is negative.
    plus_norm_sq = Fraction(5, 7)
    minus_norm_sq = 4 * plus_norm_sq
    pick_defect = plus_norm_sq - minus_norm_sq
    assert pick_defect == Fraction(-15, 7) < 0

    print("D114 adelic OS certificates: PASS")
    print("Toeplitz leading determinants:", leading)
    print("local Szego norm squared:", local_norm_sq)
    print("noncontractive Pick defect:", pick_defect)


if __name__ == "__main__":
    main()
