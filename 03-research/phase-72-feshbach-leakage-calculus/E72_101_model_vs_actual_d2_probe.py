#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, norm, solve, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import build  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_91_low_band_cofactor_probe import transport_vector  # noqa: E402


def even_basis(idx):
    n = len(idx)
    cols = []
    z = np.zeros(n)
    z[np.where(idx == 0)[0][0]] = 1.0
    cols.append(z)
    for m in idx[idx > 0]:
        col = np.zeros(n)
        col[np.where(idx == m)[0][0]] = 1.0 / np.sqrt(2.0)
        col[np.where(idx == -m)[0][0]] = 1.0 / np.sqrt(2.0)
        cols.append(col)
    return np.column_stack(cols)


def even_q_basis(idx, k, tol=1e-10):
    q = np.eye(len(idx)) - np.outer(k, k)
    u, s, _ = svd(q @ even_basis(idx), full_matrices=False)
    return u[:, s > tol]


def setup_pair(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    h_model, _, _ = build(lam, n_modes, include_arith=False)

    _, vec_actual = eigh(h_actual)
    xi = vec_actual[:, 0]
    xi = (xi + xi[::-1]) / 2
    xi = xi / norm(xi)

    evals_model, vec_model = eigh(h_model)
    e0 = evals_model[0]
    k = vec_model[:, 0]
    k = (k + k[::-1]) / 2
    k = k / norm(k)
    if np.dot(xi, k) < 0:
        xi = -xi

    d = 2 * np.pi * idx / L
    q = np.eye(len(idx)) - np.outer(k, k)
    bq = even_q_basis(idx, k)
    c_actual = bq.T @ (q @ (h_actual - e0 * np.eye(len(idx))) @ q) @ bq
    c_model = bq.T @ (q @ (h_model - e0 * np.eye(len(idx))) @ q) @ bq
    return idx, L, d, xi, k, bq, c_actual, c_model


def run():
    s = 10 + 0.2j
    hcut = 18
    print("E72.101 model-vs-actual D2 probe")
    print(" lam   N    tau      |D2_actual|   |D2_model|   |diff|    model/actual")
    for lam, n_modes in [(8, 24), (12, 28), (16, 34), (20, 40), (24, 48)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        mask = (np.abs(d) <= hcut).astype(float)
        a = bq.T @ (s / (s * s - d * d))
        for tau in finite_roots(xi, d, hmax=10.0)[:4]:
            c_tau = bq.T @ (mask * transport_vector(d, k, L, tau))
            d2_actual = np.vdot(a, solve(c_actual, c_tau))
            d2_model = np.vdot(a, solve(c_model, c_tau))
            ratio = abs(d2_model) / max(abs(d2_actual), 1e-30)
            print(
                f"{lam:4.0f} {n_modes:3d} {tau:6.3f} "
                f"{abs(d2_actual):14.3e} {abs(d2_model):12.3e} "
                f"{abs(d2_actual-d2_model):9.3e} {ratio:13.3e}"
            )


if __name__ == "__main__":
    run()
