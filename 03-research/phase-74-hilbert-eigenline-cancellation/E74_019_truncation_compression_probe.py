#!/usr/bin/env python3
"""Resolve Cauchy compression as a function of mesh reach and arithmetic."""

import sys

import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows  # noqa: E402


def compression(h, q):
    g = q @ q.conj().T
    gv, gu = np.linalg.eigh(g)
    gih = gu @ np.diag(gv ** -0.5) @ gu.conj().T
    c = gih @ (q @ h @ q.conj().T) @ gih
    return np.linalg.eigvalsh(c), gv[-1] / gv[0]


def run():
    print("E74.19 truncation/compression audit")
    print("reach=dmax/gamma. full and arch columns are compression eigenvalues divided by L.")
    print(" lam  N      L gamma reach gramCond fullLo fullHi archLo archHi primeLo primeHi")
    for lam in [12, 16, 20]:
        L = 2.0 * np.log(lam)
        for n_modes in [8, 12, 16, 20, 24, 28, 32]:
            hf, idx, _ = build(lam, n_modes, include_arith=True)
            ha, _, _ = build(lam, n_modes, include_arith=False)
            d = 2.0 * np.pi * idx / L
            for gamma in GAMMAS[:3]:
                q = cauchy_rows(-1j * gamma, d)
                ef, condg = compression(hf, q)
                ea, _ = compression(ha, q)
                ep, _ = compression(hf - ha, q)
                print(
                    f"{lam:4d} {n_modes:2d} {L:7.3f} {gamma:6.2f}"
                    f" {max(abs(d))/gamma:5.2f} {condg:8.1e}"
                    f" {ef[0]/L:6.3f} {ef[1]/L:6.3f}"
                    f" {ea[0]/L:6.3f} {ea[1]/L:6.3f}"
                    f" {ep[0]/L:7.3f} {ep[1]/L:7.3f}"
                )


if __name__ == "__main__":
    run()
