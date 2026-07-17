#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, lstsq, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_380_actual_packet_wwr_probe import q_matrix_fast  # noqa: E402
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


def quotient_coefficients(h, mu, d, L):
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

    _, si, vhi = svd(inter_basis.conj().T, full_matrices=True)
    rank_i = int(np.sum(si > 1e-10)) if len(si) else 0
    q_basis = vhi.conj().T[:, rank_i:]
    return max(image_rel), crit_nodes, q_basis


def transformed_row(z, d, L):
    return (1.0 - np.exp(z * L)) / (1j * z - d)


def packet_from_row(a, idx, d, L, xi, y):
    return a @ (q_matrix_fast(idx, d, L, y) @ xi)


def bexp(x, L):
    return np.log(max(float(abs(x)), 1e-300)) / np.log(L)


def run():
    print("E73.176 quotient packet linearity")
    print("Checks B_r(y)=sum_j conj(q_rj) B_{z_j}(y), z_j=i gamma_j.")
    print(" lam     L imageRel form rowRel pktRel b0B")
    ysamp = np.linspace(0.0, 1.0, 9)
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20)]:
        h, mu, idx, d, L, xi = setup(lam, n_modes)
        image_rel, crit_nodes, q_basis = quotient_coefficients(h, mu, d, L)
        for r in range(min(3, q_basis.shape[1])):
            a_combo = np.zeros_like(d, dtype=complex)
            rows = []
            for qj, z in zip(q_basis[:, r], crit_nodes):
                row = transformed_row(z, d, L)
                rows.append(row)
                a_combo += np.conj(qj) * row
            # Recompute via the E73 stable Cauchy formula.
            a_direct = np.zeros_like(d, dtype=complex)
            for qj, z in zip(q_basis[:, r], crit_nodes):
                gamma = (-1j * z).real
                a_direct += np.conj(qj) * (1.0 - np.exp(1j * gamma * L)) / (-gamma - d)
            row_rel = norm(a_combo - a_direct) / max(norm(a_direct), 1e-300)
            vals_direct = []
            vals_combo = []
            for u in ysamp:
                y = u * L
                vals_direct.append(packet_from_row(a_direct, idx, d, L, xi, y))
                vals_combo.append(
                    sum(
                        np.conj(qj) * packet_from_row(row, idx, d, L, xi, y)
                        for qj, row in zip(q_basis[:, r], rows)
                    )
                )
            vals_direct = np.array(vals_direct)
            vals_combo = np.array(vals_combo)
            pkt_rel = norm(vals_direct - vals_combo) / max(norm(vals_direct), 1e-300)
            b0 = abs(vals_direct[0])
            print(
                f"{lam:4d} {L:7.3f} {image_rel:8.1e} {r:4d} "
                f"{row_rel:7.1e} {pkt_rel:7.1e} {bexp(b0, L):6.2f}"
            )


if __name__ == "__main__":
    run()
