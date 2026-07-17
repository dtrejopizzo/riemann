#!/usr/bin/env python3
import sys

import mpmath as mp
import numpy as np
from numpy.linalg import eigh, inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_182_closed_series_arch_probe import packet_modes  # noqa: E402
from E73_197_signed_wr_tail_probe import tail_grouped  # noqa: E402


mp.mp.dps = 80


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


def projector(q):
    return q.conj().T @ inv(q @ q.conj().T) @ q


def cpx(z):
    return mp.mpc(float(np.real(z)), float(np.imag(z)))


def signed_tail_digamma(const, linear, L, R, exp_terms=80):
    total = mp.mpc(0)
    keys = set(const) | set(linear)
    Rmp = mp.mpf(R)
    Lmp = mp.mpf(L)
    for om0 in keys:
        om = mp.mpf(float(om0))
        c = cpx(const.get(om0, 0j))
        ell = cpx(linear.get(om0, 0j))
        z = Rmp + mp.mpf("0.25") - 0.5j * om
        d1 = mp.mpf("0.5") * (mp.digamma(Rmp + mp.mpf("0.5")) - mp.digamma(z))
        d2 = mp.mpf("0.25") * mp.polygamma(1, z)
        # Exponential corrections are tiny; sum a small geometric head
        # explicitly and ignore the rigorously negligible remainder for this probe.
        e1 = mp.mpc(0)
        e2 = mp.mpc(0)
        for r in range(R, R + exp_terms):
            a = mp.mpf(2 * r) + mp.mpf("0.5") - 1j * om
            e = mp.e ** (-a * Lmp)
            e1 += e / a
            e2 += e * (1 + a * Lmp) / (a * a)
        total += c * (d1 - e1)
        total += ell * (d2 - e2)
    # Add S0 exponential correction weighted by B(0)=sum c_omega.
    b0 = sum(cpx(v) for v in const.values())
    s0e = mp.mpc(0)
    for r in range(R, R + exp_terms):
        b = mp.mpf(2 * r + 1)
        s0e += (mp.e ** (-b * Lmp)) / b
    total += b0 * s0e
    return complex(total)


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.198 digamma WR tail")
    print("Compares direct grouped tail with digamma/polygamma signed form.")
    print(" lam     L gamma row    R groupB digamB errB")
    for lam, n_modes in [(12, 16), (16, 20)]:
        idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(d), dtype=complex)
        gamma = GAMMAS[0]
        q = cauchy_rows(-1j * gamma, d)
        eta = (ident - projector(q)) @ xi
        row = q[0]
        const, linear = packet_modes(row, idx, d, eta, L)
        for R in [400, 1000, 2500]:
            grouped = tail_grouped(const, linear, L, R, 30000)
            digam = signed_tail_digamma(const, linear, L, R)
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f} {0:3d}"
                f" {R:5d} {bexp(grouped, L):7.2f}"
                f" {bexp(digam, L):7.2f} {bexp(digam-grouped, L):7.2f}"
            )


if __name__ == "__main__":
    run()
