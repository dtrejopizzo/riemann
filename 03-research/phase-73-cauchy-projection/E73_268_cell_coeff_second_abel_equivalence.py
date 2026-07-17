#!/usr/bin/env python3
import math
import sys

import mpmath as mp
import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build, make_q, primes_upto  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_182_closed_series_arch_probe import packet_modes  # noqa: E402
from E73_201_mp_finite_assembly_probe import mp_arch_closed_digamma, mp_prime_modes  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402


mp.mp.dps = 90


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


def qcell_eval(row, eta, idx, L, y):
    total = 0j
    for a, ma in enumerate(idx):
        if abs(row[a]) == 0:
            continue
        for b, mb in enumerate(idx):
            total += row[a] * make_q(int(ma), int(mb), L)(y) * eta[b]
    return total


def mp_eval_modes(const, linear, y):
    ymp = mp.mpf(y)
    total = mp.mpc(0)
    for om, c in const.items():
        total += mp.mpc(complex(c)) * mp.e ** (1j * mp.mpf(float(om)) * ymp)
    for om, ell in linear.items():
        total += mp.mpc(complex(ell)) * ymp * mp.e ** (1j * mp.mpf(float(om)) * ymp)
    return total


def prime_cell_sum(row, eta, idx, L, lam):
    total = 0j
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = math.log(int(p))
        pm = int(p)
        k = 1
        while pm <= maxn:
            total += lp * (pm ** -0.5) * qcell_eval(row, eta, idx, L, k * lp)
            pm *= int(p)
            k += 1
    return total


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def run():
    print("E73.268 cell/coefficient equivalence")
    print("Checks B(y)=qQ_yeta modes, prime modes=prime cells, and center agreement.")
    print(" lam      L gamma row maxBerrB primeErrB centerErrB matrixErrB centerB")
    sample_fracs = [0.0, 0.17, 0.37, 0.61, 0.83, 1.0]
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20)]:
        h_actual, h_arch, idx, d, L, xi = setup(lam, n_modes)
        eye = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            qmat = cauchy_rows(-1j * gamma, d)
            res = eye - projector(qmat)
            eta = res @ xi
            for row_id in range(2):
                row = qmat[row_id]
                const, linear = packet_modes(row, idx, d, eta, L)
                max_berr = 0.0
                for frac in sample_fracs:
                    y = frac * L
                    max_berr = max(
                        max_berr,
                        abs(qcell_eval(row, eta, idx, L, y) - complex(mp_eval_modes(const, linear, y))),
                    )
                prime_modes_val = mp_prime_modes(const, linear, L, lam)
                prime_cell_val = prime_cell_sum(row, eta, idx, L, lam)
                center_coeff = mp_arch_closed_digamma(const, linear, L, 80) - prime_modes_val
                matrix_center = row @ h_actual @ eta
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(max_berr, L):8.2f}"
                    f" {bexp(prime_modes_val-prime_cell_val, L):9.2f}"
                    f" {bexp(center_coeff-(row @ h_arch @ eta - prime_cell_val), L):10.2f}"
                    f" {bexp(center_coeff-matrix_center, L):10.2f}"
                    f" {bexp(center_coeff, L):8.2f}"
                )


if __name__ == "__main__":
    run()

