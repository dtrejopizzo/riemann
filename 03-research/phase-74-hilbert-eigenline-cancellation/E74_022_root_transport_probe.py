#!/usr/bin/env python3
"""Relate critical Cauchy cancellation to transport of finite Weyl roots."""

import sys

import numpy as np
from numpy.linalg import eigh, norm
from scipy.optimize import newton

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def cauchy(t, d, xi):
    return float(np.sum(xi / (t - d)))


def nearest_root(gamma, d, xi):
    try:
        return newton(
            lambda t: cauchy(t, d, xi),
            gamma,
            fprime=lambda t: float(np.sum(-xi / (t - d) ** 2)),
            tol=1e-13,
            maxiter=20,
        )
    except RuntimeError:
        return np.nan


def bexp(x, L):
    return np.log(max(float(abs(x)), 1e-300)) / np.log(L)


def run():
    print("E74.22 finite-root transport audit")
    print("delta=tau_L-gamma; shift evaluates normalized C at gamma+1/L.")
    print(" lam      L gamma reach delta rootValB critValB derivB shiftB")
    for lam, n_modes in [(12, 20), (16, 24), (20, 28), (24, 32)]:
        h, idx, L = build(lam, n_modes, include_arith=True)
        _, vecs = eigh(h)
        xi = vecs[:, 0]
        xi /= norm(xi)
        d = 2.0 * np.pi * idx / L
        for gamma in GAMMAS[:3]:
            tau = nearest_root(gamma, d, xi)
            row = 1.0 / (gamma - d)
            row_shift = 1.0 / (gamma + 1.0 / L - d)
            crit = abs(np.dot(row / norm(row), xi))
            shift = abs(np.dot(row_shift / norm(row_shift), xi))
            deriv = abs(np.sum(-xi / (gamma - d) ** 2)) / norm(row)
            root_val = abs(cauchy(tau, d, xi)) if np.isfinite(tau) else np.nan
            print(
                f"{lam:4d} {L:8.3f} {gamma:6.2f} {max(abs(d))/gamma:5.2f}"
                f" {tau-gamma: .3e} {bexp(root_val,L):8.2f}"
                f" {bexp(crit,L):8.2f} {bexp(deriv,L):6.2f} {bexp(shift,L):6.2f}"
            )


if __name__ == "__main__":
    run()
