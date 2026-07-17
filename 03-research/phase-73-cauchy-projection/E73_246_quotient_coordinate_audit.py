#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_245_curv_quotient_defect import (  # noqa: E402
    dd_local_columns,
    project_to_rowspace,
    rowspace_basis,
    setup,
)
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def rank_from_svd(s, tol=1e-10):
    if len(s) == 0 or s[0] == 0:
        return 0
    return int(np.sum(s > tol * s[0]))


def quotient_defects(lam, n_modes, rat_power):
    H, idx, d, L, mu, xi = setup(lam, n_modes)
    eye = np.eye(len(idx), dtype=complex)
    E = H - mu * eye
    defects = []
    labels = []
    ranks = []
    for gamma_id, gamma in enumerate(GAMMAS[:2]):
        Q = cauchy_rows(-1j * gamma, d)
        P = projector(Q)
        R = eye - P
        prim = dd_local_columns(gamma, d, L, rat_power)
        rows = prim.conj().T @ E
        basis = rowspace_basis(rows)
        ranks.append(basis.shape[0])
        for row_id in range(2):
            rho = Q[row_id] @ H @ R
            delta = rho - project_to_rowspace(rho, basis)
            defects.append(delta)
            labels.append((gamma_id, gamma, row_id))
    return H, idx, d, L, mu, xi, np.vstack(defects), labels, ranks


def coordinate_audit(lam, n_modes, rat_power):
    _H, _idx, _d, L, _mu, xi, D, labels, ranks = quotient_defects(
        lam, n_modes, rat_power
    )
    _u, s, vh = svd(D, full_matrices=False)
    r = rank_from_svd(s)
    basis = vh[:r, :]
    coeff = D @ basis.conj().T
    zq = basis @ xi
    pair_direct = D @ xi
    pair_coord = coeff @ zq
    coord_err = norm(pair_direct - pair_coord)
    pair_norm = norm(pair_direct)
    if r:
        coeff_norms = np.array([norm(c) for c in coeff])
    else:
        coeff_norms = np.array([0.0])
    return {
        "L": L,
        "labels": labels,
        "ranks": ranks,
        "defect_rank": r,
        "singular": s,
        "pair_direct": pair_direct,
        "pair_norm": pair_norm,
        "coord_err": coord_err,
        "zq": zq,
        "coeff_norms": coeff_norms,
    }


def run():
    print("E73.246 quotient coordinate audit")
    print("Stack defects delta_a for two critical gammas and two Cauchy rows.")
    print("Coordinate form: delta_a xi = theta_a dot z_Q.")
    print(
        " lam      L pow MDranks qRank s1B sLastB pairMaxB pairNormB "
        "zQMaxB zQNormB coeffMaxB coordErrB"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20)]:
        for rat_power in [0, 1, 2]:
            out = coordinate_audit(lam, n_modes, rat_power)
            L = out["L"]
            s = out["singular"]
            r = out["defect_rank"]
            s1 = s[0] if len(s) else 0.0
            slast = s[r - 1] if r else 0.0
            pair = out["pair_direct"]
            zq = out["zq"]
            coeff_norms = out["coeff_norms"]
            print(
                f"{lam:4d} {L:8.3f} {rat_power:3d}"
                f" {str(out['ranks']):>9s} {r:5d}"
                f" {bexp(s1, L):6.2f} {bexp(slast, L):7.2f}"
                f" {bexp(np.max(np.abs(pair)), L):8.2f}"
                f" {bexp(out['pair_norm'], L):9.2f}"
                f" {bexp(np.max(np.abs(zq)) if len(zq) else 0.0, L):7.2f}"
                f" {bexp(norm(zq), L):8.2f}"
                f" {bexp(np.max(coeff_norms), L):9.2f}"
                f" {bexp(out['coord_err'], L):9.2f}"
            )
    print()
    print("Per-coordinate pairings for canonical pow=0:")
    print(" lam      L qRank label        pairB")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20)]:
        out = coordinate_audit(lam, n_modes, 0)
        L = out["L"]
        for label, pair in zip(out["labels"], out["pair_direct"]):
            gamma_id, gamma, row_id = label
            print(
                f"{lam:4d} {L:8.3f} {out['defect_rank']:5d}"
                f" g{gamma_id}:{gamma:5.1f}:r{row_id}"
                f" {bexp(pair, L):10.2f}"
            )


if __name__ == "__main__":
    run()
