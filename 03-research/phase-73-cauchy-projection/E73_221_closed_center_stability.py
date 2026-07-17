#!/usr/bin/env python3
import sys

import mpmath as mp
import numpy as np
from numpy.linalg import inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_182_closed_series_arch_probe import packet_modes  # noqa: E402
import E73_201_mp_finite_assembly_probe as mpff  # noqa: E402


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
    return idx.astype(int), d, L, xi


def closed_center_at_dps(const, linear, L, lam, dps, R=80):
    old = mp.mp.dps
    mp.mp.dps = dps
    try:
        return mpff.mp_arch_closed_digamma(const, linear, L, R) - mpff.mp_prime_modes(
            const, linear, L, lam
        )
    finally:
        mp.mp.dps = old


def bexp(z, L):
    return np.log(max(float(abs(complex(z))), 1e-300)) / np.log(L)


def run():
    print("E73.221 closed-center stability audit")
    print("Compares dps=80,100,140 for C_a=A_L^digamma-P_L.")
    print(" lam     L    N gamma row centerB diff80B diff100B rel80 rel100")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (ident - projector(q)) @ xi
            for row_id in range(2):
                row = q[row_id]
                const, linear = packet_modes(row, idx, d, eta, L)
                c80 = closed_center_at_dps(const, linear, L, lam, 80)
                c100 = closed_center_at_dps(const, linear, L, lam, 100)
                c140 = closed_center_at_dps(const, linear, L, lam, 140)
                d80 = c80 - c140
                d100 = c100 - c140
                rel80 = abs(complex(d80)) / max(abs(complex(c140)), 1e-300)
                rel100 = abs(complex(d100)) / max(abs(complex(c140)), 1e-300)
                print(
                    f"{lam:4d} {L:7.3f} {n_modes:4d} {gamma:7.2f} {row_id:3d}"
                    f" {bexp(c140, L):7.2f} {bexp(d80, L):7.2f}"
                    f" {bexp(d100, L):8.2f} {rel80:7.1e} {rel100:8.1e}"
                )


if __name__ == "__main__":
    run()
