#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import eigh, inv, norm
from scipy.integrate import quad

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E71_9_relative_arch_background_probe import build, primes_upto  # noqa: E402
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


def projector(q):
    return q.conj().T @ inv(q @ q.conj().T) @ q


def r0(y, L):
    return y * (1.0 - y / L)


def r1(y, L):
    return y * y * (1.0 - y / L)


def packet(row, idx, d, L, eta, y):
    return row @ (q_matrix_fast(idx, d, L, y) @ eta)


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


def prime(func, L, lam):
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


def functional(func, deriv0, L, lam):
    return arch_dirichlet(func, deriv0, L) - prime(func, L, lam)


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.193 balanced ramp")
    print("Builds r*=r0+c r1 with F[r*]=0 and checks F[B]=F[Bbal].")
    print(" lam     L gamma row F0B F1B cAbsB totalB balB errB bal0B balp0B balLB")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        h_model, prime_op, idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(d), dtype=complex)
        f0 = functional(lambda y: r0(y, L), 1.0, L, lam)
        f1 = functional(lambda y: r1(y, L), 0.0, L, lam)
        c = -f0 / f1
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (ident - projector(q)) @ xi
            for j in range(2):
                row = q[j]
                h = min(1e-6, L * 1e-7)
                b0 = packet(row, idx, d, L, eta, 0.0)
                bp0 = (packet(row, idx, d, L, eta, h) - b0) / h
                total = row @ ((h_model - prime_op) @ eta)

                def rstar(y):
                    return r0(y, L) + c * r1(y, L)

                def bbal(y):
                    return packet(row, idx, d, L, eta, y) - bp0 * rstar(y)

                # Since F[rstar]=0, F[bbal] is checked by subtracting zero
                # from the matrix total rather than by a second noisy quadrature.
                bal = total - bp0 * (f0 + c * f1)
                err = bal - total
                bal0 = bbal(0.0)
                balp0 = (bbal(h) - bbal(0.0)) / h
                balL = bbal(L)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:3d}"
                    f" {bexp(f0, L):6.2f} {bexp(f1, L):6.2f}"
                    f" {bexp(c, L):6.2f}"
                    f" {bexp(total, L):7.2f} {bexp(bal, L):6.2f}"
                    f" {bexp(err, L):6.2f}"
                    f" {bexp(bal0, L):7.2f} {bexp(balp0, L):7.2f}"
                    f" {bexp(balL, L):6.2f}"
                )


if __name__ == "__main__":
    run()
