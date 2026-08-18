#!/usr/bin/env python3
"""Exact finite certificates for D.103 graph-norm audit."""

from fractions import Fraction


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mobius(n):
    value = n
    primes = 0
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            primes += 1
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        primes += 1
    return -1 if primes % 2 else 1


def main() -> None:
    cutoff = 6
    zeta = [[Fraction(1 if (m + 1) % (n + 1) == 0 else 0)
             for n in range(cutoff)] for m in range(cutoff)]
    gram = matmul(transpose(zeta), zeta)

    # Mixed-prime and prime-power mismatches.
    assert gram[1][2] == 1  # columns 2 and 3 meet at 6
    assert gram[0][1] == 3  # multiples of 2 up to 6
    assert gram[0][3] == 1  # multiples of 4 up to 6
    assert gram[0][1] != gram[0][3]

    # Exact Mobius inverse and its growing first-column norm.
    inverse = [[Fraction(mobius((m + 1) // (n + 1))
                                if (m + 1) % (n + 1) == 0 else 0)
                for n in range(cutoff)] for m in range(cutoff)]
    identity = matmul(zeta, inverse)
    for i in range(cutoff):
        for j in range(cutoff):
            assert identity[i][j] == (1 if i == j else 0)
    squarefree_count = sum(mobius(n) ** 2 for n in range(1, cutoff + 1))
    first_column_norm_sq = sum(inverse[i][0] ** 2 for i in range(cutoff))
    assert first_column_norm_sq == squarefree_count

    # Any strictly positive diagonal target weight leaves the 2--3 cross term.
    weights = [Fraction(k + 1) for k in range(cutoff)]
    weighted_cross = sum(
        weights[m] * zeta[m][1] * zeta[m][2] for m in range(cutoff)
    )
    assert weighted_cross == weights[5] > 0

    print("D103 graph-norm certificates: PASS")
    print("Gram (2,3), (1,2), (1,4):", gram[1][2], gram[0][1], gram[0][3])
    print("Mobius first-column norm squared:", first_column_norm_sq)
    print("positive weighted 2--3 cross term:", weighted_cross)


if __name__ == "__main__":
    main()
