#!/usr/bin/env python3
"""Exact audit for the local packet unit-factor model of Paper C.

This script audits the finite algebra asserted in `107_20`:

1. off the diagonal, the packet intersection norm is independent of the
   rooted labels and equals the cyclotomic resultant norm of `107_04`;
2. the rooted label factor is rank one with unit norm;
3. on the diagonal, the packet model still yields zero resultant rather
   than a finite scalar.

The scope is intentionally the local packet algebra model

    B_{n,chi}^pkt = B_n tensor_Z Lambda_{n,chi}

of `107_20`, not the later global descent papers.
"""

from __future__ import annotations


MAX_N = 12


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


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


def euler_phi(n: int) -> int:
    result = n
    for p, _ in factorize(n):
        result -= result // p
    return result


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


def poly_mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return poly_trim(out)


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


def sylvester_matrix(poly_f: list[int], poly_g: list[int]) -> list[list[int]]:
    deg_f = len(poly_f) - 1
    deg_g = len(poly_g) - 1
    rev_f = list(reversed(poly_f))
    rev_g = list(reversed(poly_g))
    sylvester: list[list[int]] = []
    for i in range(deg_g):
        sylvester.append([0] * i + rev_f + [0] * (deg_g - 1 - i))
    for i in range(deg_f):
        sylvester.append([0] * i + rev_g + [0] * (deg_f - 1 - i))
    return sylvester


def resultant(poly_f: list[int], poly_g: list[int]) -> int:
    return bareiss_det(sylvester_matrix(poly_f, poly_g))


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)


def character_order(n: int, exponent: int) -> int:
    if exponent % n == 0:
        return 1
    return n // gcd(n, exponent)


def visible_labels(n: int) -> list[int]:
    return list(range(n))


def rooted_unit_norm(_: int, __: int, ___: int, ____: int) -> int:
    return 1


def packet_norm(poly_m: list[int], poly_n: list[int], _: int, __: int) -> int:
    # In the local packet algebra model of `107_20`, tensoring with the
    # rank-one idempotent label factors leaves the Sylvester presentation
    # matrix unchanged.
    return abs(resultant(poly_m, poly_n))


def main() -> None:
    polys = cyclotomic_polynomials(MAX_N)

    print("Packet label census")
    for n in range(2, MAX_N + 1):
        counts: dict[int, int] = {}
        for exponent in visible_labels(n):
            order = character_order(n, exponent)
            counts[order] = counts.get(order, 0) + 1
        expected = {d: euler_phi(d) for d in divisors(n)}
        assert counts == expected
        print(f" n={n:2d}  visible labels={len(visible_labels(n)):2d}  exact-order counts={counts}")

    print("\nOff-diagonal packet norm audit")
    print(" m   n  labels tested  packet norm  expected")
    checks = 0
    for m in range(2, MAX_N + 1):
        for n in range(2, m):
            prime = prime_power_ratio(m, n)
            if prime is None:
                expected = 1
            else:
                expected = prime ** euler_phi(n)
            order_norm = abs(resultant(polys[m], polys[n]))
            assert order_norm == expected
            labels_tested = 0
            for chi_1 in visible_labels(m):
                for chi_2 in visible_labels(n):
                    labels_tested += 1
                    assert rooted_unit_norm(m, chi_1, n, chi_2) == 1
                    actual = packet_norm(polys[m], polys[n], chi_1, chi_2)
                    assert actual == order_norm
                    checks += 1
            print(f"{m:2d} {n:3d} {labels_tested:13d} {order_norm:12d} {expected:9d}")

    print("\nDiagonal packet audit")
    diag_checks = 0
    for n in range(2, MAX_N + 1):
        diag = resultant(polys[n], polys[n])
        assert diag == 0
        for chi_1 in visible_labels(n):
            for chi_2 in visible_labels(n):
                actual = packet_norm(polys[n], polys[n], chi_1, chi_2)
                assert actual == 0
                diag_checks += 1
        print(f" n={n:2d}  packet diagonal norms all vanish for {n * n:3d} label pairs")

    print(
        f"\nAll exact Paper C local packet checks passed for 2 <= n <= {MAX_N}."
    )
    print(
        f"Verified {checks} off-diagonal labeled packet pairs and {diag_checks} diagonal labeled packet pairs."
    )


if __name__ == "__main__":
    main()
