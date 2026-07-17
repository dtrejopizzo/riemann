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
    defect = norm((h_actual - vals[0] * np.eye(h_actual.shape[0])) @ xi)
    return h_actual, vals[0], idx.astype(int), d, L, xi, defect


def local_basis(off_nodes, crit_nodes, d, L):
    cols = []
    for k in crit_nodes:
        gamma = (-1j * k).real
        dd = np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
        for beta in off_nodes:
            denom = np.array([dm * dm + beta * beta for dm in d], dtype=complex)
            for r in [0, 1, 2]:
                cols.append(dd.copy() if r == 0 else dd / (denom ** r))
        cols.append((d ** 2) * dd)
    return np.column_stack(cols)


def source_vector(b, off_nodes, crit_nodes, d, L):
    total = np.zeros_like(d, dtype=complex)
    for k in crit_nodes:
        gamma = (-1j * k).real
        coeff = pi_kernel(b, k, off_nodes)
        total += coeff * np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
    return total


def image_projector(mat, tol=1e-10):
    u, s, _ = svd(mat, full_matrices=True)
    rank = int(np.sum(s > tol * s[0])) if len(s) else 0
    return u[:, :rank], u[:, rank:], rank


def run():
    print("E73.021 dual residual split probe")
    print("Residual after Image((C_E-mu)P) projection split into xi and xi-orthogonal parts.")
    print(
        " lam     L   dim rank  eigDef      |res|/|S|    xiShare     expXi "
        "   orthShare  cokerDim"
    )
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (18, 22)]:
        h, mu, idx, d, L, xi, eig_defect = setup_full(lam, n_modes)
        prim = local_basis(off_nodes, crit_nodes, d, L)
        image = (h - mu * np.eye(h.shape[0])) @ prim
        u_img, u_coker, rank = image_projector(image)
        for b in off_nodes:
            src = source_vector(b, off_nodes, crit_nodes, d, L)
            resid = src - u_img @ (u_img.conj().T @ src)
            xi_coeff = np.vdot(xi, resid)
            xi_part = xi * xi_coeff
            orth = resid - xi_part
            rel_res = norm(resid) / max(norm(src), 1e-30)
            xi_share = norm(xi_part) / max(norm(resid), 1e-30)
            orth_share = norm(orth) / max(norm(resid), 1e-30)
            exp_xi = abs(cmath.exp(b.real * L) * xi_coeff)
            print(
                f"{lam:4d} {L:7.3f} {len(idx):5d} {rank:4d} {eig_defect:8.1e} "
                f"{rel_res:12.2e} {xi_share:10.2e} {exp_xi:10.2e} "
                f"{orth_share:11.2e} {u_coker.shape[1]:9d}"
            )


if __name__ == "__main__":
    run()
