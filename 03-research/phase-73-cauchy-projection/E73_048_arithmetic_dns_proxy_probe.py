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


def pole_sep(t, d):
    return float(np.min(np.abs(t - d)))


def root_proxy(t, roots, d, mode):
    if len(roots) == 0:
        return 1.0
    root_dist = float(np.min(np.abs(t - roots)))
    sep = max(pole_sep(t, d), 1e-300)
    if mode == "near":
        return 1.0 / max(root_dist, 1e-300)
    if mode == "far":
        return root_dist
    if mode == "slope":
        return root_dist / sep
    if mode == "divisor_small":
        return root_dist / (sep + root_dist)
    if mode == "divisor_large":
        return (sep + root_dist) / max(root_dist, 1e-300)
    raise ValueError(mode)


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
        row = {
            "j": j,
            "gamma": gamma,
            "gweight": gweight,
            "cval": cval,
            "term": gweight * cval,
        }
        for mode in ["near", "far", "slope", "divisor_small", "divisor_large"]:
            row[mode] = gweight * root_proxy(t, roots, d, mode)
        rows.append(row)
    return L, rows


def capture(rows, key, r):
    total = sum(row["term"] for row in rows)
    selected = sorted(rows, reverse=True, key=lambda row: row[key])[:r]
    ids = {row["j"] for row in selected}
    cap = sum(row["term"] for row in rows if row["j"] in ids) / max(total, 1e-300)
    post = sorted(rows, reverse=True, key=lambda row: row["term"])[:r]
    post_ids = {row["j"] for row in post}
    return cap, len(ids & post_ids), selected[0]["gamma"]


def run():
    print("E73.048 arithmetic DNS proxy probe")
    print("Selectors use finite divisor/pole geometry but not C_x(gamma) values.")
    print(
        " lam     L sigma     tau  m   WCS  geom3 near3 far3 slope3 small3 large3"
        " post3 best bestCap firstBest firstPost"
    )
    modes = ["gweight", "near", "far", "slope", "divisor_small", "divisor_large"]
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (18, 22), (20, 24), (24, 28)]:
        for sigma, tau, m in [(0.05, GAMMAS[0], 2), (0.10, GAMMAS[0], 2), (0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            L, rows = rows_for_case(lam, n_modes, sigma, tau, m, 6)
            total = sum(row["term"] for row in rows)
            caps = {mode: capture(rows, mode, 3) for mode in modes}
            post3 = capture(rows, "term", 3)[0]
            best_mode = max(modes, key=lambda mode: caps[mode][0])
            first_post = sorted(rows, reverse=True, key=lambda row: row["term"])[0]["gamma"]
            print(
                f"{lam:4d} {L:7.3f} {sigma:5.2f} {tau:7.2f} {m:2d} {total:8.2e}"
                f" {caps['gweight'][0]:5.2f} {caps['near'][0]:5.2f} {caps['far'][0]:5.2f}"
                f" {caps['slope'][0]:6.2f} {caps['divisor_small'][0]:6.2f} {caps['divisor_large'][0]:6.2f}"
                f" {post3:5.2f} {best_mode:>12s} {caps[best_mode][0]:7.2f}"
                f" {caps[best_mode][2]:9.3f} {first_post:9.3f}"
            )


if __name__ == "__main__":
    run()
