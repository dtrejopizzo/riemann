#!/usr/bin/env python3
"""Audit whether the observed Cauchy lock is rank/parity/precision driven."""

import sys

import numpy as np
from numpy.linalg import eigh, matrix_rank, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")

from E71_9_relative_arch_background_probe import build  # noqa: E402


# Evaluation ordinates only.  Neither build() nor this audit's construction
# passes them into the CCM matrix.
EVAL_GAMMAS = (14.134725141734694, 21.022039638771555)


def parity_matrix(n):
    return np.fliplr(np.eye(n))


def normalized_cauchy(gamma, d, xi):
    r = 1.0 / (gamma - d)
    return abs(np.dot(r, xi)) / norm(r)


def analyze(lam, n_modes):
    full, idx, L = build(lam, n_modes, include_arith=True)
    arch, idx0, L0 = build(lam, n_modes, include_arith=False)
    if not np.array_equal(idx, idx0) or L != L0:
        raise RuntimeError("arithmetic and archimedean builds use different meshes")

    prime = arch - full
    vals, vecs = eigh(full)
    xi = vecs[:, 0]
    mu = vals[0]
    gap = vals[1] - vals[0]
    residual = norm(full @ xi - mu * xi)

    J = parity_matrix(len(idx))
    parity_defect = norm(full @ J - J @ full) / max(norm(full), 1e-300)
    parity_sign = 1.0 if norm(J @ xi - xi) <= norm(J @ xi + xi) else -1.0
    xi_par = xi + parity_sign * J @ xi
    xi_par /= norm(xi_par)
    parity_residual = norm(full @ xi_par - mu * xi_par)

    _, singulars, vh = svd(full)
    tol = singulars[0] * len(idx) * np.finfo(float).eps
    rank = matrix_rank(full, tol=tol)
    prime_rank = matrix_rank(prime)
    d = 2.0 * np.pi * idx / L
    locks = [normalized_cauchy(gamma, d, xi) for gamma in EVAL_GAMMAS]
    neighbors = [normalized_cauchy(gamma + 0.125, d, xi) for gamma in EVAL_GAMMAS]
    null_basis = vh[rank:, :].T

    def kernel_overlap(t):
        r = 1.0 / (t - d)
        return norm(null_basis.T @ r) / norm(r)

    kernel_locks = [kernel_overlap(gamma) for gamma in EVAL_GAMMAS]
    kernel_neighbors = [kernel_overlap(gamma + 0.125) for gamma in EVAL_GAMMAS]

    return {
        "lam": lam,
        "N": n_modes,
        "dim": len(idx),
        "L": L,
        "mu": mu,
        "gap": gap,
        "rank": rank,
        "prime_rank": prime_rank,
        "smin": singulars[-1],
        "res": residual,
        "pres": parity_residual,
        "pdef": parity_defect,
        "q0": locks[0],
        "q1": locks[1],
        "n0": neighbors[0],
        "n1": neighbors[1],
        "k0": kernel_locks[0],
        "k1": kernel_locks[1],
        "kn0": kernel_neighbors[0],
        "kn1": kernel_neighbors[1],
    }


def run():
    print("P76.001 dependency/rank audit")
    print("H construction receives no zero ordinates; gammas are evaluation-only.")
    print(
        "lam N dim     L       mu        gap rank pRank      smin"
        "       eigRes       parRes   parityDef      q(g1)      q(g2)"
        "    q(g1+.125) q(g2+.125)    K(g1)      K(g2)"
        "    K(g1+.125) K(g2+.125)"
    )
    cases = ((6, 8), (8, 10), (10, 12), (12, 16), (12, 24))
    for case in cases:
        a = analyze(*case)
        print(
            f"{a['lam']:3d} {a['N']:2d} {a['dim']:3d} {a['L']:6.3f}"
            f" {a['mu']:10.3e} {a['gap']:10.3e} {a['rank']:4d}"
            f" {a['prime_rank']:5d} {a['smin']:10.3e} {a['res']:12.3e}"
            f" {a['pres']:12.3e} {a['pdef']:11.3e} {a['q0']:10.3e}"
            f" {a['q1']:10.3e} {a['n0']:13.3e} {a['n1']:13.3e}"
            f" {a['k0']:10.3e} {a['k1']:10.3e} {a['kn0']:13.3e}"
            f" {a['kn1']:13.3e}"
        )


if __name__ == "__main__":
    run()
