#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_182_closed_series_arch_probe import packet_modes  # noqa: E402
from E73_201_mp_finite_assembly_probe import mp_arch_closed_digamma, mp_prime_modes  # noqa: E402


def cauchy_rows(w, d):
    return np.vstack([1.0 / (w + 1j * d), 1.0 / (-w + 1j * d)])


def projector(q):
    return q.conj().T @ inv(q @ q.conj().T) @ q


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return H, idx.astype(int), d, L, xi


def closed_center(row, idx, d, eta, L, lam):
    const, linear = packet_modes(row, idx, d, eta, L)
    return mp_arch_closed_digamma(const, linear, L, 80) - mp_prime_modes(const, linear, L, lam)


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.220 closed digamma center check")
    print("Compares C_a=A_L^digamma-P_L against q_a H eta at the E73.219 center.")
    print(" lam     L    N gamma row matrixB closedB errB relErr")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        H, idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (ident - projector(q)) @ xi
            for row_id in range(2):
                row = q[row_id]
                matrix = row @ (H @ eta)
                closed = closed_center(row, idx, d, eta, L, lam)
                err = complex(closed) - matrix
                rel = abs(err) / max(abs(matrix), 1e-300)
                print(
                    f"{lam:4d} {L:7.3f} {n_modes:4d} {gamma:7.2f} {row_id:3d}"
                    f" {bexp(matrix, L):7.2f} {bexp(closed, L):7.2f}"
                    f" {bexp(err, L):7.2f} {rel:8.1e}"
                )


if __name__ == "__main__":
    run()
