#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import eigh, lstsq, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build, primes_upto  # noqa: E402
from E72_380_actual_packet_wwr_probe import q_matrix_fast  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_003_critical_source_probe import dd_kernel  # noqa: E402


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    h_arch, _, _ = build(lam, n_modes, include_arith=False)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    phase = np.sign(np.real(np.vdot(xi, np.ones_like(xi))))
    if phase == 0:
        phase = 1.0
    xi = phase * xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h_actual, h_arch, vals[0], idx.astype(int), d, L, xi


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


def quotient_forms(h, mu, d, L):
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

    # Each quotient scalar form ell_r(G) = a_r dot xi.
    rows = []
    for r in range(q_basis.shape[1]):
        avec = np.zeros_like(d, dtype=complex)
        for qj, k in zip(q_basis[:, r], crit_nodes):
            gamma = (-1j * k).real
            avec += np.conj(qj) * (1.0 - np.exp(1j * gamma * L)) / (-gamma - d)
        rows.append(avec)
    return max(image_rel), inter_dim, np.array(rows, dtype=complex)


def rowspace_decomposition(a, h, mu, xi):
    e = h - mu * np.eye(h.shape[0])
    # Solve e y ~= conjugate(a) in the Hermitian convention, so y^* e xi = 0.
    y, *_ = lstsq(e, np.conj(a), rcond=None)
    rebuilt = np.conj(e @ y)
    residual = a - rebuilt
    scalar = np.sum(a * xi)
    return norm(y), norm(residual), abs(scalar), norm(residual) / max(norm(a), 1e-300)


def prime_rows(lam, L):
    rows = []
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = math.log(p)
        n = p
        k = 1
        while n <= maxn:
            rows.append((n, lp * n ** -0.5, k * lp))
            if n > maxn // p:
                break
            n *= p
            k += 1
    return rows


def row_packet(a, idx, d, L, xi, y):
    q = q_matrix_fast(idx, d, L, y)
    return a @ (q @ xi)


def transformed_prime_size(a, idx, d, L, xi, lam):
    total = 0j
    abs_total = 0.0
    for _, weight, y in prime_rows(lam, L):
        val = weight * row_packet(a, idx, d, L, xi, y)
        total += val
        abs_total += abs(val)
    return abs(total), abs_total


def bexp(x, L):
    return np.log(max(float(abs(x)), 1e-300)) / np.log(L)


def run():
    print("E73.173 eigenline Cauchy-transform probe")
    print("Tests whether QG linear forms are controlled by the finite eigenline row equation.")
    print(" lam     L imageRel form qgB rowResB preB archB primeB muqB absErrB")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20)]:
        h, h_arch, mu, idx, d, L, xi = setup(lam, n_modes)
        pmat = h_arch - h
        image_rel, inter_dim, rows = quotient_forms(h, mu, d, L)
        for r, a in enumerate(rows[:3]):
            pre, row_res, scalar, rel = rowspace_decomposition(a, h, mu, xi)
            arch_val = a @ (h_arch @ xi)
            prime_val = a @ (pmat @ xi)
            muq = mu * (a @ xi)
            abs_err = abs((arch_val - prime_val) - muq)
            print(
                f"{lam:4d} {L:7.3f} {image_rel:8.1e} {r:4d} "
                f"{bexp(scalar, L):6.2f} {bexp(row_res, L):7.2f} "
                f"{bexp(pre, L):6.2f} {bexp(arch_val, L):7.2f} "
                f"{bexp(prime_val, L):7.2f} {bexp(muq, L):6.2f} {bexp(abs_err, L):7.2f}"
            )


if __name__ == "__main__":
    run()
