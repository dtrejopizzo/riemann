#!/usr/bin/env python3
"""Audit real-rootedness of the cleared boundary-transfer numerator."""

import random

import mpmath as mp
import numpy as np

from P76_002_mp_entry_audit import build_mp


def random_symmetric(n, seed=7620):
    rng = random.Random(seed)
    H = mp.matrix(n)
    for i in range(n):
        for j in range(i, n):
            value = mp.mpf(str(rng.gauss(0, 1)))
            H[i, j] = value
            H[j, i] = value
    return H


def numerator_roots(H, idx, L, side):
    vals, _ = mp.eigsy(H)
    mu = vals[0]
    A = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    boundary_pos = 0 if side < 0 else H.cols - 1
    boundary_idx = idx[0] if side < 0 else idx[-1]
    b = mp.matrix([H[j + 1, boundary_pos] for j in range(H.rows - 2)])
    x = A ** -1 * b

    inner_idx = idx[1:-1]
    scale = max(abs(2 * mp.pi * n / L) for n in idx)
    inner_nodes = [float((2 * mp.pi * n / L) / scale) for n in inner_idx]
    boundary_node = float((2 * mp.pi * boundary_idx / L) / scale)
    base = np.poly1d(np.poly(inner_nodes))
    numerator = np.poly1d(base.coeffs.copy())
    for j, node in enumerate(inner_nodes):
        quotient, remainder = np.polydiv(base, np.poly1d([1.0, -node]))
        if np.max(np.abs(remainder.coeffs)) > 1e-7:
            raise RuntimeError("polynomial division residual too large")
        numerator -= float(x[j]) * np.polymul(np.poly1d([1.0, -boundary_node]), quotient)
    roots = np.roots(numerator)
    return roots * float(scale)


def report(tag, H, idx, L, gamma):
    for side in (-1, 1):
        roots = numerator_roots(H, idx, L, side)
        nonreal = int(np.sum(np.abs(roots.imag) > 1e-7))
        max_imag = float(np.max(np.abs(roots.imag)))
        realish = roots[np.abs(roots.imag) <= 1e-7].real
        nearest = float(realish[np.argmin(np.abs(realish - gamma))]) if len(realish) else np.nan
        print(f"{tag:10s} {side:+2d} {nonreal:8d} {max_imag:12.3e} {nearest-gamma:15.3e}")


def run():
    mp.mp.dps = 70
    n_modes = 9
    gamma = 14.134725141734694
    zeta, idx, L = build_mp(6, n_modes, 70)
    planted, _, _ = build_mp(
        6,
        n_modes,
        70,
        planted=("14.134725141734693790", "0.30", "5.0"),
    )
    random_h = random_symmetric(len(idx))
    print("P76.020 boundary numerator root reality")
    print("case       side  nonreal      maxImag  nearestShift")
    report("zeta", zeta, idx, L, gamma)
    report("planted", planted, idx, L, gamma)
    report("random", random_h, idx, L, gamma)


if __name__ == "__main__":
    run()
