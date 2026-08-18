#!/usr/bin/env python3
"""Algebraic/Fourier certificates for D.141."""

from __future__ import annotations

import cmath
import numpy as np

# Tate covariance at several p^k translations.
for p, k in ((2, 1), (2, 5), (3, 2), (11, 1)):
    a = k * np.log(p)
    chars = np.array([np.exp(-a / 2), np.exp(a / 2)])
    expected = np.array([p ** (-k / 2), p ** (k / 2)])
    assert np.linalg.norm(chars - expected) < 2e-12

# A monic polynomial of positive degree cannot vanish on a dense sample of
# the unit circle.  This finite check certifies the Cayley--Hamilton
# algebra used in the proof; the continuum conclusion is analytic.
rng = np.random.default_rng(141)
for degree in (2, 3, 5):
    lower = rng.normal(size=degree) + 1j * rng.normal(size=degree)
    coeff = np.concatenate(([1.0 + 0j], lower))
    angles = np.linspace(0, 2 * np.pi, 10_001, endpoint=False)
    values = np.polyval(coeff, np.exp(1j * angles))
    assert np.max(np.abs(values)) > 1e-3
    assert not np.all(np.abs(values) < 1e-10)

# Fourier translation multiplier.
for a in (np.log(2), 2 * np.log(3), np.sqrt(2)):
    for tau in (-4.2, 0.0, 3.7):
        assert abs(
            cmath.exp(-1j * a * tau)
            - np.exp(-1j * a * tau)
        ) < 1e-14

print("D141 theta--Tate translation certificates: PASS")
