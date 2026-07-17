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


def setup(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    mu = vals[0]
    xi = vecs[:, 0].astype(complex)
    if xi[len(xi) // 2].real < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h.astype(complex), float(mu), idx.astype(int), d, float(L), xi


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


def orth_basis(mat, reltol=1e-8):
    u, s, _ = svd(mat, full_matrices=False)
    if len(s) == 0 or s[0] == 0:
        return np.zeros((mat.shape[0], 0), dtype=complex), s
    rank = int(np.sum(s > reltol * s[0]))
    return u[:, :rank], s


def quotient_model(h, mu, d, L):
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    prim, _ = canonical_basis(off_nodes, crit_nodes, d, L, max_power=2, endpoint_powers=[1])
    src_basis, labels = canonical_basis(off_nodes, crit_nodes, d, L, max_power=3, endpoint_powers=[1, 2])
    principal = np.array([lab[0] != "endpoint" for lab in labels], dtype=bool)
    cauchy0_rows = [i for i, lab in enumerate(labels) if lab[0] == "cauchy0"]

    image = (h - mu * np.eye(h.shape[0], dtype=complex)) @ prim
    coeff_cols = []
    image_rel = []
    for j in range(image.shape[1]):
        coeff, *_ = lstsq(src_basis, image[:, j], rcond=None)
        coeff_cols.append(coeff)
        image_rel.append(norm(image[:, j] - src_basis @ coeff) / max(norm(image[:, j]), 1e-300))
    coeff_action = np.column_stack(coeff_cols)
    m = coeff_action[principal, :]
    qm, _ = orth_basis(m, reltol=1e-6)

    principal_indices = np.flatnonzero(principal)
    row_map = {orig: pos for pos, orig in enumerate(principal_indices)}
    c_embed = np.zeros((len(principal_indices), len(cauchy0_rows)), dtype=complex)
    for j, orig in enumerate(cauchy0_rows):
        c_embed[row_map[orig], j] = 1.0

    pm = qm @ qm.conj().T if qm.shape[1] else np.zeros((m.shape[0], m.shape[0]), dtype=complex)
    quotient_cols = (np.eye(m.shape[0], dtype=complex) - pm) @ c_embed
    qbasis, qsing = orth_basis(quotient_cols, reltol=1e-7)
    return src_basis, labels, principal, cauchy0_rows, pm, qbasis, max(image_rel)


def bexp(z, L):
    return np.log(max(float(abs(complex(z))), 1e-300)) / np.log(L)


def bridge_metrics(rho, src_basis, labels, principal, cauchy0_rows, pm, qbasis):
    coeff, *_ = lstsq(src_basis, rho, rcond=None)
    fit_rel = norm(rho - src_basis @ coeff) / max(norm(rho), 1e-300)
    principal_coeff = coeff[principal]
    cauchy_coeff = np.array([coeff[i] for i in cauchy0_rows], dtype=complex)

    principal_indices = np.flatnonzero(principal)
    row_map = {orig: pos for pos, orig in enumerate(principal_indices)}
    cauchy_principal = np.zeros_like(principal_coeff)
    for j, orig in enumerate(cauchy0_rows):
        cauchy_principal[row_map[orig]] = cauchy_coeff[j]

    eye = np.eye(pm.shape[0], dtype=complex)
    residual_principal = (eye - pm) @ principal_coeff
    residual_cauchy = (eye - pm) @ cauchy_principal
    bridge_error = (eye - pm) @ (principal_coeff - cauchy_principal)
    quotient_projection = qbasis @ (qbasis.conj().T @ residual_principal) if qbasis.shape[1] else 0.0

    base = max(norm(residual_principal), 1e-300)
    return (
        fit_rel,
        norm(residual_principal),
        norm(residual_cauchy) / base,
        norm(bridge_error) / base,
        norm(residual_principal - quotient_projection) / base,
    )


def run():
    print("E74.11 algebraic quotient bridge probe")
    print("Tests whether APR rho=qH(I-P) reduces, modulo left coborders, to the canonical cauchy0 quotient.")
    print("bridgeRel close to 0 would support the E73.277 N1 bridge; large values falsify direct bridge closure.")
    print(" lam      L gamma row fitRel imageRel resB cauchyRel bridgeRel quotMiss")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (20, 24)]:
        h, mu, idx, d, L, xi = setup(lam, n_modes)
        src_basis, labels, principal, cauchy0_rows, pm, qbasis, image_rel = quotient_model(h, mu, d, L)
        eye = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            rproj = eye - projector(q)
            for row_id in range(2):
                rho = q[row_id] @ h @ rproj
                fit_rel, res_norm, cauchy_rel, bridge_rel, quot_miss = bridge_metrics(
                    rho, src_basis, labels, principal, cauchy0_rows, pm, qbasis
                )
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {fit_rel:7.1e} {image_rel:8.1e}"
                    f" {bexp(res_norm, L):5.2f}"
                    f" {cauchy_rel:9.2e} {bridge_rel:9.2e} {quot_miss:8.2e}"
                )


if __name__ == "__main__":
    run()
