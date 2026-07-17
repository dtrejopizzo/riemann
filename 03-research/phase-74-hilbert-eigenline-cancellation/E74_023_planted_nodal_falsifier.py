#!/usr/bin/env python3
"""Apply the Phase 71 planted off-line control to CAUCHY-EIG-LOC."""

import sys

import numpy as np
from numpy.linalg import eigh, norm
from scipy.optimize import newton

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E71_2_convergence_detector import build_QW  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def cauchy(t, d, xi):
    return float(np.sum(xi / (t - d)))


def local_root(gamma, d, xi):
    try:
        return newton(
            lambda t: cauchy(t, d, xi),
            gamma,
            fprime=lambda t: float(np.sum(-xi / (t - d) ** 2)),
            tol=1e-12,
            maxiter=30,
        )
    except RuntimeError:
        return np.nan


def normalized_value(gamma, d, xi):
    row = 1.0 / (gamma - d)
    return abs(np.dot(row / norm(row), xi))


def run_case(tag, planted, lam=12, n_modes=24):
    h, idx, L = build_QW(lam, n_modes, planted=planted)
    vals, vecs = eigh(h)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2.0
    xi /= norm(xi)
    d = 2.0 * np.pi * idx / L
    for gamma in GAMMAS[:3]:
        tau = local_root(gamma, d, xi)
        print(
            f"{tag:8s} {gamma:8.3f} {normalized_value(gamma,d,xi):11.3e}"
            f" {tau:12.6f} {tau-gamma: .3e} {vals[0]: .3e}"
        )


def run():
    print("E74.23 planted off-line nodal falsifier")
    print("case gamma normQxi localRoot rootShift mu")
    run_case("zeta", None)
    run_case("planted", (25.0, 0.30, 5.0))


if __name__ == "__main__":
    run()
