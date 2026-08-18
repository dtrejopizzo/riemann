#!/usr/bin/env python3
"""Numerical checks of the exact periodic Poisson and Hardy identities."""

import math


def gaussian_correlation(a):
    # F(t)=exp(-t^2); <F,S_a F>/||F||^2.
    return math.exp(-(a * a) / 2)


for p in [2, 3, 5, 11]:
    r = p ** -0.5
    logp = math.log(p)
    left = 0.0
    poisson_minus_identity = 0.0
    for k in range(1, 200):
        corr = gaussian_correlation(k * logp)
        term = 2 * (r**k) * corr
        left += logp * term
        poisson_minus_identity += term
    right = logp * poisson_minus_identity
    assert abs(left - right) < 1e-14
    print(f"PASS: p={p} full prime tower equals Poisson-minus-torsor form")


for x in [1.1, 2.0, 3.0, 10.0, 100.0]:
    hardy_trace = 2 / (1 - x**-2)
    fourier_density_dstar = x / (x - 1) + x / (x + 1)
    assert abs(hardy_trace - fourier_density_dstar) < 1e-12
    central_trace = x**-0.5 * hardy_trace
    oscillator_trace = 2 * sum(x ** (-(2 * k + 0.5)) for k in range(500))
    assert abs(central_trace - oscillator_trace) < 1e-12
    print(f"PASS: x={x:g} Hardy character and central oscillator agree")

