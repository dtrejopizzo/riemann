#!/usr/bin/env python3
import math
import sys

import mpmath as mp
import numpy as np
from numpy.linalg import inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_223_coefficient_ball_budget import coefficient_maps, cauchy_rows, projector  # noqa: E402
from E73_224_weight_amplification_budget import weight  # noqa: E402


mp.mp.dps = 80


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi.astype(complex)


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def run():
    print("E73.236 endpoint moment divisibility")
    print("Checks sum c=0, sum l=0 and invariance under W,V constant gauges.")
    print(" lam      L gamma row sumCB sumLB centerB gaugedB diffB")
    cache = {}
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        idx, d, L, xi = setup(lam, n_modes)
        I = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            eta = (I - projector(Q)) @ xi
            for row_id in range(2):
                const_map, linear_map = coefficient_maps(Q[row_id], idx, d, L)
                c = {om: vec @ eta for om, vec in const_map.items()}
                ell = {om: vec @ eta for om, vec in linear_map.items()}
                sum_c = sum(c.values())
                sum_l = sum(ell.values())
                center = 0j
                gauged = 0j
                alpha = None
                beta = None
                weights_c = {}
                weights_l = {}
                for om in c:
                    key = (lam, float(L), float(om), "c")
                    weights_c[om] = complex(cache.setdefault(key, weight(lam, L, om, "c")))
                for om in ell:
                    key = (lam, float(L), float(om), "l")
                    weights_l[om] = complex(cache.setdefault(key, weight(lam, L, om, "l")))
                if weights_c:
                    alpha = sum(weights_c.values()) / len(weights_c)
                else:
                    alpha = 0j
                if weights_l:
                    beta = sum(weights_l.values()) / len(weights_l)
                else:
                    beta = 0j
                for om, coeff in c.items():
                    center += coeff * weights_c[om]
                    gauged += coeff * (weights_c[om] - alpha)
                for om, coeff in ell.items():
                    center += coeff * weights_l[om]
                    gauged += coeff * (weights_l[om] - beta)
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(sum_c, L):7.2f} {bexp(sum_l, L):7.2f}"
                    f" {bexp(center, L):8.2f} {bexp(gauged, L):8.2f}"
                    f" {bexp(center-gauged, L):7.2f}"
                )


if __name__ == "__main__":
    run()
