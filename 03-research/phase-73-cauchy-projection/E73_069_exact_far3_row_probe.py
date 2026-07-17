#!/usr/bin/env python3
import sys
import math
import cmath
import numpy as np
from numpy.linalg import eigh, norm
from scipy.optimize import brentq

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_065_rowspace_cmain_probe import hermite_kernel_bound, bexp  # noqa: E402


def setup_exact(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    d = 2.0 * np.pi * idx / L
    e = h_actual - vals[0] * np.eye(len(idx))
    return d, L, xi, e


def cauchy_real(t, d, xi):
    return float(np.sum(xi / (t - d)))


def finite_roots(d, xi, hmax):
    roots = []
    ds = np.sort(d)
    for left_pole, right_pole in zip(ds[:-1], ds[1:]):
        left = left_pole + 1e-8
        right = right_pole - 1e-8
        if right <= left:
            continue
        try:
            fa = cauchy_real(left, d, xi)
            fb = cauchy_real(right, d, xi)
            if np.isfinite(fa) and np.isfinite(fb) and fa * fb < 0:
                root = brentq(lambda x: cauchy_real(x, d, xi), left, right, xtol=1e-13)
                if -hmax <= root <= hmax:
                    roots.append(root)
        except Exception:
            pass
    return np.array(sorted(roots))


def far3_rows(lam, n_modes, sigma, tau, m, ncrit):
    d, L, xi, e = setup_exact(lam, n_modes)
    roots = finite_roots(d, xi, hmax=max(GAMMAS[:ncrit]) + 10.0)
    a = sigma + 1j * tau
    rows = []
    for gamma in GAMMAS[:ncrit]:
        t = -gamma
        pref = math.exp(sigma * L) * hermite_kernel_bound(a, 1j * gamma, m) * abs(1.0 - cmath.exp(1j * gamma * L))
        far = float(np.min(np.abs(t - roots))) if len(roots) else 1.0
        krow = 1.0 / (t - d)
        signed = abs(np.dot(krow, xi))
        row_norm = norm(krow)
        rows.append(
            {
                "gamma": gamma,
                "far_score": pref * far,
                "pref": pref,
                "signed": signed,
                "row_norm": row_norm,
                "rel_row": signed / max(row_norm, 1e-300),
                "weighted": pref * signed,
                "eres": norm(e @ xi),
            }
        )
    rows.sort(reverse=True, key=lambda row: row["far_score"])
    return L, rows[:3]


def run():
    print("E73.069 exact FAR3 row probe")
    print("Uses the exact ground eigenvector, not the symmetric gauge vector.")
    print(" lam     L tau   gamma  signedB relB weightB  ||Ex||B  signed    weighted")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28)]:
        for sigma, tau, m in [(0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            L, rows = far3_rows(lam, n_modes, sigma, tau, m, 12)
            for row in rows:
                print(
                    f"{lam:4d} {L:7.3f} {tau:7.2f} {row['gamma']:7.2f}"
                    f" {bexp(row['signed'], L):8.3f} {bexp(row['rel_row'], L):7.3f}"
                    f" {bexp(row['weighted'], L):7.3f} {bexp(row['eres'], L):8.3f}"
                    f" {row['signed']:9.3e} {row['weighted']:10.3e}"
                )


if __name__ == "__main__":
    run()
