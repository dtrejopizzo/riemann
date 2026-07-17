#!/usr/bin/env python3
import sys

import mpmath as mp
import numpy as np
from numpy.linalg import inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_206_hp_matrix_entry_probe import hp_matrix  # noqa: E402


# Certified rho exponents from E73.217, keyed by (lambda, Csec).
RHO_B = {
    (8, "1"): -55.67,
    (8, "1e6"): -45.98,
    (10, "1"): -52.16,
    (10, "1e6"): -43.11,
    (12, "1"): -49.87,
    (12, "1e6"): -41.26,
}


def cauchy_rows(w, d):
    return np.vstack([1.0 / (w + 1j * d), 1.0 / (-w + 1j * d)])


def projector(q):
    return q.conj().T @ inv(q @ q.conj().T) @ q


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.218 Cauchy projection radius budget")
    print("Propagates certified eigenline radius through eta=(I-P_w)xi.")
    print(" lam     L    N  dim Csec gamma  ||I-P||B rhoXiB rhoEtaB")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        idx, L, _mat = hp_matrix(lam, n_modes, include_arith=True)
        d = 2.0 * np.pi * idx / L
        dim = len(idx)
        for csec in ["1", "1e6"]:
            rho = L ** RHO_B[(lam, csec)]
            for gamma in GAMMAS[:2]:
                q = cauchy_rows(-1j * gamma, d)
                p = projector(q)
                op = norm(np.eye(len(d)) - p, 2)
                rho_eta = mp.mpf(str(op)) * rho
                print(
                    f"{lam:4d} {L:7.3f} {n_modes:4d} {dim:4d}"
                    f" {str(csec):>4s} {gamma:7.2f}"
                    f" {bexp(op, L):8.2f} {bexp(rho, L):7.2f}"
                    f" {bexp(rho_eta, L):8.2f}"
                )


if __name__ == "__main__":
    run()
