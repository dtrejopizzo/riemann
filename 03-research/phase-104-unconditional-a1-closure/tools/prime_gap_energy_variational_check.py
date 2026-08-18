#!/usr/bin/env python3
"""Finite checks for 104_101.

This is a diagnostic/checker, not a certificate of an asymptotic theorem.
It checks the exact prime-gap decomposition and constructs the fixed-wheel
0--1 countermodel used in the no-go theorem.
"""

from __future__ import annotations

import math


def sieve(limit: int) -> list[bool]:
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if is_prime[p]:
            is_prime[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [bool(v) for v in is_prime]


def check_gap_identity(limit: int = 200_000) -> tuple[float, float]:
    # One extra prime is needed to close the last cell.
    work = 2 * limit
    isp = sieve(work)
    primes = [n for n in range(2, work + 1) if isp[n]]
    assert primes[-1] > limit

    q = [0.0] * (limit + 1)
    S = [0.0] * (limit + 1)
    pi = [0] * (limit + 1)
    count = 0
    for n in range(2, limit + 1):
        q[n] = 1.0 / math.log(n)
        S[n] = S[n - 1] + q[n]
        count += int(isp[n])
        pi[n] = count

    direct = sum(
        (pi[m] - S[m]) ** 2 / (m * (m + 1)) for m in range(2, limit + 1)
    )

    by_gaps = 0.0
    completed_square = 0.0
    for k0, p in enumerate(primes):
        if p > limit:
            break
        pnext = primes[k0 + 1]
        stop = min(pnext - 1, limit)
        d = (k0 + 1) - S[p]
        h = 0.0
        vals: list[tuple[float, float]] = []
        for m in range(p, stop + 1):
            if m > p:
                h += q[m]
            w = 1.0 / (m * (m + 1))
            vals.append((w, h))
            by_gaps += w * (d - h) ** 2

        W = sum(w for w, _ in vals)
        hbar = sum(w * h0 for w, h0 in vals) / W
        variance = sum(w * (h0 - hbar) ** 2 for w, h0 in vals)
        completed_square += W * (d - hbar) ** 2 + variance

        # On a complete gap the weight telescopes exactly.
        if stop == pnext - 1:
            assert abs(W - (1.0 / p - 1.0 / pnext)) < 2e-16

    err_gap = abs(direct - by_gaps)
    err_square = abs(direct - completed_square)
    assert err_gap < 2e-12
    assert err_square < 2e-12
    return err_gap, err_square


def check_fixed_wheel_model(
    limit: int = 1_000_000,
    start: int = 10_000,
    wheel: int = 30,
    beta: float = 0.75,
    c: float = 0.1,
) -> dict[str, float]:
    # F is the desired cumulative count after `start`.  At a wheel candidate
    # we copy floor(F); between candidates the count is held fixed.
    F = 0.0
    previous_floor: int | None = None
    A = 0
    qsum = 0.0
    energy = 0.0
    selected: list[int] = []
    tracking_values: list[float] = []

    previous_n = start - 1
    for n in range(start, limit + 1):
        qsum += 1.0 / math.log(n)
        F = qsum + c * (n**beta - start**beta)
        if math.gcd(n, wheel) == 1:
            target = math.floor(F)
            if previous_floor is None:
                previous_floor = target
            else:
                jump = target - previous_floor
                assert jump in (0, 1), (n, jump)
                if jump:
                    selected.append(n)
                    A += 1
                previous_floor = target

        if previous_floor is None:
            discrepancy = 0.0
        else:
            discrepancy = A - qsum
            # A-F is a bounded sawtooth.  Its additive constant depends on
            # the first candidate and is irrelevant to the asymptotic.
            tracking_values.append(A - F)
            energy += discrepancy * discrepancy / (n * (n + 1))
        previous_n = n

    assert previous_n == limit
    assert selected
    assert all(math.gcd(n, wheel) == 1 for n in selected)

    tracking_width = max(tracking_values) - min(tracking_values)
    assert tracking_width < 2.0

    max_gap_ratio = max(
        (v - u) / math.log(v) for u, v in zip(selected, selected[1:])
    )
    assert max_gap_ratio < 4.0

    drift = A - qsum
    scaled_drift = drift / (limit**beta)
    return {
        "selected": float(len(selected)),
        "tracking_width": tracking_width,
        "max_gap_over_log": max_gap_ratio,
        "terminal_scaled_drift": scaled_drift,
        "energy": energy,
        "polynomial_scale": limit ** (2 * beta - 1),
    }


def main() -> None:
    err_gap, err_square = check_gap_identity()
    model = check_fixed_wheel_model()
    print("104_101 prime-gap variational checker")
    print(f"gap identity absolute error       {err_gap:.3e}")
    print(f"completed-square absolute error  {err_square:.3e}")
    for key, value in model.items():
        print(f"{key:31s} {value:.12g}")
    print("PASS")


if __name__ == "__main__":
    main()
