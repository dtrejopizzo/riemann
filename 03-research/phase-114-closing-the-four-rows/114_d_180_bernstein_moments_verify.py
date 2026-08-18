#!/usr/bin/env python3
"""Independent high-precision audit of the Bernstein log moments in D.180."""

import math
import mpmath as mp

mp.mp.dps = 60


def H(n, power=1):
    return mp.fsum(mp.mpf(1) / mp.mpf(j) ** power for j in range(1, n + 1))


for n in range(0, 8):
    for k in range(n + 1):
        b = lambda x: math.comb(n, k) * x**k * (1 - x) ** (n - k)
        den = mp.mpf(n + 1)
        hk, hnk, hn1 = H(k), H(n - k), H(n + 1)
        h2k, h2nk, h2n1 = H(k, 2), H(n - k, 2), H(n + 1, 2)
        exact = [
            1 / den,
            (hk - hn1) / den,
            (hnk - hn1) / den,
            ((hk - hn1) ** 2 + h2n1 - h2k) / den,
            ((hnk - hn1) ** 2 + h2n1 - h2nk) / den,
            ((hk - hn1) * (hnk - hn1) - mp.zeta(2) + h2n1) / den,
        ]
        numeric = [
            mp.quad(lambda x: b(x), [0, 1]),
            mp.quad(lambda x: b(x) * mp.log(x), [0, 1]),
            mp.quad(lambda x: b(x) * mp.log(1 - x), [0, 1]),
            mp.quad(lambda x: b(x) * mp.log(x) ** 2, [0, 1]),
            mp.quad(lambda x: b(x) * mp.log(1 - x) ** 2, [0, 1]),
            mp.quad(lambda x: b(x) * mp.log(x) * mp.log(1 - x), [0, 1]),
        ]
        assert max(abs(a - c) for a, c in zip(exact, numeric)) < mp.mpf("1e-48")

# Exact coefficient identity for shifted Legendre polynomials.
for n in range(0, 20):
    for x in (mp.mpf("0.07"), mp.mpf("0.31"), mp.mpf("0.73"), mp.mpf("0.96")):
        rhs = mp.fsum(
            (-1) ** (n + k)
            * math.comb(n, k)
            * math.comb(n, k)
            * x**k
            * (1 - x) ** (n - k)
            for k in range(n + 1)
        )
        assert abs(rhs - mp.legendre(n, 2 * x - 1)) < mp.mpf("1e-48")

print("D180 Bernstein endpoint moments: PASS")
