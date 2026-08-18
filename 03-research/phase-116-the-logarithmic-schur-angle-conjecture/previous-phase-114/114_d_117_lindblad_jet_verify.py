#!/usr/bin/env python3
"""Finite exact certificates for D.117 source-derived Lindblad audit."""

from fractions import Fraction
from math import gcd


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))]
            for i in range(len(a))]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def identity(n):
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def cyclic_shift(n, step):
    s = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for j in range(n):
        s[(j + step) % n][j] = 1
    return s


def quadratic(a, x):
    return sum(x[i] * a[i][j] * x[j]
               for i in range(len(x)) for j in range(len(x)))


def main() -> None:
    # A finite translation jump is exactly (I-S)^*(I-S), hence positive.
    n = 7
    s = cyclic_shift(n, 2)
    i = identity(n)
    d = sub(i, s)
    lap_factor = matmul(transpose(d), d)
    lap_expanded = sub(scale(2, i), add(s, transpose(s)))
    assert lap_factor == lap_expanded
    for x in ([Fraction(k - 3) for k in range(n)],
              [Fraction((-1) ** k) for k in range(n)]):
        assert quadratic(lap_factor, x) >= 0

    # On a cyclic approximation the kernel of several jumps consists of
    # vectors constant on the subgroup orbits.  Coprime steps 2 and 3 on
    # seven sites generate the whole cycle, so only constants remain.
    s2 = cyclic_shift(n, 2)
    s3 = cyclic_shift(n, 3)
    l2 = matmul(transpose(sub(i, s2)), sub(i, s2))
    l3 = matmul(transpose(sub(i, s3)), sub(i, s3))
    total = add(l2, l3)
    ones = [Fraction(1) for _ in range(n)]
    assert quadratic(total, ones) == 0
    assert gcd(gcd(2, 3), n) == 1
    nonconstant_jet = [Fraction(2) ** k for k in range(n)]
    assert quadratic(total, nonconstant_jet) > 0

    # Exact boundary expansion for a unitary shift:
    # w||F-SF||^2 = 2w||F||^2 - 2w Re<F,SF>.
    w = Fraction(5, 13)
    norm2 = Fraction(17, 7)
    correlation = Fraction(-2, 9)
    energy = w * (2 * norm2 - 2 * correlation)
    expanded = 2 * w * norm2 - 2 * w * correlation
    assert energy == expanded

    # Source factorization at a toy prime with Green depth rho^k.
    contact = Fraction(7, 1)  # represents log p symbolically
    rho = Fraction(1, 3)      # represents p^{-1/2}
    weights = [contact * rho**k for k in range(1, 5)]
    assert weights[2] == contact * rho**3
    assert all(weights[k + 1] == rho * weights[k]
               for k in range(len(weights) - 1))

    # Positivity L>=0 does not imply the shifted sharp bound L>=cI.
    positive_spectrum = [Fraction(0), Fraction(1), Fraction(4)]
    requested_shift = Fraction(2)
    assert min(positive_spectrum) >= 0
    assert min(positive_spectrum) < requested_shift

    print("D117 source Lindblad/jet certificates: PASS")
    print("jump Laplacian factorization: exact")
    print("constant/jet energies:", quadratic(total, ones),
          quadratic(total, nonconstant_jet))
    print("source depth weights:", weights)
    print("positive versus requested spectral edge:",
          min(positive_spectrum), requested_shift)


if __name__ == "__main__":
    main()
