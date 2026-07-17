#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_245_curv_quotient_defect import bexp, setup  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402


def reduced_adjugate_data(H, mu):
    vals, vecs = eigh(H)
    j0 = int(np.argmin(np.abs(vals - mu)))
    nonzero = [abs(vals[j] - mu) for j in range(len(vals)) if j != j0]
    log_abs_scale = sum(math.log(max(v, 1e-300)) for v in nonzero)
    xi = vecs[:, j0].astype(complex)
    if xi[len(xi) // 2].real < 0:
        xi = -xi
    xi = xi / norm(xi)
    return xi, log_abs_scale, vals


def run():
    print("E73.259 ETA adjugate certificate")
    print("For simple ground eigenvalue, Adj_red(E)=scale*xi xi*. ETA-DIV iff rho Adj_red(E)=0.")
    print(
        " lam      L gamma row etaB rhoPairB adjNormB adjScaledB "
        "detScaleLog gapB errXiB"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20), (20, 24)]:
        H, _idx, d, L, mu, xi_setup = setup(lam, n_modes)
        xi_adj, log_adj_scale, vals = reduced_adjugate_data(H, mu)
        # Align phase with setup vector for diagnostic.
        phase = np.vdot(xi_adj, xi_setup)
        if abs(phase) > 0:
            xi_adj = xi_adj * phase / abs(phase)
        err_xi = norm(xi_adj - xi_setup)
        gap = sorted(abs(vals - mu))[1]
        eye = np.eye(len(d), dtype=complex)
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            P = projector(Q)
            R = eye - P
            eta = R @ xi_setup
            for row_id in range(2):
                rho = Q[row_id] @ H @ R
                pair = rho @ xi_setup
                # Avoid forming the huge/small adjugate.  The reduced adjugate
                # row is scale*(rho xi)*xi^*.
                adj_norm_log = log_adj_scale + math.log(max(abs(pair), 1e-300))
                adj_scaled = abs(pair) * norm(xi_adj)
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(norm(eta), L):6.2f}"
                    f" {bexp(pair, L):8.2f}"
                    f" {adj_norm_log / math.log(L):8.2f}"
                    f" {bexp(adj_scaled, L):10.2f}"
                    f" {log_adj_scale:11.2f}"
                    f" {bexp(gap, L):6.2f}"
                    f" {bexp(err_xi, L):7.2f}"
                )


if __name__ == "__main__":
    run()
