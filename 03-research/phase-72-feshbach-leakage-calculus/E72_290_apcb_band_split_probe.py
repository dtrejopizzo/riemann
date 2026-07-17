#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


def band_basis(idx, L, eb, cut):
    d = 2.0 * np.pi * idx / L
    mask = np.abs(d) < cut
    gram = eb.T @ (mask[:, None] * eb)
    vals, vecs = np.linalg.eigh(gram)
    low = vecs[:, vals > 1e-8]
    high = vecs[:, vals < 1.0 - 1e-8]
    return low, high


def split_profile(lam, n_modes, cut):
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    delta = c_actual - c_model
    low, high = band_basis(idx, L, eb, cut)
    total = max(float(eigvalsh(delta)[-1]), 0.0)
    low_pos = max(float(eigvalsh(low.T @ delta @ low)[-1]), 0.0) if low.size else 0.0
    high_pos = max(float(eigvalsh(high.T @ delta @ high)[-1]), 0.0) if high.size else 0.0
    cross = norm(low.T @ delta @ high, 2) if low.size and high.size else 0.0
    return L, low.shape[1], high.shape[1], total, low_pos, high_pos, cross


def run():
    print("E72.290 APCB band-split probe")
    print("Delta_arith split by mesh-frequency cut |d|<cut in the corrected even sector.")
    print("lam cut L rankLow rankHigh total+/L2 low+/L2 high+/L2 cross/L2")
    for cut in [2.0, 4.0]:
        for lam, n_modes in [(16, 40), (24, 56), (32, 72)]:
            L, rlow, rhigh, total, low_pos, high_pos, cross = split_profile(lam, n_modes, cut)
            L2 = L * L
            print(
                f"{lam:3.0f} {cut:3.0f} {L:.6f} {rlow:7d} {rhigh:8d} "
                f"{total / L2:.6e} {low_pos / L2:.6e} "
                f"{high_pos / L2:.6e} {cross / L2:.6e}",
                flush=True,
            )


if __name__ == "__main__":
    run()
