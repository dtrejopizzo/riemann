#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    phase = np.sign(np.real(np.vdot(xi, np.ones_like(xi))))
    if phase == 0:
        phase = 1.0
    xi = phase * xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return vals[0], idx.astype(int), d, L, xi


def stable_g(gamma, d, L, xi):
    return (1.0 - np.exp(1j * gamma * L)) * np.sum(xi / (-gamma - d))


def phi_raw(s, d, L, xi):
    return (2.0 / np.sqrt(L)) * np.sin(s * L / 2.0) * np.sum(xi / (s - d))


def bexp(x, L):
    return np.log(max(float(abs(x)), 1e-300)) / np.log(L)


def run():
    print("E73.178 characteristic-node equivalence probe")
    print("Checks G_L(i gamma)=i sqrt(L) exp(i gamma L/2) Phi_L(-gamma).")
    print(" lam     L      maxRel      maxAbs    maxNodeB    maxPhiB    scaleB")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (20, 24), (24, 28), (32, 36)]:
        _mu, _idx, d, L, xi = setup(lam, n_modes)
        rels = []
        abss = []
        gs = []
        phis = []
        for gamma in GAMMAS[:5]:
            g = stable_g(gamma, d, L, xi)
            phi = phi_raw(-gamma, d, L, xi)
            rhs = 1j * np.sqrt(L) * np.exp(1j * gamma * L / 2.0) * phi
            rels.append(abs(g - rhs) / max(abs(g), abs(rhs), 1e-300))
            abss.append(abs(g - rhs))
            gs.append(g)
            phis.append(phi)
        scale = max(abs(g) / max(abs(p), 1e-300) for g, p in zip(gs, phis))
        print(
            f"{lam:4d} {L:7.3f} {max(rels):10.2e} {max(abss):10.2e} "
            f"{bexp(max(abs(v) for v in gs), L):9.2f} "
            f"{bexp(max(abs(v) for v in phis), L):8.2f} "
            f"{bexp(scale, L):7.2f}"
        )


if __name__ == "__main__":
    run()
