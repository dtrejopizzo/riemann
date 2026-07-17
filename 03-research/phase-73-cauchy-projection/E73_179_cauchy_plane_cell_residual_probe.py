#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, lstsq, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402


def setup(lam, n_modes, include_arith):
    h, idx, L = build(lam, n_modes, include_arith=include_arith)
    vals, vecs = eigh(h)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h, vals[0], d, L, xi


def cauchy_rows(w, d):
    return np.vstack([1.0 / (w + 1j * d), 1.0 / (-w + 1j * d)])


def cauchy_plane_data(h, mu, d, xi, gamma):
    w = -1j * gamma
    plane = cauchy_rows(w, d)
    a = np.zeros((2, 2), dtype=complex)
    rho = np.zeros_like(plane)
    for j in range(2):
        row_h = plane[j] @ h
        coeff, *_ = lstsq(plane.T, row_h, rcond=None)
        a[j] = coeff
        rho[j] = row_h - coeff @ plane
    hvec = plane @ xi
    rvec = rho @ xi
    lhs = (mu * np.eye(2, dtype=complex) - a) @ hvec
    return hvec, rvec, a, rho, lhs


def run():
    print("E73.179 Cauchy-plane cell residual probe")
    print("Verifies (mu I-A)h=rho xi and compares zeta/arch residual channels.")
    print("errB is log_L absolute identity error; relative error is ill-conditioned in tiny zeta rows.")
    print(" lam     L gamma   hB_z   rB_z  invB_z  errB_z   hB_a   rB_a  invB_a  errB_a")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        hz, muz, d, L, xz = setup(lam, n_modes, include_arith=True)
        ha, mua, da, _, xa = setup(lam, n_modes, include_arith=False)
        for gamma in GAMMAS[:3]:
            hvec_z, rvec_z, a_z, _rho_z, lhs_z = cauchy_plane_data(hz, muz, d, xz, gamma)
            hvec_a, rvec_a, a_a, _rho_a, lhs_a = cauchy_plane_data(ha, mua, da, xa, gamma)
            inv_z = norm(np.linalg.inv(muz * np.eye(2) - a_z), ord=2)
            inv_a = norm(np.linalg.inv(mua * np.eye(2) - a_a), ord=2)
            err_z = norm(lhs_z - rvec_z)
            err_a = norm(lhs_a - rvec_a)
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {bexp(norm(hvec_z), L):6.2f} {bexp(norm(rvec_z), L):6.2f}"
                f" {bexp(inv_z, L):7.2f} {bexp(err_z, L):7.2f}"
                f" {bexp(norm(hvec_a), L):7.2f} {bexp(norm(rvec_a), L):6.2f}"
                f" {bexp(inv_a, L):7.2f} {bexp(err_a, L):7.2f}"
            )


if __name__ == "__main__":
    run()
