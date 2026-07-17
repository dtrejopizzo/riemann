#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import cholesky, eigvalsh, norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402


def generalized_eigs(a, b):
    chol = cholesky(b)
    x = solve(chol, a)
    rel = solve(chol, x.T).T
    rel = 0.5 * (rel + rel.T)
    return eigvalsh(rel)


def run():
    print("E72.148 RFBD progressive uniform-gap probe", flush=True)
    print(
        " lam    L    dim   theta_H   eta_H  modelFloor/L  ||Delta||/L",
        flush=True,
    )
    rows = []
    # The last larger window from E72_139_rfbd_uniform_gap_probe is intentionally omitted
    # here so the probe stays interactive; the slow script remains available for deeper runs.
    for lam, n_modes in [(8, 24), (12, 30), (16, 38), (20, 46), (24, 54), (30, 66)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        theta = generalized_eigs(c_actual, c_model)[0]
        delta = c_actual - c_model
        model_floor = eigvalsh(c_model)[0] / L
        dnorm = norm(delta, 2) / L
        rows.append((L, theta, 1.0 - theta, model_floor, dnorm))
        print(
            f"{lam:4.0f} {L:6.3f} {len(bq.T):6d} "
            f"{theta:9.4f} {1.0-theta:7.4f} "
            f"{model_floor:13.4f} {dnorm:12.4f}",
            flush=True,
        )
    rows = np.array(rows)
    coeff = np.polyfit(rows[:, 0], rows[:, 1], 1)
    print("summary:", flush=True)
    print(
        f" theta range=[{rows[:,1].min():.4f},{rows[:,1].max():.4f}] "
        f"slope={coeff[0]:+.4f} intercept={coeff[1]:+.4f}",
        flush=True,
    )


if __name__ == "__main__":
    run()
