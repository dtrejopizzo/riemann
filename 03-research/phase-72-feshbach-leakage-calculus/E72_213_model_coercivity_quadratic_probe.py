#!/usr/bin/env python3
import sys

from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402


WINDOWS = [(6, 18), (8, 24), (10, 28), (12, 32), (16, 40), (20, 48), (24, 56), (28, 64)]


def run():
    print("E72.213 model coercivity quadratic probe")
    print("tests lambda_min(C_model) scaling")
    print("lam L dim minC minC/L minC/L2 maxC cond")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        vals = eigvalsh(c_model)
        print(
            f"{lam:3.0f} {L:5.2f} {len(idx):3d} "
            f"{vals[0]:.6e} {vals[0]/L:.6e} {vals[0]/(L*L):.6e} "
            f"{vals[-1]:.6e} {vals[-1]/vals[0]:.3e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
