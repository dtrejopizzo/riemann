#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-74-hilbert-eigenline-cancellation")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402
from E73_224_weight_amplification_budget import weight  # noqa: E402
from E74_002_closed_mesh_action_probe import harmonic_symbol, hilbert_mesh  # noqa: E402


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H)
    xi = vecs[:, 0].astype(complex)
    if xi[len(xi) // 2].real < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi


def weights(lam, L, d, cache):
    Wodd = np.array(
        [
            complex(cache.setdefault((lam, float(L), float(x), "c"), weight(lam, L, x, "c")))
            - complex(cache.setdefault((lam, float(L), float(-x), "c"), weight(lam, L, -x, "c")))
            for x in d
        ],
        dtype=complex,
    )
    Ueven = np.array(
        [
            (
                complex(cache.setdefault((lam, float(L), float(x), "c"), weight(lam, L, x, "c")))
                - complex(cache.setdefault((lam, float(L), float(x), "l"), weight(lam, L, x, "l"))) / L
            )
            + (
                complex(cache.setdefault((lam, float(L), float(-x), "c"), weight(lam, L, -x, "c")))
                - complex(cache.setdefault((lam, float(L), float(-x), "l"), weight(lam, L, -x, "l"))) / L
            )
            for x in d
        ],
        dtype=complex,
    )
    return Wodd, Ueven


def hpr_direct(idx, A, r, eta, Wodd, Ueven):
    diag = np.sum(eta * r * Ueven)
    rAeta = np.sum(Wodd * r * (A @ eta))
    etaAr = np.sum(Wodd * eta * (A @ r))
    return diag, rAeta, etaAr, diag + rAeta + etaAr


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def run():
    print("E74.3 harmonic-symbol normal form")
    print("HPR = <r, U eta> + <r, W (A+H_beta) eta> exactly.")
    print(" lam      L gamma row totalB normalErrB diagB WAetaB WHetaB AplusHnormB cancelB")
    cache = {}
    for lam, n_modes in [(12, 16), (16, 20), (20, 24), (24, 28)]:
        idx, d, L, xi = setup(lam, n_modes)
        A = hilbert_mesh(idx)
        I = np.eye(len(idx), dtype=complex)
        Wodd, Ueven = weights(lam, L, d, cache)
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            eta = (I - projector(Q)) @ xi
            alpha = gamma * L / (2.0 * math.pi)
            for row_id, beta in [(0, alpha), (1, -alpha)]:
                r = Q[row_id]
                Hsym = harmonic_symbol(idx, beta)
                diag, WAeta, WHeta_direct, total = hpr_direct(idx, A, r, eta, Wodd, Ueven)
                WHeta = np.sum(r * Wodd * Hsym * eta)
                normal = diag + np.sum(r * Wodd * ((A @ eta) + Hsym * eta))
                denom = max(abs(diag) + abs(WAeta) + abs(WHeta), 1e-300)
                cancel = abs(total) / denom
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(total, L):7.2f}"
                    f" {bexp(total - normal, L):10.2f}"
                    f" {bexp(diag, L):7.2f}"
                    f" {bexp(WAeta, L):7.2f}"
                    f" {bexp(WHeta, L):7.2f}"
                    f" {bexp(norm((A @ eta) + Hsym * eta), L):11.2f}"
                    f" {bexp(cancel, L):8.2f}"
                )


if __name__ == "__main__":
    run()
