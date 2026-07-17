#!/usr/bin/env python3
import math
import sys

import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402
from E73_224_weight_amplification_budget import weight  # noqa: E402


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H)
    xi = vecs[:, 0].astype(complex)
    if xi[len(xi) // 2].real < 0:
        xi = -xi
    xi = xi / np.linalg.norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi


def hilbert_mesh(idx):
    n = len(idx)
    A = np.zeros((n, n), dtype=complex)
    for j in range(n):
        for b in range(n):
            if j != b:
                A[j, b] = 1.0 / (2j * math.pi * (idx[b] - idx[j]))
    return A


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def run():
    print("E73.305 Hilbert product rule")
    print("off=sum F_j[r_j(A eta)_j+eta_j(A r)_j].")
    print(" lam      L gamma row directB prodB errB randErrB diagB rAetaB etaArB cancelB")
    cache = {}
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        idx, d, L, xi = setup(lam, n_modes)
        A = hilbert_mesh(idx)
        I = np.eye(len(idx), dtype=complex)
        Wodd = np.array([
            complex(cache.setdefault((lam, float(L), float(x), "c"), weight(lam, L, x, "c")))
            - complex(cache.setdefault((lam, float(L), float(-x), "c"), weight(lam, L, -x, "c")))
            for x in d
        ])
        Ueven = np.array([
            (
                complex(cache.setdefault((lam, float(L), float(x), "c"), weight(lam, L, x, "c")))
                - complex(cache.setdefault((lam, float(L), float(x), "l"), weight(lam, L, x, "l"))) / L
            )
            + (
                complex(cache.setdefault((lam, float(L), float(-x), "c"), weight(lam, L, -x, "c")))
                - complex(cache.setdefault((lam, float(L), float(-x), "l"), weight(lam, L, -x, "l"))) / L
            )
            for x in d
        ])
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            eta = (I - projector(Q)) @ xi
            for row_id in range(2):
                r = Q[row_id]
                rng = np.random.default_rng(1000 + 37 * lam + 3 * row_id + int(gamma))
                Frand = rng.normal(size=len(idx)) + 1j * rng.normal(size=len(idx))
                rand_direct = 0j
                for j in range(len(idx)):
                    for b in range(len(idx)):
                        if j != b:
                            rand_direct += r[j] * eta[b] * (Frand[j] - Frand[b]) / (
                                2j * math.pi * (idx[b] - idx[j])
                            )
                rand_prod = np.sum(Frand * r * (A @ eta)) + np.sum(Frand * eta * (A @ r))
                diag = np.sum(eta * r * Ueven)
                off_direct = 0j
                for j in range(len(idx)):
                    for b in range(len(idx)):
                        if j != b:
                            off_direct += r[j] * eta[b] * (Wodd[j] - Wodd[b]) / (
                                2j * math.pi * (idx[b] - idx[j])
                            )
                rAeta = np.sum(Wodd * r * (A @ eta))
                etaAr = np.sum(Wodd * eta * (A @ r))
                prod = rAeta + etaAr
                total = diag + off_direct
                prod_total = diag + prod
                cancel = abs(total) / max(abs(diag) + abs(rAeta) + abs(etaAr), 1e-300)
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(total, L):8.2f} {bexp(prod_total, L):7.2f}"
                    f" {bexp(total-prod_total, L):6.2f} {bexp(rand_direct-rand_prod, L):8.2f}"
                    f" {bexp(diag, L):7.2f}"
                    f" {bexp(rAeta, L):8.2f} {bexp(etaAr, L):7.2f}"
                    f" {bexp(cancel, L):8.2f}"
                )


if __name__ == "__main__":
    run()
