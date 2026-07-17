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


def psd_projection_distance(krel):
    eigs, vecs = np.linalg.eigh(krel)
    pos = np.maximum(eigs, 0.0)
    pmat = (vecs * pos) @ vecs.T
    dist = norm(krel - pmat, "fro")
    return dist, eigvalsh(pmat)[0], eigs[0]


def run():
    print("E72.142 SDP distance certificate probe")
    print(" lam   L  dim  distPSD  dist2  margin  minP  minK")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40), (18, 44)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        krel = relative_matrix(c_actual, c_model)
        dist, min_p, min_k = psd_projection_distance(krel)
        print(
            f"{lam:4.0f} {L:5.2f} {krel.shape[0]:4d} "
            f"{dist:7.3f} {dist*dist:6.3f} {1-dist*dist:7.3f} "
            f"{min_p:6.1e} {min_k:6.3f}"
        )


if __name__ == "__main__":
    run()
