#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import cholesky, norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64)]


def geom(idx, L, bq, chol, y):
    u = u_matrix(idx, L, y)
    raw = bq.T @ u @ bq
    x = solve(chol, raw)
    rel = solve(chol, x.T).T
    return float(norm(rel, "fro") ** 2)


def run():
    print("E72.211 continuous Geom envelope probe")
    print("Geom_x(y)=||C^-1/2 B* U_y B C^-1/2||_HS^2")
    print("lam L dim maxG at maxG*L maxG*L2 maxG*L3 intG intG*L2")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        chol = cholesky(c_model)
        us = np.linspace(0.02, 0.98, 97)
        gs = np.array([geom(idx, L, bq, chol, float(u * L)) for u in us])
        imax = int(np.argmax(gs))
        int_g = float(np.trapezoid(gs, us))
        maxg = float(gs[imax])
        print(
            f"{lam:3.0f} {L:5.2f} {len(idx):3d} {maxg:.6e} {us[imax]:.3f} "
            f"{maxg*L:.3e} {maxg*L*L:.3e} {maxg*L**3:.3e} "
            f"{int_g:.3e} {int_g*L*L:.3e}",
            flush=True,
        )

    print("\nShape samples")
    print("lam u=0.1 u=0.25 u=0.5 u=0.75 u=0.9")
    for lam, n_modes in WINDOWS[:4]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        chol = cholesky(c_model)
        vals = [geom(idx, L, bq, chol, u * L) for u in [0.1, 0.25, 0.5, 0.75, 0.9]]
        print(f"{lam:3.0f} " + " ".join(f"{v:.4e}" for v in vals), flush=True)


if __name__ == "__main__":
    run()
