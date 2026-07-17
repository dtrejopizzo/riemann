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
    return d, L, xi


def cauchy_rows(w, d):
    return np.vstack([1.0 / (w + 1j * d), 1.0 / (-w + 1j * d)])


def projector(q):
    return q.conj().T @ inv(q @ q.conj().T) @ q


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.191 endpoint rank-one source")
    print("Measures S_eta, S_q, and B_a'(0)=-(2/L)S_qS_eta.")
    print(" lam     L gamma row SetaB SqB prodB xiSumB parSumB etaNorm")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24), (24, 28), (32, 36)]:
        d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(d), dtype=complex)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            p = projector(q)
            eta = (ident - p) @ xi
            xip = p @ xi
            seta = np.sum(eta)
            xsum = np.sum(xi)
            psum = np.sum(xip)
            for j in range(2):
                sq = np.sum(q[j])
                prod = -(2.0 / L) * sq * seta
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:3d}"
                    f" {bexp(seta, L):6.2f} {bexp(sq, L):6.2f}"
                    f" {bexp(prod, L):6.2f}"
                    f" {bexp(xsum, L):7.2f} {bexp(psum, L):8.2f}"
                    f" {norm(eta):7.4f}"
                )


if __name__ == "__main__":
    run()
