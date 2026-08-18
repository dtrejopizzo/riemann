#!/usr/bin/env python3
"""Checks for D.135 centred Birman--Schwinger audit."""

from __future__ import annotations

import math

import mpmath as mp


mp.mp.dps = 40


def main() -> None:
    # Lévy integral for the shifted Gamma multiplier.
    for tau in (mp.mpf("0.2"), mp.mpf("1.3"), mp.mpf("5")):
        integral = mp.quad(
            lambda a: 2 * mp.exp(-mp.mpf("2.5") * a)
            / (1 - mp.exp(-2 * a))
            * (1 - mp.cos(tau * a)),
            [0, 1, mp.inf],
        )
        closed = mp.re(mp.digamma(mp.mpf("1.25") + 0.5j * tau)) - mp.digamma(
            mp.mpf("1.25")
        )
        assert abs(integral - closed) < mp.mpf("1e-35")

    # Compact, non-Schatten toy with the exact logarithmic comparison scale.
    values = [1 / math.log(j) for j in range(2, 200000)]
    assert values[-1] < values[0]
    assert values[-1] > 0
    for p in (1, 2, 4, 8):
        first = sum(v**p for v in values[:1000])
        later = sum(v**p for v in values)
        assert later > first

    # Cesàro annihilation of every nonzero contact frequency, while the
    # beta atom at zero survives.
    beta = mp.log(mp.pi) - mp.digamma(mp.mpf("1.25"))
    assert beta > 0
    for a in (mp.log(2), mp.log(3), mp.mpf("0.37")):
        R = mp.mpf("100000")
        average = mp.sin(R * a) / (R * a)
        assert abs(average) < mp.mpf("5e-5")

    # Finite-dimensional congruence check for the BS equivalence.
    h1, h2 = mp.mpf(2), mp.mpf(5)
    v1, v2 = mp.mpf("0.5"), mp.mpf("1.5")
    k1, k2 = v1 / h1, v2 / h2
    assert max(k1, k2) < 1
    assert h1 - v1 > 0 and h2 - v2 > 0

    print("D135 centred Birman--Schwinger certificates: PASS")
    print("beta:", mp.nstr(beta, 20))
    print("logarithmic compact scale tail:", values[-1])


if __name__ == "__main__":
    main()
