#!/usr/bin/env python3
"""Finite-dimensional checks for D.138.

The script checks the transported defect identity, the Birman--Schwinger
inertia count, and unitarity of the Julia colligation for random strict
contractions.  It is a certificate for the algebraic identities only, not
for the infinite-dimensional row-D inequality.
"""

from __future__ import annotations

import numpy as np


def psqrt(a: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh((a + a.conj().T) / 2)
    assert vals.min() > -1e-11
    return (vecs * np.sqrt(np.maximum(vals, 0.0))) @ vecs.conj().T


rng = np.random.default_rng(138)

for n, m in [(4, 6), (7, 5), (9, 11)]:
    x = rng.normal(size=(m, n)) + 1j * rng.normal(size=(m, n))
    # Make a strict contraction.
    a = 0.82 * x / np.linalg.svd(x, compute_uv=False)[0]
    i_n = np.eye(n)
    i_m = np.eye(m)
    d_a = psqrt(i_n - a.conj().T @ a)
    d_ast = psqrt(i_m - a @ a.conj().T)

    # Julia operator: C^n (+) C^m -> C^m (+) C^n.
    u = np.block([[a, d_ast], [d_a, -a.conj().T]])
    assert np.linalg.norm(u.conj().T @ u - np.eye(n + m)) < 2e-10
    assert np.linalg.norm(u @ u.conj().T - np.eye(n + m)) < 2e-10
    assert np.linalg.norm(a @ d_a - d_ast @ a) < 2e-10

    # Transport by an arbitrary positive reference R.
    y = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    r = y.conj().T @ y + 0.3 * i_n
    rhalf = psqrt(r)
    w = a @ rhalf
    lhs = r - w.conj().T @ w
    rhs = rhalf @ (i_n - a.conj().T @ a) @ rhalf
    assert np.linalg.norm(lhs - rhs) < 2e-9

# General inertia identity, including expansive singular values.
for n, m in [(8, 6), (6, 10)]:
    a = rng.normal(size=(m, n)) + 1j * rng.normal(size=(m, n))
    a /= 1.25
    k = a.conj().T @ a
    defect = np.eye(n) - k
    count_k = int(np.sum(np.linalg.eigvalsh(k) > 1 + 1e-10))
    count_d = int(np.sum(np.linalg.eigvalsh(defect) < -1e-10))
    assert count_k == count_d

# The model lower bound 1/log(j) is in no finite Schatten class.  Check the
# partial sums grow for several p; divergence itself is proved analytically.
for p in (1, 2, 4, 8):
    ns = (2_000, 20_000, 200_000)
    sums = [np.sum(np.log(np.arange(2, n + 2)) ** (-p)) for n in ns]
    assert sums[0] < sums[1] < sums[2]

print("D138 Fredholm--Julia certificates: PASS")
