#!/usr/bin/env python3
"""Executable checks for 114_d_10_EXACT_DIRICHLET_REDUCTION.md.

The proof is in the note.  This file guards the normalization and the factor
in the digamma multiplier, where a factor-of-four mistake is easy to make.
"""

from __future__ import annotations

import mpmath as mp
import numpy as np


def check_translation_identity() -> None:
    rng = np.random.default_rng(11410)
    f = rng.normal(size=31) + 1j * rng.normal(size=31)
    shifted = np.roll(f, 7)
    lhs = 2.0 * np.real(np.vdot(shifted, f))
    rhs = 2.0 * np.vdot(f, f).real - np.vdot(f - shifted, f - shifted).real
    assert abs(lhs - rhs) < 1e-11


def check_digamma_factor() -> None:
    mp.mp.dps = 80
    for tau in (mp.mpf("0.1"), mp.mpf("1.75"), mp.mpf("13")):
        exact = -(
            mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * tau / 2))
            - mp.digamma(mp.mpf(1) / 4)
        )
        partial = -mp.fsum(
            (tau * tau) / (a * (4 * a * a + tau * tau))
            for a in (mp.mpf(j) + mp.mpf(1) / 4 for j in range(20000))
        )
        assert abs(exact - partial) < mp.mpf("1e-6")


if __name__ == "__main__":
    check_translation_identity()
    check_digamma_factor()
    print("PASS: translation energy and digamma normalization")
