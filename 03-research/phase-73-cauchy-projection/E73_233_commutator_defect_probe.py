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
from E73_223_coefficient_ball_budget import cauchy_rows  # noqa: E402


def projector(q):
    return q.conj().T @ inv(q @ q.conj().T) @ q


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
    return math.log(max(float(abs(z)), 1e-300)) / math.log(L)


def run():
    print("E73.233 canonical commutator defect identity")
    print("Checks C=qH(I-P)xi = <D,xi>, D=[I-P,H]q*+mu(I-P)q*.")
    print(" lam      L gamma row centerB pairB errB ||D||B ||comm||B ||muterm||B")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        H, idx, d, L, mu, xi = setup(lam, n_modes)
        I = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            P = projector(Q)
            R = I - P
            for row_id in range(2):
                q = Q[row_id : row_id + 1, :]
                qstar = q.conj().T[:, 0]
                center = (q @ H @ R @ xi)[0]
                S = R @ H @ qstar
                Y = R @ qstar
                D = S - (H - mu * I) @ Y
                comm = R @ H @ qstar - H @ R @ qstar
                muterm = mu * R @ qstar
                pair = np.vdot(D, xi)
                err = pair - center
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(center, L):8.2f} {bexp(pair, L):7.2f}"
                    f" {bexp(err, L):7.2f} {bexp(norm(D), L):7.2f}"
                    f" {bexp(norm(comm), L):9.2f} {bexp(norm(muterm), L):10.2f}"
                )


if __name__ == "__main__":
    run()
