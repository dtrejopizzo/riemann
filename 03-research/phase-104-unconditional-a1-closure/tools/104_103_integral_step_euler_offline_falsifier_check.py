#!/usr/bin/env python3
"""Reproduction checks for 104_103.

The analytic continuation is proved in the document.  Here we check the
rounded 0-1 construction numerically and the Euler composition identity
coefficient-by-coefficient with exact integer vectors for logarithms.
"""

from __future__ import annotations

import cmath
import math
from collections import defaultdict


def density(x: float, beta: float, gamma: float) -> float:
    return (1.0 - 2.0 * x ** (beta - 1.0) * math.cos(gamma * math.log(x))) / math.log(x)


def cell_integral(n: int, beta: float, gamma: float) -> float:
    """Two-point Gauss integral on [n,n+1]."""
    mid = n + 0.5
    off = 0.5 / math.sqrt(3.0)
    return 0.5 * (density(mid - off, beta, gamma) + density(mid + off, beta, gamma))


def staircase(n0: int, n1: int, beta: float, gamma: float, wheel: int):
    f = 0.0
    f_at = {}
    for n in range(n0, n1):
        f += cell_integral(n, beta, gamma)
        f_at[n + 1] = f

    candidates = [n for n in range(n0 + 1, n1 + 1) if math.gcd(n, wheel) == 1]
    previous_floor = 0
    selected = []
    max_increment = 0
    min_increment = 1
    previous_f = 0.0
    tracking = 0.0
    count = 0
    for n in candidates:
        current_f = f_at[n]
        increment = math.floor(current_f) - previous_floor
        assert increment in (0, 1), (n, current_f, previous_floor, increment)
        max_increment = max(max_increment, increment)
        min_increment = min(min_increment, increment)
        if increment:
            selected.append(n)
        count += increment
        tracking = max(tracking, abs(count - current_f))
        previous_floor = math.floor(current_f)
        previous_f = current_f

    gaps = [b - a for a, b in zip(selected, selected[1:])]
    max_gap_ratio = max(g / math.log(a) for a, g in zip(selected, gaps))
    return selected, tracking, max_gap_ratio, min_increment, max_increment, previous_f


def factor_vector(n: int) -> dict[int, int]:
    ans = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            ans[d] = ans.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        ans[n] = ans.get(n, 0) + 1
    return ans


def add_scaled(dst: dict[int, int], src: dict[int, int], scale: int) -> None:
    for p, e in src.items():
        dst[p] = dst.get(p, 0) + scale * e


def euler_coefficients(generators: list[int], cutoff: int) -> dict[int, int]:
    g = {1: 1}
    for q in generators:
        old = list(g.items())
        additions = defaultdict(int)
        power = q
        while power <= cutoff:
            for m, coeff in old:
                if m * power <= cutoff:
                    additions[m * power] += coeff
            if power > cutoff // q:
                break
            power *= q
        for m, coeff in additions.items():
            g[m] = g.get(m, 0) + coeff
    return g


def mangoldt_vectors(generators: list[int], cutoff: int) -> dict[int, dict[int, int]]:
    lam: dict[int, dict[int, int]] = {}
    for q in generators:
        qvec = factor_vector(q)
        power = q
        while power <= cutoff:
            target = lam.setdefault(power, {})
            add_scaled(target, qvec, 1)
            if power > cutoff // q:
                break
            power *= q
    return lam


def divisors(n: int):
    small = []
    large = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
        d += 1
    return small + large[::-1]


def check_exact_composition(generators: list[int], cutoff: int) -> tuple[int, int]:
    g = euler_coefficients(generators, cutoff)
    lam = mangoldt_vectors(generators, cutoff)
    collisions = sum(1 for value in g.values() if value > 1)
    checked = 0
    for m, gm in g.items():
        left = {p: gm * e for p, e in factor_vector(m).items()}
        right: dict[int, int] = {}
        for d in divisors(m):
            if d in lam and m // d in g:
                add_scaled(right, lam[d], g[m // d])
        assert left == right, (m, left, right)
        checked += 1
    return checked, collisions


def e1_series(w: complex) -> complex:
    # E1(w) = -gamma-log(w)-sum_{k>=1} (-w)^k/(k*k!).
    total = 0j
    factorial = 1.0
    power = 1 + 0j
    for k in range(1, 80):
        factorial *= k
        power *= -w
        term = power / (k * factorial)
        total += term
        if abs(term) < 1e-18:
            break
    return -0.5772156649015328606 - cmath.log(w) - total


def check_log_coefficient(L: float) -> float:
    target = 0.5772156649015328606 + math.log(L)
    errors = []
    for j in range(3, 9):
        z = (10.0 ** (-j)) * (1.0 + 0.3j)
        value = -e1_series(z * L) - cmath.log(z)
        errors.append(abs(value - target))
    assert errors[-1] < 2e-7, errors
    assert errors[-1] < errors[0], errors
    return errors[-1]


def main() -> None:
    beta = 0.75
    gamma = 1.0

    selected, tracking, gap_ratio, amin, amax, _ = staircase(
        4096, 100000, beta, gamma, 6
    )
    assert all(math.gcd(n, 6) == 1 for n in selected)
    assert tracking < 1.0000001
    assert gap_ratio < 12.0
    assert amin == 0 and amax == 1

    # A smaller all-integer prefix makes products and norm collisions visible.
    small_selected, _, _, _, _, _ = staircase(64, 700, beta, gamma, 1)
    # The finite prefix [5,7,35] installs the norm collision prescribed
    # in (9a); it does not affect the tail profile.
    generators = [5, 7, 35] + small_selected[:39]
    checked, collisions = check_exact_composition(generators, 120000)
    assert collisions > 0

    log_error = check_log_coefficient(math.log(4096.0))

    print("104_103 integral-step Euler off-line falsifier: PASS")
    print(f"  wheel-prefix selected={len(selected)} tracking={tracking:.6g}")
    print(f"  max gap/log x={gap_ratio:.6g}")
    print(f"  exact Euler coefficients checked={checked} collisions={collisions}")
    print(f"  local +log(s-rho) coefficient error={log_error:.3e}")


if __name__ == "__main__":
    main()
