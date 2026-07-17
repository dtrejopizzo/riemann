#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_159_prime_block_psd_probe import block_matrices, psd_part, relative_matrix  # noqa: E402


def prepare_windows(windows):
    prepared = []
    for lam, n_modes in windows:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        krel = relative_matrix(c_actual - c_model, c_model)
        blocks = block_matrices(lam, idx, L, bq, c_model, 2)
        p0 = psd_part(blocks[0])
        p1 = psd_part(blocks[1])
        prepared.append((lam, L, krel, p0, p1))
    return prepared


def max_distance_for_weight(a, b, prepared):
    max_dist = 0.0
    rows = []
    for lam, L, krel, p0, p1 in prepared:
        dist = norm(krel - a * p0 - b * p1, "fro")
        max_dist = max(max_dist, dist)
        rows.append((lam, L, dist))
    return max_dist, rows


def run():
    print("E72.162 fixed two-block weights probe")
    windows = [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36)]
    candidates = [
        (0.75, 0.55),
        (0.80, 0.55),
        (0.85, 0.50),
        (0.80, 0.50),
        (0.75, 0.60),
        (0.70, 0.60),
        (0.85, 0.60),
    ]
    print(" a     b    maxDist  margin   per-window")
    prepared = prepare_windows(windows)
    best = (np.inf, None, None, None)
    for a, b in candidates:
        max_dist, rows = max_distance_for_weight(a, b, prepared)
        if max_dist < best[0]:
            best = (max_dist, a, b, rows)
        details = " ".join(f"{int(lam)}:{dist:.3f}" for lam, _, dist in rows)
        print(f"{a:4.2f} {b:5.2f} {max_dist:8.3f} {1-max_dist*max_dist:7.3f}  {details}")
    print(
        f"best_fixed a={best[1]:.2f} b={best[2]:.2f} "
        f"maxDist={best[0]:.3f} margin={1-best[0]*best[0]:.3f}"
    )


if __name__ == "__main__":
    run()
