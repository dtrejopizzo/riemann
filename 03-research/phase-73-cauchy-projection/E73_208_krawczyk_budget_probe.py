#!/usr/bin/env python3
import sys

import mpmath as mp
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_206_hp_matrix_entry_probe import hp_matrix  # noqa: E402
from E73_207_hp_bordered_eigen_probe import mat_vec, mp_norm  # noqa: E402


mp.mp.dps = 100


def spectral_norm_mp(A):
    # A is small in this audit; convert A^T A to mp symmetric eigenvalues.
    B = A.T * A
    vals, _ = mp.eigsy(B)
    return mp.sqrt(max(vals))


def build_center(lam, n_modes):
    idx, L, mat_list = hp_matrix(lam, n_modes, include_arith=True)
    mat_list = [[mp.re(v) for v in row] for row in mat_list]
    H = mp.matrix(mat_list)
    vals, vecs = mp.eigsy(H)
    mu = vals[0]
    xi = [vecs[i, 0] for i in range(len(idx))]
    nrm = mp_norm(xi)
    xi = [v / nrm for v in xi]
    hx = mat_vec(mat_list, xi)
    jmax = max(range(len(xi)), key=lambda j: abs(xi[j]))
    ell = [mp.mpf("0") for _ in xi]
    ell[jmax] = 1 / xi[jmax]
    n = len(xi)
    J = mp.matrix(n + 1)
    for i in range(n):
        for j in range(n):
            J[i, j] = H[i, j] - (mu if i == j else 0)
        J[i, n] = -xi[i]
    for j in range(n):
        J[n, j] = ell[j]
    J[n, n] = 0
    F = mp.matrix([hx[i] - mu * xi[i] for i in range(n)] + [sum(ell[j] * xi[j] for j in range(n)) - 1])
    step_vec = mp.lu_solve(J, F)
    Y = J ** -1
    return L, n, mp_norm([step_vec[i] for i in range(n + 1)]), spectral_norm_mp(Y)


def admissible(Ynorm, step, epsH, safety=mp.mpf("0.5")):
    # Krawczyk sufficient bound:
    # step + Y epsH + Y(epsH+2rho)rho < rho.
    # Search for a rho satisfying the inequality with a safety factor.
    lower = max(2 * (step + Ynorm * epsH), mp.mpf("1e-300"))
    rho = lower
    for _ in range(200):
        lhs = step + Ynorm * epsH + Ynorm * (epsH + 2 * rho) * rho
        if lhs < safety * rho:
            return rho, lhs / rho
        rho *= 2
        if rho > 1:
            return None, None
    return None, None


def max_eps_for_success(Ynorm, step):
    lo = mp.mpf("0")
    hi = mp.mpf("1")
    while admissible(Ynorm, step, hi)[0] is not None:
        hi *= 2
        if hi > 1:
            break
    for _ in range(160):
        mid = (lo + hi) / 2
        if admissible(Ynorm, step, mid)[0] is not None:
            lo = mid
        else:
            hi = mid
    rho, ratio = admissible(Ynorm, step, lo)
    return lo, rho, ratio


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.208 Krawczyk budget audit")
    print("Point high-precision center plus explicit radius inequality.")
    print(" lam     L    N  dim  stepB  YnormB  epsHmaxB   rhoB  ratio")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        L, n, step, Ynorm = build_center(lam, n_modes)
        epsH, rho, ratio = max_eps_for_success(Ynorm, step)
        print(
            f"{lam:4d} {L:7.3f} {n_modes:4d} {n:4d}"
            f" {bexp(step, L):7.2f} {bexp(Ynorm, L):7.2f}"
            f" {bexp(epsH, L):9.2f} {bexp(rho, L):6.2f}"
            f" {float(ratio):6.3f}"
        )


if __name__ == "__main__":
    run()
