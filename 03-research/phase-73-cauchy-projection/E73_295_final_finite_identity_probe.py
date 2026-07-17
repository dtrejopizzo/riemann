#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import eigh, inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_195_finite_frequency_certificate_probe import cauchy_rows  # noqa: E402
from E73_287_closed_weight_formula_probe import closed_V, closed_W  # noqa: E402
from E73_290_diag_off_kernel_probe import kernel_explicit  # noqa: E402


def bexp(z, L):
    return np.log(max(float(abs(complex(z))), 1e-300)) / np.log(L)


def projector(q):
    return q.conj().T @ inv(q @ q.conj().T) @ q


def setup(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    j0 = int(np.argmin(vals))
    mu = vals[j0]
    xi = vecs[:, j0].astype(complex)
    if xi[len(xi) // 2].real < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h.astype(complex), idx.astype(int), d, L, mu, xi, vals


def adj_scaled_pair(row, vals, mu, xi):
    # Avoid forming Adj_red(E).  For a simple eigenvalue,
    # rho Adj_red / ||Adj_red|| has norm |rho xi|.
    pair = row @ xi
    nonzero = [abs(v - mu) for v in vals if abs(v - mu) > 1e-12]
    log_scale = sum(math.log(max(v, 1e-300)) for v in nonzero)
    return abs(pair), log_scale


def run():
    print("E73.295 final finite identity probe")
    print("Compares qHRxi, -q[H,P]xi, closed kernel pairing, and normalized adjugate defect.")
    print(
        " lam     L gamma row qHRB commB kernB adjB errCommB errKernB errAdjB"
    )
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        h, idx, d, L, mu, xi, vals = setup(lam, n_modes)
        eye = np.eye(len(d), dtype=complex)
        freqs = np.array(sorted(set([float(x) for x in d] + [float(-x) for x in d])), dtype=float)
        W = np.array([closed_W(o, L, lam) for o in freqs], dtype=complex)
        V = np.array([closed_V(o, L, lam) for o in freqs], dtype=complex)
        Wg = W - np.mean(W)
        Ug = (W - V / L) - np.mean(W - V / L)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            p = projector(q)
            rproj = eye - p
            eta = rproj @ xi
            comm = h @ p - p @ h
            for row_id in range(2):
                row = q[row_id]
                rho = row @ h @ rproj
                qhr = rho @ xi
                comm_pair = -(row @ comm @ xi)
                ker = kernel_explicit(row, idx, d, freqs, Wg, Ug)
                kern_pair = np.dot(eta, ker)
                adj_normed, _log_scale = adj_scaled_pair(rho, vals, mu, xi)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {row_id:3d}"
                    f" {bexp(qhr,L):6.2f} {bexp(comm_pair,L):6.2f}"
                    f" {bexp(kern_pair,L):6.2f} {bexp(adj_normed,L):5.2f}"
                    f" {bexp(qhr-comm_pair,L):9.2f}"
                    f" {bexp(qhr-kern_pair,L):9.2f}"
                    f" {bexp(abs(qhr)-adj_normed,L):8.2f}"
                )


if __name__ == "__main__":
    run()
