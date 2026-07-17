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
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi


def cauchy_rows(w, d):
    return np.vstack([1.0 / (w + 1j * d), 1.0 / (-w + 1j * d)])


def orthogonal_projector_from_rows(q):
    gram = q @ q.conj().T
    return q.conj().T @ inv(gram) @ q


def packet_matrix(row, idx, d, L, eta, y):
    return row @ (q_matrix_fast(idx, d, L, y) @ eta)


def fourier_sum(coeff, d, r, sign=1.0):
    return np.sum(coeff * np.exp(1j * sign * d * r))


def packet_conv(row, d, L, eta, y):
    def integrand(t):
        a_pos = fourier_sum(row, d, t + y, sign=1.0)
        a_neg = fourier_sum(row, d, t + y, sign=-1.0)
        e_neg = fourier_sum(eta, d, t, sign=-1.0)
        e_pos = fourier_sum(eta, d, t, sign=1.0)
        return (a_pos * e_neg + a_neg * e_pos) / L

    re, _ = quad(lambda t: np.real(integrand(t)), 0.0, L - y, limit=250)
    im, _ = quad(lambda t: np.imag(integrand(t)), 0.0, L - y, limit=250)
    return re + 1j * im


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.190 transverse convolution form")
    print("Checks convolution representation and A_a'=D-aA_a.")
    print(" lam     L gamma row convErr qetaB Bp0B rankBp0B derivErr")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(d), dtype=complex)
        sample_y = [0.0, 0.17 * L, 0.41 * L, 0.73 * L]
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            proj = orthogonal_projector_from_rows(q)
            eta = (ident - proj) @ xi
            for j, a in enumerate([-1j * gamma, 1j * gamma]):
                row = q[j]
                diffs = []
                scale = 0.0
                for y in sample_y:
                    mat = packet_matrix(row, idx, d, L, eta, y)
                    cv = packet_conv(row, d, L, eta, y)
                    diffs.append(abs(mat - cv))
                    scale = max(scale, abs(mat), abs(cv))

                h = min(1e-6, L * 1e-7)
                bp0 = (packet_matrix(row, idx, d, L, eta, h) - packet_matrix(row, idx, d, L, eta, 0.0)) / h
                rank_bp0 = -(2.0 / L) * np.sum(row) * np.sum(eta)

                r = 0.37 * L
                A = fourier_sum(row, d, r, sign=1.0)
                D = fourier_sum(np.ones_like(row), d, r, sign=1.0)
                Aprime = fourier_sum(1j * d * row, d, r, sign=1.0)
                deriv_rhs = D - a * A
                deriv_err = abs(Aprime - deriv_rhs) / max(abs(Aprime), 1e-300)

                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:3d}"
                    f" {max(diffs) / max(scale, 1e-300):7.1e}"
                    f" {bexp(row @ eta, L):6.2f}"
                    f" {bexp(bp0, L):6.2f}"
                    f" {bexp(rank_bp0, L):9.2f}"
                    f" {deriv_err:8.1e}"
                )


if __name__ == "__main__":
    run()
