#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, norm
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


def run():
    s = 10 + 0.2j
    sb = np.conj(s)
    print("E72.78 core Cauchy root identity probe")
    print("   lam      tau        |raw|       |formula|        diff")
    for lam, n_modes in [(8, 24), (12, 28), (20, 40)]:
        h_actual, idx, L = build(lam, n_modes, include_arith=True)
        _, vec_actual = eigh(h_actual)
        xi = vec_actual[:, 0]
        xi = (xi + xi[::-1]) / 2
        xi = xi / norm(xi)
        d = 2 * np.pi * idx / L
        r_even = s / (s * s - d * d)
        m_sb = np.dot(xi, 1 / (sb - d))
        for tau in finite_roots(xi, d)[:4]:
            s_tau = 2 * tau / (tau * tau - d * d)
            raw = np.vdot(r_even, s_tau * xi)
            formula = -2 * tau * m_sb / (sb * sb - tau * tau)
            print(
                f"{lam:6.1f} {tau:8.3f} {abs(raw):12.3e} "
                f"{abs(formula):14.3e} {abs(raw - formula):11.3e}"
            )


if __name__ == "__main__":
    run()
