#!/usr/bin/env python3
"""Numerical verification of the exact finite kernel identity in D.156."""

import mpmath as mp

mp.mp.dps = 70
T = mp.log(5) / 2


def g(s: mp.mpf) -> mp.mpf:
    return 1 + 2 * s - 3 * s**2 + s**4


def direct(t: mp.mpf, jmax: int) -> mp.mpf:
    ans = mp.mpf("0")
    for j in range(jmax + 1):
        b = 2 * j + mp.mpf("0.5")
        conv = mp.quad(lambda s: mp.exp(-b * abs(t - s)) * g(s), [-T, t, T])
        ans += 2 * g(t) / b - conv
    return ans


def kernel(t: mp.mpf, jmax: int) -> mp.mpf:
    def kval(x: mp.mpf) -> mp.mpf:
        return sum(mp.exp(-(2 * j + mp.mpf("0.5")) * x) for j in range(jmax + 1))

    def hval(x: mp.mpf) -> mp.mpf:
        return sum(
            mp.exp(-(2 * j + mp.mpf("0.5")) * x)
            / (2 * j + mp.mpf("0.5"))
            for j in range(jmax + 1)
        )

    integ = mp.quad(lambda s: kval(abs(t - s)) * (g(t) - g(s)), [-T, t, T])
    return integ + (hval(t + T) + hval(T - t)) * g(t)


for jmax in (0, 2, 8, 24):
    for t in (-T / 3, mp.mpf("0.137"), 2 * T / 5):
        a = direct(t, jmax)
        b = kernel(t, jmax)
        assert abs(a - b) < mp.mpf("1e-55"), (jmax, t, a - b)

# Closed geometric kernel agrees with a long partial sum away from zero.
for x in (mp.mpf("0.02"), mp.mpf("0.3"), mp.mpf("1.1")):
    closed = mp.exp(-x / 2) / (1 - mp.exp(-2 * x))
    partial = sum(mp.exp(-(2 * j + mp.mpf("0.5")) * x) for j in range(4000))
    assert abs(closed - partial) < mp.mpf("1e-55")

print("D156 general Gamma singular-kernel identity: PASS")
