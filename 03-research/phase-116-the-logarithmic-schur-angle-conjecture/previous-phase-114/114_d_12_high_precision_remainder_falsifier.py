#!/usr/bin/env python3
"""High-precision witness disproving the sufficient inequality R_ar <= 0.

The test is C_c^infinity and satisfies both ruling moments identically.
Gauss--Legendre orders 16, 24 and 32 are printed to show stabilization.
This is a numerical falsifier, not a proof of any statement about RH.
"""

from __future__ import annotations

import mpmath as mp

mp.mp.dps = 35

L = mp.log(3)
H = mp.mpf(7) / 20
CENTERS = (-L, mp.mpf(0), L)
COEFFICIENTS = (mp.mpf(1), -2 * mp.cosh(L / 2), mp.mpf(1))
RADIUS = L + H
DIAMETER = 2 * RADIUS


def prime_power_terms(limit: int) -> list[tuple[int, int]]:
    """Return (p^k,p) up to limit."""
    primes: list[int] = []
    for n in range(2, limit + 1):
        if all(n % p for p in primes if p * p <= n):
            primes.append(n)
    terms: list[tuple[int, int]] = []
    for p in primes:
        q = p
        while q <= limit:
            terms.append((q, p))
            q *= p
    return sorted(terms)


def compute(order: int) -> dict[str, mp.mpf]:
    nodes, weights = mp.gauss_quadrature(order, "legendre")
    nodes = list(nodes)
    weights = list(weights)

    def bump(x: mp.mpf) -> mp.mpf:
        z = x / H
        if abs(z) >= 1:
            return mp.mpf(0)
        return mp.exp(-1 / (1 - z * z))

    def integrate(fun, a: mp.mpf, b: mp.mpf) -> mp.mpf:
        middle = (a + b) / 2
        half = (b - a) / 2
        return half * mp.fsum(
            w * fun(middle + half * x) for x, w in zip(nodes, weights)
        )

    def bump_correlation(a: mp.mpf) -> mp.mpf:
        a = abs(a)
        if a >= 2 * H:
            return mp.mpf(0)
        lower = max(-H, a - H)
        upper = min(H, a + H)
        return integrate(lambda u: bump(u) * bump(u - a), lower, upper)

    def correlation(a: mp.mpf) -> mp.mpf:
        return mp.fsum(
            COEFFICIENTS[i]
            * COEFFICIENTS[j]
            * bump_correlation(a + CENTERS[j] - CENTERS[i])
            for i in range(3)
            for j in range(3)
        )

    norm = correlation(mp.mpf(0))

    # For an even bump phi, its two exponential moments agree.  Translation
    # multiplies them by exp(+-center/2), and
    #  exp(-L/2)+exp(L/2)-2 cosh(L/2)=0.
    base_plus = integrate(lambda u: bump(u) * mp.exp(u / 2), -H, H)
    base_minus = integrate(lambda u: bump(u) * mp.exp(-u / 2), -H, H)
    moment_plus = base_plus * mp.fsum(
        c * mp.exp(x / 2) for c, x in zip(COEFFICIENTS, CENTERS)
    )
    moment_minus = base_minus * mp.fsum(
        c * mp.exp(-x / 2) for c, x in zip(COEFFICIENTS, CENTERS)
    )

    limit = int(mp.floor(mp.exp(DIAMETER)))
    contact = mp.fsum(
        2
        * mp.log(p)
        / mp.sqrt(n)
        * correlation(mp.log(n))
        for n, p in prime_power_terms(limit)
    )

    breakpoints = sorted(
        {
            mp.mpf(0),
            DIAMETER,
            2 * H,
            L - 2 * H,
            L,
            L + 2 * H,
            2 * L - 2 * H,
            2 * L,
            2 * L + 2 * H,
        }
    )
    breakpoints = [x for x in breakpoints if 0 <= x <= DIAMETER]

    def outer_integral(fun) -> mp.mpf:
        return mp.fsum(
            integrate(fun, breakpoints[i], breakpoints[i + 1])
            for i in range(len(breakpoints) - 1)
        )

    continuous_hodge = 2 * outer_integral(
        lambda a: mp.exp(a / 2) * correlation(a)
    )

    def archimedean_integrand(a: mp.mpf) -> mp.mpf:
        if a == 0:
            return mp.mpf(0)
        density = mp.exp(-a / 2) / (1 - mp.exp(-2 * a))
        return density * (2 * norm - 2 * correlation(a))

    archimedean_energy = outer_integral(archimedean_integrand)
    tail = mp.fsum(
        mp.exp(-(2 * j + mp.mpf("0.5")) * DIAMETER)
        / (2 * j + mp.mpf("0.5"))
        for j in range(150)
    )
    archimedean_energy += 2 * norm * tail
    m_zero = mp.log(mp.pi) - mp.digamma(mp.mpf("0.25"))
    green = m_zero * norm - archimedean_energy

    nuclear = contact + green
    remainder = nuclear - continuous_hodge
    return {
        "moment_minus": moment_minus,
        "moment_plus": moment_plus,
        "norm": norm,
        "contact": contact,
        "green": green,
        "continuous_hodge": continuous_hodge,
        "nuclear": nuclear,
        "remainder": remainder,
    }


if __name__ == "__main__":
    results = []
    for quadrature_order in (16, 24, 32):
        result = compute(quadrature_order)
        results.append(result)
        print(f"order={quadrature_order}")
        for key, value in result.items():
            print(f"  {key:18s} {mp.nstr(value, 22)}")

    final = results[-1]
    assert abs(final["moment_minus"]) < mp.mpf("1e-30")
    assert abs(final["moment_plus"]) < mp.mpf("1e-30")
    assert final["continuous_hodge"] < 0
    assert final["nuclear"] < 0
    assert final["remainder"] > mp.mpf("0.04")
    assert abs(results[-1]["remainder"] - results[-2]["remainder"]) < mp.mpf(
        "1e-6"
    )
    numerical_lower = mp.mpf("0.0463")
    numerical_upper = mp.mpf("0.0465")
    assert all(
        numerical_lower < result["remainder"] < numerical_upper
        for result in results
    )
    print("stable numerical enclosure: [0.0463, 0.0465]")
    print(
        "NUMERICAL VERDICT: robust positive witness; a rigorous sign "
        "certificate still requires interval/ball arithmetic."
    )
