#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402
from E72_290_apcb_band_split_probe import band_basis  # noqa: E402


def high_gersh(lam, n_modes, cut=4.0):
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    delta = c_actual - c_model
    low, high = band_basis(idx, L, eb, cut)
    hblock = high.T @ delta @ high
    eig_top = float(eigvalsh(hblock)[-1])
    diag = np.diag(hblock)
    off = hblock - np.diag(diag)
    return {
        "L": L,
        "dim": hblock.shape[0],
        "eig": eig_top,
        "diag_max": float(np.max(diag)),
        "off_row": float(np.max(np.sum(np.abs(off), axis=1))),
        "abs_row": float(np.max(np.sum(np.abs(hblock), axis=1))),
        "fro": float(norm(hblock, "fro")),
    }


def run():
    print("E72.291 high-band Gershgorin probe")
    print("High block is |d|>=4. Gershgorin ceiling: lambda_max <= max_i sum_j |H_ij|.")
    print("lam L dim eig/L2 diagMax/L2 offRow/L2 absRow/L2 fro/L2")
    for lam, n_modes in [(16, 40), (24, 56), (32, 72)]:
        r = high_gersh(lam, n_modes)
        L2 = r["L"] * r["L"]
        print(
            f"{lam:3.0f} {r['L']:.6f} {r['dim']:4d} "
            f"{r['eig'] / L2:.6e} {r['diag_max'] / L2:.6e} "
            f"{r['off_row'] / L2:.6e} {r['abs_row'] / L2:.6e} "
            f"{r['fro'] / L2:.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
