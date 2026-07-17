#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import det, norm, solve, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_246_quotient_coordinate_audit import quotient_defects, rank_from_svd  # noqa: E402
from E73_248_symbolic_pivot_rule_probe import best_minor_rule  # noqa: E402


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def rowspace_basis(rows, tol=1e-10):
    _u, s, vh = svd(rows, full_matrices=False)
    if len(s) == 0:
        return rows[:0]
    rank = int(np.sum(s > tol * s[0]))
    return vh[:rank, :]


def project_row(row, basis):
    if basis.shape[0] == 0:
        return np.zeros_like(row)
    return (row @ basis.conj().T) @ basis


def run():
    print("E73.251 coordinate functional probe")
    print("For max-minor J*: z_j = m_j xi, M=D_J^{-1}D_Q.")
    print(
        " lam      L pow pivIdx              row rankE zMaxB absCeilB gainB "
        "mNormB relDistB rowDistB moment0B moment1B"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20)]:
        for rat_power in [0, 1, 2]:
            H, idx, _d, L, mu, xi, D, _labels, _ranks = quotient_defects(
                lam, n_modes, rat_power
            )
            _u, s, _vh = svd(D, full_matrices=False)
            r = rank_from_svd(s)
            D = D[:r, :]
            piv = best_minor_rule(D, r)
            DJ = D[:, piv]
            M = solve(DJ, D)
            z = M @ xi
            abs_ceil = np.array([np.sum(np.abs(row * xi)) for row in M])
            m_norm = np.array([norm(row) for row in M])
            E = H - mu * np.eye(H.shape[0], dtype=complex)
            ebasis = rowspace_basis(E)
            row_dist = np.array([norm(row - project_row(row, ebasis)) for row in M])
            rel_dist = row_dist / np.maximum(m_norm, 1e-300)
            moment0 = np.array([abs(np.sum(row)) for row in M])
            moment1 = np.array([abs(np.sum(row * idx)) for row in M])
            gain = np.max(abs_ceil) / max(np.max(np.abs(z)), 1e-300)
            print(
                f"{lam:4d} {L:8.3f} {rat_power:3d}"
                f" {str([int(idx[j]) for j in piv]):>18s}"
                f" all {ebasis.shape[0]:5d}"
                f" {bexp(np.max(np.abs(z)), L):6.2f}"
                f" {bexp(np.max(abs_ceil), L):8.2f}"
                f" {bexp(gain, L):6.2f}"
                f" {bexp(np.max(m_norm), L):6.2f}"
                f" {bexp(np.max(rel_dist), L):8.2f}"
                f" {bexp(np.max(row_dist), L):8.2f}"
                f" {bexp(np.max(moment0), L):8.2f}"
                f" {bexp(np.max(moment1), L):8.2f}"
            )
            for j, row in enumerate(M):
                zj = z[j]
                ceilj = abs_ceil[j]
                print(
                    f"{'':4s} {'':8s} {'':3s}"
                    f" coord{j}"
                    f" {bexp(zj, L):8.2f}"
                    f" ceil {bexp(ceilj, L):8.2f}"
                    f" gain {bexp(ceilj / max(abs(zj), 1e-300), L):7.2f}"
                    f" relRow {bexp(rel_dist[j], L):8.2f}"
                )
            print("-")


if __name__ == "__main__":
    run()
