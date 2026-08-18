#!/usr/bin/env python3
"""Certificates for the D.164 integer-cell collision and depth Gram."""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np


mp.mp.dps = 60


def von_mangoldt_table(nmax: int) -> np.ndarray:
    lam = np.zeros(nmax + 1)
    prime = np.ones(nmax + 1, dtype=bool)
    prime[:2] = False
    for p in range(2, int(math.isqrt(nmax)) + 1):
        if prime[p]:
            prime[p * p :: p] = False
    for p in np.flatnonzero(prime):
        q = int(p)
        while q <= nmax:
            lam[q] = math.log(p)
            q *= int(p)
    return lam


def main() -> None:
    nmax = 20000
    lam = von_mangoldt_table(nmax)

    for N in (5, 8, 12, 49, 128, 999, 4096, 19999):
        ellmax = math.log1p(1 / N)

        # Same-side labels are separated by more than one whole cell.
        assert math.log(N / (N - 1)) > ellmax

        labels = np.flatnonzero(lam[: N + 1] > 0)
        for i, n in enumerate(labels):
            for m in labels[i + 1 :]:
                assert abs(math.log(m / n)) > ellmax

        # Cross-side collision iff the integer product is exactly N.
        for n in labels:
            for m in labels:
                distance = abs(math.log(N / (int(n) * int(m))))
                if int(n) * int(m) == N:
                    assert distance == 0
                else:
                    assert distance + 2.0e-15 >= ellmax

        weights = lam[labels] / np.sqrt(labels)
        V = float(weights @ weights)
        H = sum(
            lam[n] * lam[N // n] / math.sqrt(N)
            for n in labels
            if N % int(n) == 0 and lam[N // int(n)] > 0
        )
        gram = np.array([[V, H], [H, V]])
        eig = np.linalg.eigvalsh(gram)
        assert eig[0] >= -1.0e-12
        assert abs(eig[-1] - (V + H)) < 2.0e-12

        # Direct finite-depth Euler ledger for V.
        euler = 0.0
        for p in range(2, N + 1):
            if abs(lam[p] - math.log(p)) > 1.0e-13:
                continue
            if p > N:
                break
            K = int(math.log(N) / math.log(p) + 1.0e-14)
            euler += math.log(p) ** 2 / p * (1 - float(p) ** (-K)) / (1 - 1 / p)
        assert abs(V - euler) < 2.0e-11

    # Prime-power collision ledger H_{p^k}.
    for p, k in ((2, 3), (2, 7), (3, 4), (5, 3), (7, 2)):
        N = p**k
        H = sum(
            lam[n] * lam[N // n] / math.sqrt(N)
            for n in range(2, N)
            if N % n == 0
        )
        expected = (k - 1) * math.log(p) ** 2 / math.sqrt(N)
        assert abs(H - expected) < 2.0e-13

    # Directed local Gamma/prolate lower-bound scale at sample cells.
    c = mp.mpf("0.10")
    ratios = []
    Vsum = np.cumsum(
        np.divide(lam * lam, np.arange(nmax + 1), out=np.zeros(nmax + 1),
                  where=np.arange(nmax + 1) > 0)
    )
    for N in (100, 1000, 5000, 10000, 20000):
        ell = mp.log(1 + mp.mpf(1) / N)
        h = mp.re(mp.digamma(mp.mpf("1.25") + 0.5j * c / ell)) - mp.digamma(
            mp.mpf("1.25")
        )
        mu = (1 - 2 * c / mp.pi) * h
        ratios.append(float(mu / mp.sqrt(Vsum[N])))
    assert ratios[-1] > ratios[0]

    print("D164 integer-cell depth Gram: PASS")
    print("local Gamma / boundary-synthesis sample ratios =", ratios)
    print("V_20000/log^2(20000) =", Vsum[20000] / math.log(20000) ** 2)


if __name__ == "__main__":
    main()
