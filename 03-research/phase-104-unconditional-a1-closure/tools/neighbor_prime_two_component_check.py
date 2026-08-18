#!/usr/bin/env python3
"""Finite two-component hypocoercive lift on neighboring prime towers.

The symmetric part is the neighboring-prime diffusion from 104_115.  The
skew part is assembled from oriented cycles on triples of consecutive
primes.  The script checks J*=-J, J1=0, computes the sharp finite Schur
scale ||A^{-1/2} J A^{-1/2}||^{-1}, and measures the adjacent-Laguerre
cross term.

This is a structural diagnostic; it does not assert the missing bridge to
the linear Mangoldt functional B_n.
"""

from __future__ import annotations

import runpy
from pathlib import Path
import numpy as np


BASE = runpy.run_path(str(Path(__file__).with_name("neighbor_prime_resolvent_check.py")))
first_primes = BASE["first_primes"]
laguerre = BASE["laguerre"]
build_neighbor_generator = BASE["build_neighbor_generator"]
weighted_inner = BASE["weighted_inner"]


def triangle_current(s: np.ndarray, pi: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    size = len(pi)
    conductance = pi[:, None] * s
    flux = np.zeros((size, size), dtype=float)
    for j in range(size - 2):
        amplitude = min(conductance[j, j + 1], conductance[j + 1, j + 2])
        cycle = ((j, j + 1), (j + 1, j + 2), (j + 2, j))
        for left, right in cycle:
            flux[left, right] += amplitude
            flux[right, left] -= amplitude
    current = flux / pi[:, None]
    return current, flux


def schur_scale(s: np.ndarray, current: np.ndarray, pi: np.ndarray) -> tuple[float, float]:
    root = np.sqrt(pi)
    a = root[:, None] * (-s) / root[None, :]
    j = root[:, None] * current / root[None, :]
    eigenvalues, vectors = np.linalg.eigh((a + a.T) / 2.0)
    keep = eigenvalues > 1e-10
    u = vectors[:, keep]
    lam = eigenvalues[keep]
    reduced_j = u.T @ j @ u
    normalized = reduced_j / np.sqrt(lam[:, None] * lam[None, :])
    norm = np.linalg.svd(normalized, compute_uv=False)[0]
    eta_max = 1.0 / norm
    skew_error = np.max(np.abs(j + j.T))
    return float(eta_max), float(skew_error)


def run_case(size: int, epsilon: float, n: int) -> tuple[float, float]:
    primes = first_primes(size)
    s, pi, x = build_neighbor_generator(primes, epsilon)
    current, flux = triangle_current(s, pi)
    g = laguerre(n - 1, 1.0, x)
    h = laguerre(n - 2, 2.0, x)

    eta_max, skew_error = schur_scale(s, current, pi)
    row_error = np.max(np.abs(current @ np.ones(size)))
    weighted_skew_error = np.max(np.abs(pi[:, None] * current + (pi[:, None] * current).T))
    cross = weighted_inner(pi, g, current @ h).real
    energy_g = weighted_inner(pi, g, (-s) @ g).real
    energy_h = weighted_inner(pi, h, (-s) @ h).real

    eta = -0.9 * eta_max * (1.0 if cross >= 0.0 else -1.0)
    block_form = energy_g + energy_h + 2.0 * eta * cross

    print(f"J={size:3d} epsilon={epsilon:.3f} n={n:3d}")
    print(f"  current_row_error      = {row_error:.3e}")
    print(f"  weighted_skew_error    = {weighted_skew_error:.3e}")
    print(f"  transformed_skew_error = {skew_error:.3e}")
    print(f"  eta_max                = {eta_max:.6e}")
    print(f"  laguerre_cross         = {cross:+.6e}")
    print(f"  energy_pair            = {energy_g + energy_h:.6e}")
    print(f"  optimized_block_form   = {block_form:.6e}")

    assert np.max(np.abs(flux + flux.T)) < 1e-12
    assert row_error < 1e-10
    assert weighted_skew_error < 1e-10
    assert skew_error < 1e-9
    assert block_form >= -1e-8
    return cross, eta_max


def main() -> None:
    crosses = []
    for n in (4, 8, 12, 16, 20, 24, 32, 40, 48):
        cross, _ = run_case(size=48, epsilon=0.5, n=n)
        crosses.append(cross)
    assert max(abs(value) for value in crosses) > 1e-8
    print("PASS: two-component neighboring-prime Schur audit")


if __name__ == "__main__":
    main()
