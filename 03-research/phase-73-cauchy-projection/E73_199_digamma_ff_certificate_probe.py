#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import eigh, inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import GAMMA, LOG4PI, build, primes_upto  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_182_closed_series_arch_probe import eval_modes, exp_int, integrate_modes, packet_modes  # noqa: E402
from E73_198_digamma_wr_tail_probe import signed_tail_digamma  # noqa: E402


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


def prime_modes(const, linear, L, lam):
    total = 0j
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = math.log(p)
        n = p
        k = 1
        while n <= maxn:
            total += lp * n ** -0.5 * eval_modes(const, linear, k * lp)
            if n > maxn // p:
                break
            n *= p
            k += 1
    return total


def arch_closed_digamma(row, idx, d, L, eta, r_terms):
    const, linear = packet_modes(row, idx, d, eta, L)
    b0 = eval_modes(const, linear, 0.0)
    w02 = integrate_modes(const, linear, 0.5, L) + integrate_modes(const, linear, -0.5, L)
    wra = 0j
    for r in range(r_terms):
        wra += integrate_modes(const, linear, -(2 * r + 0.5), L)
        wra -= b0 * exp_int(-(2 * r + 1.0), L)
    wra += signed_tail_digamma(const, linear, L, r_terms)
    wrb = b0 * 0.5 * np.log(np.tanh(L / 2.0))
    wr = 0.5 * (LOG4PI + GAMMA) * b0 + wra + wrb
    return w02 - wr


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.199 digamma finite-frequency certificate")
    print("Finite WR head plus closed signed digamma tail, compared to matrix residual.")
    print(" lam     L gamma row    R matrixB certB absErrB relErr")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        h_model, prime, idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(d), dtype=complex)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (ident - projector(q)) @ xi
            for row_id in range(2):
                row = q[row_id]
                const, linear = packet_modes(row, idx, d, eta, L)
                pri = prime_modes(const, linear, L, lam)
                matrix = row @ ((h_model - prime) @ eta)
                for r_terms in [60, 120, 240]:
                    arch = arch_closed_digamma(row, idx, d, L, eta, r_terms)
                    cert = arch - pri
                    err = cert - matrix
                    rel = abs(err) / max(abs(matrix), 1e-300)
                    print(
                        f"{lam:4d} {L:7.3f} {gamma:7.2f} {row_id:3d}"
                        f" {r_terms:4d} {bexp(matrix, L):7.2f}"
                        f" {bexp(cert, L):7.2f} {bexp(err, L):7.2f}"
                        f" {rel:7.1e}"
                    )


if __name__ == "__main__":
    run()
