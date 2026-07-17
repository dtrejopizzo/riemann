#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, lstsq, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_003_critical_source_probe import dd_kernel  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402


def bexp(z, L):
    value = max(float(abs(complex(z))), 1e-300)
    return np.log(value) / np.log(L)


def setup(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    mu = vals[0]
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h.astype(complex), float(mu), idx.astype(int), d, L, xi.astype(complex)


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
                cols.append(dd / (denom**r))
                labels.append(("rat", ki, bi, r))
        for q in endpoint_powers:
            cols.append((d ** (2 * q)) * dd)
            labels.append(("endpoint", ki, -1, q))
    return np.column_stack(cols), labels


def orth_basis(mat, reltol):
    u, s, _vh = svd(mat, full_matrices=False)
    if len(s) == 0 or s[0] == 0:
        return np.zeros((mat.shape[0], 0), dtype=complex), s
    rank = int(np.sum(s > reltol * s[0]))
    return u[:, :rank], s


def cauchy0_quotient_projector(src_basis, labels, h, mu, off_nodes, crit_nodes, d, L):
    prim, _ = canonical_basis(off_nodes, crit_nodes, d, L, max_power=2, endpoint_powers=[1])
    image = (h - mu * np.eye(h.shape[0], dtype=complex)) @ prim

    coeff_cols = []
    image_rel = []
    for j in range(image.shape[1]):
        coeff, *_ = lstsq(src_basis, image[:, j], rcond=None)
        coeff_cols.append(coeff)
        image_rel.append(norm(image[:, j] - src_basis @ coeff) / max(norm(image[:, j]), 1e-30))
    coeff_action = np.column_stack(coeff_cols)

    principal = np.array([lab[0] != "endpoint" for lab in labels], dtype=bool)
    cauchy0_rows = [i for i, lab in enumerate(labels) if lab[0] == "cauchy0"]
    principal_indices = np.flatnonzero(principal)
    row_map = {orig: pos for pos, orig in enumerate(principal_indices)}

    m = coeff_action[principal, :]
    c = np.zeros((m.shape[0], len(cauchy0_rows)), dtype=complex)
    for j, orig in enumerate(cauchy0_rows):
        c[row_map[orig], j] = 1.0

    qm, _ = orth_basis(m, reltol=1e-6)
    qc, _ = orth_basis(c, reltol=1e-12)
    cross = qc.conj().T @ qm
    u, s, _vh = svd(cross, full_matrices=False)
    inter_rank = int(np.sum(s > 0.99))
    inter_in_c = qc @ u[:, :inter_rank] if inter_rank else np.zeros((c.shape[0], 0), dtype=complex)
    p_inter = inter_in_c @ inter_in_c.conj().T

    def project_cauchy0_coeff(coeff):
        pc = coeff[principal]
        cvec = np.array([coeff[i] for i in cauchy0_rows], dtype=complex)
        embedded = c @ cvec
        quot = embedded - p_inter @ embedded
        out = np.zeros_like(coeff)
        for orig, val in zip(principal_indices, quot):
            out[orig] = val
        return out

    return project_cauchy0_coeff, max(image_rel), inter_rank


def run():
    print("E73.278 APR-to-cauchy0 bridge probe")
    print("Fits rho=qH(I-P_w) in canonical source coordinates and compares scalar center")
    print("with the cauchy0 quotient component inherited from E73.167.")
    print(
        " lam      L gamma row fitRel imageRel intR centerB quotB remB "
        "quot/center rem/center"
    )
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (20, 24)]:
        h, mu, _idx, d, L, xi = setup(lam, n_modes)
        src_basis, labels = canonical_basis(off_nodes, crit_nodes, d, L, max_power=3, endpoint_powers=[1, 2])
        quot_project, image_rel, inter_rank = cauchy0_quotient_projector(
            src_basis, labels, h, mu, off_nodes, crit_nodes, d, L
        )
        for gamma in GAMMAS[:3]:
            q = cauchy_rows(-1j * gamma, d)
            r = np.eye(len(d), dtype=complex) - projector(q)
            for row in range(2):
                rho = q[row] @ h @ r
                coeff, *_ = lstsq(src_basis, rho, rcond=None)
                fit = src_basis @ coeff
                fit_rel = norm(rho - fit) / max(norm(rho), 1e-30)
                qcoeff = quot_project(coeff)
                quot_row = src_basis @ qcoeff
                rem_row = rho - quot_row
                center = rho @ xi
                quot_center = quot_row @ xi
                rem_center = rem_row @ xi
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row:3d}"
                    f" {fit_rel:7.1e} {image_rel:8.1e} {inter_rank:4d}"
                    f" {bexp(center, L):8.2f} {bexp(quot_center, L):7.2f}"
                    f" {bexp(rem_center, L):6.2f}"
                    f" {abs(quot_center)/max(abs(center),1e-300):10.2e}"
                    f" {abs(rem_center)/max(abs(center),1e-300):10.2e}"
                )


if __name__ == "__main__":
    run()
