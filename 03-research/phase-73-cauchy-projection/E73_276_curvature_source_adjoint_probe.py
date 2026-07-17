#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_193_balanced_ramp_probe import functional, r0, r1  # noqa: E402
from E73_223_coefficient_ball_budget import coefficient_maps, cauchy_rows, projector  # noqa: E402
from E73_224_weight_amplification_budget import weight  # noqa: E402


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return H.astype(complex), idx.astype(int), d, L, xi.astype(complex)


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def source_row_from_weights(row, idx, d, L, lam, balanced=False):
    const_map, linear_map = coefficient_maps(row, idx, d, L)
    src = np.zeros(len(idx), dtype=complex)
    cache = {}
    rstar_weight = 0j
    if balanced:
        f0 = functional(lambda y: r0(y, L), 1.0, L, lam)
        f1 = functional(lambda y: r1(y, L), 0.0, L, lam)
        c_bal = -f0 / f1
        rstar_weight = f0 + c_bal * f1
    for om, vec in const_map.items():
        key = (float(om), "c")
        w = complex(cache.setdefault(key, weight(lam, L, om, "c")))
        if balanced:
            w -= 1j * om * rstar_weight
        src += w * vec
    for om, vec in linear_map.items():
        key = (float(om), "l")
        v = complex(cache.setdefault(key, weight(lam, L, om, "l")))
        if balanced:
            v -= rstar_weight
        src += v * vec
    return src


def run():
    print("E73.276 curvature source adjoint probe")
    print("Reconstructs source row from coefficient weights and compares to qH.")
    print(" lam      L gamma row srcErrB balErrB aprErrB centerB srcEtaB balEtaB")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        H, idx, d, L, xi = setup(lam, n_modes)
        I = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            P = projector(Q)
            R = I - P
            eta = R @ xi
            A = Q @ H @ Q.conj().T @ inv(Q @ Q.conj().T)
            for row_id in range(2):
                row = Q[row_id]
                src = source_row_from_weights(row, idx, d, L, lam, balanced=False)
                src_bal = source_row_from_weights(row, idx, d, L, lam, balanced=True)
                qh = row @ H
                rho = row @ H @ R
                apr = row @ H - A[row_id] @ Q
                center = rho @ xi
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(norm(src-qh), L):8.2f}"
                    f" {bexp(norm(src_bal-qh), L):8.2f}"
                    f" {bexp(norm(apr-rho), L):8.2f}"
                    f" {bexp(center, L):8.2f}"
                    f" {bexp(src @ eta, L):8.2f}"
                    f" {bexp(src_bal @ eta, L):8.2f}"
                )


if __name__ == "__main__":
    run()
