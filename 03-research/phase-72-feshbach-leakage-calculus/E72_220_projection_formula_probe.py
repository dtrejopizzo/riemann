#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair, even_basis  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402


def raw_direct(idx, L, bq, y):
    mat = bq.T @ u_matrix(idx, L, y) @ bq
    return float(norm(mat, "fro") ** 2)


def raw_projection(idx, L, k, y):
    eb = even_basis(idx)
    eproj = eb @ eb.T
    p = eproj - np.outer(k, k)
    u = u_matrix(idx, L, y)
    # ||P U P||_HS^2 on range(P) = Tr(P U* P U P)
    val = np.trace(p @ u.conj().T @ p @ u @ p)
    return float(np.real(val))


def components(idx, L, k, y):
    eb = even_basis(idx)
    eproj = eb @ eb.T
    p = eproj - np.outer(k, k)
    u = u_matrix(idx, L, y)
    full_even = float(np.real(np.trace(eproj @ u.conj().T @ eproj @ u @ eproj)))
    removed = full_even - float(np.real(np.trace(p @ u.conj().T @ p @ u @ p)))
    kk = float(abs(np.vdot(k, u @ k)) ** 2)
    leak = float(norm((eproj - np.outer(k, k)) @ u @ k) ** 2 + norm((eproj - np.outer(k, k)) @ u.conj().T @ k) ** 2)
    return full_even, removed, kk, leak


def run():
    print("E72.220 projection formula probe")
    print("checks ||B*UB||_HS^2 = Tr(P U* P U P), P=E-kk*")
    print("lam u direct proj relErr fullEven removed kk leak")
    for lam, n_modes in [(12, 32), (16, 40), (20, 48), (24, 56)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        for ufrac in [0.1, 0.25, 0.5, 0.75, 0.9]:
            y = ufrac * L
            direct = raw_direct(idx, L, bq, y)
            proj = raw_projection(idx, L, k, y)
            full_even, removed, kk, leak = components(idx, L, k, y)
            rel = abs(direct - proj) / max(abs(direct), 1e-30)
            print(
                f"{lam:3.0f} {ufrac:.2f} {direct:.9e} {proj:.9e} {rel:.2e} "
                f"{full_even:.9e} {removed:.9e} {kk:.3e} {leak:.3e}",
                flush=True,
            )


if __name__ == "__main__":
    run()
