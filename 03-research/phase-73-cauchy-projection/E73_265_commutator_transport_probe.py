#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import norm

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
    return h_actual.astype(complex), h_arch.astype(complex), idx.astype(int), d, L, float(mu), xi.astype(complex)


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def rel(z, base):
    return abs(complex(z)) / max(abs(complex(base)), 1e-300)


def run():
    print("E73.265 commutator transport probe")
    print("Compares right-projected Schur pairing q H R xi with left-projected eigenline pairing q R H xi.")
    print(
        " lam      L gamma row centerB rightAB rightPB leftAB leftPB "
        "leftMatchB commAB commPB commMatchB"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20), (20, 24)]:
        h_actual, h_arch, idx, d, L, mu, xi = setup(lam, n_modes)
        h_prime = h_arch - h_actual
        eye = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            qmat = cauchy_rows(-1j * gamma, d)
            proj = projector(qmat)
            res = eye - proj
            for row_id in range(2):
                q = qmat[row_id : row_id + 1, :]
                right_a = (q @ h_arch @ res @ xi)[0]
                right_p = (q @ h_prime @ res @ xi)[0]
                center = right_a - right_p

                # Left-projected matching uses a=qR in the eigenline equation:
                # qR H^A xi - qR H^P xi = mu qR xi = 0.
                left_a = (q @ res @ h_arch @ xi)[0]
                left_p = (q @ res @ h_prime @ xi)[0]
                left_match = left_a - left_p

                # The center is the difference of arch/prime commutators.
                comm_a = right_a - left_a
                comm_p = right_p - left_p
                comm_match = comm_a - comm_p
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(center, L):8.2f}"
                    f" {bexp(right_a, L):8.2f}"
                    f" {bexp(right_p, L):8.2f}"
                    f" {bexp(left_a, L):7.2f}"
                    f" {bexp(left_p, L):7.2f}"
                    f" {bexp(left_match, L):10.2f}"
                    f" {bexp(comm_a, L):7.2f}"
                    f" {bexp(comm_p, L):7.2f}"
                    f" {bexp(comm_match-center, L):10.2f}"
                )


if __name__ == "__main__":
    run()

