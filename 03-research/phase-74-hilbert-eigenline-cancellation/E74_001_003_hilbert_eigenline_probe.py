#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import norm

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
    xi = xi / norm(xi)
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


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def coeff_bilinear(r, Ar):
    den = np.sum(r * r)
    if abs(den) < 1e-300:
        return 0j
    return np.sum(r * Ar) / den


def coeff_hermitian(r, Ar):
    den = np.vdot(r, r)
    if abs(den) < 1e-300:
        return 0j
    return np.vdot(r, Ar) / den


def hpr_terms(idx, A, r, eta, Wodd, Ueven):
    diag = np.sum(eta * r * Ueven)
    rAeta = np.sum(Wodd * r * (A @ eta))
    etaAr = np.sum(Wodd * eta * (A @ r))
    off_direct = 0j
    for j in range(len(idx)):
        for b in range(len(idx)):
            if j != b:
                off_direct += r[j] * eta[b] * (Wodd[j] - Wodd[b]) / (
                    2j * math.pi * (idx[b] - idx[j])
                )
    return diag, rAeta, etaAr, off_direct


def run():
    print("E74.1-E74.3 Hilbert eigenline probe")
    print("Tests: bridge HPR=commutator, Ar=c r+rho, and one-sided collapse size.")
    print(
        " lam      L gamma row cBil cHerm "
        "rhoRelB rhoPairB totalB bridgeErrB rAetaB etaArB oneSideB oneSideErrB cancelB"
    )
    cache = {}
    for lam, n_modes in [(12, 16), (16, 20), (20, 24), (24, 28)]:
        idx, d, L, xi = setup(lam, n_modes)
        A = hilbert_mesh(idx)
        I = np.eye(len(idx), dtype=complex)
        Wodd, Ueven = weights(lam, L, d, cache)
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            eta = (I - projector(Q)) @ xi
            for row_id in range(2):
                r = Q[row_id]
                Ar = A @ r
                c_b = coeff_bilinear(r, Ar)
                c_h = coeff_hermitian(r, Ar)
                rho = Ar - c_b * r
                diag, rAeta, etaAr, off_direct = hpr_terms(idx, A, r, eta, Wodd, Ueven)
                total = diag + off_direct
                prod_total = diag + rAeta + etaAr
                rho_pair = np.sum(Wodd * eta * rho)
                one_side = diag + c_b * np.sum(Wodd * eta * r) + rho_pair
                denom = max(abs(diag) + abs(rAeta) + abs(etaAr), 1e-300)
                cancel = abs(total) / denom
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {c_b.real:+.3e}{c_b.imag:+.3e}i"
                    f" {c_h.real:+.3e}{c_h.imag:+.3e}i"
                    f" {bexp(norm(rho) / max(norm(Ar), 1e-300), L):8.2f}"
                    f" {bexp(rho_pair, L):8.2f}"
                    f" {bexp(total, L):7.2f}"
                    f" {bexp(total - prod_total, L):10.2f}"
                    f" {bexp(rAeta, L):7.2f}"
                    f" {bexp(etaAr, L):7.2f}"
                    f" {bexp(one_side, L):8.2f}"
                    f" {bexp(total - one_side, L):11.2f}"
                    f" {bexp(cancel, L):8.2f}"
                )


if __name__ == "__main__":
    run()
