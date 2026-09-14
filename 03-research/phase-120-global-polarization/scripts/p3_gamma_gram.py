#!/usr/bin/env python3
"""Numerical audit of the exact positive Gamma-reservoir factorization.

This script is reconnaissance for the analytic identity proved from the
digamma series in P3_FORMAL_SPEC_AND_AUDIT.md. It does not test row (d).
"""

import mpmath as mp

mp.mp.dps = 60


def gram_partial(tau, terms):
    t = mp.mpf(tau) / 2
    return mp.fsum(
        t * t / ((n + mp.mpf("0.25")) * ((n + mp.mpf("0.25")) ** 2 + t * t))
        for n in range(terms)
    )


def gram_exact(tau):
    z = mp.mpf("0.25") + mp.j * mp.mpf(tau) / 2
    return mp.re(mp.digamma(z)) - mp.digamma(mp.mpf("0.25"))


def tail_bound(tau, terms):
    # Since each summand <= t^2/(n+1/4)^3, bound the tail by the
    # corresponding Hurwitz zeta tail.
    t = mp.mpf(tau) / 2
    return t * t * mp.zeta(3, terms + mp.mpf("0.25"))


def heat_partial(tau, terms):
    # Corrected positive-carrier multiplier 2*integral c(u)(1-cos(tau*u))du.
    return 2 * mp.fsum(
        mp.mpf(tau) ** 2
        / ((2 * n + mp.mpf("0.5")) * ((2 * n + mp.mpf("0.5")) ** 2 + mp.mpf(tau) ** 2))
        for n in range(terms)
    )


print("tau       exact Gamma Gram          partial(2000)             error       tail bound")
for tau in (0, mp.mpf("0.1"), 1, 5, 20, 100):
    exact = gram_exact(tau)
    partial = gram_partial(tau, 2000)
    heat = heat_partial(tau, 2000)
    error = exact - partial
    bound = tail_bound(tau, 2000)
    assert exact >= 0
    assert error >= 0
    assert error <= bound
    assert mp.almosteq(partial, heat)
    print(
        f"{mp.nstr(tau, 6):>6}  {mp.nstr(exact, 20):>24}  "
        f"{mp.nstr(partial, 20):>24}  {mp.nstr(error, 6):>10}  {mp.nstr(bound, 6):>10}"
    )

m0_from_psi = mp.log(mp.pi) - mp.digamma(mp.mpf("0.25"))
m0_closed = mp.log(mp.pi) + mp.euler + mp.pi / 2 + 3 * mp.log(2)
assert mp.almosteq(m0_from_psi, m0_closed)
print("m0 identity:", mp.nstr(m0_from_psi, 30))
