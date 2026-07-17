#!/usr/bin/env python3
"""Test whether ordinary block-gap perturbation can force Cauchy localization."""

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


def orth_complement(u):
    uu, _, _ = svd(u, full_matrices=True)
    return uu[:, u.shape[1] :]


def run():
    print("E74.20 Feshbach block audit")
    print("B=U*HV is the cross block. eigCross is B eta for the actual eigenline complement.")
    print(" lam      L gamma BnormB gapB ratio eigCrossB uB blockEqB")
    for lam, n_modes in [(12, 20), (16, 24), (20, 28), (24, 32)]:
        h, idx, L = build(lam, n_modes, include_arith=True)
        vals, vecs = eigh(h)
        mu = vals[0]
        xi = vecs[:, 0].astype(complex)
        xi /= norm(xi)
        d = 2.0 * np.pi * idx / L
        for gamma in GAMMAS[:3]:
            q = cauchy_rows(-1j * gamma, d)
            g = q @ q.conj().T
            gv, gu = eigh(g)
            gih = gu @ np.diag(gv ** -0.5) @ gu.conj().T
            uiso = q.conj().T @ gih
            v = orth_complement(uiso)
            a = uiso.conj().T @ h @ uiso
            b = uiso.conj().T @ h @ v
            small = uiso.conj().T @ xi
            eta = v.conj().T @ xi
            eig_cross = b @ eta
            block_err = (a - mu * np.eye(2)) @ small + eig_cross
            gap = np.min(np.linalg.eigvalsh(a) - mu)
            print(
                f"{lam:4d} {L:8.3f} {gamma:6.2f}"
                f" {bexp(norm(b,2),L):6.2f} {bexp(gap,L):5.2f}"
                f" {norm(b,2)/max(gap,1e-300):5.2f}"
                f" {bexp(norm(eig_cross),L):9.2f} {bexp(norm(small),L):5.2f}"
                f" {bexp(norm(block_err),L):8.2f}"
            )


if __name__ == "__main__":
    run()
