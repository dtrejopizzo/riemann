#!/usr/bin/env python3
"""Separate directional cancellation from the eigensolver precision floor."""

import sys

import mpmath as mp
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402


def mp_matrix(a):
    return mp.matrix([[mp.mpc(complex(z).real, complex(z).imag) for z in row] for row in a])


def mp_col(a):
    return mp.matrix([mp.mpc(complex(z).real, complex(z).imag) for z in a])


def mp_norm(v):
    return mp.sqrt(sum(abs(v[j]) ** 2 for j in range(v.rows)))


def sci(x):
    return mp.nstr(x, 6, min_fixed=0, max_fixed=0)


def run_case(lam, n_modes, gamma):
    h, idx, L = build(lam, n_modes, include_arith=True)
    d = 2.0 * np.pi * idx / L
    q = cauchy_rows(-1j * gamma, d)
    r = np.eye(len(idx), dtype=complex) - projector(q)

    vals, vecs = eigh(h)
    mu64 = vals[0]
    xi64 = vecs[:, 0].astype(complex)
    xi64 /= norm(xi64)
    eig64 = norm(h @ xi64 - mu64 * xi64)
    scal64 = [abs(q[j] @ h @ r @ xi64) for j in range(2)]

    mp.mp.dps = 80
    hm = mp_matrix(h)
    # eigh exploits Hermitian structure and returns orthonormal eigenvectors.
    evals, evecs = mp.eigh(hm)
    mum = evals[0]
    xim = evecs[:, 0]
    qm = mp_matrix(q)
    # Rebuild the orthogonal projector at high precision.  Importing the
    # double-precision projector would leave Q(I-P) at the 1e-16 floor and
    # can dominate the directional scalar after multiplication by H.
    gram = qm * qm.transpose_conj()
    pm = qm.transpose_conj() * (gram ** -1) * qm
    rm = mp.eye(len(idx)) - pm
    eigmp = mp_norm(hm * xim - mum * xim)
    scalmp = [abs((qm[j, :] * hm * rm * xim)[0]) for j in range(2)]

    print(
        f"{lam:4d} {L:8.3f} {gamma:6.2f} "
        f"{eig64:9.2e} {scal64[0]:9.2e} {scal64[1]:9.2e} "
        f"{sci(eigmp):>12} {sci(scalmp[0]):>12} {sci(scalmp[1]):>12}"
    )


def run():
    print("E74.16 arbitrary-precision floor audit")
    print("Matrix entries remain the same double-precision CCM data; only the eigenproblem is refined.")
    print(" lam      L gamma     eig64    row0-64    row1-64        eigMP       row0-MP       row1-MP")
    for lam, n_modes in [(6, 8), (8, 10), (10, 12)]:
        run_case(lam, n_modes, GAMMAS[0])


if __name__ == "__main__":
    run()
