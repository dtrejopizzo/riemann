#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import eigh, inv, norm
from scipy.special import polygamma

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_182_closed_series_arch_probe import (  # noqa: E402
    derivative0_modes,
    exp_int,
    integrate_modes,
    packet_modes,
    second_derivative0_modes,
)


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


def odd_tail_sum(R, p):
    # sum_{r=R}^\infty (2r+1)^(-p)
    return ((-1) ** p) * float(polygamma(p - 1, R + 0.5)) / ((2**p) * math.factorial(p - 1))


def grouped_derivative_bound(const, linear, L, s):
    total = 0.0
    keys = set(const) | set(linear)
    for om in keys:
        c = const.get(om, 0j)
        ell = linear.get(om, 0j)
        lam = 0.5 + 1j * om
        total += abs(c * (lam**s) + s * ell * (lam ** (s - 1)))
        total += L * abs(ell * (lam**s))
    return math.exp(L / 2.0) * total


def wr_tail_direct(const, linear, L, R, R_big=20000):
    b0 = sum(const.values())
    total = 0j
    for r in range(R, R_big):
        total += integrate_modes(const, linear, -(2 * r + 0.5), L)
        total -= b0 * exp_int(-(2 * r + 1.0), L)
    return total


def wr_tail_accel2_direct(const, linear, L, R, R_big=20000):
    raw = wr_tail_direct(const, linear, L, R, R_big=R_big)
    b0 = sum(const.values())
    bp0 = derivative0_modes(const, linear)
    bpp0 = second_derivative0_modes(const, linear)
    c1 = bp0 + 0.5 * b0
    c2 = 0.5 * bpp0 + 0.5 * bp0 + 0.125 * b0
    # E73.182 adds these infinite-tail approximants to the partial WR sum.
    accel = c1 * odd_tail_sum(R, 2) + 2.0 * c2 * odd_tail_sum(R, 3)
    return raw - accel


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.196 WR tail certified finite-frequency")
    print("Compares accelerated order-2 WR tail with grouped derivative bound.")
    print(" lam     L gamma row    R tailB boundB ratioB M3B")
    for lam, n_modes in [(12, 16), (16, 20)]:
        idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(d), dtype=complex)
        for gamma in GAMMAS[:1]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (ident - projector(q)) @ xi
            row = q[0]
            const, linear = packet_modes(row, idx, d, eta, L)
            M3 = grouped_derivative_bound(const, linear, L, 3)
            for R in [400, 1000, 2500]:
                tail = wr_tail_accel2_direct(const, linear, L, R)
                bound = M3 * odd_tail_sum(R, 4)
                ratio = bound / max(abs(tail), 1e-300)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {0:3d}"
                    f" {R:5d}"
                    f" {bexp(tail, L):7.2f} {bexp(bound, L):7.2f}"
                    f" {bexp(ratio, L):7.2f} {bexp(M3, L):7.2f}"
                )


if __name__ == "__main__":
    run()
