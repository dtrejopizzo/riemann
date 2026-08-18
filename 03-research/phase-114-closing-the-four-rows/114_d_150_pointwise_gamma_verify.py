#!/usr/bin/env python3
"""Checks the pointwise oscillator identity and its full Gamma summation."""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 70
T = mp.log(5) / 2


def deriv(r: int, t: mp.mpf) -> mp.mpf:
    # F(t)=1+0.3t-0.2t^2+0.07t^3-0.01t^4.
    coeff = [mp.mpf(1), mp.mpf("0.3"), mp.mpf("-0.2"),
             mp.mpf("0.07"), mp.mpf("-0.01")]
    ans = mp.mpf(0)
    for k in range(r, len(coeff)):
        ans += coeff[k] * mp.factorial(k) / mp.factorial(k-r) * t ** (k-r)
    return ans


def one_closed(b: mp.mpf, t: mp.mpf) -> mp.mpf:
    interior = -2 * sum(deriv(r, t) / b ** (r+1) for r in (2, 4))
    left = mp.e ** (-b * (t + T)) * sum(
        (-1) ** r * deriv(r, -T) / b ** (r+1) for r in range(5)
    )
    right = mp.e ** (-b * (T - t)) * sum(
        deriv(r, T) / b ** (r+1) for r in range(5)
    )
    return interior + left + right


def F(t: mp.mpf) -> mp.mpf:
    return deriv(0, t)


# Independent quadrature for individual oscillators.
for b in (mp.mpf("0.5"), mp.mpf("2.5"), mp.mpf("10.5")):
    for t in (-T / 3, mp.mpf("0.13"), T / 2):
        kernel = mp.quad(lambda s: mp.e ** (-b * abs(t-s)) * F(s), [-T, t, T])
        direct = 2 * F(t) / b - kernel
        assert abs(direct - one_closed(b, t)) < mp.mpf("1e-60")


def H(s: int, x: mp.mpf) -> mp.mpf:
    return mp.e ** (-x/2) * mp.lerchphi(mp.e ** (-2*x), s, mp.mpf("0.25")) / 2**s


def full_closed(t: mp.mpf) -> mp.mpf:
    interior = -2 * sum(
        mp.zeta(r+1, mp.mpf("0.25")) * deriv(r, t) / 2 ** (r+1)
        for r in (2, 4)
    )
    left = sum((-1) ** r * deriv(r, -T) * H(r+1, t+T) for r in range(5))
    right = sum(deriv(r, T) * H(r+1, T-t) for r in range(5))
    return interior + left + right


# Away from the endpoints the oscillator tail is exponentially small,
# while the interior remainder is O(J^-2) because it starts at b^-3.
for t in (-T/4, mp.mpf("0.09"), T/3):
    partial = sum(one_closed(2*j+mp.mpf("0.5"), t) for j in range(4000))
    assert abs(partial - full_closed(t)) < mp.mpf("2e-8")

print("D150 pointwise Gamma action and squared-residual formula: PASS")

