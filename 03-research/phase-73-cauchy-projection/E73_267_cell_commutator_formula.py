#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build, make_q, primes_upto  # noqa: E402
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


def qcell_matrix(idx, L, y):
    n = len(idx)
    mat = np.zeros((n, n), dtype=float)
    for a, ma in enumerate(idx):
        for b, mb in enumerate(idx):
            mat[a, b] = make_q(int(ma), int(mb), L)(y)
    return mat.astype(complex)


def prime_cell_sum(row, eta, idx, L, lam):
    total = 0j
    abs_sum = 0.0
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = math.log(int(p))
        pm = int(p)
        k = 1
        while pm <= maxn:
            y = k * lp
            weight = lp * (pm ** -0.5)
            term = weight * (row @ qcell_matrix(idx, L, y) @ eta)[0]
            total += term
            abs_sum += abs(term)
            pm *= int(p)
            k += 1
    return total, abs_sum


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def run():
    print("E73.267 prime cell commutator formula")
    print("Checks qH^P Rxi equals finite prime-cell sum of q Q_y Rxi.")
    print(" lam      L gamma row primeB cellB errB absCellB abs/prime archB centerB")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20)]:
        h_actual, h_arch, idx, d, L, xi = setup(lam, n_modes)
        h_prime = h_arch - h_actual
        eye = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            qmat = cauchy_rows(-1j * gamma, d)
            res = eye - projector(qmat)
            eta = res @ xi
            for row_id in range(2):
                row = qmat[row_id : row_id + 1, :]
                prime = (row @ h_prime @ eta)[0]
                cell, abs_cell = prime_cell_sum(row, eta, idx, L, lam)
                arch = (row @ h_arch @ eta)[0]
                center = arch - prime
                ratio = abs_cell / max(abs(prime), 1e-300)
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(prime, L):8.2f}"
                    f" {bexp(cell, L):7.2f}"
                    f" {bexp(prime-cell, L):7.2f}"
                    f" {bexp(abs_cell, L):8.2f}"
                    f" {ratio:9.2e}"
                    f" {bexp(arch, L):7.2f}"
                    f" {bexp(center, L):8.2f}"
                )


if __name__ == "__main__":
    run()

