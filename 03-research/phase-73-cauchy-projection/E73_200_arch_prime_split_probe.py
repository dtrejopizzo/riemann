#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_182_closed_series_arch_probe import arch_closed_series, packet_modes  # noqa: E402
from E73_195_finite_frequency_certificate_probe import prime_modes  # noqa: E402
from E73_199_digamma_ff_certificate_probe import arch_closed_digamma  # noqa: E402


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    h_model, _, _ = build(lam, n_modes, include_arith=False)
    prime = h_model - h_actual
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h_model, prime, idx.astype(int), d, L, xi


def cauchy_rows(w, d):
    return np.vstack([1.0 / (w + 1j * d), 1.0 / (-w + 1j * d)])


def projector(q):
    return q.conj().T @ inv(q @ q.conj().T) @ q


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.200 arch/prime split diagnostic")
    print("Compares each certificate side before final cancellation.")
    print(" lam     L gamma row archM archD archE primeM primeF primeE finalE")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        h_model, prime, idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(d), dtype=complex)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (ident - projector(q)) @ xi
            for row_id in range(2):
                row = q[row_id]
                const, linear = packet_modes(row, idx, d, eta, L)
                arch_matrix = row @ (h_model @ eta)
                arch_digamma = arch_closed_digamma(row, idx, d, L, eta, 80)
                arch_accel = arch_closed_series(row, idx, d, L, eta, r_terms=2500, accel=True)
                prime_matrix = row @ (prime @ eta)
                prime_freq = prime_modes(const, linear, L, lam)
                final_matrix = row @ ((h_model - prime) @ eta)
                final_cert = arch_digamma - prime_freq
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {row_id:3d}"
                    f" {bexp(arch_matrix, L):6.2f} {bexp(arch_digamma, L):6.2f}"
                    f" {bexp(arch_digamma-arch_matrix, L):6.2f}"
                    f" {bexp(prime_matrix, L):7.2f} {bexp(prime_freq, L):7.2f}"
                    f" {bexp(prime_freq-prime_matrix, L):7.2f}"
                    f" {bexp(final_cert-final_matrix, L):7.2f}"
                    f"  accelE={bexp(arch_accel-arch_matrix, L):.2f}"
                )


if __name__ == "__main__":
    run()
