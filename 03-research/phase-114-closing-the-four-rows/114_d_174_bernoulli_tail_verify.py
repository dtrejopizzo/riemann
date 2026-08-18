#!/usr/bin/env python3
"""Numerical checks for the exact identities and tail bound in D.174."""

import math
import mpmath as mp

mp.mp.dps = 400
L = mp.log(5)


def q_exact(x):
    return x * mp.exp(3 * x / 2) / mp.expm1(2 * x)


def coefficients(count):
    # Divide exp(3x/2) by (exp(2x)-1)/x in formal power series.
    numerator = [(mp.mpf(3) / 2) ** n / mp.factorial(n) for n in range(count)]
    denominator = [mp.mpf(2) ** (n + 1) / mp.factorial(n + 1) for n in range(count)]
    result = [mp.mpf(0)] * count
    for n in range(count):
        result[n] = (
            numerator[n]
            - mp.fsum(denominator[k] * result[n - k] for k in range(1, n + 1))
        ) / denominator[0]
    return result


def epsilon_bound(M):
    ratio = L / mp.pi
    u = 3 * L / 2
    J = math.ceil(M / 2)
    total = 1 + L + 2 * mp.zeta(2) * ratio**2 / (1 - ratio**2)
    tail_a = (
        2
        * mp.zeta(2)
        * ratio ** (2 * math.ceil(J / 2))
        / (1 - ratio**2)
    )
    tail_e = u**J / mp.factorial(J) / (1 - u / (J + 1))
    return (mp.exp(u) * tail_a + total * tail_e) / 2


for M in (20, 40, 80, 150):
    coeff = coefficients(M)
    epsilon = epsilon_bound(M)
    for j in range(1, 200):
        x = L * j / 200
        approximation = mp.fsum(coeff[n] * x**n for n in range(M))
        assert abs(q_exact(x) - approximation) <= epsilon * (x / L) ** M

# r_1(0)=log(2)+pi/4 and r_1'=(1/2-q)/x.
for x in (mp.mpf("0.001"), mp.mpf("0.2"), L):
    y = mp.exp(-x / 2)
    h1 = mp.atanh(y) + mp.atan(y)
    r1 = h1 + mp.log(x) / 2
    derivative = mp.diff(
        lambda z: mp.atanh(mp.exp(-z / 2))
        + mp.atan(mp.exp(-z / 2))
        + mp.log(z) / 2,
        x,
    )
    assert abs(derivative - (mp.mpf("0.5") - q_exact(x)) / x) < mp.mpf("1e-90")
    if x == mp.mpf("0.001"):
        assert abs(r1 - (mp.log(2) + mp.pi / 4)) < mp.mpf("0.001")

print("D174 Bernoulli polynomialization checks: PASS")
