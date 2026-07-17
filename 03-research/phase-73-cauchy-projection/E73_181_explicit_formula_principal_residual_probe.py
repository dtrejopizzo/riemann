#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import eigh, lstsq, norm
from scipy.integrate import quad

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import GAMMA, LOG4PI, build, primes_upto  # noqa: E402
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
    return h_actual, h_model, prime, vals[0], idx.astype(int), d, L, xi


def cauchy_rows(w, d):
    return np.vstack([1.0 / (w + 1j * d), 1.0 / (-w + 1j * d)])


def plane_action(op, plane):
    coeffs = []
    for j in range(2):
        row = plane[j] @ op
        coeff, *_ = lstsq(plane.T, row, rcond=None)
        coeffs.append(coeff)
    return np.array(coeffs)


def packet(row, idx, d, L, xi, y):
    return row @ (q_matrix_fast(idx, d, L, y) @ xi)


def packet_derivative0(row, idx, d, L, xi):
    h = min(1e-6, L * 1e-7)
    return (packet(row, idx, d, L, xi, h) - packet(row, idx, d, L, xi, 0.0)) / h


def arch_functional(row, idx, d, L, xi):
    b0 = packet(row, idx, d, L, xi, 0.0)
    db0 = packet_derivative0(row, idx, d, L, xi)

    def b(y):
        return packet(row, idx, d, L, xi, y)

    def wri(y):
        if y < 1e-8:
            return (db0 + b0 / 2.0) / 2.0
        return (np.exp(y / 2.0) * b(y) - b0) / (2.0 * np.sinh(y))

    w02_re, _ = quad(lambda y: np.real(b(y) * (np.exp(y / 2.0) + np.exp(-y / 2.0))), 0, L, limit=250)
    w02_im, _ = quad(lambda y: np.imag(b(y) * (np.exp(y / 2.0) + np.exp(-y / 2.0))), 0, L, limit=250)
    wra_re, _ = quad(lambda y: np.real(wri(y)), 0, L, limit=250)
    wra_im, _ = quad(lambda y: np.imag(wri(y)), 0, L, limit=250)
    w02 = w02_re + 1j * w02_im
    wra = wra_re + 1j * wra_im
    wrb = b0 * 0.5 * np.log(np.tanh(L / 2.0))
    wr = 0.5 * (LOG4PI + GAMMA) * b0 + wra + wrb
    return w02 - wr


def prime_functional(row, idx, d, L, xi, lam):
    total = 0j
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = math.log(p)
        n = p
        k = 1
        while n <= maxn:
            total += lp * n ** -0.5 * packet(row, idx, d, L, xi, k * lp)
            if n > maxn // p:
                break
            n *= p
            k += 1
    return total


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.181 explicit-formula principal residual probe")
    print("Verifies A_L[B_q]-P_L[B_q] minus Cauchy principal part equals SCRCE signed scalar.")
    print(" lam     L gamma row archErr primeErr signedB quadB errB principalB")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        h, h_model, prime, _mu, idx, d, L, xi = setup(lam, n_modes)
        for gamma in GAMMAS[:2]:
            w = -1j * gamma
            plane = cauchy_rows(w, d)
            hvec = plane @ xi
            a_mod = plane_action(h_model, plane)
            a_pri = plane_action(prime, plane)
            for j in range(2):
                arch_quad = arch_functional(plane[j], idx, d, L, xi)
                prime_quad = prime_functional(plane[j], idx, d, L, xi, lam)
                arch_mat = plane[j] @ (h_model @ xi)
                prime_mat = plane[j] @ (prime @ xi)
                principal = (a_mod[j] - a_pri[j]) @ hvec
                signed_mat = (arch_mat - prime_mat) - principal
                signed_quad = (arch_quad - prime_quad) - principal
                arch_err = abs(arch_quad - arch_mat) / max(abs(arch_mat), 1e-300)
                prime_err = abs(prime_quad - prime_mat) / max(abs(prime_mat), 1e-300)
                err = abs(signed_quad - signed_mat)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:3d}"
                    f" {arch_err:7.1e} {prime_err:8.1e}"
                    f" {bexp(signed_mat, L):7.2f} {bexp(signed_quad, L):6.2f}"
                    f" {bexp(err, L):6.2f} {bexp(principal, L):10.2f}"
                )


if __name__ == "__main__":
    run()
