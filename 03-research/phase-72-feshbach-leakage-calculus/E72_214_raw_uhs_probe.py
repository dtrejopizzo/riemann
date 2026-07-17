#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64)]


def raw_hs(idx, L, bq, u):
    mat = bq.T @ u_matrix(idx, L, u * L) @ bq
    return float(norm(mat, "fro") ** 2)


def run():
    print("E72.214 raw U_y Hilbert-Schmidt probe")
    print("UHS candidate: ||B* U_y B||_HS^2 <= C L^2 Phi(y/L)")
    print("lam L qdim u0.1/L2 u0.25/L2 u0.5/L2 u0.75/L2 u0.9/L2 maxRaw/L2")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        us = [0.1, 0.25, 0.5, 0.75, 0.9]
        vals = [raw_hs(idx, L, bq, u) / (L * L) for u in us]
        grid = np.linspace(0.02, 0.98, 97)
        maxv = max(raw_hs(idx, L, bq, float(u)) / (L * L) for u in grid)
        print(
            f"{lam:3.0f} {L:5.2f} {bq.shape[1]:4d} "
            + " ".join(f"{v:.3f}" for v in vals)
            + f" {maxv:.3f}",
            flush=True,
        )


if __name__ == "__main__":
    run()
