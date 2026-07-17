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
    return np.log(max(float(abs(complex(z))), 1e-300)) / np.log(L)


def setup(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    mu = vals[0]
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h.astype(complex), float(mu), d, L, xi.astype(complex)


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


def orth_projector(mat, reltol):
    u, s, _vh = svd(mat, full_matrices=False)
    if len(s) == 0 or s[0] == 0:
        return np.zeros((mat.shape[0], mat.shape[0]), dtype=complex), 0, s
    rank = int(np.sum(s > reltol * s[0]))
    q = u[:, :rank]
    return q @ q.conj().T, rank, s


def quotient_data(src_basis, h, mu, off_nodes, crit_nodes, d, L):
    prim, _ = canonical_basis(off_nodes, crit_nodes, d, L, max_power=2, endpoint_powers=[1])
    image = (h - mu * np.eye(h.shape[0], dtype=complex)) @ prim
    coeff_cols = []
    image_rel = []
    for j in range(image.shape[1]):
        coeff, *_ = lstsq(src_basis, image[:, j], rcond=None)
        coeff_cols.append(coeff)
        image_rel.append(norm(image[:, j] - src_basis @ coeff) / max(norm(image[:, j]), 1e-30))
    action = np.column_stack(coeff_cols)
    p_img, rank_img, s_img = orth_projector(action, reltol=1e-6)
    p_src, rank_src, s_src = orth_projector(src_basis, reltol=1e-10)
    return action, p_img, rank_img, p_src, rank_src, max(image_rel), s_img, s_src


def sector_norms(coeff, labels):
    out = {}
    for val, lab in zip(coeff, labels):
        out.setdefault(lab[0], 0.0)
        out[lab[0]] += float(abs(val) ** 2)
    return {k: v**0.5 for k, v in out.items()}


def run():
    print("E73.279 coupled APR quotient probe")
    print("Projects rho=qH(I-P_w) to the fixed canonical quotient S_L/M_L.")
    print("class captures all sectors; small classPair would make COUPLED-APR-QUOT plausible.")
    print(
        " lam      L gamma row fitRel imageRel rS rM qDim centerB classB genB "
        "class/center gen/center c0 rat end"
    )
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20)]:
        h, mu, d, L, xi = setup(lam, n_modes)
        src_basis, labels = canonical_basis(off_nodes, crit_nodes, d, L, max_power=3, endpoint_powers=[1, 2])
        action, p_img, rank_img, _p_src, rank_src, image_rel, _s_img, _s_src = quotient_data(
            src_basis, h, mu, off_nodes, crit_nodes, d, L
        )
        qdim = rank_src - rank_img
        for gamma in GAMMAS[:3]:
            q = cauchy_rows(-1j * gamma, d)
            r = np.eye(len(d), dtype=complex) - projector(q)
            for row in range(2):
                rho = q[row] @ h @ r
                coeff, *_ = lstsq(src_basis, rho, rcond=None)
                fit = src_basis @ coeff
                fit_rel = norm(rho - fit) / max(norm(rho), 1e-30)
                class_coeff = coeff - p_img @ coeff
                gen_coeff = p_img @ coeff
                class_row = src_basis @ class_coeff
                gen_row = src_basis @ gen_coeff
                center = rho @ xi
                class_pair = class_row @ xi
                gen_pair = gen_row @ xi
                sectors = sector_norms(class_coeff, labels)
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row:3d}"
                    f" {fit_rel:7.1e} {image_rel:8.1e} {rank_src:3d} {rank_img:3d} {qdim:4d}"
                    f" {bexp(center,L):8.2f} {bexp(class_pair,L):7.2f}"
                    f" {bexp(gen_pair,L):6.2f}"
                    f" {abs(class_pair)/max(abs(center),1e-300):10.2e}"
                    f" {abs(gen_pair)/max(abs(center),1e-300):10.2e}"
                    f" {sectors.get('cauchy0',0.0):.1e}"
                    f" {sectors.get('rat',0.0):.1e}"
                    f" {sectors.get('endpoint',0.0):.1e}"
                )


if __name__ == "__main__":
    run()
