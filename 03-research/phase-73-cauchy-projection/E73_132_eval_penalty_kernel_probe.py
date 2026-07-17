#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402


def orient(x):
    x = (x + x[::-1]) / 2.0
    x = x / norm(x)
    if x[len(x) // 2] < 0:
        x = -x
    return x


def setup(lam, n_modes, include_arith=True):
    h, idx, L = build(lam, n_modes, include_arith=include_arith)
    vals, vecs = eigh(h)
    xi = orient(vecs[:, 0])
    d = 2.0 * np.pi * idx / L
    return h, vals[0], d, L, xi


def eval_matrix(d, gammas, normalize=True):
    rows = []
    for gamma in gammas:
        row = 1.0 / (-gamma - d)
        if normalize:
            row = row / max(norm(row), 1e-300)
        rows.append(row)
    return np.vstack(rows)


def probe(lam, n_modes, gammas, rho):
    h, mu, d, L, xi = setup(lam, n_modes, include_arith=True)
    k = eval_matrix(d, gammas, normalize=True)
    penalty = k.T @ k
    vals, vecs = eigh(h + rho * penalty)
    eta = orient(vecs[:, 0])
    if np.dot(eta, xi) < 0:
        eta = -eta
    leak_xi = norm(k @ xi)
    leak_eta = norm(k @ eta)
    shift = vals[0] - mu
    overlap_loss = 1.0 - abs(float(np.dot(xi, eta)))
    return L, leak_xi, leak_eta, shift, overlap_loss


def run():
    print("E73.132 critical evaluation penalty kernel probe")
    print("Adds rho*K^T K for normalized critical Cauchy rows K.")
    print("Small shift/overlap loss means xi_zeta already lies near ker K.")
    print(" lam     L rho      leakXiB leakEtaB  shiftB overlapLossB")
    gammas = GAMMAS[:3]
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32)]:
        for rho in [1e-6, 1e-3, 1.0]:
            L, leak_xi, leak_eta, shift, overlap_loss = probe(lam, n_modes, gammas, rho)
            print(
                f"{lam:4d} {L:7.3f} {rho:7.1e}"
                f" {bexp(leak_xi, L):8.3f} {bexp(leak_eta, L):8.3f}"
                f" {bexp(abs(shift), L):7.3f} {bexp(overlap_loss, L):12.3f}"
            )


if __name__ == "__main__":
    run()

