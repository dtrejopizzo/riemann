#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, pinv, norm
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
    return idx, L, d, xi, k, q, c


def shorted_weyl_size(q, c, r_even, w):
    qw = q @ w
    u = pinv(c, rcond=1e-10) @ qw
    return norm(qw), norm(u), abs(np.vdot(r_even, u))


def run():
    s = 10 + 0.2j
    print("E72.76 core/displacement split probe")
    print("   lam      tau     core_weyl      disp_weyl     total_weyl")
    for lam, n_modes in [(8, 24), (12, 28), (16, 34), (20, 40)]:
        idx, L, d, xi, k, q, c = setup(lam, n_modes)
        h = k - xi
        r_even = s / (s * s - d * d)
        for tau in finite_roots(xi, d)[:4]:
            e_tau = np.exp(1j * tau * L)
            s_tau = 2 * tau / (tau * tau - d * d)
            r_minus = 1 / (tau - d)
            w_core = 1j * s_tau * xi
            w_disp = s_tau * (1j * h - (e_tau - 1) / L * np.dot(r_minus, h))
            core = shorted_weyl_size(q, c, r_even, w_core)[2]
            disp = shorted_weyl_size(q, c, r_even, w_disp)[2]
            total = shorted_weyl_size(q, c, r_even, w_core + w_disp)[2]
            print(f"{lam:6.1f} {tau:8.3f} {core:13.3e} {disp:14.3e} {total:14.3e}")


if __name__ == "__main__":
    run()
