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


def ramp(y, L):
    return y * (1.0 - y / L)


def packet(row, idx, d, L, eta, y):
    return row @ (q_matrix_fast(idx, d, L, y) @ eta)


def arch_dirichlet_scalar(func, deriv0, L):
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


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.192 ramp-normalized packet")
    print("Splits B=Bp0*r0+Brem and measures ramp vs double-zero remainder.")
    print(" lam     L gamma row totalB rampB remB checkB rem0B remp0B remLB")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        h_model, prime, idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(d), dtype=complex)
        r_arch = arch_dirichlet_scalar(lambda y: ramp(y, L), 1.0, L)
        r_prime = prime_scalar(lambda y: ramp(y, L), L, lam)
        r_match = r_arch - r_prime
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (ident - projector(q)) @ xi
            for j in range(2):
                row = q[j]
                h = min(1e-6, L * 1e-7)
                b0 = packet(row, idx, d, L, eta, 0.0)
                bp0 = (packet(row, idx, d, L, eta, h) - b0) / h
                total = row @ ((h_model - prime) @ eta)
                ramp_part = bp0 * r_match
                rem_part = total - ramp_part

                def brem(y):
                    return packet(row, idx, d, L, eta, y) - bp0 * ramp(y, L)

                rem0 = brem(0.0)
                remp0 = (brem(h) - brem(0.0)) / h
                remL = brem(L)
                check = rem_part + ramp_part - total
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:3d}"
                    f" {bexp(total, L):7.2f} {bexp(ramp_part, L):6.2f}"
                    f" {bexp(rem_part, L):6.2f} {bexp(check, L):7.2f}"
                    f" {bexp(rem0, L):6.2f} {bexp(remp0, L):7.2f}"
                    f" {bexp(remL, L):6.2f}"
                )


if __name__ == "__main__":
    run()
