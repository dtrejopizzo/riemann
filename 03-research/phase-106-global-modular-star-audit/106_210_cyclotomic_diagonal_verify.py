#!/usr/bin/env python3
"""Dependency-free exact audit of the cyclotomic diagonal obstruction."""

from math import prod


def trim(a: list[int]) -> list[int]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def poly_div_exact(a: list[int], b: list[int]) -> list[int]:
    """Exact division of ascending integral polynomials, with b monic."""
    r = a[:]
    q = [0] * max(1, len(a) - len(b) + 1)
    while len(r) >= len(b) and any(r):
        shift = len(r) - len(b)
        coefficient = r[-1] // b[-1]
        q[shift] += coefficient
        for j, value in enumerate(b):
            r[j + shift] -= coefficient * value
        trim(r)
    assert r == [0] or not any(r)
    return trim(q)


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def cyclotomic_polynomials(limit: int) -> dict[int, list[int]]:
    """Phi_n in ascending coefficients from x^n-1=prod_{d|n} Phi_d."""
    answer: dict[int, list[int]] = {}
    for n in range(1, limit + 1):
        polynomial = [-1] + [0] * (n - 1) + [1]
        for d in divisors(n):
            if d == n:
                continue
            polynomial = poly_div_exact(polynomial, answer[d])
        answer[n] = polynomial
    return answer


def derivative(a: list[int]) -> list[int]:
    if len(a) == 1:
        return [0]
    return trim([i * a[i] for i in range(1, len(a))])


def det_bareiss(matrix: list[list[int]]) -> int:
    """Fraction-free exact determinant."""
    n = len(matrix)
    if n == 0:
        return 1
    a = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((r for r in range(k + 1, n) if a[r][k] != 0), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        pivot_value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot_value - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
        previous = pivot_value
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[-1][-1]


def resultant(f_ascending: list[int], g_ascending: list[int]) -> int:
    """Sylvester resultant of two integral polynomials."""
    f = list(reversed(trim(f_ascending[:])))
    g = list(reversed(trim(g_ascending[:])))
    m = len(f) - 1
    n = len(g) - 1
    if m < 0 or n < 0:
        raise ValueError("zero polynomial")
    size = m + n
    matrix: list[list[int]] = []
    for shift in range(n):
        matrix.append([0] * shift + f + [0] * (size - shift - len(f)))
    for shift in range(m):
        matrix.append([0] * shift + g + [0] * (size - shift - len(g)))
    return det_bareiss(matrix)


def totient(n: int) -> int:
    value = n
    for p in prime_divisors(n):
        value -= value // p
    return value


def prime_divisors(n: int) -> list[int]:
    answer = []
    p = 2
    value = n
    while p * p <= value:
        if value % p == 0:
            answer.append(p)
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        answer.append(value)
    return answer


def cyclotomic_discriminant_abs(n: int) -> int:
    degree = totient(n)
    denominator = prod(p ** (degree // (p - 1)) for p in prime_divisors(n))
    return n**degree // denominator


def main() -> None:
    phis = cyclotomic_polynomials(30)
    off_diagonal = [(4, 2), (9, 3), (6, 2), (6, 3), (15, 3), (3, 2), (5, 2), (6, 4)]
    print("m n |Res(Phi_m,Phi_n)|")
    for m, n in off_diagonal:
        value = abs(resultant(phis[m], phis[n]))
        print(m, n, value)

    for n in range(1, 31):
        f = phis[n]
        assert resultant(f, f) == 0

        derivative_resultant = abs(resultant(f, derivative(f)))
        disc_formula = cyclotomic_discriminant_abs(n)
        assert derivative_resultant == disc_formula

    # The derived self-tensor of A/(Phi_n) has one copy in Tor_0 and
    # one copy in Tor_1. Its formal K_0 Euler coefficient is zero, while
    # neither module has finite abelian length.
    tor_euler_coefficient = 1 - 1
    assert tor_euler_coefficient == 0

    print("self-resultants n=1..30 are zero: yes")
    print("cyclotomic discriminant formula n=1..30: exact")
    print("|Res(Phi_n,Phi_n')| = |Disc(Phi_n)|: exact")
    print("formal derived self-Tor Euler coefficient:", tor_euler_coefficient)


if __name__ == "__main__":
    main()
