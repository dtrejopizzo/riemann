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
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h_actual.astype(complex), h_arch.astype(complex), idx.astype(int), d, L, xi.astype(complex)


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def rel(z, base):
    return abs(complex(z)) / max(abs(complex(base)), 1e-300)


def row_angle(a, b):
    denom = norm(a) * norm(b)
    if denom == 0:
        return 0.0
    return abs(np.vdot(a.reshape(-1), b.reshape(-1))) / denom


def run():
    print("E73.264 paired arch-prime alignment probe")
    print("Tests whether UNIF-ETA is row alignment or only xi-paired cancellation.")
    print(
        " lam      L gamma row centerB archB primeB "
        "pairRel rowDiffRel rowCos etaArchRel etaPrimeRel"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20), (20, 24)]:
        h_actual, h_arch, idx, d, L, xi = setup(lam, n_modes)
        h_prime = h_arch - h_actual
        eye = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            qmat = cauchy_rows(-1j * gamma, d)
            res = eye - projector(qmat)
            eta = res @ xi
            for row_id in range(2):
                q = qmat[row_id : row_id + 1, :]
                rho_a = q @ h_arch @ res
                rho_p = q @ h_prime @ res
                arch = (rho_a @ xi)[0]
                prime = (rho_p @ xi)[0]
                center = arch - prime
                rowdiff_rel = norm(rho_a - rho_p) / max(norm(rho_a), norm(rho_p), 1e-300)
                pair_rel = rel(center, arch)
                eta_arch = (q @ h_arch @ eta)[0]
                eta_prime = (q @ h_prime @ eta)[0]
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(center, L):8.2f}"
                    f" {bexp(arch, L):7.2f}"
                    f" {bexp(prime, L):7.2f}"
                    f" {pair_rel:8.1e}"
                    f" {rowdiff_rel:10.3e}"
                    f" {row_angle(rho_a, rho_p):7.4f}"
                    f" {rel(eta_arch, arch):10.2e}"
                    f" {rel(eta_prime, prime):11.2e}"
                )


if __name__ == "__main__":
    run()

