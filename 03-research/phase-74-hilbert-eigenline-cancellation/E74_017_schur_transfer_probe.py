#!/usr/bin/env python3
"""Audit the exact 2x2 transfer from Q xi to Q H (I-P_Q) xi."""

import sys

import numpy as np
from numpy.linalg import eigh, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402


def bexp(x, L):
    return np.log(max(float(abs(x)), 1e-300)) / np.log(L)


def run():
    print("E74.17 exact Schur-transfer audit")
    print("QH(I-P)xi = T Qxi, T=mu I-QHQ*(QQ*)^-1.")
    print("minTB/maxTB are L-exponents of singular values; errB certifies the identity.")
    print(" lam      L gamma qxiB hprB minTB maxTB condT errB")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (20, 24), (24, 28)]:
        h, idx, L = build(lam, n_modes, include_arith=True)
        vals, vecs = eigh(h)
        mu = vals[0]
        xi = vecs[:, 0].astype(complex)
        xi /= norm(xi)
        d = 2.0 * np.pi * idx / L
        for gamma in GAMMAS[:3]:
            q = cauchy_rows(-1j * gamma, d)
            gram = q @ q.conj().T
            p = projector(q)
            transfer = mu * np.eye(2) - (q @ h @ q.conj().T) @ np.linalg.inv(gram)
            qxi = q @ xi
            hpr = q @ h @ (np.eye(len(idx)) - p) @ xi
            rhs = transfer @ qxi
            sing = svd(transfer, compute_uv=False)
            err = norm(hpr - rhs) / max(norm(hpr), norm(rhs), 1e-300)
            print(
                f"{lam:4d} {L:8.3f} {gamma:6.2f}"
                f" {bexp(norm(qxi),L):5.2f} {bexp(norm(hpr),L):5.2f}"
                f" {bexp(sing[-1],L):6.2f} {bexp(sing[0],L):6.2f}"
                f" {sing[0]/max(sing[-1],1e-300):6.1e} {bexp(err,L):5.2f}"
            )


if __name__ == "__main__":
    run()
