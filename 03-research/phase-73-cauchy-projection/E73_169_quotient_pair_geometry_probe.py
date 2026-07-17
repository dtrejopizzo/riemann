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


def quotient_basis(lam, n_modes):
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

    qm, sm, _ = svd(m, full_matrices=False)
    rank_m = int(np.sum(sm > 1e-6 * sm[0])) if len(sm) else 0
    qm = qm[:, :rank_m]
    qc = np.eye(5, dtype=complex)
    # Express M inside C coordinates by projecting principal image to cauchy0 coordinates.
    # The intersection basis is recovered from principal angles between C and M.
    # Since C is coordinate identity, use C^*M restricted to cauchy0 rows.
    c_in_principal = c
    u, s, vh = svd(c_in_principal.conj().T @ qm, full_matrices=False)
    inter_dim = int(np.sum(s > 0.99))
    inter_basis = u[:, :inter_dim]
    p_inter = inter_basis @ inter_basis.conj().T if inter_dim else np.zeros((5, 5), dtype=complex)
    p_q = np.eye(5, dtype=complex) - p_inter
    uq, sq, _ = svd(p_q, full_matrices=False)
    qbasis = uq[:, : int(np.sum(sq > 0.5))]

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
    return L, max(image_rel), inter_dim, qbasis, p_q, g_vals, pi_rows


def cos_abs(a, b):
    den = norm(a) * norm(b)
    return float(abs(np.vdot(a, b)) / den) if den else 0.0


def run():
    print("E73.169 quotient pair geometry probe")
    print("Coordinates Pi_Q and G_Q in the 3D quotient basis and measures angular avoidance.")
    print(" lam     L inter imageRel  |Gq|     rows: cos(PiQ,GQ)/|PiQ|/scalar")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (20, 24), (24, 28), (32, 36)]:
        L, image_rel, inter_dim, qbasis, p_q, g, pi_rows = quotient_basis(lam, n_modes)
        gq = qbasis.conj().T @ (p_q @ g)
        bits = []
        for b, pi in pi_rows:
            piq = qbasis.conj().T @ (p_q @ pi)
            cosv = cos_abs(piq, gq)
            quot_scalar = abs(cmath.exp(b.real * L) * np.sum((p_q @ pi) * g))
            bits.append(f"{cosv:.2f}/{norm(piq):.1e}/{quot_scalar:.1e}")
        print(
            f"{lam:4d} {L:7.3f} {inter_dim:5d} {image_rel:8.1e} "
            f"{norm(gq):8.1e} {'  '.join(bits)}"
        )


if __name__ == "__main__":
    run()
