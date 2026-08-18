#!/usr/bin/env python3
"""Numerical/exact audits for D.132.

Checks the multiscale B-spline attenuation, elementary coefficient bounds,
large-sieve recurrence scales and the resulting Logvinenko--Sereda loss.
It does not certify row D.
"""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np


def von_mangoldt_values(limit: int):
    lam = np.zeros(limit + 1)
    prime = np.ones(limit + 1, dtype=bool)
    prime[:2] = False
    for p in range(2, limit + 1):
        if not prime[p]:
            continue
        if p * p <= limit:
            prime[p * p : limit + 1 : p] = False
        q = p
        while q <= limit:
            lam[q] = math.log(p)
            q *= p
    idx = np.flatnonzero(lam)
    return idx, lam[idx]


def bands(T: float, eps: float):
    lo = math.log(2)
    lowers = []
    while lo < 2 * T:
        lowers.append(lo)
        lo *= 2
    J = len(lowers)
    data = []
    for lo in lowers:
        crude_mass = 4 * lo * math.exp(lo)
        m = math.ceil(
            (lo + math.log(4 * lo * J / eps)) / math.log(math.pi)
        )
        h = 2 * math.pi / lo
        assert crude_mass * math.pi ** (-m) <= eps / J
        data.append((lo, m, h, crude_mass))
    return data


def sinc(x: np.ndarray) -> np.ndarray:
    ans = np.ones_like(x)
    nz = x != 0
    ans[nz] = np.sin(x[nz]) / x[nz]
    return ans


# 1. The elementary band estimate |sinc x| <= 1/pi on [pi,2pi].
x = np.linspace(math.pi, 2 * math.pi, 100_001)
assert np.max(np.abs(np.sin(x) / x)) < 1 / math.pi

# 2. Directly verify the product-kernel attenuation on all active prime
# powers for moderate windows.
eps = 0.1
for T in (1.0, 2.0, 3.0, 4.0, 5.0):
    X = int(math.exp(2 * T))
    n, lam = von_mangoldt_values(X)
    freq = np.log(n)
    weight = lam / np.sqrt(n)
    data = bands(T, eps)
    multiplier = np.ones_like(freq)
    for _, m, h, _ in data:
        multiplier *= sinc(h * freq / 2) ** m
    attenuated_l1 = float(np.sum(weight * np.abs(multiplier)))
    support_length = sum(m * h for _, m, h, _ in data)
    crude_A = 4 * T * math.exp(T)
    assert float(weight.sum()) <= crude_A
    assert attenuated_l1 <= eps + 1e-13
    print(
        f"T={T:g}: bands={len(data)}, support={support_length:.6g}, "
        f"attenuated L1={attenuated_l1:.3e}"
    )

# 3. Gamma monotonicity derivative bound.
mp.mp.dps = 50
half_trigamma = mp.polygamma(1, mp.mpf(1) / 4) / 2
assert half_trigamma < 9

# Fixed central radius for epsilon=.1 and g=1.
target = 2 * eps + 2
gamma = lambda t: mp.re(mp.digamma(mp.mpf(1) / 4 + 0.5j * t)) - mp.log(
    mp.pi
)
lo, hi = mp.mpf(0), mp.mpf(100)
while gamma(hi) < target:
    hi *= 2
for _ in range(120):
    mid = (lo + hi) / 2
    if gamma(mid) < target:
        lo = mid
    else:
        hi = mid
R0 = float(hi)
assert gamma(R0) >= target

# 4. Quantify the generic LS loss against the required mass fraction.
C_LS = 10.0
for T in (2.0, 4.0, 8.0, 16.0, 32.0):
    data = bands(T, eps)
    a0 = sum(m * h for _, m, h, _ in data)
    a = 2 * R0 + 2 * a0
    A_bound = 4 * T * math.exp(T)
    derivative_bound = 9 + 4 * T * A_bound
    thickness = 2 / (a * derivative_bound)
    log_eta = C_LS * (a * T + 1) * math.log(thickness / C_LS)
    M = float(mp.log(mp.pi) - mp.digamma(mp.mpf(1) / 4)) + 2 * A_bound
    required = M / (M + 1)
    assert log_eta < 0
    assert required > 0.5
    print(
        f"LS T={T:g}: a={a:.4g}, gamma={thickness:.3e}, "
        f"log(eta)>={log_eta:.3e}, required mass={required:.12f}"
    )

# 5. Pairwise and k-th moment recurrence scales.
for T in (2.0, 4.0, 8.0):
    X = math.exp(2 * T)
    pair_scale = X
    assert pair_scale > 1
    for k in (1, 2, 4):
        moment_scale = X**k
        separation = math.log1p(1 / moment_scale)
        assert separation >= 1 / (2 * moment_scale)
    print(f"large-sieve T={T:g}: X={X:.6g}, T*X={T*X:.6g}")

# 6. Exact Tate-coordinate convention.
assert abs((0.5 - 1j * (-0.5j)) - 0) < 1e-15
assert abs((0.5 - 1j * (0.5j)) - 1) < 1e-15

print(f"D132 fixed Gamma radius R0={R0:.12g}")
print("D132 global phase / Logvinenko--Sereda audit: PASS")
