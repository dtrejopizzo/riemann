#!/usr/bin/env python3
import sys
import cmath
import math
import numpy as np
from numpy.linalg import eigh, norm
from scipy.optimize import brentq

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def setup_full(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2.0
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return d, L, xi


def cauchy_real(t, d, xi):
    return float(np.sum(xi / (t - d)))


def finite_roots_signed(d, xi, hmax):
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


def hermite_kernel_bound(a, k, m, theta=0.5):
    beta = k - a
    w0 = 1.0 / (2.0 * a)
    wstar = -1.0 / beta
    dist = abs(wstar - w0)
    radius = theta * dist
    major = 1.0 / (abs(beta) * (1.0 - theta) * dist)
    total = 0.0
    for p in range(m):
        inner = 0.0
        for rr in range(p, m):
            inner += math.comb(rr, p) * (abs(w0) ** (rr - p)) * (radius ** (-rr))
        total += inner / math.factorial(p)
    return major * total


def rows_for_case(lam, n_modes, sigma, tau, m, ncrit):
    d, L, xi = setup_full(lam, n_modes)
    roots = finite_roots_signed(d, xi, hmax=max(GAMMAS[:ncrit]) + 10.0)
    a = sigma + 1j * tau
    rows = []
    for j, gamma in enumerate(GAMMAS[:ncrit]):
        t = -gamma
        geom = hermite_kernel_bound(a, 1j * gamma, m)
        mesh = abs(1.0 - cmath.exp(1j * gamma * L))
        gweight = math.exp(sigma * L) * geom * mesh
        cval = abs(cauchy_real(t, d, xi))
        if len(roots):
            far = float(np.min(np.abs(t - roots)))
        else:
            far = 1.0
        rows.append(
            {
                "j": j,
                "gamma": gamma,
                "term": gweight * cval,
                "far_score": gweight * far,
            }
        )
    return L, rows


def capture(rows, key, r):
    total = sum(row["term"] for row in rows)
    selected = sorted(rows, reverse=True, key=lambda row: row[key])[:r]
    ids = {row["j"] for row in selected}
    return sum(row["term"] for row in rows if row["j"] in ids) / max(total, 1e-300)


def min_r_for(rows, key, threshold):
    for r in range(1, len(rows) + 1):
        if capture(rows, key, r) >= threshold:
            return r
    return len(rows)


def run():
    print("E73.050 FAR-DNS window stress")
    print("Measures capture of the far-divisor selector as the critical window grows.")
    print(" lam     L sigma     tau  m nK      WCS  far3 far5 far8 post3 r90 r95 r99")
    cases = [(16, 20), (18, 22), (20, 24), (24, 28)]
    for lam, n_modes in cases:
        for ncrit in [6, 8, 10, 12]:
            for sigma, tau, m in [(0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
                L, rows = rows_for_case(lam, n_modes, sigma, tau, m, ncrit)
                total = sum(row["term"] for row in rows)
                far3 = capture(rows, "far_score", min(3, ncrit))
                far5 = capture(rows, "far_score", min(5, ncrit))
                far8 = capture(rows, "far_score", min(8, ncrit))
                post3 = capture(rows, "term", min(3, ncrit))
                r90 = min_r_for(rows, "far_score", 0.90)
                r95 = min_r_for(rows, "far_score", 0.95)
                r99 = min_r_for(rows, "far_score", 0.99)
                print(
                    f"{lam:4d} {L:7.3f} {sigma:5.2f} {tau:7.2f} {m:2d} {ncrit:2d}"
                    f" {total:8.2e} {far3:5.2f} {far5:5.2f} {far8:5.2f}"
                    f" {post3:5.2f} {r90:3d} {r95:3d} {r99:3d}"
                )


if __name__ == "__main__":
    run()
