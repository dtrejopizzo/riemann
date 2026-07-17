#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402


def run():
    print("E72.136 model Gershgorin coercivity probe")
    print(" lam   L  minEig/L  minDiag/L  maxOffRow/L  GershLow/L")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        diag = np.abs(np.diag(c_model))
        off = np.sum(np.abs(c_model), axis=1) - diag
        g_low = np.min(diag - off)
        print(
            f"{lam:4.0f} {L:5.2f} {eigvalsh(c_model)[0]/L:9.3e} "
            f"{np.min(diag)/L:9.3e} {np.max(off)/L:12.3e} {g_low/L:11.3e}"
        )


if __name__ == "__main__":
    run()
