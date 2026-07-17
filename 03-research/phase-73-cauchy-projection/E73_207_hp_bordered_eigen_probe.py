#!/usr/bin/env python3
import sys

import mpmath as mp
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_206_hp_matrix_entry_probe import hp_matrix  # noqa: E402


mp.mp.dps = 100


def mp_norm(vec):
    return mp.sqrt(sum(abs(v) ** 2 for v in vec))


def mat_vec(mat, vec):
    return [sum(mat[i][j] * vec[j] for j in range(len(vec))) for i in range(len(vec))]


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def audit(lam, n_modes):
    idx, L, mat_list = hp_matrix(lam, n_modes, include_arith=True)
    mat_list = [[mp.re(v) for v in row] for row in mat_list]
    H = mp.matrix(mat_list)
    vals, vecs = mp.eigsy(H)
    mu0 = vals[0]
    mu1 = vals[1]
    xi = [vecs[i, 0] for i in range(len(idx))]
    nrm = mp_norm(xi)
    xi = [v / nrm for v in xi]
    hx = mat_vec(mat_list, xi)
    res = mp_norm([hx[i] - mu0 * xi[i] for i in range(len(idx))])
    gap = mu1 - mu0
    # Build bordered residual step in mp arithmetic.
    jmax = max(range(len(xi)), key=lambda j: abs(xi[j]))
    ell = [mp.mpf("0") for _ in xi]
    ell[jmax] = 1 / xi[jmax]
    J = mp.matrix(len(idx) + 1)
    for i in range(len(idx)):
        for j in range(len(idx)):
            J[i, j] = mat_list[i][j] - (mu0 if i == j else 0)
        J[i, len(idx)] = -xi[i]
    for j in range(len(idx)):
        J[len(idx), j] = ell[j]
    J[len(idx), len(idx)] = 0
    F = mp.matrix([hx[i] - mu0 * xi[i] for i in range(len(idx))] + [sum(ell[j] * xi[j] for j in range(len(idx))) - 1])
    step = mp.lu_solve(J, F)
    return L, len(idx), mu0, gap, res, mp_norm([step[i] for i in range(len(idx) + 1)])


def run():
    print("E73.207 high-precision bordered eigen audit")
    print("Uses closed mp matrix entries and mp.eigsy.")
    print(" lam     L    N  dim    muB    gapB     resB    stepB")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        L, dim, mu, gap, res, step = audit(lam, n_modes)
        print(
            f"{lam:4d} {L:7.3f} {n_modes:4d} {dim:4d}"
            f" {bexp(mu, L):7.2f} {bexp(gap, L):7.2f}"
            f" {bexp(res, L):8.2f} {bexp(step, L):8.2f}"
        )


if __name__ == "__main__":
    run()
