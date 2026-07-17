#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_182_closed_series_arch_probe import packet_modes  # noqa: E402
from E73_201_mp_finite_assembly_probe import mp_arch_closed_digamma, mp_prime_modes  # noqa: E402


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h_actual, vals, idx.astype(int), d, L, xi


def cauchy_rows(w, d):
    return np.vstack([1.0 / (w + 1j * d), 1.0 / (-w + 1j * d)])


def projector(q):
    return q.conj().T @ inv(q @ q.conj().T) @ q


def certificate(row, idx, d, eta, L, lam):
    const, linear = packet_modes(row, idx, d, eta, L)
    return mp_arch_closed_digamma(const, linear, L, 80) - mp_prime_modes(const, linear, L, lam)


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.203 interval budget probe")
    print("Eigenline gap and functional sensitivity for the E73.202 certificate.")
    print(" lam     L gamma row centerB gapB eigResB eigRadB sensB etaRadB totalRadB ratio")
    for lam, n_modes in [(12, 16), (16, 20)]:
        h, vals, idx, d, L, xi = setup(lam, n_modes)
        mu = vals[0]
        gap = vals[1] - vals[0]
        eig_res = norm(h @ xi - mu * xi)
        eig_rad = 2.0 * eig_res / max(gap, 1e-300)
        ident = np.eye(len(d), dtype=complex)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            p = projector(q)
            eta = (ident - p) @ xi
            proj_norm = norm(ident - p, 2)
            eta_rad = proj_norm * eig_rad
            for row_id in range(2):
                row = q[row_id]
                center = certificate(row, idx, d, eta, L, lam)
                # By E73.199, eta -> C_a(eta) is the same linear functional as
                # eta -> row H eta.  Use the matrix row for this sensitivity
                # budget; the special-function certificate is only needed for
                # the cancellation center.
                sens = norm(row @ h)
                total_rad = sens * eta_rad
                ratio = total_rad / max(abs(complex(center)), 1e-300)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {row_id:3d}"
                    f" {bexp(center, L):7.2f} {bexp(gap, L):5.2f}"
                    f" {bexp(eig_res, L):8.2f} {bexp(eig_rad, L):8.2f}"
                    f" {bexp(sens, L):7.2f} {bexp(eta_rad, L):8.2f}"
                    f" {bexp(total_rad, L):9.2f} {ratio:8.1e}"
                )


if __name__ == "__main__":
    run()
