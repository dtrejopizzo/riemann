#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import cholesky, eigvalsh, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402


def generalized_eigs(a, b):
    chol = cholesky(b)
    x = solve(chol, a)
    rel = solve(chol, x.T).T
    rel = 0.5 * (rel + rel.T)
    return eigvalsh(rel)


def run():
    print("E72.134 relative coercivity probe")
    print(" lam   L  minGen(act/model)  maxGen  minModel/L  theta*minModel/L")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        ge = generalized_eigs(c_actual, c_model)
        min_model = eigvalsh(c_model)[0]
        print(
            f"{lam:4.0f} {L:5.2f} {ge[0]:18.3e} {ge[-1]:7.3e} "
            f"{min_model/L:11.3e} {ge[0]*min_model/L:17.3e}"
        )


if __name__ == "__main__":
    run()
