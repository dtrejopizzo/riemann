#!/usr/bin/env python3
import math
import sys

import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_223_coefficient_ball_budget import coefficient_maps, cauchy_rows, projector  # noqa: E402
from E73_224_weight_amplification_budget import weight  # noqa: E402


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H)
    mu = vals[0]
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / np.linalg.norm(xi)
    d = 2.0 * np.pi * idx / L
    return H.astype(complex), idx.astype(int), d, L, float(mu), xi.astype(complex)


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def source_row_from_weights(row, idx, d, L, lam):
    const_map, linear_map = coefficient_maps(row, idx, d, L)
    src = np.zeros(len(idx), dtype=complex)
    cache = {}
    for om, vec in const_map.items():
        key = (lam, float(L), float(om), "c")
        w = complex(cache.setdefault(key, weight(lam, L, om, "c")))
        src += w * vec
    for om, vec in linear_map.items():
        key = (lam, float(L), float(om), "l")
        v = complex(cache.setdefault(key, weight(lam, L, om, "l")))
        src += v * vec
    return src


def run():
    print("E73.241 curvature source row audit")
    print("Compares coefficient/weight source row with qH, and residual modulo Cauchy plane.")
    print(" lam      L gamma row srcEtaB qHEtaB src-qHB rhoEtaB trivialCobB")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20)]:
        H, idx, d, L, mu, xi = setup(lam, n_modes)
        I = np.eye(len(idx), dtype=complex)
        E = H - mu * I
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            P = projector(Q)
            R = I - P
            eta = R @ xi
            for row_id in range(2):
                row = Q[row_id]
                src = source_row_from_weights(row, idx, d, L, lam)
                qh = row @ H
                rho = qh @ R
                src_eta = src @ eta
                qh_eta = qh @ eta
                # Trivial right-side identity qH eta = qE eta because q eta=0.
                trivial = row @ (E @ eta)
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(src_eta, L):8.2f} {bexp(qh_eta, L):7.2f}"
                    f" {bexp((src-qh) @ eta, L):8.2f}"
                    f" {bexp(rho @ xi, L):8.2f}"
                    f" {bexp(trivial-qh_eta, L):11.2f}"
                )


if __name__ == "__main__":
    run()
