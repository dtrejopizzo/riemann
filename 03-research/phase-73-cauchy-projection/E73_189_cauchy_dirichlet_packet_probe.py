#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, inv, norm
from scipy.integrate import quad

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_380_actual_packet_wwr_probe import q_matrix_fast  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


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


def orthogonal_projector_from_rows(q):
    gram = q @ q.conj().T
    return q.conj().T @ inv(gram) @ q


def packet(row, idx, d, L, eta, y):
    return row @ (q_matrix_fast(idx, d, L, y) @ eta)


def arch_dirichlet(row, idx, d, L, eta):
    def b(y):
        return packet(row, idx, d, L, eta, y)

    h = min(1e-6, L * 1e-7)
    db0 = (b(h) - b(0.0)) / h

    def wr(y):
        if y < 1e-8:
            return db0 / 2.0
        return np.exp(y / 2.0) * b(y) / (2.0 * np.sinh(y))

    w02_re, _ = quad(lambda y: np.real(b(y) * (np.exp(y / 2.0) + np.exp(-y / 2.0))), 0, L, limit=250)
    w02_im, _ = quad(lambda y: np.imag(b(y) * (np.exp(y / 2.0) + np.exp(-y / 2.0))), 0, L, limit=250)
    wr_re, _ = quad(lambda y: np.real(wr(y)), 0, L, limit=250)
    wr_im, _ = quad(lambda y: np.imag(wr(y)), 0, L, limit=250)
    return (w02_re + 1j * w02_im) - (wr_re + 1j * wr_im)


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.189 Cauchy-Dirichlet packet")
    print("Checks B_perp(0)=B_perp(L)=0 and the simplified archimedean cell.")
    print(" lam     L gamma row qetaB B0B BLB archB matB errB primeB signedB")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        h_model, prime, idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(d), dtype=complex)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            proj = orthogonal_projector_from_rows(q)
            eta = (ident - proj) @ xi
            for j in range(2):
                b0 = packet(q[j], idx, d, L, eta, 0.0)
                bL = packet(q[j], idx, d, L, eta, L)
                arch_q = arch_dirichlet(q[j], idx, d, L, eta)
                arch_m = q[j] @ (h_model @ eta)
                prime_m = q[j] @ (prime @ eta)
                signed = arch_m - prime_m
                err = arch_q - arch_m
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:3d}"
                    f" {bexp(q[j] @ eta, L):6.2f}"
                    f" {bexp(b0, L):6.2f} {bexp(bL, L):6.2f}"
                    f" {bexp(arch_q, L):7.2f} {bexp(arch_m, L):6.2f}"
                    f" {bexp(err, L):6.2f} {bexp(prime_m, L):7.2f}"
                    f" {bexp(signed, L):8.2f}"
                )


if __name__ == "__main__":
    run()
