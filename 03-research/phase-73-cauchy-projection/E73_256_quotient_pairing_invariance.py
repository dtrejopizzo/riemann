#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_245_curv_quotient_defect import (  # noqa: E402
    bexp,
    dd_local_columns,
    project_to_rowspace,
    rowspace_basis,
    setup,
)
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402


def audit_case(lam, n_modes, rat_power):
    H, _idx, d, L, mu, xi = setup(lam, n_modes)
    eye = np.eye(len(d), dtype=complex)
    E = H - mu * eye
    rows = []
    for gamma in GAMMAS[:2]:
        Q = cauchy_rows(-1j * gamma, d)
        P = projector(Q)
        R = eye - P
        prim = dd_local_columns(gamma, d, L, rat_power)
        module_rows = prim.conj().T @ E
        basis = rowspace_basis(module_rows)
        for row_id in range(2):
            rho = Q[row_id] @ H @ R
            generated = project_to_rowspace(rho, basis)
            delta = rho - generated
            rows.append(
                {
                    "gamma": gamma,
                    "row_id": row_id,
                    "rho_pair": rho @ xi,
                    "gen_pair": generated @ xi,
                    "delta_pair": delta @ xi,
                    "inv_err": (delta @ xi) - (rho @ xi),
                    "e_xi": norm(E @ xi),
                    "module_rank": basis.shape[0],
                    "rho_norm": norm(rho),
                    "delta_norm": norm(delta),
                    "gen_norm": norm(generated),
                }
            )
    return L, rows


def run():
    print("E73.256 quotient pairing invariance")
    print("Because M_DD={Y*E} and E xi=0, projection modulo M_DD cannot change row pairing with xi.")
    print(
        " lam      L pow gamma row rank rhoPairB genPairB deltaPairB "
        "invErrB ExiB rhoNormB deltaNormB"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20)]:
        for rat_power in [0, 1, 2, 3]:
            L, rows = audit_case(lam, n_modes, rat_power)
            for r in rows:
                print(
                    f"{lam:4d} {L:8.3f} {rat_power:3d}"
                    f" {r['gamma']:6.2f} {r['row_id']:3d} {r['module_rank']:4d}"
                    f" {bexp(r['rho_pair'], L):8.2f}"
                    f" {bexp(r['gen_pair'], L):8.2f}"
                    f" {bexp(r['delta_pair'], L):10.2f}"
                    f" {bexp(r['inv_err'], L):8.2f}"
                    f" {bexp(r['e_xi'], L):6.2f}"
                    f" {bexp(r['rho_norm'], L):8.2f}"
                    f" {bexp(r['delta_norm'], L):10.2f}"
                )


if __name__ == "__main__":
    run()
