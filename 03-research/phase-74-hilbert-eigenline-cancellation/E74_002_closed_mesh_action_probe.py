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
from E73_223_coefficient_ball_budget import cauchy_rows  # noqa: E402


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L


def hilbert_mesh(idx):
    n = len(idx)
    A = np.zeros((n, n), dtype=complex)
    for j in range(n):
        for b in range(n):
            if j != b:
                A[j, b] = 1.0 / (2j * math.pi * (idx[b] - idx[j]))
    return A


def exact_action(idx, L, beta):
    """Closed finite sum for r_n=L/(2*pi*i)/(n-beta)."""
    out = np.zeros(len(idx), dtype=complex)
    for jj, n in enumerate(idx):
        s = 0j
        for m in idx:
            if m != n:
                s += 1.0 / ((m - n) * (m - beta))
        out[jj] = -L / (4.0 * math.pi * math.pi) * s
    return out


def harmonic_symbol(idx, beta):
    """h_n such that A r = h_n r_n for r_n=L/(2*pi*i)/(n-beta)."""
    h = np.zeros(len(idx), dtype=complex)
    for jj, n in enumerate(idx):
        s = 0j
        for m in idx:
            if m != n:
                s += 1.0 / (m - n) - 1.0 / (m - beta)
        h[jj] = -1j / (2.0 * math.pi) * s
    return h


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def run():
    print("E74.2 closed finite-mesh Hilbert action")
    print("Ar = H_beta r with H_beta(n)=-i/(2pi) sum_{m!=n}[1/(m-n)-1/(m-beta)].")
    print(" lam      L gamma row beta formulaErrB multErrB meanH spreadH maxH minH")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24), (24, 28), (28, 32)]:
        idx, d, L = setup(lam, n_modes)
        A = hilbert_mesh(idx)
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            alpha = gamma * L / (2.0 * math.pi)
            for row_id, beta in [(0, alpha), (1, -alpha)]:
                r = Q[row_id]
                Ar = A @ r
                closed = exact_action(idx, L, beta)
                h = harmonic_symbol(idx, beta)
                mult = h * r
                formula_err = norm(Ar - closed) / max(norm(Ar), 1e-300)
                mult_err = norm(Ar - mult) / max(norm(Ar), 1e-300)
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {beta:9.3f}"
                    f" {bexp(formula_err, L):11.2f}"
                    f" {bexp(mult_err, L):8.2f}"
                    f" {h.mean().real:+.3e}{h.mean().imag:+.3e}i"
                    f" {np.std(h):8.2e}"
                    f" {np.max(np.abs(h)):8.2e}"
                    f" {np.min(np.abs(h)):8.2e}"
                )


if __name__ == "__main__":
    run()
