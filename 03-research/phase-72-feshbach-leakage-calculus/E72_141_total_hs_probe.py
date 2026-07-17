#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import cholesky, eigvalsh, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402


def relative_matrix(c_actual, c_model):
    delta = c_actual - c_model
    chol = cholesky(c_model)
    x = solve(chol, delta)
    rel = solve(chol, x.T).T
    return 0.5 * (rel + rel.T)


def run():
    print("E72.141 total relative HS probe")
    print(" lam   L  dim  totalHS  totalHS2  negHS  posHS  trace  min  max")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40), (18, 44)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        rel = relative_matrix(c_actual, c_model)
        eigs = eigvalsh(rel)
        neg = eigs[eigs < 0.0]
        pos = eigs[eigs > 0.0]
        total_hs2 = float(np.sum(eigs * eigs))
        neg_hs = float(np.sqrt(np.sum(neg * neg)))
        pos_hs = float(np.sqrt(np.sum(pos * pos)))
        print(
            f"{lam:4.0f} {L:5.2f} {len(eigs):4d} "
            f"{np.sqrt(total_hs2):8.3f} {total_hs2:9.3f} "
            f"{neg_hs:6.3f} {pos_hs:6.3f} {np.sum(eigs):6.3f} "
            f"{eigs[0]:6.3f} {eigs[-1]:6.3f}"
        )


if __name__ == "__main__":
    run()
