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
    return h_actual.astype(complex), h_arch.astype(complex), idx.astype(int), d, L, float(mu), xi.astype(complex)


def bexp(z, L):
    if isinstance(z, np.ndarray):
        z = norm(z)
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def run():
    print("E73.266 rank-two transport collapse audit")
    print("Checks qHRxi = (mu e_a - qHQ*G) h, h=Qxi.")
    print(
        " lam      L gamma row centerB r2B errB hB muB BHopB "
        "archR2B primeR2B archErrB primeErrB"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20), (20, 24)]:
        h_actual, h_arch, idx, d, L, mu, xi = setup(lam, n_modes)
        h_prime = h_arch - h_actual
        eye = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            qmat = cauchy_rows(-1j * gamma, d)
            gram_inv = inv(qmat @ qmat.conj().T)
            proj = projector(qmat)
            res = eye - proj
            hvec = qmat @ xi
            b_actual = qmat @ h_actual @ qmat.conj().T @ gram_inv
            b_arch = qmat @ h_arch @ qmat.conj().T @ gram_inv
            b_prime = qmat @ h_prime @ qmat.conj().T @ gram_inv
            branch = (mu * np.eye(2) - b_actual) @ hvec
            arch_branch = (qmat @ h_arch @ xi) - b_arch @ hvec
            prime_branch = (qmat @ h_prime @ xi) - b_prime @ hvec
            center = qmat @ h_actual @ res @ xi
            arch_right = qmat @ h_arch @ res @ xi
            prime_right = qmat @ h_prime @ res @ xi
            for row_id in range(2):
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(center[row_id], L):8.2f}"
                    f" {bexp(branch[row_id], L):7.2f}"
                    f" {bexp(center[row_id]-branch[row_id], L):7.2f}"
                    f" {bexp(hvec, L):7.2f}"
                    f" {bexp(mu, L):7.2f}"
                    f" {bexp(norm(b_actual, 2), L):7.2f}"
                    f" {bexp(arch_branch[row_id], L):8.2f}"
                    f" {bexp(prime_branch[row_id], L):9.2f}"
                    f" {bexp(arch_right[row_id]-arch_branch[row_id], L):9.2f}"
                    f" {bexp(prime_right[row_id]-prime_branch[row_id], L):10.2f}"
                )


if __name__ == "__main__":
    run()

