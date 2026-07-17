#!/usr/bin/env python3
import sys
import cmath
import numpy as np
from numpy.linalg import eigh, norm
from scipy.optimize import brentq

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS, g_cancelled  # noqa: E402


def setup_full(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2.0
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi


def cauchy_real(t, d, xi):
    return float(np.sum(xi / (t - d)))


def finite_roots(d, xi, hmax):
    roots = []
    order = np.argsort(d)
    ds = d[order]
    for a, b in zip(ds[:-1], ds[1:]):
        left = a + 1e-8
        right = b - 1e-8
        if right <= left or right < 0:
            continue
        try:
            fa = cauchy_real(left, d, xi)
            fb = cauchy_real(right, d, xi)
            if np.isfinite(fa) and np.isfinite(fb) and fa * fb < 0:
                r = brentq(lambda x: cauchy_real(x, d, xi), left, right, xtol=1e-12)
                if 0 < r <= hmax:
                    roots.append(r)
        except Exception:
            pass
    return np.array(sorted(roots))


def run():
    print("E73.034 finite root alignment probe")
    print("Compares zeta critical heights with finite Cauchy roots and cancelled values.")
    print(" lam     L  #roots   gamma       nearestRoot       dist      |g_cancelled|")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (18, 22), (20, 24), (24, 28)]:
        idx, d, L, xi = setup_full(lam, n_modes)
        roots = finite_roots(d, xi, hmax=45.0)
        for gamma in GAMMAS[:5]:
            if len(roots):
                j = int(np.argmin(np.abs(roots - gamma)))
                nearest = roots[j]
                dist = abs(nearest - gamma)
            else:
                nearest = np.nan
                dist = np.nan
            gval = abs(g_cancelled(1j * gamma, d, xi, L))
            print(
                f"{lam:4d} {L:7.3f} {len(roots):7d} {gamma:10.6f} "
                f"{nearest:16.9f} {dist:10.3e} {gval:16.3e}"
            )


if __name__ == "__main__":
    run()
