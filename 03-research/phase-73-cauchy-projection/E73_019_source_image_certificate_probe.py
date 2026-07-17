#!/usr/bin/env python3
import sys
import cmath
import numpy as np
from numpy.linalg import eigh, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_003_critical_source_probe import dd_kernel, pi_kernel  # noqa: E402


def setup_full(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2.0
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h_actual, vals[0], idx.astype(int), d, L, xi


def local_basis(off_nodes, crit_nodes, d, L):
    cols = []
    labels = []
    for ki, k in enumerate(crit_nodes):
        gamma = (-1j * k).real
        dd = np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
        for bi, beta in enumerate(off_nodes):
            denom = np.array([dm * dm + beta * beta for dm in d], dtype=complex)
            for r in [0, 1, 2]:
                cols.append(dd.copy() if r == 0 else dd / (denom ** r))
                labels.append(("rat", ki, bi, r))
        cols.append((d ** 2) * dd)
        labels.append(("poly", ki, -1, 1))
    return np.column_stack(cols), labels


def source_vector(b, off_nodes, crit_nodes, d, L):
    total = np.zeros_like(d, dtype=complex)
    for k in crit_nodes:
        gamma = (-1j * k).real
        coeff = pi_kernel(b, k, off_nodes)
        total += coeff * np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
    return total


def svd_projector(mat, tol=1e-10):
    u, s, _ = svd(mat, full_matrices=False)
    rank = int(np.sum(s > tol * s[0])) if len(s) else 0
    cond = float(s[0] / s[rank - 1]) if rank else np.inf
    return u[:, :rank], rank, cond


def run():
    print("E73.019 source image certificate probe")
    print("Tests S_b in Image((C_E-mu)P_{O,K}).")
    print(" lam     L   dim  imgRank  imgCond       bRe       |S|      relRes    expPair")
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20)]:
        h, mu, idx, d, L, xi = setup_full(lam, n_modes)
        prim, _ = local_basis(off_nodes, crit_nodes, d, L)
        image = (h - mu * np.eye(h.shape[0])) @ prim
        u_img, irank, icond = svd_projector(image)
        for b in off_nodes:
            src = source_vector(b, off_nodes, crit_nodes, d, L)
            resid = src - u_img @ (u_img.conj().T @ src)
            rel = norm(resid) / max(norm(src), 1e-30)
            exp_pair = abs(cmath.exp(b.real * L) * np.vdot(xi, resid))
            print(
                f"{lam:4d} {L:7.3f} {len(idx):5d} {irank:8d} {icond:8.1e} "
                f"{b.real:9.3f} {norm(src):9.2e} {rel:10.2e} {exp_pair:10.2e}"
            )


if __name__ == "__main__":
    run()
