#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import eigh, norm, slogdet

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_245_curv_quotient_defect import bexp, setup  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402


def replace_row(e, i, row):
    out = e.copy()
    out[i, :] = row
    return out


def reduced_data(H, mu):
    vals, vecs = eigh(H)
    j0 = int(np.argmin(np.abs(vals - mu)))
    xi = vecs[:, j0].astype(complex)
    if xi[len(xi) // 2].real < 0:
        xi = -xi
    xi = xi / norm(xi)
    nonzero = [vals[j] - mu for j in range(len(vals)) if j != j0]
    log_scale = sum(math.log(max(abs(v), 1e-300)) for v in nonzero)
    return xi, log_scale, vals


def row_replacement_logs(E, rho):
    logs = []
    for i in range(E.shape[0]):
        sign, logabs = slogdet(replace_row(E, i, rho))
        if abs(sign) == 0:
            logs.append(-math.inf)
        else:
            logs.append(float(logabs))
    return logs


def logsumexp(vals):
    finite = [v for v in vals if math.isfinite(v)]
    if not finite:
        return -math.inf
    m = max(finite)
    return m + math.log(sum(math.exp(v - m) for v in finite))


def run():
    print("E73.260 row-replacement ETA-ADJ verifier")
    print("Direct zero-free determinant form: det ReplaceRow(E;i,rho), normalized by reduced cofactor scale.")
    print(
        " lam      L gamma row rhoPairB maxDetB l2DetB "
        "predMaxB predL2B detScaleLog gapB"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20)]:
        H, _idx, d, L, mu, xi_setup = setup(lam, n_modes)
        xi, log_scale, vals = reduced_data(H, mu)
        # Align diagnostic vector to setup vector.
        phase = np.vdot(xi, xi_setup)
        if abs(phase) > 0:
            xi = xi * phase / abs(phase)
        E = H - mu * np.eye(len(d), dtype=complex)
        gap = sorted(abs(vals - mu))[1]
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            P = projector(Q)
            R = np.eye(len(d), dtype=complex) - P
            for row_id in range(2):
                rho = Q[row_id] @ H @ R
                pair = rho @ xi
                logs = row_replacement_logs(E, rho)
                max_log = max(logs)
                l2_log = 0.5 * logsumexp([2 * v for v in logs])
                # If adj(E)=scale xi xi*, replacing row i gives, up to the
                # standard sign convention, scale*(rho xi)*conj(xi_i).
                pred_max_log = log_scale + math.log(max(abs(pair), 1e-300)) + math.log(
                    max(np.max(np.abs(xi)), 1e-300)
                )
                pred_l2_log = log_scale + math.log(max(abs(pair), 1e-300))
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(pair, L):8.2f}"
                    f" {(max_log - log_scale) / math.log(L):7.2f}"
                    f" {(l2_log - log_scale) / math.log(L):7.2f}"
                    f" {(pred_max_log - log_scale) / math.log(L):8.2f}"
                    f" {(pred_l2_log - log_scale) / math.log(L):7.2f}"
                    f" {log_scale:11.2f}"
                    f" {bexp(gap, L):6.2f}"
                )


if __name__ == "__main__":
    run()
