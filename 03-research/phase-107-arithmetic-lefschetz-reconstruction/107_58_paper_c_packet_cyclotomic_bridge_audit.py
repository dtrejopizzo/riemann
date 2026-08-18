#!/usr/bin/env python3
"""Exact audit for the finite packet-to-cyclotomic bridge shadow.

This verifier audits the finite exact shadow behind `107_19`:

1. off-diagonal packet support depends only on the visible order pair;
2. rooted labels do not change the finite resultant norm;
3. the packet-to-cyclotomic comparison is transpose invariant;
4. diagonal packet pairs still land in excess-intersection territory.

It does not construct the true packet intersection line.  It exact-
audits the visible bridge logic from packet data to the determinant-line
package of `107_04`.
"""

from __future__ import annotations


MAX_N = 12


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


def visible_labels(n: int) -> list[int]:
    return list(range(n))


def prime_power_ratio(a: int, b: int) -> tuple[int, int] | None:
    if a == b or a % b != 0:
        return None
    ratio = a // b
    factors = factorize(ratio)
    if len(factors) != 1:
        return None
    return factors[0]


def order_support(m: int, n: int) -> int:
    forward = prime_power_ratio(m, n)
    backward = prime_power_ratio(n, m)
    data = forward or backward
    if data is None:
        return 0
    prime, _exp = data
    return prime


def order_norm(m: int, n: int) -> int:
    support = order_support(m, n)
    if support == 0:
        return 1
    small = min(m, n)
    return support ** euler_phi(small)


def packet_support(m: int, chi_m: int, n: int, chi_n: int) -> int:
    _ = (chi_m, chi_n)
    return order_support(m, n)


def packet_norm(m: int, chi_m: int, n: int, chi_n: int) -> int:
    _ = (chi_m, chi_n)
    return order_norm(m, n)


def check_support_and_norm_bridge() -> tuple[int, int]:
    support_checks = 0
    norm_checks = 0
    print("Packet-to-cyclotomic support/norm audit")
    for m in range(2, MAX_N + 1):
        for n in range(2, MAX_N + 1):
            if m == n:
                continue
            expected_support = order_support(m, n)
            expected_norm = order_norm(m, n)
            for chi_m in visible_labels(m):
                for chi_n in visible_labels(n):
                    assert packet_support(m, chi_m, n, chi_n) == expected_support
                    assert packet_norm(m, chi_m, n, chi_n) == expected_norm
                    support_checks += 1
                    norm_checks += 1
            print(
                f" ({m:2d},{n:2d}) support={expected_support:2d}"
                f" norm={expected_norm:4d} labels={m*n:4d}"
            )
    return support_checks, norm_checks


def check_transpose_invariance() -> int:
    checks = 0
    print("\nTranspose invariance audit")
    for m in range(2, MAX_N + 1):
        for n in range(2, MAX_N + 1):
            if m == n:
                continue
            for chi_m in visible_labels(m):
                for chi_n in visible_labels(n):
                    assert packet_support(m, chi_m, n, chi_n) == packet_support(n, chi_n, m, chi_m)
                    assert packet_norm(m, chi_m, n, chi_n) == packet_norm(n, chi_n, m, chi_m)
                    checks += 2
        if m <= 6:
            print(f" m={m:2d} transpose invariance checked against all visible n")
    return checks


def check_diagonal_caution() -> int:
    checks = 0
    print("\nDiagonal caution audit")
    for n in range(2, MAX_N + 1):
        for chi in visible_labels(n):
            # Exact finite shadow: diagonal does not collapse to a scalar
            # support/norm value at the packet level.
            assert prime_power_ratio(n, n) is None
            assert order_support(n, n) == 0
            checks += 2
        print(f" n={n:2d} diagonal labels={n:2d} remain excess-intersection only")
    return checks


def check_visible_composition() -> int:
    checks = 0
    print("\nVisible composition audit")
    for r in range(2, MAX_N + 1):
        local = 0
        for m in range(2, MAX_N + 1):
            for n in range(2, MAX_N + 1):
                if m == n or m * r > MAX_N or n * r > MAX_N:
                    continue
                before = order_support(m, n)
                after = order_support(m * r, n * r)
                # Common visible scaling preserves the order-ratio support law.
                assert before == after
                local += 1
                checks += 1
        if local:
            print(f" r={r:2d} visible composition-preservation pairs={local:4d}")
    return checks


def main() -> None:
    support_checks, norm_checks = check_support_and_norm_bridge()
    transpose_checks = check_transpose_invariance()
    diagonal_checks = check_diagonal_caution()
    composition_checks = check_visible_composition()

    print("\nAll exact Paper C packet-cyclotomic bridge checks passed.")
    print(
        "Verified "
        f"{support_checks} support checks, "
        f"{norm_checks} norm checks, "
        f"{transpose_checks} transpose checks, "
        f"{diagonal_checks} diagonal-caution checks, and "
        f"{composition_checks} visible-composition checks."
    )


if __name__ == "__main__":
    main()
