#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, lstsq, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402


def setup(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    d = 2.0 * np.pi * idx / L
    return h, vals[0], d, L, xi


def cauchy_rows(w, d):
    return np.vstack([1.0 / (w + 1j * d), 1.0 / (-w + 1j * d)])


def project_row_to_plane(row, plane_rows):
    # Solve row ~= a q_w + b q_-w using transpose so coefficients multiply rows.
    coeff, *_ = lstsq(plane_rows.T, row, rcond=None)
    fit = coeff @ plane_rows
    residual = row - fit
    return coeff, residual


def run():
    print("E73.154 Cauchy-plane action probe")
    print("Projects q_w H_L and q_-w H_L onto span{q_w,q_-w}.")
    print("resB=log_L relative residual; evalB=log_L |res xi|; hB=log_L(|H0(w)|+|H0(-w)|).")
    print(" lam     L gamma row   resB  evalB     hB    invB    |a|B    |b|B  eigRel")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        h, mu, d, L, xi = setup(lam, n_modes)
        for gamma in GAMMAS[:3]:
            w = -1j * gamma
            plane = cauchy_rows(w, d)
            hsum = abs(plane[0] @ xi) + abs(plane[1] @ xi)
            amat = np.zeros((2, 2), dtype=complex)
            residuals = []
            for jj in range(2):
                row_j = plane[jj] @ h
                coeff_j, residual_j = project_row_to_plane(row_j, plane)
                amat[jj, :] = coeff_j
                residuals.append(residual_j)
            inv_norm = norm(np.linalg.inv(mu * np.eye(2) - amat), ord=2)
            for j in range(2):
                row = plane[j] @ h
                coeff = amat[j]
                residual = residuals[j]
                rel_res = norm(residual) / max(norm(row), 1e-300)
                eval_res = abs(residual @ xi)
                lhs = row @ xi
                rhs = mu * (plane[j] @ xi)
                eig_rel = abs(lhs - rhs) / max(abs(lhs), abs(rhs), 1e-300)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:3d}"
                    f" {bexp(rel_res, L):6.3f}"
                    f" {bexp(eval_res, L):6.3f}"
                    f" {bexp(hsum, L):6.3f}"
                    f" {bexp(inv_norm, L):7.3f}"
                    f" {bexp(abs(coeff[0]), L):7.3f}"
                    f" {bexp(abs(coeff[1]), L):7.3f}"
                    f" {eig_rel:8.1e}"
                )


if __name__ == "__main__":
    run()
