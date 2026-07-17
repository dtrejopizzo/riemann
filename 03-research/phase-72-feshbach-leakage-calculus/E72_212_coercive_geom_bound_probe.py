#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import cholesky, eigvalsh, norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56)]


def geom_and_raw(idx, L, bq, chol, y):
    u = u_matrix(idx, L, y)
    raw = bq.T @ u @ bq
    x = solve(chol, raw)
    rel = solve(chol, x.T).T
    return float(norm(rel, "fro") ** 2), float(norm(raw, "fro") ** 2)


def run():
    print("E72.212 coercive geometric bound probe")
    print("compares Geom to rawHS/lambda_min(C)^2")
    print("lam L dim minC minC/L u Geom rawHS crudeBound ratio")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        chol = cholesky(c_model)
        minc = float(eigvalsh(c_model)[0])
        for u in [0.1, 0.25, 0.5, 0.75, 0.9]:
            g, raw = geom_and_raw(idx, L, bq, chol, u * L)
            crude = raw / (minc * minc)
            ratio = crude / max(g, 1e-300)
            print(
                f"{lam:3.0f} {L:5.2f} {len(idx):3d} {minc:.3e} {minc/L:.3e} "
                f"{u:.2f} {g:.3e} {raw:.3e} {crude:.3e} {ratio:.2e}",
                flush=True,
            )


if __name__ == "__main__":
    run()
