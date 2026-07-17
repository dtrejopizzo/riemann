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
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / np.linalg.norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi.astype(complex)


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def project_rows(g, rows):
    A = np.vstack(rows)
    # Orthogonal projection of g onto row span in C^n.
    gram = A @ A.conj().T
    coeff = np.linalg.lstsq(gram, A @ g, rcond=None)[0]
    return A.conj().T @ coeff


def run():
    print("E73.239 moment annihilator audit")
    print("Projects weights onto endpoint/derivative moment rows and measures residual pairing.")
    print(" lam      L gamma row centerB res2B res3B mom2B mom3B resNorm2B resNorm3B")
    cache = {}
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        idx, d, L, xi = setup(lam, n_modes)
        I = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            eta = (I - projector(Q)) @ xi
            for row_id in range(2):
                const_map, linear_map = coefficient_maps(Q[row_id], idx, d, L)
                oms_c = sorted(const_map)
                oms_l = sorted(linear_map)
                x = []
                g = []
                for om in oms_c:
                    x.append(const_map[om] @ eta)
                    key = (lam, float(L), float(om), "c")
                    g.append(complex(cache.setdefault(key, weight(lam, L, om, "c"))))
                for om in oms_l:
                    x.append(linear_map[om] @ eta)
                    key = (lam, float(L), float(om), "l")
                    g.append(complex(cache.setdefault(key, weight(lam, L, om, "l"))))
                x = np.array(x, dtype=complex)
                g = np.array(g, dtype=complex)
                n_c = len(oms_c)
                n_l = len(oms_l)
                row_c = np.r_[np.ones(n_c), np.zeros(n_l)].astype(complex)
                row_l = np.r_[np.zeros(n_c), np.ones(n_l)].astype(complex)
                row_d = np.r_[[1j * om for om in oms_c], np.ones(n_l)].astype(complex)
                proj2 = project_rows(g, [row_c, row_l])
                proj3 = project_rows(g, [row_c, row_l, row_d])
                res2 = g - proj2
                res3 = g - proj3
                center = np.dot(x, g)
                mom2 = np.dot(x, proj2)
                mom3 = np.dot(x, proj3)
                pair2 = np.dot(x, res2)
                pair3 = np.dot(x, res3)
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(center, L):8.2f} {bexp(pair2, L):7.2f}"
                    f" {bexp(pair3, L):7.2f} {bexp(mom2, L):7.2f}"
                    f" {bexp(mom3, L):7.2f} {bexp(np.linalg.norm(res2), L):10.2f}"
                    f" {bexp(np.linalg.norm(res3), L):10.2f}"
                )


if __name__ == "__main__":
    run()
