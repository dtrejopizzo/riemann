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
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H)
    mu = vals[0]
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return H.astype(complex), idx.astype(int), d, L, float(mu), xi.astype(complex)


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def run():
    print("E73.240 eigen-coefficient branch audit")
    print("Checks QH(I-P)xi = (mu I-A)Qxi and exposes h-dependence.")
    print(" lam      L gamma row centerB branchB errB hB muB opAB")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20), (20, 24)]:
        H, idx, d, L, mu, xi = setup(lam, n_modes)
        I = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            P = projector(Q)
            R = I - P
            h = Q @ xi
            A = Q @ H @ Q.conj().T @ inv(Q @ Q.conj().T)
            branch = (mu * np.eye(2) - A) @ h
            center = Q @ H @ R @ xi
            op_a = norm(A, 2)
            for row_id in range(2):
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(center[row_id], L):8.2f}"
                    f" {bexp(branch[row_id], L):8.2f}"
                    f" {bexp(center[row_id]-branch[row_id], L):7.2f}"
                    f" {bexp(norm(h), L):7.2f} {bexp(mu, L):7.2f}"
                    f" {bexp(op_a, L):7.2f}"
                )


if __name__ == "__main__":
    run()
