#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import eigh, inv, norm
from scipy.integrate import quad

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build, primes_upto  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_182_closed_series_arch_probe import (  # noqa: E402
    arch_closed_series,
    eval_modes,
    packet_modes,
)


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
            y = k * lp
            total += lp * n ** -0.5 * eval_modes(const, linear, y)
            if n > maxn // p:
                break
            n *= p
            k += 1
    return total


def r0(y, L):
    return y * (1.0 - y / L)


def r1(y, L):
    return y * y * (1.0 - y / L)


def arch_dirichlet(func, deriv0, L):
    def wr(y):
        if y < 1e-8:
            return deriv0 / 2.0
        return np.exp(y / 2.0) * func(y) / (2.0 * np.sinh(y))

    a_re, _ = quad(lambda y: np.real(func(y) * (np.exp(y / 2.0) + np.exp(-y / 2.0))), 0, L, limit=250)
    a_im, _ = quad(lambda y: np.imag(func(y) * (np.exp(y / 2.0) + np.exp(-y / 2.0))), 0, L, limit=250)
    w_re, _ = quad(lambda y: np.real(wr(y)), 0, L, limit=250)
    w_im, _ = quad(lambda y: np.imag(wr(y)), 0, L, limit=250)
    return (a_re + 1j * a_im) - (w_re + 1j * w_im)


def prime_scalar(func, L, lam):
    total = 0j
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = math.log(p)
        n = p
        k = 1
        while n <= maxn:
            total += lp * n ** -0.5 * func(k * lp)
            if n > maxn // p:
                break
            n *= p
            k += 1
    return total


def functional_scalar(func, deriv0, L, lam):
    return arch_dirichlet(func, deriv0, L) - prime_scalar(func, L, lam)


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.195 finite-frequency certificate")
    print("Closed frequency evaluation of F[B_bal]=F[B_perp].")
    print(" lam     L gamma row modes matrixB closedB absErrB relErr cAbsB")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        h_model, prime, idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(d), dtype=complex)
        f0 = functional_scalar(lambda y: r0(y, L), 1.0, L, lam)
        f1 = functional_scalar(lambda y: r1(y, L), 0.0, L, lam)
        c = -f0 / f1
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (ident - projector(q)) @ xi
            for j in range(2):
                row = q[j]
                const, linear = packet_modes(row, idx, d, eta, L)
                arch = arch_closed_series(row, idx, d, L, eta, r_terms=2500, accel=True)
                pri = prime_modes(const, linear, L, lam)
                closed = arch - pri
                matrix = row @ ((h_model - prime) @ eta)
                err = abs(closed - matrix)
                rel = err / max(abs(matrix), 1e-300)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:3d}"
                    f" {len(const)+len(linear):5d}"
                    f" {bexp(matrix, L):7.2f} {bexp(closed, L):7.2f}"
                    f" {bexp(err, L):7.2f} {rel:7.1e}"
                    f" {bexp(c, L):6.2f}"
                )


if __name__ == "__main__":
    run()
