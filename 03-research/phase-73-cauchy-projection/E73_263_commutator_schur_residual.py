#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    h_arch, _, _ = build(lam, n_modes, include_arith=False)
    vals, vecs = np.linalg.eigh(h_actual)
    mu = vals[0]
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return (
        h_actual.astype(complex),
        h_arch.astype(complex),
        idx.astype(int),
        d,
        L,
        float(mu),
        xi.astype(complex),
    )


def bexp(z, L):
    if isinstance(z, np.ndarray):
        z = z.reshape(-1)[0]
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def run():
    print("E73.263 commutator-Schur residual audit")
    print("rho=qHR=qH-(qHQ*)GQ=-q[H,P]; reports arch/prime split paired with xi.")
    print(
        " lam      L gamma row centerB schurErrB commErrB "
        "archB primeB cancelB rhoNormB archNormB primeNormB"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20), (20, 24)]:
        h_actual, h_arch, idx, d, L, _mu, xi = setup(lam, n_modes)
        h_prime = h_arch - h_actual
        eye = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            qmat = cauchy_rows(-1j * gamma, d)
            gram_inv = inv(qmat @ qmat.conj().T)
            proj = projector(qmat)
            res = eye - proj
            for row_id in range(2):
                q = qmat[row_id : row_id + 1, :]
                rho = q @ h_actual @ res
                schur = q @ h_actual - (q @ h_actual @ qmat.conj().T @ gram_inv) @ qmat
                comm = -(q @ (h_actual @ proj - proj @ h_actual))
                rho_arch = q @ h_arch @ res
                rho_prime = q @ h_prime @ res
                center = (rho @ xi)[0]
                arch = (rho_arch @ xi)[0]
                prime = (rho_prime @ xi)[0]
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(center, L):8.2f}"
                    f" {bexp((rho-schur) @ xi, L):9.2f}"
                    f" {bexp((rho-comm) @ xi, L):8.2f}"
                    f" {bexp(arch, L):7.2f}"
                    f" {bexp(prime, L):7.2f}"
                    f" {bexp(arch-prime, L):8.2f}"
                    f" {bexp(norm(rho), L):8.2f}"
                    f" {bexp(norm(rho_arch), L):9.2f}"
                    f" {bexp(norm(rho_prime), L):10.2f}"
                )


if __name__ == "__main__":
    run()
