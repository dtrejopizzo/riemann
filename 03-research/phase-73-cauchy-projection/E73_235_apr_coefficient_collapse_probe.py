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
from E73_182_closed_series_arch_probe import packet_modes  # noqa: E402
from E73_201_mp_finite_assembly_probe import mp_arch_closed_digamma, mp_prime_modes  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows  # noqa: E402


mp.mp.dps = 100


def projector(q):
    return q.conj().T @ inv(q @ q.conj().T) @ q


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return H.astype(complex), idx.astype(int), d, L, xi.astype(complex)


def closed_center(row, idx, d, eta, L, lam):
    const, linear = packet_modes(row, idx, d, eta, L)
    return mp_arch_closed_digamma(const, linear, L, 80) - mp_prime_modes(const, linear, L, lam)


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def run():
    print("E73.235 APR coefficient collapse")
    print("Compares principal residual, eta-matrix residual, and coefficient/weight closed center.")
    print(" lam      L gamma row aprB etaB coeffB apr-etaB eta-coeffB ||Qeta||B")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        H, idx, d, L, xi = setup(lam, n_modes)
        I = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            P = projector(Q)
            R = I - P
            eta = R @ xi
            A = Q @ H @ Q.conj().T @ inv(Q @ Q.conj().T)
            h = Q @ xi
            qeta_norm = norm(Q @ eta)
            for row_id in range(2):
                row = Q[row_id]
                apr = (row @ H @ xi) - (A @ h)[row_id]
                eta_matrix = row @ H @ eta
                coeff = closed_center(row, idx, d, eta, L, lam)
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(apr, L):7.2f} {bexp(eta_matrix, L):7.2f}"
                    f" {bexp(coeff, L):8.2f}"
                    f" {bexp(apr-eta_matrix, L):9.2f}"
                    f" {bexp(eta_matrix-complex(coeff), L):10.2f}"
                    f" {bexp(qeta_norm, L):9.2f}"
                )


if __name__ == "__main__":
    run()
