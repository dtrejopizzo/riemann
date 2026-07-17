#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import cholesky, eigvalsh, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402


def relative_delta_eigs(c_actual, c_model):
    delta = c_actual - c_model
    chol = cholesky(c_model)
    x = solve(chol, delta)
    rel = solve(chol, x.T).T
    rel = 0.5 * (rel + rel.T)
    return eigvalsh(rel)


def run():
    print("E72.140 negative-HS certificate probe")
    print(" lam   L  dim  etaOp  negHS  negHS2  margin  thetaHS  negTrace")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40), (18, 44)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        eigs = relative_delta_eigs(c_actual, c_model)
        neg = eigs[eigs < 0.0]
        eta_op = max(0.0, -float(eigs[0]))
        neg_hs2 = float(np.sum(neg * neg))
        neg_hs = np.sqrt(neg_hs2)
        theta_hs = 1.0 - neg_hs
        margin = 1.0 - neg_hs2
        neg_trace = float(np.sum(-neg))
        print(
            f"{lam:4.0f} {L:5.2f} {len(eigs):4d} "
            f"{eta_op:6.3f} {neg_hs:6.3f} {neg_hs2:7.3f} "
            f"{margin:7.3f} {theta_hs:8.3f} {neg_trace:9.3e}"
        )


if __name__ == "__main__":
    run()
