#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import cholesky, eigvalsh, norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import primes_upto  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_158_prime_cell_psd_probe import q_matrix  # noqa: E402
from E72_159_prime_block_psd_probe import psd_part, relative_matrix  # noqa: E402


def blocks_for_cut(lam, idx, L, bq, c_model, cut):
    mats = [np.zeros((len(bq.T), len(bq.T))) for _ in range(2)]
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = np.log(p)
        pm = p
        me = 1
        while pm <= maxn:
            y = me * lp
            weight = lp * (pm ** -0.5)
            bin_id = 0 if y <= cut * L else 1
            comp = bq.T @ (-weight * q_matrix(idx, L, y)) @ bq
            mats[bin_id] += relative_matrix(comp, c_model)
            if pm > maxn // p:
                break
            pm *= p
            me += 1
    return mats


def run(a=0.70, b=0.60):
    print(f"E72.164 cut-weight probe fixed a={a:.2f}, b={b:.2f}")
    print(" cut   maxDist  margin  per-window")
    windows = [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36)]
    cuts = np.linspace(0.35, 0.65, 13)
    prepared = []
    for lam, n_modes in windows:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        krel = relative_matrix(c_actual - c_model, c_model)
        prepared.append((lam, idx, L, bq, c_model, krel))
    best = (np.inf, None, None)
    for cut in cuts:
        rows = []
        max_dist = 0.0
        for lam, idx, L, bq, c_model, krel in prepared:
            blocks = blocks_for_cut(lam, idx, L, bq, c_model, cut)
            p0 = psd_part(blocks[0])
            p1 = psd_part(blocks[1])
            dist = norm(krel - a * p0 - b * p1, "fro")
            max_dist = max(max_dist, dist)
            rows.append((lam, dist))
        if max_dist < best[0]:
            best = (max_dist, cut, rows)
        details = " ".join(f"{int(lam)}:{dist:.3f}" for lam, dist in rows)
        print(f"{cut:4.2f} {max_dist:8.3f} {1-max_dist*max_dist:7.3f} {details}")
    print(f"best_cut={best[1]:.2f} maxDist={best[0]:.3f} margin={1-best[0]*best[0]:.3f}")


if __name__ == "__main__":
    run()
