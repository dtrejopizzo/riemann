#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402
from E72_290_apcb_band_split_probe import band_basis  # noqa: E402


def budget(lam, n_modes, cut=4.0):
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    delta = c_actual - c_model
    low, high = band_basis(idx, L, eb, cut)
    a = low.T @ delta @ low
    b = low.T @ delta @ high
    d = high.T @ delta @ high
    cross_schur = np.sqrt(np.max(np.sum(np.abs(b), axis=1)) * np.max(np.sum(np.abs(b), axis=0)))
    return {
        "L": L,
        "rank_low": a.shape[0],
        "low_pos": max(float(eigvalsh(a)[-1]), 0.0),
        "low_row": float(np.max(np.sum(np.abs(a), axis=1))),
        "cross_op": float(norm(b, 2)),
        "cross_fro": float(norm(b, "fro")),
        "cross_schur": float(cross_schur),
        "high_row": float(np.max(np.sum(np.abs(d), axis=1))),
    }


def run():
    print("E72.292 low/cross band budget probe")
    print("Cutoff |d|<4. Low is finite rank; cross can be bounded by Frobenius or Schur.")
    print("lam L rankLow low+/L2 lowRow/L2 cross/L2 crossF/L2 crossSchur/L2 highRow/L2")
    for lam, n_modes in [(16, 40), (24, 56), (32, 72)]:
        r = budget(lam, n_modes)
        L2 = r["L"] * r["L"]
        print(
            f"{lam:3.0f} {r['L']:.6f} {r['rank_low']:7d} "
            f"{r['low_pos'] / L2:.6e} {r['low_row'] / L2:.6e} "
            f"{r['cross_op'] / L2:.6e} {r['cross_fro'] / L2:.6e} "
            f"{r['cross_schur'] / L2:.6e} {r['high_row'] / L2:.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
