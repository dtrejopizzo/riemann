#!/usr/bin/env python3
import cmath
import sys

import numpy as np
from numpy.linalg import eigh, lstsq, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_003_critical_source_probe import dd_kernel, pi_kernel  # noqa: E402


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    phase = np.sign(np.real(np.vdot(xi, np.ones_like(xi))))
    if phase == 0:
        phase = 1.0
    xi = phase * xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h_actual, vals[0], idx.astype(int), d, L, xi


def canonical_basis(off_nodes, crit_nodes, d, L, max_power, endpoint_powers):
    cols = []
    labels = []
    for ki, k in enumerate(crit_nodes):
        gamma = (-1j * k).real
        dd = np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
        cols.append(dd)
        labels.append(("cauchy0", ki, -1, 0))
        for bi, beta in enumerate(off_nodes):
            denom = np.array([dm * dm + beta * beta for dm in d], dtype=complex)
            for r in range(1, max_power + 1):
                cols.append(dd / (denom ** r))
                labels.append(("rat", ki, bi, r))
        for q in endpoint_powers:
            cols.append((d ** (2 * q)) * dd)
            labels.append(("endpoint", ki, -1, q))
    return np.column_stack(cols), labels


def quotient_projector(lam, n_modes):
    h, mu, idx, d, L, xi = setup(lam, n_modes)
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    prim, _ = canonical_basis(off_nodes, crit_nodes, d, L, max_power=2, endpoint_powers=[1])
    src_basis, labels = canonical_basis(off_nodes, crit_nodes, d, L, max_power=3, endpoint_powers=[1, 2])
    principal = np.array([lab[0] != "endpoint" for lab in labels], dtype=bool)
    cauchy0_rows = [i for i, lab in enumerate(labels) if lab[0] == "cauchy0"]
    principal_indices = np.flatnonzero(principal)
    row_map = {orig: pos for pos, orig in enumerate(principal_indices)}

    image = (h - mu * np.eye(h.shape[0])) @ prim
    coeff_cols = []
    image_rel = []
    for j in range(image.shape[1]):
        coeff, *_ = lstsq(src_basis, image[:, j], rcond=None)
        coeff_cols.append(coeff)
        image_rel.append(norm(image[:, j] - src_basis @ coeff) / max(norm(image[:, j]), 1e-30))
    coeff_action = np.column_stack(coeff_cols)
    m = coeff_action[principal, :]

    c = np.zeros((m.shape[0], len(cauchy0_rows)), dtype=complex)
    for j, orig in enumerate(cauchy0_rows):
        c[row_map[orig], j] = 1.0

    u_m, s_m, _ = svd(m, full_matrices=False)
    rank_m = int(np.sum(s_m > 1e-6 * s_m[0])) if len(s_m) else 0
    q_m = u_m[:, :rank_m]
    u, s, _ = svd(c.conj().T @ q_m, full_matrices=False)
    inter_dim = int(np.sum(s > 0.99))
    inter_basis = u[:, :inter_dim]
    p_inter = inter_basis @ inter_basis.conj().T if inter_dim else np.zeros((5, 5), dtype=complex)
    p_q = np.eye(5, dtype=complex) - p_inter

    g_vals = []
    for k in crit_nodes:
        gamma = (-1j * k).real
        dd = np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
        g_vals.append(np.vdot(xi, dd))
    return L, max(image_rel), inter_dim, p_q, np.array(g_vals, dtype=complex), off_nodes, crit_nodes


def bexp(x, L):
    return np.log(max(x, 1e-300)) / np.log(L)


def run():
    print("E73.170 quotient budget probe")
    print("Measures QUOT-NORM versus exact QUOT-PAIR on the quotient.")
    print(" lam     L inter imageRel row  piQB  gQB normB pairB lossB pairVal normVal")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (20, 24), (24, 28), (32, 36)]:
        L, image_rel, inter_dim, p_q, g, off_nodes, crit_nodes = quotient_projector(lam, n_modes)
        gq = p_q @ g
        gqn = norm(gq)
        for row_idx, b in enumerate(off_nodes):
            pi = np.array([pi_kernel(b, k, off_nodes) for k in crit_nodes], dtype=complex)
            piq = p_q @ pi
            norm_val = abs(cmath.exp(b.real * L)) * norm(piq) * gqn
            pair_val = abs(cmath.exp(b.real * L) * np.sum(piq * gq))
            loss = norm_val / max(pair_val, 1e-300)
            print(
                f"{lam:4d} {L:7.3f} {inter_dim:5d} {image_rel:8.1e} {row_idx:3d} "
                f"{bexp(norm(piq), L):6.2f} {bexp(gqn, L):6.2f} "
                f"{bexp(norm_val, L):6.2f} {bexp(pair_val, L):6.2f} {bexp(loss, L):6.2f} "
                f"{pair_val:9.2e} {norm_val:9.2e}"
            )


if __name__ == "__main__":
    run()
