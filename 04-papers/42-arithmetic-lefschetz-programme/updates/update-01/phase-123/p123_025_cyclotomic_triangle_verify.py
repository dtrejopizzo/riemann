#!/usr/bin/env python3
"""Exact polynomial and matrix regressions for P123.025, not a proof of B."""
from math import gcd


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def divexact(a, b):
    a, b = trim(a), trim(b)
    assert b[-1] == 1
    q = [0] * max(1, len(a)-len(b)+1)
    while len(a) >= len(b) and a != [0]:
        k, v = len(a)-len(b), a[-1]
        q[k] = v
        for j, bj in enumerate(b):
            a[k+j] -= v*bj
        a = trim(a)
    assert a == [0], a
    return trim(q)


def substitute(a, m):
    b = [0] * ((len(a)-1)*m+1)
    for i, x in enumerate(a):
        b[i*m] = x
    return trim(b)


def bareiss(a):
    a = [row[:] for row in a]
    n, den, sign = len(a), 1, 1
    if not n:
        return 1
    for k in range(n-1):
        if not a[k][k]:
            pivot = next((i for i in range(k+1, n) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        p = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                num = p*a[i][j]-a[i][k]*a[k][j]
                assert num % den == 0
                a[i][j] = num//den
        for i in range(k+1, n):
            a[i][k] = 0
        den = p
    return sign*a[-1][-1]


def fixed_matrix(p):
    """I-T in the integral basis 1,T,... of Z[T]/p(T)."""
    d = len(p)-1
    a = [[int(i == j) for j in range(d)] for i in range(d)]
    for j in range(d-1):
        a[j+1][j] -= 1
    for i in range(d):
        a[i][-1] += p[i]
    return a


phis = {}
for n in range(1, 145):
    polynomial = [-1]+[0]*(n-1)+[1]
    for d in range(1, n):
        if n % d == 0:
            polynomial = divexact(polynomial, phis[d])
    phis[n] = polynomial

for n in range(2, 31):
    total = [-1]+[0]*(n-1)+[1]
    p = phis[n]
    q = divexact(total, p)
    assert mul(p, q) == total
    assert sum(q) == 0
    a = sum(p)
    assert a > 0
    # Independent integral matrix determinant calculation of the contact index.
    assert bareiss(fixed_matrix(p)) == a
    # Resolution quotient chain map has degree -1 P, degree 0 identity.
    # After evaluation its H^-1 map is a, and H^0 map is identity.
    assert sum(mul(p, q)) == a*sum(q) == 0
print('PASS integral filtration and fixed-contact determinant checks for 2 <= n <= 30')

for m in range(1, 13):
    for n in range(2, 13):
        indices = [d for d in range(1, m*n+1) if d//gcd(d, m) == n]
        rhs = [1]
        for d in indices:
            rhs = mul(rhs, phis[d])
        assert substitute(phis[n], m) == rhs, (m, n, indices)
        assert sum(substitute(phis[n], m)) == sum(phis[n])
assert substitute(phis[2], 2) == phis[4]
assert substitute(phis[3], 2) == mul(phis[3], phis[6])
assert substitute(phis[2], 3) == mul(phis[2], phis[6])
assert substitute(phis[3], 2) != phis[6]
assert sum(substitute(phis[3], 2)) == 3 != sum(phis[6])
assert sum(substitute(phis[2], 3)) == 2 != sum(phis[6])
print('PASS exact power-pullback component formula for 1 <= m <= 12, 2 <= n <= 12')

for n, wanted in [(2,2),(4,2),(3,3),(6,1)]:
    assert sum(phis[n]) == wanted
    print(f'n={n}: horizontal H^-1 map is multiplication by {wanted}; '
          f'contact cokernel Z/{wanted}')
def remainder(a, p):
    a = trim(a)
    while len(a) >= len(p):
        k, v = len(a)-len(p), a[-1]
        for i, x in enumerate(p):
            a[k+i] -= v*x
        a = trim(a)
    return a


for n, expected, smith in [
    (2, [[-2]], (2,)),
    (3, [[-1,-1],[1,-2]], (1,3)),
    (4, [[-2,0],[0,-2]], (2,2)),
    (6, [[-2,2],[-2,-4]], (2,6)),
]:
    p = phis[n]
    q = divexact([-1]+[0]*(n-1)+[1], p)
    d = len(p)-1
    matrix = [[0]*d for _ in range(d)]
    for j in range(d):
        col = remainder([0]*j+q, p)
        for i, x in enumerate(col):
            matrix[i][j] = x
    assert matrix == expected
    index = abs(bareiss(matrix))
    entry_gcd = gcd(*(x for row in matrix for x in row))
    computed = (index,) if d == 1 else (entry_gcd, index//entry_gcd)
    assert computed == smith
assert remainder([1,-1,1], phis[6]) == [0]  # T(T-1) = -1 on G_6.
print('PASS P123.026 integral gluing matrices and Smith invariants for 2,4,3,6')
print('SCOPE: polynomial/resolution regressions; no common diagonal, analytic realization, RR or RH')
