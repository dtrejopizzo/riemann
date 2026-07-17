#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_182_closed_series_arch_probe import exp_int, integrate_modes, packet_modes  # noqa: E402


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


def tail_direct(const, linear, L, R, R_big):
    b0 = sum(const.values())
    total = 0j
    for r in range(R, R_big):
        total += integrate_modes(const, linear, -(2 * r + 0.5), L)
        total -= b0 * exp_int(-(2 * r + 1.0), L)
    return total


def tail_grouped(const, linear, L, R, R_big):
    b0 = sum(const.values())
    total = 0j
    keys = set(const) | set(linear)
    for om in keys:
        c = const.get(om, 0j)
        ell = linear.get(om, 0j)
        for r in range(R, R_big):
            a = 2.0 * r + 0.5 - 1j * om
            s1 = (1.0 - np.exp(-a * L)) / a
            s2 = (1.0 - np.exp(-a * L) * (1.0 + a * L)) / (a * a)
            total += c * s1 + ell * s2
    for r in range(R, R_big):
        total -= b0 * (1.0 - np.exp(-(2 * r + 1.0) * L)) / (2 * r + 1.0)
    return total


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.197 signed WR tail grouped form")
    print("Checks grouped frequency tail against direct integrate_modes tail.")
    print(" lam     L gamma row    R directB groupB errB")
    for lam, n_modes in [(12, 16), (16, 20)]:
        idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(d), dtype=complex)
        gamma = GAMMAS[0]
        q = cauchy_rows(-1j * gamma, d)
        eta = (ident - projector(q)) @ xi
        row = q[0]
        const, linear = packet_modes(row, idx, d, eta, L)
        for R in [400, 1000, 2500]:
            direct = tail_direct(const, linear, L, R, 12000)
            grouped = tail_grouped(const, linear, L, R, 12000)
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f} {0:3d}"
                f" {R:5d} {bexp(direct, L):7.2f}"
                f" {bexp(grouped, L):7.2f} {bexp(grouped-direct, L):7.2f}"
            )


if __name__ == "__main__":
    run()
