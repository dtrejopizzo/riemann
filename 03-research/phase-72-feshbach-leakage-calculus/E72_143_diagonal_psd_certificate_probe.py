#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import cholesky, eigvalsh, norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402


def relative_matrix(c_actual, c_model):
    delta = c_actual - c_model
    chol = cholesky(c_model)
    x = solve(chol, delta)
    rel = solve(chol, x.T).T
    return 0.5 * (rel + rel.T)


def run():
    print("E72.143 diagonal PSD certificate probe")
    print(" lam   L  dim  optPSDdist  diagPSDdist  diagDist2  diagMargin  offFrob")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40), (18, 44)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        krel = relative_matrix(c_actual, c_model)
        eigs = eigvalsh(krel)
        opt = np.sqrt(np.sum(eigs[eigs < 0.0] ** 2))
        diag_pos = np.diag(np.maximum(np.diag(krel), 0.0))
        diag_dist = norm(krel - diag_pos, "fro")
        off = krel - np.diag(np.diag(krel))
        print(
            f"{lam:4.0f} {L:5.2f} {krel.shape[0]:4d} "
            f"{opt:10.3f} {diag_dist:12.3f} {diag_dist*diag_dist:10.3f} "
            f"{1-diag_dist*diag_dist:10.3f} {norm(off,'fro'):8.3f}"
        )


if __name__ == "__main__":
    run()
