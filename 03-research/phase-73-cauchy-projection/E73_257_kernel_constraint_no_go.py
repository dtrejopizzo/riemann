#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_245_curv_quotient_defect import bexp, setup  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402


def null_basis(Q, tol=1e-12):
    _u, s, vh = svd(Q, full_matrices=True)
    if len(s) == 0:
        rank = 0
    else:
        rank = int(np.sum(s > tol * s[0]))
    return vh[rank:, :].conj().T


def deterministic_kernel_vectors(Z):
    # Columns are an orthonormal basis for ker Q. Use deterministic test
    # vectors so the probe is reproducible.
    out = []
    if Z.shape[1] == 0:
        return out
    out.append(Z[:, 0])
    out.append(Z[:, -1])
    coeff = np.ones(Z.shape[1], dtype=complex)
    out.append(Z @ (coeff / norm(coeff)))
    coeff = np.array([(-1) ** j for j in range(Z.shape[1])], dtype=complex)
    out.append(Z @ (coeff / norm(coeff)))
    coeff = np.exp(1j * np.arange(Z.shape[1]))
    out.append(Z @ (coeff / norm(coeff)))
    return [v / norm(v) for v in out]


def run():
    print("E73.257 kernel-constraint no-go")
    print("Tests whether Q eta=0 alone can explain q_a H eta small.")
    print(
        " lam      L gamma row kerDim actualB opKerB sampleMaxB "
        "sampleMeanB gapActualToOpB qetaB"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20), (20, 24)]:
        H, _idx, d, L, _mu, xi = setup(lam, n_modes)
        eye = np.eye(len(d), dtype=complex)
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            P = projector(Q)
            R = eye - P
            eta = R @ xi
            Z = null_basis(Q)
            samples = deterministic_kernel_vectors(Z)
            qeta = norm(Q @ eta)
            for row_id in range(2):
                row = Q[row_id] @ H
                actual = row @ eta
                # Operator norm of q_a H restricted to ker Q.
                op_ker = norm(row @ Z) if Z.shape[1] else 0.0
                vals = np.array([row @ v for v in samples], dtype=complex)
                sample_max = np.max(np.abs(vals)) if len(vals) else 0.0
                sample_mean = np.mean(np.abs(vals)) if len(vals) else 0.0
                gap = op_ker / max(abs(actual), 1e-300)
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {Z.shape[1]:6d}"
                    f" {bexp(actual, L):8.2f}"
                    f" {bexp(op_ker, L):7.2f}"
                    f" {bexp(sample_max, L):10.2f}"
                    f" {bexp(sample_mean, L):11.2f}"
                    f" {bexp(gap, L):14.2f}"
                    f" {bexp(qeta, L):7.2f}"
                )


if __name__ == "__main__":
    run()
