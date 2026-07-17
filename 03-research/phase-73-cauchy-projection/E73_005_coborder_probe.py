#!/usr/bin/env python3
import sys
import cmath
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_003_critical_source_probe import pi_kernel, dd_kernel  # noqa: E402


def setup_full(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h_actual, vals[0], idx.astype(int), d, L, xi


def source_vector(b, off_nodes, crit_nodes, d, L):
    out = []
    for dm in d:
        sb = 0j
        for k in crit_nodes:
            gamma = (-1j * k).real
            sb += pi_kernel(b, k, off_nodes) * dd_kernel(-gamma, dm, L)
        out.append(sb)
    return np.array(out, dtype=complex)


def min_primitive(h, mu, xi, s):
    # Spectral pseudoinverse of A=h-mu I on xi^perp.
    vals, vecs = eigh(h)
    coeff = vecs.conj().T @ s
    ycoeff = np.zeros_like(coeff, dtype=complex)
    for j, lam in enumerate(vals):
        gap = lam - mu
        if abs(gap) > 1e-9:
            ycoeff[j] = coeff[j] / gap
    y = vecs @ ycoeff
    resid = s - (h - mu * np.eye(h.shape[0])) @ y
    return y, resid


def run():
    print("E73.005 coborder primitive probe")
    print(" lam     L   dim      |S|      eigRes    expEig    |Ymin|    |DY|     |D2Y|")
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    b = off_nodes[0]
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18)]:
        h, mu, idx, d, L, xi = setup_full(lam, n_modes)
        s = source_vector(b, off_nodes, crit_nodes, d, L)
        y, resid = min_primitive(h, mu, xi, s)
        eig = abs(np.vdot(xi, s))
        exp_eig = abs(cmath.exp(b.real * L)) * eig
        dy = norm(d * y)
        d2y = norm((d ** 2) * y)
        print(
            f"{lam:4.0f} {L:7.3f} {len(idx):5d} {norm(s):9.3e} {eig:9.3e} "
            f"{exp_eig:9.3e} {norm(y):9.3e} {dy:9.3e} {d2y:9.3e}"
        )


if __name__ == "__main__":
    run()
