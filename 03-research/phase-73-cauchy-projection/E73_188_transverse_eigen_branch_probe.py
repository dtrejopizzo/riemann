#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h_actual, vals[0], d, L, xi


def cauchy_rows(w, d):
    return np.vstack([1.0 / (w + 1j * d), 1.0 / (-w + 1j * d)])


def orthogonal_projector_from_rows(q):
    gram = q @ q.conj().T
    return q.conj().T @ inv(gram) @ q


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.188 transverse eigen-branch")
    print("Verifies QH(I-P)xi = (mu I - QHQ*(QQ*)^-1)Qxi and Q(I-P)xi=0.")
    print(" lam     L gamma  kerB directB branchB errB hB aNormB")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24), (24, 28), (32, 36)]:
        hmat, mu, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(d), dtype=complex)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            proj = orthogonal_projector_from_rows(q)
            eta = (ident - proj) @ xi
            h = q @ xi
            gram = q @ q.conj().T
            aq = q @ hmat @ q.conj().T @ inv(gram)

            direct = q @ (hmat @ eta)
            branch = (mu * np.eye(2) - aq) @ h
            err = norm(direct - branch)
            ker = norm(q @ eta)
            anorm = norm(aq, 2)
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {bexp(ker, L):6.2f}"
                f" {bexp(norm(direct), L):8.2f}"
                f" {bexp(norm(branch), L):8.2f}"
                f" {bexp(err, L):6.2f}"
                f" {bexp(norm(h), L):6.2f}"
                f" {bexp(anorm, L):7.2f}"
            )


if __name__ == "__main__":
    run()
