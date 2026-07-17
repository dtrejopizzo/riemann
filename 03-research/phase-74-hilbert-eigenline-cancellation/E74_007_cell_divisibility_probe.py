#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402


def setup(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    xi = vecs[:, 0].astype(complex)
    if xi[len(xi) // 2].real < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi


def q_cell_apply(q, d, idx, L, eta, y):
    s = np.sin(d * y)
    c = np.cos(d * y)
    out = np.sum(q * eta * (2.0 * (1.0 - y / L) * c))
    n = len(idx)
    for j in range(n):
        for b in range(n):
            if j != b:
                out += q[j] * eta[b] * (s[j] - s[b]) / (math.pi * (idx[b] - idx[j]))
    return out


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def trap_integral(vals, ys, weights=None):
    if weights is None:
        return np.trapezoid(vals, ys)
    return np.trapezoid(vals * weights, ys)


def run():
    print("E74.7 cell divisibility probe")
    print("Tests endpoint and Laplace/Fourier moments of B(y)=qQ_y eta under Q eta=0.")
    print(" lam      L gamma row qetaB B0B BLB d0B dLB int1B intExp+B intExp-B intOsc+B intOsc-B")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24), (24, 28)]:
        idx, d, L, xi = setup(lam, n_modes)
        I = np.eye(len(idx), dtype=complex)
        # Dense enough for a diagnostic; Q_y is bandlimited on this finite mesh.
        ys = np.linspace(0.0, L, 8 * len(idx) + 1)
        dy = ys[1] - ys[0]
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            eta = (I - projector(Q)) @ xi
            qeta = norm(Q @ eta)
            for row_id in range(2):
                q = Q[row_id]
                vals = np.array([q_cell_apply(q, d, idx, L, eta, y) for y in ys])
                B0 = vals[0]
                BL = vals[-1]
                d0 = (vals[1] - vals[0]) / dy
                dL = (vals[-1] - vals[-2]) / dy
                int1 = trap_integral(vals, ys)
                int_exp_p = trap_integral(vals, ys, np.exp((gamma / L) * ys))
                int_exp_m = trap_integral(vals, ys, np.exp(-(gamma / L) * ys))
                int_osc_p = trap_integral(vals, ys, np.exp(1j * gamma * ys))
                int_osc_m = trap_integral(vals, ys, np.exp(-1j * gamma * ys))
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(qeta, L):6.2f}"
                    f" {bexp(B0, L):5.2f}"
                    f" {bexp(BL, L):5.2f}"
                    f" {bexp(d0, L):5.2f}"
                    f" {bexp(dL, L):5.2f}"
                    f" {bexp(int1, L):6.2f}"
                    f" {bexp(int_exp_p, L):8.2f}"
                    f" {bexp(int_exp_m, L):8.2f}"
                    f" {bexp(int_osc_p, L):8.2f}"
                    f" {bexp(int_osc_m, L):8.2f}"
                )


if __name__ == "__main__":
    run()
