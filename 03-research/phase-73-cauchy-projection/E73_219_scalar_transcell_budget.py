#!/usr/bin/env python3
import math
import sys

import mpmath as mp
import numpy as np
from numpy.linalg import inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


mp.mp.dps = 100


RHO_B = {
    (8, "1"): -55.67,
    (8, "1e6"): -45.98,
    (10, "1"): -52.16,
    (10, "1e6"): -43.11,
    (12, "1"): -49.87,
    (12, "1e6"): -41.26,
}


EPSH_B = {
    (8, "1"): -82.17,
    (8, "1e6"): -72.48,
    (10, "1"): -76.51,
    (10, "1e6"): -67.47,
    (12, "1"): -72.75,
    (12, "1e6"): -64.13,
}


def cauchy_rows(w, d):
    return np.vstack([1.0 / (w + 1j * d), 1.0 / (-w + 1j * d)])


def projector(q):
    return q.conj().T @ inv(q @ q.conj().T) @ q


def bexp(z, L):
    return math.log(max(float(abs(z)), 1e-300)) / math.log(L)


def center_data(lam, n_modes):
    # E73.206 audits this legacy center against the closed high-precision matrix.
    H0, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H0)
    xi0 = vecs[:, 0]
    if xi0[len(xi0) // 2] < 0:
        xi0 = -xi0
    xi0 = xi0 / norm(xi0)
    return idx.astype(int), L, H0, xi0, float(vals[0])


def scalar_budget(center, csec_label):
    idx, L, H0, xi0, mu0 = center
    lam = int(round(math.exp(L / 2.0)))
    n_modes = int((len(idx) - 1) / 2)
    d = 2.0 * np.pi * idx / L
    dim = len(idx)
    epsH = float(L ** EPSH_B[(lam, csec_label)])
    rho_eta = float(L ** RHO_B[(lam, csec_label)])
    rows = []
    ident = np.eye(len(idx), dtype=complex)
    for gamma in GAMMAS[:2]:
        q = cauchy_rows(-1j * gamma, d)
        P = projector(q)
        eta0 = (ident - P) @ xi0
        eta_norm = norm(eta0)
        for row_id in range(2):
            row = q[row_id]
            center = row @ (H0 @ eta0)
            sens_eta = norm(row @ H0)
            sens_H = norm(row) * eta_norm
            rad_eta = sens_eta * rho_eta
            rad_H = sens_H * epsH
            rad_mix = norm(row) * epsH * rho_eta
            rad_total = rad_eta + rad_H + rad_mix
            rows.append(
                {
                    "gamma": gamma,
                    "row_id": row_id,
                    "center": center,
                    "sens_eta": sens_eta,
                    "epsH": epsH,
                    "rho_eta": rho_eta,
                    "rad_eta": rad_eta,
                    "rad_H": rad_H,
                    "rad_mix": rad_mix,
                    "rad_total": rad_total,
                    "ratio": rad_total / max(abs(center), 1e-300),
                    "mu0": mu0,
                }
            )
    return L, dim, rows


def run():
    print("E73.219 scalar TRANS-CELL radius budget")
    print("Interval radius for C_a(eta)=q_a H eta from [H] and [eta].")
    print("Centers use the legacy matrix audited against closed entries in E73.206.")
    print(
        " lam     L    N  dim Csec gamma row centerB radEtaB radHB radMixB "
        "radTotB ratio"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        center = center_data(lam, n_modes)
        for csec_label in ["1", "1e6"]:
            L, dim, rows = scalar_budget(center, csec_label)
            for row in rows:
                print(
                    f"{lam:4d} {L:7.3f} {n_modes:4d} {dim:4d}"
                    f" {csec_label:>4s} {row['gamma']:7.2f} {row['row_id']:3d}"
                    f" {bexp(row['center'], L):7.2f}"
                    f" {bexp(row['rad_eta'], L):7.2f}"
                    f" {bexp(row['rad_H'], L):6.2f}"
                    f" {bexp(row['rad_mix'], L):8.2f}"
                    f" {bexp(row['rad_total'], L):7.2f}"
                    f" {row['ratio']:8.1e}"
                )


if __name__ == "__main__":
    run()
