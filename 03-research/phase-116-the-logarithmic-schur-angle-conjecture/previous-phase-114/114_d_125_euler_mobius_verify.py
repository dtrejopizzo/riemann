#!/usr/bin/env python3
"""Exact finite certificates for D.125 Euler--Mobius renewal audit."""

from fractions import Fraction


def factor(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def mobius(n):
    fac = factor(n)
    return 0 if any(k > 1 for k in fac.values()) else (-1) ** len(fac)


def degree(n):
    # An exact additive surrogate for log n: assign prime p the rational p.
    return sum(Fraction(p*k) for p, k in factor(n).items())


def von_mangoldt_degree(n):
    fac = factor(n)
    return Fraction(next(iter(fac))) if len(fac) == 1 else Fraction(0)


def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))]
            for i in range(len(a))]


def sub(a, b):
    return [[a[i][j]-b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def main() -> None:
    nmax = 18
    # Omit central square roots in the matrix certificate; the derivation
    # and Mobius identities are unchanged by the multiplicative weight.
    z = [[Fraction(0) for _ in range(nmax)] for _ in range(nmax)]
    m = [[Fraction(0) for _ in range(nmax)] for _ in range(nmax)]
    d = [[Fraction(0) for _ in range(nmax)] for _ in range(nmax)]
    for n in range(1, nmax+1):
        d[n-1][n-1] = degree(n)
        for q in range(1, nmax+1):
            if n % q == 0:
                divisor = n // q
                z[n-1][q-1] = 1
                m[n-1][q-1] = mobius(divisor)
    identity = [[Fraction(i == j) for j in range(nmax)]
                for i in range(nmax)]
    assert matmul(z, m) == identity

    commutator = sub(matmul(d, z), matmul(z, d))
    contact = matmul(commutator, m)
    for n in range(1, nmax+1):
        assert contact[n-1][0] == von_mangoldt_degree(n)

    # A Gram square of the contact is not its Hermitian linearization.
    ct = [list(row) for row in zip(*contact)]
    square = matmul(ct, contact)
    linear = [[contact[i][j] + ct[i][j] for j in range(nmax)]
              for i in range(nmax)]
    assert square != linear

    # Finite central Mobius first-column norms increase.
    norm6 = sum(Fraction(mobius(n)**2, n) for n in range(1, 7))
    norm18 = sum(Fraction(mobius(n)**2, n) for n in range(1, 19))
    assert norm18 > norm6

    print("D125 Euler-Mobius renewal certificates: PASS")
    print("triangular inverse and logarithmic commutator: exact")
    print("contact square differs from linear contact")
    print("Mobius central column norms:", norm6, norm18)


if __name__ == "__main__":
    main()
