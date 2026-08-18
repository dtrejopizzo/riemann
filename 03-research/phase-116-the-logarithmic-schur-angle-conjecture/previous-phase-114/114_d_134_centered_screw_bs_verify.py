#!/usr/bin/env python3
"""Checks for D.134 centred screw/Birman--Schwinger factorization.

The checks are local algebra and special-function identities only; RH is
neither assumed nor tested.
"""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np


mp.mp.dps = 60


def close(a, b, tol=1e-12):
    assert abs(a - b) <= tol * max(1.0, abs(a), abs(b)), (a, b)


# 1. Exact 5/4 Gamma screw integral.
def h54(tau):
    return mp.re(mp.digamma(mp.mpf(5) / 4 + 0.5j * tau)) - mp.digamma(
        mp.mpf(5) / 4
    )


def screw_integral(tau):
    density = lambda r: mp.e ** (-mp.mpf(5) * r / 2) / (1 - mp.e ** (-2 * r))
    return 2 * mp.quad(lambda r: density(r) * (1 - mp.cos(tau * r)), [0, 1, mp.inf])


for tau in (mp.mpf("0.1"), mp.mpf("1"), mp.mpf("4.25")):
    close(h54(tau), screw_integral(tau), 2e-16)
    assert h54(tau) > 0


# 2. Fourier transform of exp(-|t|/2).
for tau in (0.0, 0.7, 3.0):
    numeric = mp.quad(lambda t: mp.e ** (-abs(t) / 2) * mp.cos(tau * t), [-mp.inf, mp.inf])
    exact = 1 / (tau * tau + 0.25)
    close(numeric, exact, 1e-13)


# 3. Balanced J_+/J_- identity on a discrete overlap.
rng = np.random.default_rng(134)
left = rng.normal(size=100) + 1j * rng.normal(size=100)
right = rng.normal(size=100) + 1j * rng.normal(size=100)
jplus = (right + left) / math.sqrt(2)
jminus = (right - left) / math.sqrt(2)
lhs = np.vdot(jplus, jplus).real - np.vdot(jminus, jminus).real
rhs = 2 * np.vdot(left, right).real
close(lhs, rhs, 1e-13)


# 4. Matrix model of R-W*W and the Birman--Schwinger inertia identity.
n = 24
m = 31
X = rng.normal(size=(n, n))
R = X.T @ X + 0.7 * np.eye(n)
W = 0.34 * rng.normal(size=(m, n))
eval_R, evec_R = np.linalg.eigh(R)
Rinvhalf = (evec_R / np.sqrt(eval_R)) @ evec_R.T
K = Rinvhalf @ W.T @ W @ Rinvhalf
danger = np.count_nonzero(np.linalg.eigvalsh(K) > 1 + 1e-10)
morse = np.count_nonzero(np.linalg.eigvalsh(R - W.T @ W) < -1e-10)
assert danger == morse
assert (np.linalg.eigvalsh(K)[-1] <= 1) == (
    np.linalg.eigvalsh(R - W.T @ W)[0] >= -1e-10
)


# 5. Schur capacity I-WR^{-1}W* has the same nonzero threshold spectrum.
Kchannel = W @ np.linalg.solve(R, W.T)
nonzero_source = np.linalg.eigvalsh(K)[-n:]
nonzero_channel = np.linalg.eigvalsh(Kchannel)[-n:]
assert np.max(np.abs(nonzero_source - nonzero_channel)) < 1e-10


# 6. The non-Schatten lower scale 1/log(j) has divergent p-sums.  Grouping
# j in [exp(m),exp(m+1)) gives a lower block mass exp(m)/(m+1)^p.
for p in (1, 2, 10):
    blocks = [math.exp(mm) / (mm + 1) ** p for mm in range(20, 61)]
    assert blocks[-1] > blocks[0]
    assert blocks[-1] > 1e6


# 7. Every p^k has the source coefficient log(p)/sqrt(p^k).
p = 5
weights = [math.log(p) / math.sqrt(p**k) for k in range(1, 8)]
for k, weight in enumerate(weights, start=1):
    close(weight, math.log(p) * p ** (-k / 2), 1e-15)
    if k > 1:
        close(weight / weights[k - 2], p ** (-0.5), 1e-15)


beta = mp.log(mp.pi) - mp.digamma(mp.mpf(5) / 4)
assert beta > 0


print("D134 centred screw/Birman--Schwinger audit: PASS")
