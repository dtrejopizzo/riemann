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
    cross = qc.conj().T @ qm
    u, s, vh = svd(cross, full_matrices=False)
    # Intersection directions in C coordinates are the left singular vectors with singular value near 1.
    inter_dim = int(np.sum(s > 0.99))
    inter_basis = u[:, :inter_dim]
    p_inter = inter_basis @ inter_basis.conj().T if inter_dim else np.zeros((5, 5), dtype=complex)
    p_q = np.eye(5, dtype=complex) - p_inter

    g_vals = []
    for k in crit_nodes:
        gamma = (-1j * k).real
        dd = np.array([dd_kernel(-gamma, dm, L) for dm in d], dtype=complex)
        g_vals.append(np.vdot(xi, dd))
    g_vals = np.array(g_vals, dtype=complex)

    pi_rows = []
    for b in off_nodes:
        pi_vec = np.array([pi_kernel(b, k, off_nodes) for k in crit_nodes], dtype=complex)
        pi_rows.append((b, pi_vec))
    return L, max(image_rel), s, p_q, g_vals, pi_rows


def safe_ratio(a, b):
    return a / max(b, 1e-300)


def run():
    print("E73.168 quotient dual probe")
    print("Measures the dual cancelled-Cauchy vector G_K after quotient projection P_Q,L.")
    print(" lam     L inter imageRel  |PQG|/|G|  |PIG| rows: scalarRatio maxPiQ")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (20, 24), (24, 28), (32, 36)]:
        L, image_rel, angles, p_q, g, pi_rows = local_objects(lam, n_modes)
        pqg = p_q @ g
        g_ratio = norm(pqg) / max(norm(g), 1e-30)
        row_bits = []
        max_piq = 0.0
        for b, pi_vec in pi_rows:
            piq = p_q @ pi_vec
            max_piq = max(max_piq, norm(piq) / max(norm(pi_vec), 1e-30))
            full = abs(cmath.exp(b.real * L) * np.sum(pi_vec * g))
            quot = abs(cmath.exp(b.real * L) * np.sum(piq * g))
            row_bits.append(f"{safe_ratio(quot, full):.2e}")
        print(
            f"{lam:4d} {L:7.3f} {int(np.sum(angles > 0.99)):5d} {image_rel:8.1e} "
            f"{g_ratio:9.2e} {norm(pqg):9.2e} {'/'.join(row_bits):>24s} {max_piq:8.2e}"
        )


if __name__ == "__main__":
    run()
