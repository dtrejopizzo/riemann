#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import det, eigh, lstsq, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_003_critical_source_probe import dd_kernel  # noqa: E402


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


def orth_projector(mat, reltol=1e-6):
    u, s, _ = svd(mat, full_matrices=False)
    if len(s) == 0 or s[0] == 0:
        return np.zeros((mat.shape[0], 0), dtype=complex), s
    rank = int(np.sum(s > reltol * s[0]))
    return u[:, :rank], s


def local_objects(lam, n_modes):
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

    qm, _ = orth_projector(m, reltol=1e-6)
    qc, _ = orth_projector(c, reltol=1e-12)
    u, s, _ = svd(qc.conj().T @ qm, full_matrices=False)
    inter_dim = int(np.sum(s > 0.99))
    inter_basis = u[:, :inter_dim]
    p_inter = inter_basis @ inter_basis.conj().T if inter_dim else np.zeros((5, 5), dtype=complex)
    p_q = np.eye(5, dtype=complex) - p_inter

    g_stable = []
    g_herm = []
    dd_rel = []
    for k in crit_nodes:
        gamma = (-1j * k).real
        dd = np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
        stable = (1.0 - np.exp(1j * gamma * L)) * np.sum(xi / (-gamma - d))
        direct = np.sum(xi * dd)
        g_stable.append(stable)
        g_herm.append(np.vdot(xi, dd))
        dd_rel.append(abs(direct - stable) / max(abs(stable), 1e-30))
    return (
        L,
        max(image_rel),
        inter_dim,
        inter_basis,
        p_q,
        np.array(g_stable),
        np.array(g_herm),
        max(dd_rel),
    )


def wedge_distance(inter_basis, g):
    if inter_basis.shape[1] == 0:
        return norm(g), 0.0
    gram_i = inter_basis.conj().T @ inter_basis
    stacked = np.column_stack([inter_basis, g])
    gram_s = stacked.conj().T @ stacked
    base = abs(det(gram_i))
    wedge = abs(det(gram_s))
    return np.sqrt(max(wedge, 0.0) / max(base, 1e-300)), base


def bexp(x, L):
    return np.log(max(float(abs(x)), 1e-300)) / np.log(L)


def run():
    print("E73.171 QG wedge identity probe")
    print("Uses the bilinear source convention from E73.003/E72.396.")
    print("Uses the stable Cauchy form of DD on the natural mesh d_m L=2*pi*m.")
    print("Validates ||P_Q G||^2 = det Gram(I_L,G) / det Gram(I_L).")
    print(" lam     L inter imageRel    ddRel herm/bilin   qgNorm   wedge relErr    qgB")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (20, 24), (24, 28), (32, 36)]:
        L, image_rel, inter_dim, inter_basis, p_q, g, g_herm, dd_rel = local_objects(lam, n_modes)
        qg = norm(p_q @ g)
        wedge, _ = wedge_distance(inter_basis, g)
        rel = abs(qg - wedge) / max(qg, 1e-300)
        herm_ratio = norm(p_q @ g_herm) / max(qg, 1e-300)
        print(
            f"{lam:4d} {L:7.3f} {inter_dim:5d} {image_rel:8.1e} "
            f"{dd_rel:8.1e} {herm_ratio:10.2e} {qg:9.2e} "
            f"{wedge:9.2e} {rel:7.1e} {bexp(qg, L):7.2f}"
        )


if __name__ == "__main__":
    run()
