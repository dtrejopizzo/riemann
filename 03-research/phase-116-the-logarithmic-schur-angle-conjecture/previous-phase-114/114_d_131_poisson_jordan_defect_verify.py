#!/usr/bin/env python3
"""Finite checks for D.131.

The script verifies the two-projection leakage/cross/Schur identities and
the complete prime-power/Gamma signed Gram formula.  It is an algebraic
audit, not a row-D positivity certificate.
"""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np


def close(a, b, tol=2e-12):
    assert abs(a - b) <= tol * max(1.0, abs(a), abs(b)), (a, b)


# 1. Generic two-projection fiber and automatic leakage.
theta = 0.63
c, s = math.cos(theta), math.sin(theta)
P = np.array([[1.0, 0.0], [0.0, 0.0]])
Q = np.eye(2) - P
U = np.array([[c, s], [-s, c]])
Phat = U.T @ P @ U
Kleak = P @ U.T @ Q @ U @ P
close(np.linalg.norm(Kleak - (P - P @ Phat @ P)), 0.0)
assert np.linalg.eigvalsh(Kleak).min() > -1e-14

# 2. Raw corner = -leakage + indefinite cross anomaly.
for v in (
    np.array([1.2, 0.7]),
    np.array([1.2, -0.7]),
    np.array([-0.3, 2.1]),
):
    corner = float(v @ (Phat @ P - P) @ v)
    leakage = float(v @ Kleak @ v)
    cross = float(v @ (Q @ Phat @ P) @ v)
    close(corner, -leakage + cross)

vplus = np.array([1.0, 1.0])
vminus = np.array([1.0, -1.0])
assert float(vplus @ (Q @ Phat @ P) @ vplus) > 0
assert float(vminus @ (Q @ Phat @ P) @ vminus) < 0

# 3. Schur completion and the factor-two overshoot.
K = s * s
beta = c * s
X0 = -beta / (2 * K)
Schur = beta * beta / (4 * K)
close(Schur, c * c / 4)
for x, y in ((1.0, 0.4), (-0.7, 2.0), (0.2, -1.3)):
    hermitian_corner = -K * x * x + beta * x * y
    folded = -K * (x + X0 * y) ** 2 + Schur * y * y
    close(hermitian_corner, folded)
    target_minus_corner = K * (x + X0 * y) ** 2 - Schur * y * y
    added_square = K * (x + X0 * y) ** 2 + Schur * y * y
    close(added_square - target_minus_corner, 2 * Schur * y * y)

# 4. Every prime power is in the Green/Poisson first-chaos preparation.
def poisson_closed(rho: float, angle: float) -> float:
    return (1 - rho * rho) / abs(1 - rho * np.exp(1j * angle)) ** 2


def poisson_series(rho: float, angle: float, depth: int = 300) -> float:
    return 1 + 2 * sum(rho**k * math.cos(k * angle) for k in range(1, depth + 1))


tau = 0.731
for p in (2, 3, 5, 11):
    rho = p**-0.5
    angle = tau * math.log(p)
    close(poisson_closed(rho, angle), poisson_series(rho, angle), 2e-12)
    # Coefficient at p^k is Lambda(p^k)/sqrt(p^k)=log(p) rho^k.
    for k in (1, 2, 3, 7):
        close(math.log(p) * rho**k, math.log(p) / math.sqrt(p**k), 1e-14)

# 5. Complete Gamma oscillator and the signed Gram identity.
mp.mp.dps = 50
tau_mp = mp.mpf(str(tau))
ell_inf = mp.re(mp.digamma(mp.mpf(1) / 4 + 0.5j * tau_mp)) - mp.digamma(
    mp.mpf(1) / 4
)
ell_integral = mp.quad(
    lambda r: 2 * mp.e ** (-r / 2) / (1 - mp.e ** (-2 * r))
    * (1 - mp.cos(tau_mp * r)),
    [0, 1, mp.inf],
)
assert abs(ell_inf - ell_integral) < mp.mpf("2e-16")
m0 = mp.log(mp.pi) - mp.digamma(mp.mpf(1) / 4)

primes = (2, 3, 5)
prep = m0 + sum(
    mp.log(p) * poisson_closed(p**-0.5, tau * math.log(p)) for p in primes
)
boundary = ell_inf + sum(mp.log(p) for p in primes)
signed_gram = prep - boundary
explicit = m0 - ell_inf
for p in primes:
    rho = p**-0.5
    explicit += 2 * mp.log(p) * sum(
        rho**k * mp.cos(k * tau_mp * mp.log(p)) for k in range(1, 400)
    )
assert abs(signed_gram - explicit) < mp.mpf("2e-14")

# 6. Tate jets and rigid rational/Gamma asymptotic mismatch.
close(0.5 - 1j * (-0.5j), 0.0, 1e-14)
close(0.5 - 1j * (0.5j), 1.0, 1e-14)
large = mp.mpf("1000")
rational_tail = 1 / (large * large + mp.mpf(1) / 4) ** 2
gamma_completed = mp.re(mp.digamma(mp.mpf(1) / 4 + 0.5j * large)) - mp.log(
    mp.pi
)
assert rational_tail < mp.mpf("1e-11")
assert gamma_completed > 4

print("D131 Poisson leakage / Jordan defect audit: PASS")
print(f"generic Schur channel={Schur:.16g}")
print(f"Gamma signed multiplier={float(m0-ell_inf):.16g}")
print("adding the first-chaos square has the wrong sign (factor-two audit passed)")
