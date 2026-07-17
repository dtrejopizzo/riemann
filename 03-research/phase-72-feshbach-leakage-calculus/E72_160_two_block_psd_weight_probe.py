#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import cholesky, eigvalsh, norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_159_prime_block_psd_probe import block_matrices, psd_part, relative_matrix  # noqa: E402


def best_two_weights(krel, p0, p1, grid):
    best = (np.inf, 0.0, 0.0)
    for a in grid:
        for b in grid:
            dist = norm(krel - a * p0 - b * p1, "fro")
            if dist < best[0]:
                best = (dist, a, b)
    return best


def run():
    print("E72.160 two-block PSD weight probe")
    print(" lam   L  distOpt  unweighted  bestDist  a  b  margin")
    grid = np.linspace(0.0, 1.5, 61)
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        krel = relative_matrix(c_actual - c_model, c_model)
        eigs = eigvalsh(krel)
        dist_opt = np.sqrt(np.sum(eigs[eigs < 0.0] ** 2))
        blocks = block_matrices(lam, idx, L, bq, c_model, 2)
        p0 = psd_part(blocks[0])
        p1 = psd_part(blocks[1])
        unweighted = norm(krel - p0 - p1, "fro")
        best, a, b = best_two_weights(krel, p0, p1, grid)
        print(
            f"{lam:4.0f} {L:5.2f} {dist_opt:8.3f} {unweighted:10.3f} "
            f"{best:9.3f} {a:4.2f} {b:4.2f} {1-best*best:7.3f}"
        )


if __name__ == "__main__":
    run()
