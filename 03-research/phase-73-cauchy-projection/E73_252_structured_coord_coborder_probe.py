#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import norm, solve, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_245_curv_quotient_defect import dd_local_columns  # noqa: E402
from E73_246_quotient_coordinate_audit import quotient_defects, rank_from_svd  # noqa: E402
from E73_248_symbolic_pivot_rule_probe import best_minor_rule  # noqa: E402


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def rowspace_basis(rows, tol=1e-10):
    _u, s, vh = svd(rows, full_matrices=False)
    if len(s) == 0:
        return rows[:0]
    rank = int(np.sum(s > tol * s[0]))
    return vh[:rank, :]


def project(row, basis):
    if basis.shape[0] == 0:
        return np.zeros_like(row)
    return (row @ basis.conj().T) @ basis


def combined_dd_basis(gammas, d, L, E, rat_power):
    rows = []
    for gamma in gammas:
        prim = dd_local_columns(gamma, d, L, rat_power)
        rows.append(prim.conj().T @ E)
    return rowspace_basis(np.vstack(rows))


def coordinate_rows(lam, n_modes, rat_power):
    H, idx, d, L, mu, xi, D, _labels, _ranks = quotient_defects(
        lam, n_modes, rat_power
    )
    _u, s, _vh = svd(D, full_matrices=False)
    r = rank_from_svd(s)
    D = D[:r, :]
    piv = best_minor_rule(D, r)
    M = solve(D[:, piv], D)
    return H, idx, d, L, mu, xi, piv, M


def run():
    print("E73.252 structured coordinate coborder probe")
    print("Project coordinate rows m_j against combined DD-local generated image.")
    print(
        " lam      L srcPow fitPow rankS zMaxB resPairMaxB resNormMaxB "
        "relResMaxB fullRowPairB"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20)]:
        for src_power in [0, 1, 2]:
            H, _idx, d, L, mu, xi, _piv, M = coordinate_rows(
                lam, n_modes, src_power
            )
            E = H - mu * np.eye(H.shape[0], dtype=complex)
            full_basis = rowspace_basis(E)
            z = M @ xi
            for fit_power in [0, 1, 2, 3, 4]:
                basis = combined_dd_basis(GAMMAS[:2], d, L, E, fit_power)
                residuals = np.array([row - project(row, basis) for row in M])
                res_pair = residuals @ xi
                rel_res = np.array(
                    [norm(residuals[j]) / max(norm(M[j]), 1e-300) for j in range(M.shape[0])]
                )
                full_res = np.array([row - project(row, full_basis) for row in M])
                print(
                    f"{lam:4d} {L:8.3f} {src_power:6d} {fit_power:6d}"
                    f" {basis.shape[0]:5d}"
                    f" {bexp(np.max(np.abs(z)), L):6.2f}"
                    f" {bexp(np.max(np.abs(res_pair)), L):11.2f}"
                    f" {bexp(np.max([norm(x) for x in residuals]), L):11.2f}"
                    f" {bexp(np.max(rel_res), L):11.2f}"
                    f" {bexp(np.max(np.abs(full_res @ xi)), L):12.2f}"
                )
            print("-")


if __name__ == "__main__":
    run()
