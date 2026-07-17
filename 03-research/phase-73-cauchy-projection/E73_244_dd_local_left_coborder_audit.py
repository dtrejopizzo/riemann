#!/usr/bin/env python3
import cmath
import math
import sys

import numpy as np
from numpy.linalg import inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_003_critical_source_probe import dd_kernel  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H)
    mu = vals[0]
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return H.astype(complex), idx.astype(int), d, L, float(mu), xi.astype(complex)


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def dd_local_columns(gamma, d, L, rat_power):
    cols = []
    den = d * d - gamma * gamma
    for u in [gamma, -gamma]:
        dd = np.array([dd_kernel(u, dm, L) for dm in d], dtype=complex)
        # Endpoint polynomial slots from E73.015/E73.016.
        cols.append(dd)
        cols.append((d * d) * dd)
        cols.append((d**4) * dd)
        for m in range(1, rat_power + 1):
            cols.append(dd / (den**m))
            cols.append((d * d) * dd / (den**m))
    return np.column_stack(cols)


def fit_left_coborder(rho, E, prim):
    rows = prim.conj().T @ E
    sol, *_ = np.linalg.lstsq(rows.T, rho.T, rcond=None)
    return sol @ rows


def run():
    print("E73.244 DD-local left-coborder audit")
    print("Fits rho by Y*E with Y in DD_L(±gamma,d)/(d^2-gamma^2)^m local ideal.")
    print(" lam      L gamma row pow dim centerB resPairB resNormB")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20)]:
        H, idx, d, L, mu, xi = setup(lam, n_modes)
        I = np.eye(len(idx), dtype=complex)
        E = H - mu * I
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            P = projector(Q)
            R = I - P
            for row_id in range(2):
                rho = Q[row_id] @ H @ R
                center = rho @ xi
                for rat_power in [0, 1, 2, 3]:
                    prim = dd_local_columns(gamma, d, L, rat_power)
                    approx = fit_left_coborder(rho, E, prim)
                    res = rho - approx
                    print(
                        f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                        f" {rat_power:3d} {prim.shape[1]:4d}"
                        f" {bexp(center, L):8.2f}"
                        f" {bexp(res @ xi, L):8.2f} {bexp(norm(res), L):8.2f}"
                    )


if __name__ == "__main__":
    run()
