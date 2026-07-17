#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, lstsq, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

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


def plane_projector(plane):
    # Columns span the row plane as vectors in C^n.
    u, s, _ = svd(plane.T, full_matrices=False)
    rank = int(np.sum(s > 1e-12 * s[0]))
    u = u[:, :rank]
    return u @ u.conj().T


def plane_action_lstsq(op, plane):
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
    print("E73.186 transverse Schur probe")
    print("Tests rho_j xi = q_j H (I-P_Q) xi and the model-prime transverse split.")
    print(" lam     L gamma row residB transB errB  modelTB primeTB signedTB")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24), (24, 28), (32, 36)]:
        h, h_model, prime, _mu, d, L, xi = setup(lam, n_modes)
        for gamma in GAMMAS[:2]:
            plane = cauchy_rows(-1j * gamma, d)
            p = plane_projector(plane)
            qperp_xi = (np.eye(len(d)) - p) @ xi
            _a, rho = plane_action_lstsq(h, plane)
            for j in range(2):
                residual = rho[j] @ xi
                transverse = plane[j] @ (h @ qperp_xi)
                err = abs(residual - transverse)
                model_t = plane[j] @ (h_model @ qperp_xi)
                prime_t = plane[j] @ (prime @ qperp_xi)
                signed_t = model_t - prime_t
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:3d}"
                    f" {bexp(residual, L):7.2f} {bexp(transverse, L):7.2f}"
                    f" {bexp(err, L):6.2f}"
                    f" {bexp(model_t, L):8.2f} {bexp(prime_t, L):7.2f}"
                    f" {bexp(signed_t, L):8.2f}"
                )


if __name__ == "__main__":
    run()
