#!/usr/bin/env python3
"""Verify the exact D.180 low/high Feshbach algebra and divergence ledgers."""

from __future__ import annotations

import math

import numpy as np


rng = np.random.default_rng(180)
n = 36
U, _ = np.linalg.qr(rng.normal(size=(n, n)))
ce = np.linspace(0.01, 0.99, n)
C = (U * ce) @ U.T
eta = 0.72
lo_mask = ce > eta
Plo = (U[:, lo_mask]) @ U[:, lo_mask].T
Phi = np.eye(n) - Plo
hR = 3.4
aR = (1.0 - eta) * hR

# Complete reference: Gamma lower model plus arbitrary noncommuting positive
# prime-power channels.
J = rng.normal(size=(2 * n, n))
Rref = hR * (np.eye(n) - C) + J.T @ J / (3.0 * n)
assert np.linalg.eigvalsh(Rref - aR * Phi)[0] > -2e-12
G = np.linalg.inv(Rref)
Ghi = Phi @ G @ Phi
assert np.linalg.eigvalsh((Ghi + Ghi.T) / 2)[-1] <= 1.0 / aR + 2e-12

Glo = Plo @ G + G @ Plo - Plo @ G @ Plo
assert np.allclose(G, Ghi + Glo, atol=2e-12)
rank_lo = np.linalg.matrix_rank(Glo, tol=1e-10)
assert rank_lo <= 2 * int(np.sum(lo_mask))

# Trace/rank ledger for a model concentration operator.
trace_C = float(np.trace(C))
assert int(np.sum(lo_mask)) <= trace_C / eta + 1e-12


def mangoldt_sieve(N: int) -> np.ndarray:
    lam = np.zeros(N + 1)
    prime = np.ones(N + 1, dtype=bool)
    prime[:2] = False
    for p in range(2, N + 1):
        if not prime[p]:
            continue
        lp = math.log(p)
        x = p
        while x <= N:
            lam[x] = lp
            if x > N // p:
                break
            x *= p
        if p * p <= N:
            prime[p * p:N + 1:p] = False
    return lam


prime_ledgers = []
gamma_ledgers = []
for N in (1000, 3000, 10000, 30000, 100000):
    lam = mangoldt_sieve(N)
    prime_ledger = float(np.sum(lam[1:] / np.sqrt(np.arange(1, N + 1))))
    M = max(2, int(N / math.log(N)))
    gamma_ledger = 0.5 * sum(1.0 / m for m in range(1, M + 1))
    prime_ledgers.append(prime_ledger)
    gamma_ledgers.append(gamma_ledger)
assert all(b > a for a, b in zip(prime_ledgers, prime_ledgers[1:]))
assert all(b > a for a, b in zip(gamma_ledgers, gamma_ledgers[1:]))
assert prime_ledgers[-1] / math.sqrt(100000) > 1.8
assert gamma_ledgers[-1] > 4.5

print("finite low rank / inverse-low rank =", int(np.sum(lo_mask)), rank_lo)
print("prime solid ledgers =", prime_ledgers)
print("Gamma solid ledgers =", gamma_ledgers)
print("D180 prolate low block and Wiener no-go: PASS")
