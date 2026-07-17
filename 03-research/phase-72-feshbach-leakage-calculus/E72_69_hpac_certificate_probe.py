#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, pinv, norm
from scipy.optimize import brentq

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import build, make_q  # noqa: E402


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
                r = brentq(f, a, b, xtol=1e-11)
                if 0 < r < hmax:
                    roots.append(r)
        except Exception:
            pass
    return np.array(roots)


def int_exp_sin(a, d, L):
    if abs(d) < 1e-14:
        return 0.0j
    return d * (1 - np.exp(a * L)) / (a * a + d * d)


def int_exp_cos(a, d, L):
    if abs(d) < 1e-14:
        return (np.exp(a * L) - 1) / a if abs(a) > 1e-14 else L
    return a * (np.exp(a * L) - 1) / (a * a + d * d)


def int_y_exp_cos(a, d, L):
    h = 1e-6
    return (int_exp_cos(a + h, d, L) - int_exp_cos(a - h, d, L)) / (2 * h)


def hpac_matrix(idx, L, tau):
    rho = 0.5 + 1j * tau
    a = 1j * tau
    d = 2 * np.pi * idx / L
    n = len(idx)
    mat = np.zeros((n, n), dtype=complex)

    for row, dr in enumerate(d):
        for col, dc in enumerate(d):
            if row == col:
                integral = 2 * (int_exp_cos(a, dr, L) - int_y_exp_cos(a, dr, L) / L)
            else:
                denom = np.pi * (idx[col] - idx[row])
                integral = (int_exp_sin(a, dr, L) - int_exp_sin(a, dc, L)) / denom
            mat[row, col] = rho * integral

    q0 = np.zeros((n, n), dtype=float)
    for row, m in enumerate(idx):
        for col, nn in enumerate(idx):
            q0[row, col] = make_q(int(m), int(nn), L)(0.0)

    return q0 + mat


def setup(lam, n_modes, s):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    h_model, _, _ = build(lam, n_modes, include_arith=False)

    _, v_actual = eigh(h_actual)
    xi = v_actual[:, 0]
    xi = (xi + xi[::-1]) / 2
    xi = xi / norm(xi)

    evals_model, v_model = eigh(h_model)
    k = v_model[:, 0]
    k = (k + k[::-1]) / 2
    k = k / norm(k)

    d = 2 * np.pi * idx / L
    q = np.eye(len(idx)) - np.outer(k, k)
    c = q @ (h_actual - evals_model[0] * np.eye(len(idx))) @ q
    r_s = 1 / (s - d)
    v = pinv(c, rcond=1e-10) @ (q @ r_s)
    return idx, L, d, xi, k, v


def run():
    print("E72.69 HPAC finite-root certificate probe")
    print("   lam      x    N  roots used     max|F|        values")
    for lam, n_modes in [(6, 18), (8, 24), (12, 28), (16, 34), (20, 40)]:
        idx, L, d, xi, k, v = setup(lam, n_modes, 10 + 0.2j)
        roots = finite_roots(xi, d)[:4]
        vals = []
        for tau in roots:
            vals.append(abs(np.vdot(v, hpac_matrix(idx, L, tau) @ k)))
        vals = np.array(vals)
        print(
            f"{lam:6.1f} {lam * lam:6.0f} {n_modes:4d} {len(roots):10d} "
            f"{np.max(vals) if len(vals) else np.nan:12.4e} "
            f"{np.array2string(vals, precision=3)}"
        )


if __name__ == "__main__":
    run()
