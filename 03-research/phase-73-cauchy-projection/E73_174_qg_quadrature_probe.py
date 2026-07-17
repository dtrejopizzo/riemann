#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import eigh, lstsq, norm, svd
from scipy.integrate import quad

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import GAMMA, LOG4PI, build, primes_upto  # noqa: E402
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

    rows = []
    for r in range(q_basis.shape[1]):
        avec = np.zeros_like(d, dtype=complex)
        for qj, k in zip(q_basis[:, r], crit_nodes):
            gamma = (-1j * k).real
            avec += np.conj(qj) * (1.0 - np.exp(1j * gamma * L)) / (-gamma - d)
        rows.append(avec)
    return max(image_rel), inter_dim, np.array(rows, dtype=complex)


def packet(a, idx, d, L, xi, y):
    return a @ (q_matrix_fast(idx, d, L, y) @ xi)


def packet_derivative0(a, idx, d, L, xi):
    h = min(1e-6, L * 1e-7)
    return (packet(a, idx, d, L, xi, h) - packet(a, idx, d, L, xi, 0.0)) / h


def arch_quadrature(a, idx, d, L, xi):
    q0 = packet(a, idx, d, L, xi, 0.0)
    dq0 = packet_derivative0(a, idx, d, L, xi)

    def qv(y):
        return packet(a, idx, d, L, xi, y)

    def wri(y):
        if y < 1e-8:
            return (dq0 + q0 / 2.0) / 2.0
        return (np.exp(y / 2.0) * qv(y) - q0) / (2.0 * np.sinh(y))

    w02_re, _ = quad(lambda y: np.real(qv(y) * (np.exp(y / 2.0) + np.exp(-y / 2.0))), 0, L, limit=300)
    w02_im, _ = quad(lambda y: np.imag(qv(y) * (np.exp(y / 2.0) + np.exp(-y / 2.0))), 0, L, limit=300)
    wra_re, _ = quad(lambda y: np.real(wri(y)), 0, L, limit=300)
    wra_im, _ = quad(lambda y: np.imag(wri(y)), 0, L, limit=300)
    w02 = w02_re + 1j * w02_im
    wra = wra_re + 1j * wra_im
    wrb = q0 * 0.5 * np.log(np.tanh(L / 2.0))
    wr = 0.5 * (LOG4PI + GAMMA) * q0 + wra + wrb
    return w02 - wr


def prime_quadrature(a, idx, d, L, xi, lam):
    total = 0j
    maxn = int(lam * lam)
    for p in primes_upto(maxn):
        lp = math.log(p)
        n = p
        k = 1
        while n <= maxn:
            total += lp * n ** -0.5 * packet(a, idx, d, L, xi, k * lp)
            if n > maxn // p:
                break
            n *= p
            k += 1
    return total


def bexp(x, L):
    return np.log(max(float(abs(x)), 1e-300)) / np.log(L)


def run():
    print("E73.174 QG quadrature form")
    print("Rebuilds Arch_r and Prime_r from the scalar packet B_r(y)=a_r Q(y) xi.")
    print(" lam     L imageRel form archErr primeErr matchB muqB packet0B")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18)]:
        h, h_arch, mu, idx, d, L, xi = setup(lam, n_modes)
        pmat = h_arch - h
        image_rel, _, rows = quotient_forms(h, mu, d, L)
        for r, a in enumerate(rows[:3]):
            arch_mat = a @ (h_arch @ xi)
            prime_mat = a @ (pmat @ xi)
            arch_int = arch_quadrature(a, idx, d, L, xi)
            prime_sum = prime_quadrature(a, idx, d, L, xi, lam)
            match = arch_int - prime_sum
            muq = mu * (a @ xi)
            arch_err = abs(arch_int - arch_mat) / max(abs(arch_mat), 1e-300)
            prime_err = abs(prime_sum - prime_mat) / max(abs(prime_mat), 1e-300)
            q0 = abs(packet(a, idx, d, L, xi, 0.0))
            print(
                f"{lam:4d} {L:7.3f} {image_rel:8.1e} {r:4d} "
                f"{arch_err:7.1e} {prime_err:8.1e} {bexp(match, L):7.2f} "
                f"{bexp(muq, L):6.2f} {bexp(q0, L):8.2f}"
            )


if __name__ == "__main__":
    run()
