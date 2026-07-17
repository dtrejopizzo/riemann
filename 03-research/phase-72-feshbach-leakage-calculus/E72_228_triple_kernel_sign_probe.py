#!/usr/bin/env python3
import itertools
import sys

import numpy as np
from numpy.linalg import cholesky, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (24, 56), (32, 72)]
GRID_LOW = np.linspace(0.05, 0.60, 8)
GRID_HIGH = np.linspace(0.62, 0.98, 8)


def rel_u(idx, L, bq, chol, u):
    raw = bq.T @ u_matrix(idx, L, u * L) @ bq
    x = solve(chol, raw)
    rel = solve(chol, x.T).T
    return 0.5 * (rel + rel.conj().T)


def scan_block(idx, L, bq, c_model, grid):
    chol = cholesky(c_model)
    mats = [rel_u(idx, L, bq, chol, float(u)) for u in grid]
    vals = []
    worst = None
    for a, b, c in itertools.product(range(len(grid)), repeat=3):
        val = float(np.real(np.trace(mats[a] @ mats[b] @ mats[c])))
        vals.append(val)
        if worst is None or val < worst[0]:
            worst = (val, grid[a], grid[b], grid[c])
    vals = np.array(vals)
    return vals, worst


def run():
    print("E72.228 triple kernel sign probe")
    print("T(u,v,w)=Tr(M_u M_v M_w), where M_u is the Hermitian compressed one-sided cell")
    print("High HOC3 wants weighted sum of T over high cube >=0")
    print("lam block minT maxT negFrac meanT worst_u worst_v worst_w")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        for block, grid in [(0, GRID_LOW), (1, GRID_HIGH)]:
            vals, worst = scan_block(idx, L, bq, c_model, grid)
            neg_frac = float(np.mean(vals < -1.0e-12))
            print(
                f"{lam:3.0f} {block:5d} "
                f"{vals.min():+.6e} {vals.max():+.6e} {neg_frac:.3f} {vals.mean():+.6e} "
                f"{worst[1]:.3f} {worst[2]:.3f} {worst[3]:.3f}",
                flush=True,
            )


if __name__ == "__main__":
    run()
