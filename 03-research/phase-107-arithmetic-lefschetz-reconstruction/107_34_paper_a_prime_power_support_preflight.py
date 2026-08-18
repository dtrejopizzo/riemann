#!/usr/bin/env python3
"""Exact audit for the finite prime-power support law of Paper A.

This script independently checks the core arithmetic content of
`107_04`: for off-diagonal cyclotomic pairs `(m,n)` with `m > n > 1`,
the resultant support is prime-power only, and on the diagonal the
resultant vanishes rather than producing a finite scalar.
"""

from __future__ import annotations

from math import isqrt


MAX_N = 24


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def euler_phi(n: int) -> int:
    result = n
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            result -= result // p
        p += 1
    if x > 1:
        result -= result // x
    return result


def factorize(n: int) -> list[tuple[int, int]]:
    factors: list[tuple[int, int]] = []
    x = n
    p = 2
    while p * p <= x:
        exp = 0
        while x % p == 0:
            x //= p
            exp += 1
        if exp:
            factors.append((p, exp))
        p += 1
    if x > 1:
        factors.append((x, 1))
    return factors


def prime_power_ratio(m: int, n: int) -> int | None:
    if m % n != 0:
        return None
    ratio = m // n
    factors = factorize(ratio)
    if len(factors) != 1:
        return None
    return factors[0][0]


def poly_trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_div_exact(dividend: list[int], divisor: list[int]) -> list[int]:
    work = dividend[:]
    quotient = [0] * (len(work) - len(divisor) + 1)
    assert divisor[-1] == 1
    while len(work) >= len(divisor):
        coeff = work[-1]
        shift = len(work) - len(divisor)
        quotient[shift] = coeff
        for i, value in enumerate(divisor):
            work[shift + i] -= coeff * value
        poly_trim(work)
    assert work == [0] or work == []
    return poly_trim(quotient)


def poly_equal(left: list[int], right: list[int]) -> bool:
    return poly_trim(left[:]) == poly_trim(right[:])


def poly_mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return poly_trim(out)


def cyclotomic_polynomials(limit: int) -> dict[int, list[int]]:
    polys: dict[int, list[int]] = {1: [-1, 1]}
    for n in range(2, limit + 1):
        poly = [-1] + [0] * (n - 1) + [1]
        for d in divisors(n)[:-1]:
            poly = poly_div_exact(poly, polys[d])
        polys[n] = poly
    return polys


def bareiss_det(matrix: list[list[int]]) -> int:
    work = [row[:] for row in matrix]
    size = len(work)
    if size == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(size - 1):
        if work[k][k] == 0:
            swap = None
            for i in range(k + 1, size):
                if work[i][k] != 0:
                    swap = i
                    break
            if swap is None:
                return 0
            work[k], work[swap] = work[swap], work[k]
            sign *= -1
        pivot = work[k][k]
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                work[i][j] = (
                    work[i][j] * pivot - work[i][k] * work[k][j]
                ) // prev
        prev = pivot
        for i in range(k + 1, size):
            work[i][k] = 0
        for j in range(k + 1, size):
            work[k][j] = 0
    return sign * work[-1][-1]


def resultant(poly_f: list[int], poly_g: list[int]) -> int:
    deg_f = len(poly_f) - 1
    deg_g = len(poly_g) - 1
    rev_f = list(reversed(poly_f))
    rev_g = list(reversed(poly_g))
    sylvester: list[list[int]] = []
    for i in range(deg_g):
        sylvester.append([0] * i + rev_f + [0] * (deg_g - 1 - i))
    for i in range(deg_f):
        sylvester.append([0] * i + rev_g + [0] * (deg_f - 1 - i))
    return bareiss_det(sylvester)


def prime_support(value: int) -> list[int]:
    if value == 0:
        return []
    return [p for p, _ in factorize(abs(value))]


def main() -> None:
    polys = cyclotomic_polynomials(MAX_N)

    for n in range(1, MAX_N + 1):
        product = [1]
        for d in divisors(n):
            product = poly_mul(product, polys[d])
        target = [-1] + [0] * (n - 1) + [1]
        assert poly_equal(product, target)

    print("Diagonal audit")
    for n in range(1, MAX_N + 1):
        diag = resultant(polys[n], polys[n])
        assert diag == 0
        print(f" n={n:2d}  Res(Phi_{n}, Phi_{n}) = 0")

    print("\nOff-diagonal prime-power support audit")
    print(" m   n     |Res|   phi(n)  expected support")
    checks = 0
    for m in range(2, MAX_N + 1):
        for n in range(2, m):
            actual = abs(resultant(polys[m], polys[n]))
            prime = prime_power_ratio(m, n)
            if prime is None:
                expected = 1
                expected_support: list[int] = []
            else:
                expected = prime ** euler_phi(n)
                expected_support = [prime]
            assert actual == expected
            assert prime_support(actual) == expected_support
            reverse = abs(resultant(polys[n], polys[m]))
            assert reverse == actual
            checks += 1
            print(
                f"{m:2d} {n:3d} {actual:9d} {euler_phi(n):8d}"
                f"  {expected_support}"
            )

    print(f"\nAll exact Paper A finite-support checks passed for 1 <= n <= {MAX_N}.")
    print(f"Verified {checks} off-diagonal pairs and {MAX_N} diagonal pairs.")


if __name__ == "__main__":
    main()
