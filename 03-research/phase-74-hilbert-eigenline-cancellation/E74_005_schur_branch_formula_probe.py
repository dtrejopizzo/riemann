#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import cond, eigh, inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402


def setup(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    xi = vecs[:, 0].astype(complex)
    if xi[len(xi) // 2].real < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h.astype(complex), idx.astype(int), d, L, float(vals[0]), xi


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def run():
    print("E74.5 exact 2x2 Schur branch formula")
    print("S = QH(I-P)xi = (mu I - QHQ*G^-1)h, h=Qxi, G=QQ*.")
    print(" lam      L gamma condGB hB schurNormB directErrB row0B row1B eigMinB eigMaxB")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24), (24, 28), (28, 32)]:
        H, idx, d, L, mu, xi = setup(lam, n_modes)
        I = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:3]:
            Q = cauchy_rows(-1j * gamma, d)
            P = projector(Q)
            G = Q @ Q.conj().T
            hvec = Q @ xi
            schur = mu * np.eye(2, dtype=complex) - Q @ H @ Q.conj().T @ inv(G)
            S_formula = schur @ hvec
            S_direct = Q @ H @ (I - P) @ xi
            err = norm(S_formula - S_direct)
            eig = np.linalg.eigvals(schur)
            print(
                f"{lam:4d} {L:8.3f} {gamma:6.2f}"
                f" {bexp(cond(G), L):7.2f}"
                f" {bexp(norm(hvec), L):7.2f}"
                f" {bexp(norm(schur), L):10.2f}"
                f" {bexp(err, L):10.2f}"
                f" {bexp(S_direct[0], L):6.2f}"
                f" {bexp(S_direct[1], L):6.2f}"
                f" {bexp(min(abs(eig)), L):8.2f}"
                f" {bexp(max(abs(eig)), L):8.2f}"
            )


if __name__ == "__main__":
    run()
