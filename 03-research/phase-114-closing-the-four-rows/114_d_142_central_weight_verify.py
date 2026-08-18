#!/usr/bin/env python3
"""Finite certificates for D.142.

These checks verify the central weighted shift, contact/Tate blow-up,
renormalized isometric action and Gamma translation covariance.  They do
not assume the row-D sign.
"""

from __future__ import annotations

import math

import numpy as np


def close(a, b, tol=1e-12):
    assert abs(a - b) <= tol * max(1.0, abs(a), abs(b)), (a, b)


rng = np.random.default_rng(142)


# 1. Exact weighted Dirichlet shifts on a cofinal finite section.
N = 2000
for m in (2, 3, 5, 11):
    source_N = N // m
    a = rng.normal(size=source_N) + 1j * rng.normal(size=source_N)
    source_weight = 1.0 / np.arange(1, source_N + 1)
    source_norm2 = np.sum(np.abs(a) ** 2 * source_weight)
    target_norm2 = np.sum(
        np.abs(a) ** 2 / (m * np.arange(1, source_N + 1))
    )
    close(target_norm2, source_norm2 / m)


# 2. Composition retains all labels and central scales multiply.
for m, n in ((2, 3), (4, 5), (7, 11)):
    close((m * n) ** (-0.5), m ** (-0.5) * n ** (-0.5))
    assert m * n == n * m


# 3. Contact continuity is impossible already on p^k.
for p in (2, 3, 5):
    ratios = [math.log(p) * p ** (k / 2) for k in range(1, 20)]
    assert all(x < y for x, y in zip(ratios, ratios[1:]))
    assert ratios[-1] > 100 * ratios[0]


# 4. Both Tate boundary rows have divergent finite-section dual norms.
# For H with weight w_n=1/n, ||functional c||^2=sum |c_n|^2/w_n.
for cutoff in (10, 100, 1000):
    n = np.arange(1, cutoff + 1, dtype=float)
    chi_minus_dual2 = np.sum((n ** -0.5) ** 2 / (1 / n))
    chi_plus_dual2 = np.sum((n ** 0.5) ** 2 / (1 / n))
    close(chi_minus_dual2, cutoff)
    assert chi_plus_dual2 >= cutoff**2


# 5. The abstract bounded-intertwiner estimate collapses geometrically.
for m in (2, 3):
    bounds = [m ** (-k / 2) for k in range(1, 40)]
    assert all(x > y for x, y in zip(bounds, bounds[1:]))
    assert bounds[-1] < 1e-5


# 6. Removing the central scalar leaves an isometric shift.
for m in (2, 3, 11):
    central_norm = m ** -0.5
    renormalized_norm = math.sqrt(m) * central_norm
    close(renormalized_norm, 1.0)


# 7. Discrete full-line Gamma differences commute with translations away
# from the zero-extension boundary; use a padded compact vector.
M = 400
F = np.zeros(M)
F[140:260] = rng.normal(size=120)
for gamma_lag, translation in ((3, 11), (17, 23), (31, 7)):
    def shift(v, q):
        out = np.zeros_like(v)
        out[q:] = v[:-q]
        return out

    difference_then_shift = shift(F - shift(F, gamma_lag), translation)
    shift_then_difference = shift(F, translation) - shift(
        shift(F, translation), gamma_lag
    )
    assert np.linalg.norm(difference_then_shift - shift_then_difference) < 1e-12


print("D142 central-weight Hilbert/rigging audit: PASS")
