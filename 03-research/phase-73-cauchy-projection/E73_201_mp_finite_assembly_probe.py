#!/usr/bin/env python3
import math
import sys

import mpmath as mp
import numpy as np
from numpy.linalg import eigh, inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import GAMMA, LOG4PI, build, primes_upto  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_182_closed_series_arch_probe import packet_modes  # noqa: E402
from E73_199_digamma_ff_certificate_probe import arch_closed_digamma, prime_modes  # noqa: E402


mp.mp.dps = 100


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


def cpx(z):
    return mp.mpc(float(np.real(z)), float(np.imag(z)))


def mp_exp_int(alpha, L):
    if abs(alpha) < mp.mpf("1e-80"):
        return mp.mpf(L)
    return mp.expm1(alpha * L) / alpha


def mp_y_exp_int(alpha, L):
    if abs(alpha) < mp.mpf("1e-80"):
        return mp.mpf("0.5") * L * L
    return (mp.e ** (alpha * L) * (alpha * L - 1) + 1) / (alpha * alpha)


def mp_integrate_modes(const, linear, alpha, L):
    total = mp.mpc(0)
    Lmp = mp.mpf(L)
    amp = mp.mpc(alpha)
    for om, coeff in const.items():
        total += cpx(coeff) * mp_exp_int(amp + 1j * mp.mpf(float(om)), Lmp)
    for om, coeff in linear.items():
        total += cpx(coeff) * mp_y_exp_int(amp + 1j * mp.mpf(float(om)), Lmp)
    return total


def mp_eval_modes(const, linear, y):
    total = mp.mpc(0)
    ymp = mp.mpf(y)
    for om, coeff in const.items():
        total += cpx(coeff) * mp.e ** (1j * mp.mpf(float(om)) * ymp)
    for om, coeff in linear.items():
        total += cpx(coeff) * ymp * mp.e ** (1j * mp.mpf(float(om)) * ymp)
    return total


def mp_signed_tail_digamma(const, linear, L, R, exp_terms=80):
    total = mp.mpc(0)
    keys = set(const) | set(linear)
    Rmp = mp.mpf(R)
    Lmp = mp.mpf(L)
    for om0 in keys:
        om = mp.mpf(float(om0))
        coeff = cpx(const.get(om0, 0j))
        ell = cpx(linear.get(om0, 0j))
        z = Rmp + mp.mpf("0.25") - 0.5j * om
        d1 = mp.mpf("0.5") * (mp.digamma(Rmp + mp.mpf("0.5")) - mp.digamma(z))
        d2 = mp.mpf("0.25") * mp.polygamma(1, z)
        e1 = mp.mpc(0)
        e2 = mp.mpc(0)
        for r in range(R, R + exp_terms):
            a = mp.mpf(2 * r) + mp.mpf("0.5") - 1j * om
            e = mp.e ** (-a * Lmp)
            e1 += e / a
            e2 += e * (1 + a * Lmp) / (a * a)
        total += coeff * (d1 - e1)
        total += ell * (d2 - e2)
    b0 = sum(cpx(v) for v in const.values())
    s0e = mp.mpc(0)
    for r in range(R, R + exp_terms):
        b = mp.mpf(2 * r + 1)
        s0e += mp.e ** (-b * Lmp) / b
    total += b0 * s0e
    return total


def mp_arch_closed_digamma(const, linear, L, R):
    Lmp = mp.mpf(L)
    b0 = mp_eval_modes(const, linear, 0)
    w02 = mp_integrate_modes(const, linear, mp.mpf("0.5"), L) + mp_integrate_modes(
        const, linear, mp.mpf("-0.5"), L
    )
    wra = mp.mpc(0)
    for r in range(R):
        wra += mp_integrate_modes(const, linear, -(2 * r + mp.mpf("0.5")), L)
        wra -= b0 * mp_exp_int(-(2 * r + mp.mpf("1.0")), Lmp)
    wra += mp_signed_tail_digamma(const, linear, L, R)
    wrb = b0 * mp.mpf("0.5") * mp.log(mp.tanh(Lmp / 2))
    wr = mp.mpf("0.5") * (mp.mpf(LOG4PI) + mp.mpf(GAMMA)) * b0 + wra + wrb
    return w02 - wr


def mp_prime_modes(const, linear, L, lam):
    total = mp.mpc(0)
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = math.log(p)
        n = p
        k = 1
        while n <= maxn:
            total += mp.mpf(lp) * mp.power(n, mp.mpf("-0.5")) * mp_eval_modes(const, linear, k * lp)
            if n > maxn // p:
                break
            n *= p
            k += 1
    return total


def bexp(z, L):
    return np.log(max(float(abs(complex(z))), 1e-300)) / np.log(L)


def run():
    print("E73.201 multiprecision finite assembly")
    print("Compares double and mp assembly of the same finite-frequency certificate.")
    print(" lam     L gamma row doubleB mpB dbl-mpB matrix-mpB")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        h_model, prime, idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(d), dtype=complex)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (ident - projector(q)) @ xi
            for row_id in range(2):
                row = q[row_id]
                const, linear = packet_modes(row, idx, d, eta, L)
                double_cert = arch_closed_digamma(row, idx, d, L, eta, 80) - prime_modes(
                    const, linear, L, lam
                )
                mp_cert = mp_arch_closed_digamma(const, linear, L, 80) - mp_prime_modes(
                    const, linear, L, lam
                )
                matrix = row @ ((h_model - prime) @ eta)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {row_id:3d}"
                    f" {bexp(double_cert, L):7.2f} {bexp(mp_cert, L):7.2f}"
                    f" {bexp(double_cert-complex(mp_cert), L):8.2f}"
                    f" {bexp(matrix-complex(mp_cert), L):10.2f}"
                )


if __name__ == "__main__":
    run()
