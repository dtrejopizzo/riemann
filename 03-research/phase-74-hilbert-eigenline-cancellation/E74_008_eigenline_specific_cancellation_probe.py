#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, inv, norm, qr

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_182_closed_series_arch_probe import arch_closed_series, packet_modes  # noqa: E402
from E73_195_finite_frequency_certificate_probe import prime_modes  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    h_model, _, _ = build(lam, n_modes, include_arith=False)
    prime = h_model - h_actual
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0].astype(complex)
    if xi[len(xi) // 2].real < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h_model.astype(complex), prime.astype(complex), idx.astype(int), d, L, xi


def ker_sample(Q, target_norm, seed):
    rng = np.random.default_rng(seed)
    z = rng.normal(size=Q.shape[1]) + 1j * rng.normal(size=Q.shape[1])
    P = projector(Q)
    v = (np.eye(Q.shape[1], dtype=complex) - P) @ z
    return target_norm * v / norm(v)


def center(row, idx, d, L, eta, lam):
    const, linear = packet_modes(row, idx, d, eta, L)
    arch = arch_closed_series(row, idx, d, L, eta, r_terms=2500, accel=True)
    prime = prime_modes(const, linear, L, lam)
    return arch, prime, arch - prime


def bexp(z, L):
    return np.log(max(float(abs(complex(z))), 1e-300)) / np.log(L)


def run():
    print("E74.8 eigenline-specific Gamma-prime cancellation")
    print("Compare eta=(I-P)xi with random vectors in ker Q of the same norm.")
    print(" lam     L gamma row etaFinalB randMedB randMinB randMaxB etaArchB etaPrimeB sepB")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        h_model, prime, idx, d, L, xi = setup(lam, n_modes)
        I = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            eta = (I - projector(Q)) @ xi
            eta_norm = norm(eta)
            for row_id in range(2):
                row = Q[row_id]
                arch, pri, fin = center(row, idx, d, L, eta, lam)
                vals = []
                for s in range(12):
                    v = ker_sample(Q, eta_norm, 10000 + 101 * lam + 17 * row_id + s)
                    _a, _p, f = center(row, idx, d, L, v, lam)
                    vals.append(abs(f))
                vals = np.array(vals)
                sep = abs(fin) / max(abs(arch) + abs(pri), 1e-300)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {row_id:3d}"
                    f" {bexp(fin,L):9.2f}"
                    f" {bexp(np.median(vals),L):8.2f}"
                    f" {bexp(np.min(vals),L):8.2f}"
                    f" {bexp(np.max(vals),L):8.2f}"
                    f" {bexp(arch,L):8.2f}"
                    f" {bexp(pri,L):9.2f}"
                    f" {bexp(sep,L):6.2f}"
                )


if __name__ == "__main__":
    run()
