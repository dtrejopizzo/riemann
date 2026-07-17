#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_195_finite_frequency_certificate_probe import cauchy_rows  # noqa: E402


def q_cell(idx, d, y, L):
    n = len(idx)
    qy = np.zeros((n, n), dtype=complex)
    for a in range(n):
        for b in range(n):
            if a == b:
                qy[a, b] = 2.0 * (1.0 - y / L) * np.cos(d[a] * y)
            else:
                qy[a, b] = (np.sin(d[a] * y) - np.sin(d[b] * y)) / (
                    np.pi * (idx[b] - idx[a])
                )
    return qy


def two_symbol_cell_operator(idx, d, y, L):
    n = len(idx)
    op = np.zeros((n, n), dtype=complex)
    w_even = 2.0 * np.cos(d * y)
    f = 2j * np.sin(d * y)
    for j in range(n):
        for b in range(n):
            if j == b:
                fp = 2j * y * np.cos(d[j] * y)
                op[j, b] = w_even[j] - fp / (1j * L)
            else:
                lam = (f[j] - f[b]) / (d[j] - d[b])
                op[j, b] = -lam / (1j * L)
    return op


def setup(lam, n_modes):
    _h, idx, L = build(lam, n_modes, include_arith=True)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L


def run():
    print("E73.294 cell reconstruction probe")
    print("Checks Q_y = M_{2cos(dy)}-(1/(iL))Lambda_{2i sin(dy)}^full.")
    print(" lam     L gamma row y/L opRel rowRel")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        idx, d, L = setup(lam, n_modes)
        ys = [0.0, 0.17 * L, 0.50 * L, 0.83 * L, L]
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            for y in ys:
                qy = q_cell(idx, d, y, L)
                tsy = two_symbol_cell_operator(idx, d, y, L)
                op_rel = norm(qy - tsy) / max(norm(qy), 1e-300)
                for row_id in range(2):
                    row_rel = norm(q[row_id] @ qy - q[row_id] @ tsy) / max(
                        norm(q[row_id] @ qy), 1e-300
                    )
                    print(
                        f"{lam:4d} {L:7.3f} {gamma:7.2f} {row_id:3d}"
                        f" {y/L:5.2f} {op_rel:7.1e} {row_rel:7.1e}"
                    )


if __name__ == "__main__":
    run()
