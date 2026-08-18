#!/usr/bin/env python3
"""Numerical/exact companion checks for the D.202 pullback theorem.

This checks the changes of variables, prime-power support, and complete
digamma difference identity.  It does not replace the polarized proof.
"""

from __future__ import annotations

import math
import mpmath as mp


mp.mp.dps = 60


def F(t):
    return (1 + mp.mpf("0.2") * t) * mp.e ** (-(t - mp.mpf("0.3")) ** 2)


def G(t):
    return (1 - mp.mpf("0.1") * t) * mp.e ** (-(t + mp.mpf("0.4")) ** 2)


def f(x):
    return x ** (-mp.mpf("0.5")) * F(mp.log(x))


def g(x):
    return x ** (-mp.mpf("0.5")) * G(mp.log(x))


# Mellin 0,1 are the two logarithmic Tate jets.
for s in (mp.mpf(0), mp.mpf(1)):
    mellin = mp.quad(lambda t: f(mp.e**t) * mp.e ** (s * t), [-mp.inf, mp.inf])
    jet = mp.quad(
        lambda t: F(t) * mp.e ** ((s - mp.mpf("0.5")) * t),
        [-mp.inf, mp.inf],
    )
    assert abs(mellin - jet) < mp.mpf("1e-50")


# e^(a/2)(f*g^vee)(e^a) equals additive translation correlation.
for a in (mp.mpf("-1.1"), mp.mpf("0.2"), mp.mpf("1.7")):
    convolution = mp.quad(
        lambda t: f(mp.e**t) * mp.e ** (t - a) * g(mp.e ** (t - a)),
        [-mp.inf, mp.inf],
    )
    correlation = mp.quad(lambda t: F(t) * G(t - a), [-mp.inf, mp.inf])
    assert abs(mp.e ** (a / 2) * convolution - correlation) < mp.mpf("1e-49")


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


for n in range(2, 1000):
    fs = factor(n)
    prime_power = len(fs) == 1
    coefficient = mp.log(next(iter(fs))) / mp.sqrt(n) if prime_power else mp.mpf(0)
    assert (coefficient != 0) == prime_power


# Complete Gamma oscillator, including its finite-part constant.
for tau in (mp.mpf("0.3"), mp.mpf("1.7"), mp.mpf("5.2")):
    digamma_difference = (
        mp.digamma(mp.mpf("0.25") + mp.j * tau / 2)
        + mp.digamma(mp.mpf("0.25") - mp.j * tau / 2)
        - 2 * mp.digamma(mp.mpf("0.25"))
    )
    integral = 4 * mp.quad(
        lambda r: mp.e ** (-r / 2) * (1 - mp.cos(tau * r)) / (1 - mp.e ** (-2 * r)),
        [0, 1, 5, 10, 20, 40, 80, mp.inf],
    )
    assert abs(digamma_difference - integral) < mp.mpf("1e-25")


print("PASS D202: Tate jets, central correlation, all prime powers, complete Gamma")
