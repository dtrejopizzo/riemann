#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, lstsq, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    h_model, _, _ = build(lam, n_modes, include_arith=False)
    prime = h_model - h_actual
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h_actual, h_model, prime, vals[0], d, L, xi


def cauchy_rows(w, d):
    return np.vstack([1.0 / (w + 1j * d), 1.0 / (-w + 1j * d)])


def plane_action(op, plane):
    coeffs = []
    residuals = []
    for j in range(2):
        row = plane[j] @ op
        coeff, *_ = lstsq(plane.T, row, rcond=None)
        coeffs.append(coeff)
        residuals.append(row - coeff @ plane)
    return np.array(coeffs), np.array(residuals)


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.180 Cauchy-principal cell identity probe")
    print("Checks r_j = (q_j H xi) - A_j h and signed model-prime principal cancellation.")
    print(" lam     L gamma   row  cellB  princB   rB  errB  modelPB primePB signedB")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (32, 36)]:
        h, h_model, prime, _mu, d, L, xi = setup(lam, n_modes)
        for gamma in GAMMAS[:3]:
            w = -1j * gamma
            plane = cauchy_rows(w, d)
            hvec = plane @ xi
            a_act, rho_act = plane_action(h, plane)
            a_mod, _rho_mod = plane_action(h_model, plane)
            a_pri, _rho_pri = plane_action(prime, plane)
            for j in range(2):
                cell = plane[j] @ (h @ xi)
                principal = a_act[j] @ hvec
                residual_scalar = rho_act[j] @ xi
                identity_err = abs((cell - principal) - residual_scalar)

                model_principal_cell = plane[j] @ (h_model @ xi) - a_mod[j] @ hvec
                prime_principal_cell = plane[j] @ (prime @ xi) - a_pri[j] @ hvec
                signed = model_principal_cell - prime_principal_cell
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:5d}"
                    f" {bexp(cell, L):6.2f} {bexp(principal, L):7.2f}"
                    f" {bexp(residual_scalar, L):6.2f} {bexp(identity_err, L):6.2f}"
                    f" {bexp(model_principal_cell, L):8.2f}"
                    f" {bexp(prime_principal_cell, L):7.2f}"
                    f" {bexp(signed, L):7.2f}"
                )


if __name__ == "__main__":
    run()
