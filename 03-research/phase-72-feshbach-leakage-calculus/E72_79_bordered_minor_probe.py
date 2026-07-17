#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import det, eigh, norm, solve, svd
from scipy.optimize import brentq

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import build  # noqa: E402


def finite_roots(xi, d, hmax=12.0):
    order = np.argsort(d)
    dd = d[order]
    xx = xi[order]

    def f(t):
        return np.sum(xx / (t - dd))

    roots = []
    for j in range(len(dd) - 1):
        a = dd[j] + 1e-7
        b = dd[j + 1] - 1e-7
        if a >= b:
            continue
        try:
            fa, fb = f(a), f(b)
            if np.isfinite(fa) and np.isfinite(fb) and fa * fb < 0:
                root = brentq(f, a, b, xtol=1e-11)
                if 0 < root < hmax:
                    roots.append(root)
        except Exception:
            pass
    return np.array(roots)


def even_basis(idx):
    n = len(idx)
    cols = []
    zero = np.zeros(n)
    zero[np.where(idx == 0)[0][0]] = 1.0
    cols.append(zero)
    for m in idx[idx > 0]:
        col = np.zeros(n)
        col[np.where(idx == m)[0][0]] = 1.0 / np.sqrt(2.0)
        col[np.where(idx == -m)[0][0]] = 1.0 / np.sqrt(2.0)
        cols.append(col)
    return np.column_stack(cols)


def even_q_basis(idx, k, tol=1e-10):
    e = even_basis(idx)
    q = np.eye(len(idx)) - np.outer(k, k)
    u, s, _ = svd(q @ e, full_matrices=False)
    return u[:, s > tol]


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    h_model, _, _ = build(lam, n_modes, include_arith=False)

    _, vec_actual = eigh(h_actual)
    xi = vec_actual[:, 0]
    xi = (xi + xi[::-1]) / 2
    xi = xi / norm(xi)

    evals_model, vec_model = eigh(h_model)
    k = vec_model[:, 0]
    k = (k + k[::-1]) / 2
    k = k / norm(k)
    if np.dot(xi, k) < 0:
        xi = -xi

    d = 2 * np.pi * idx / L
    q = np.eye(len(idx)) - np.outer(k, k)
    c = q @ (h_actual - evals_model[0] * np.eye(len(idx))) @ q
    bq = even_q_basis(idx, k)
    ce = bq.T @ c @ bq
    return idx, L, d, xi, k, bq, ce


def bordered_pairing(ce, a, b):
    top = np.column_stack([ce.astype(complex), b])
    bottom = np.concatenate([np.conjugate(a), np.array([0.0 + 0.0j])])[None, :]
    bordered = np.vstack([top, bottom])
    return -det(bordered) / det(ce)


def run():
    s = 10 + 0.2j
    print("E72.79 bordered minor certificate probe")
    print("   lam    N      tau       kind        |solve|       absdiff       reldiff")
    for lam, n_modes in [(6, 10), (8, 12), (10, 14), (12, 16)]:
        idx, L, d, xi, k, bq, ce = setup(lam, n_modes)
        h = k - xi
        r_even = s / (s * s - d * d)
        a = bq.T @ r_even
        for tau in finite_roots(xi, d)[:3]:
            e_tau = np.exp(1j * tau * L)
            s_tau = 2 * tau / (tau * tau - d * d)
            r_minus = 1 / (tau - d)
            w_core = 1j * s_tau * xi
            w_disp = s_tau * (1j * h - (e_tau - 1) / L * np.dot(r_minus, h) * np.ones_like(h))
            w_total = w_core + w_disp
            for name, w in [("core", w_core), ("disp", w_disp), ("total", w_total)]:
                b = bq.T @ w
                direct = np.vdot(a, solve(ce, b))
                minor = bordered_pairing(ce, a, b)
                absdiff = abs(direct - minor)
                reldiff = absdiff / max(abs(direct), 1e-30)
                print(
                    f"{lam:6.1f} {n_modes:4d} {tau:8.3f} {name:>10s} "
                    f"{abs(direct):12.3e} {absdiff:12.3e} {reldiff:12.3e}"
                )


if __name__ == "__main__":
    run()
