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
    print("E72.139 relative negative spectrum probe")
    print(
        " lam   L  dim  negRank  minRelDelta  eta  negTrace  "
        "negFrob  posMax"
    )
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40), (18, 44)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        eigs = relative_delta_eigs(c_actual, c_model)
        neg = eigs[eigs < -1e-10]
        pos = eigs[eigs > 1e-10]
        eta = max(0.0, -float(eigs[0]))
        neg_trace = float(np.sum(-neg))
        neg_frob = float(np.sqrt(np.sum(neg * neg)))
        pos_max = float(pos[-1]) if len(pos) else 0.0
        print(
            f"{lam:4.0f} {L:5.2f} {len(eigs):4d} {len(neg):8d} "
            f"{eigs[0]:12.3e} {eta:6.3f} {neg_trace:9.3e} "
            f"{neg_frob:8.3e} {pos_max:7.3e}"
        )


if __name__ == "__main__":
    run()
