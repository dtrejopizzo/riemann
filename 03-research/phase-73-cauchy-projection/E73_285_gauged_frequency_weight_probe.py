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
from E73_195_finite_frequency_certificate_probe import (  # noqa: E402
    cauchy_rows,
    functional_scalar,
    prime_modes,
)
from E73_182_closed_series_arch_probe import arch_closed_series  # noqa: E402


def bexp(z, L):
    return np.log(max(float(abs(complex(z))), 1e-300)) / np.log(L)


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi.astype(complex)


def projector(q):
    return q.conj().T @ inv(q @ q.conj().T) @ q


def coeff_arrays(const, linear, freqs):
    c = np.array([const.get(float(om), 0j) for om in freqs], dtype=complex)
    l = np.array([linear.get(float(om), 0j) for om in freqs], dtype=complex)
    return c, l


def weights_for_freqs(freqs, L, lam):
    w = []
    v = []
    for om in freqs:
        om = float(om)
        w.append(functional_scalar(lambda y, o=om: np.exp(1j * o * y), 1j * om, L, lam))
        v.append(functional_scalar(lambda y, o=om: y * np.exp(1j * o * y), 1.0 + 0j, L, lam))
    return np.array(w, dtype=complex), np.array(v, dtype=complex)


def roughness(arr):
    if len(arr) < 2:
        return 0.0
    return norm(np.diff(arr)) / max(norm(arr), 1e-300)


def run():
    print("E73.285 gauged frequency weight probe")
    print("Builds exact W,V weights by applying the Gamma-prime functional to frequency basis modes.")
    print("Gauges remove only constants, justified by endpoint moments sum c=sum l=0.")
    print(
        " lam     L gamma row nfreq centerB directErrB WgB VgB Wrough Vrough "
        "cB lB pairW_B pairV_B cancel"
    )
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        idx, d, L, xi = setup(lam, n_modes)
        freqs = np.array(sorted(set([float(x) for x in d] + [float(-x) for x in d])), dtype=float)
        W, V = weights_for_freqs(freqs, L, lam)
        Wg = W - np.mean(W)
        Vg = V - np.mean(V)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (np.eye(len(d), dtype=complex) - projector(q)) @ xi
            for row_id in range(2):
                row = q[row_id]
                const, linear = packet_modes(row, idx, d, eta, L)
                c, l = coeff_arrays(const, linear, freqs)
                center_weight = np.dot(c, W) + np.dot(l, V)
                center_gauge = np.dot(c, Wg) + np.dot(l, Vg)
                arch = arch_closed_series(row, idx, d, L, eta, r_terms=2500, accel=True)
                pri = prime_modes(const, linear, L, lam)
                center_direct = arch - pri
                pW = np.dot(c, Wg)
                pV = np.dot(l, Vg)
                cancel = abs(pW + pV) / max(abs(pW) + abs(pV), 1e-300)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {row_id:3d}"
                    f" {len(freqs):5d} {bexp(center_direct,L):7.2f}"
                    f" {bexp(center_weight-center_direct,L):10.2f}"
                    f" {bexp(norm(Wg),L):5.2f} {bexp(norm(Vg),L):5.2f}"
                    f" {roughness(Wg):6.2e} {roughness(Vg):6.2e}"
                    f" {bexp(norm(c),L):5.2f} {bexp(norm(l),L):5.2f}"
                    f" {bexp(pW,L):8.2f} {bexp(pV,L):8.2f}"
                    f" {cancel:8.1e}"
                )


if __name__ == "__main__":
    run()
