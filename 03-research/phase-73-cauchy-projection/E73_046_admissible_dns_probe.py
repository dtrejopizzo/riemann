#!/usr/bin/env python3
import sys
import cmath
import math
import numpy as np
from numpy.linalg import eigh, norm

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
    a = sigma + 1j * tau
    rows = []
    for j, gamma in enumerate(GAMMAS[:ncrit]):
        geom = hermite_kernel_bound(a, 1j * gamma, m)
        mesh = abs(1.0 - cmath.exp(1j * gamma * L))
        gweight = math.exp(sigma * L) * geom * mesh
        cval = abs(cauchy_real(-gamma, d, xi))
        rows.append({"j": j, "gamma": gamma, "gweight": gweight, "cval": cval, "term": gweight * cval})
    return L, rows


def capture(rows, selector, r):
    total = sum(row["term"] for row in rows)
    selected = sorted(rows, reverse=True, key=selector)[:r]
    selected_ids = {row["j"] for row in selected}
    cap = sum(row["term"] for row in rows if row["j"] in selected_ids) / max(total, 1e-300)
    top_post = sorted(rows, reverse=True, key=lambda row: row["term"])[:r]
    post_ids = {row["j"] for row in top_post}
    overlap = len(selected_ids & post_ids)
    return cap, overlap, selected


def run():
    print("E73.046 admissible DNS probe")
    print("Dominants are selected without C_x: by geometric-mesh weight only.")
    print(
        " lam     L sigma     tau  m   WCS   adm1 adm2 adm3  post3 overlap3"
        "  firstAdmGamma firstPostGamma"
    )
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (18, 22), (20, 24), (24, 28)]:
        for sigma, tau, m in [(0.05, GAMMAS[0], 2), (0.10, GAMMAS[0], 2), (0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            L, rows = rows_for_case(lam, n_modes, sigma, tau, m, 6)
            total = sum(row["term"] for row in rows)
            adm = [capture(rows, lambda row: row["gweight"], r)[0] for r in [1, 2, 3]]
            post = [capture(rows, lambda row: row["term"], r)[0] for r in [1, 2, 3]]
            cap3, overlap3, selected = capture(rows, lambda row: row["gweight"], 3)
            first_adm = sorted(rows, reverse=True, key=lambda row: row["gweight"])[0]["gamma"]
            first_post = sorted(rows, reverse=True, key=lambda row: row["term"])[0]["gamma"]
            print(
                f"{lam:4d} {L:7.3f} {sigma:5.2f} {tau:7.2f} {m:2d}"
                f" {total:8.2e} {adm[0]:5.2f} {adm[1]:5.2f} {adm[2]:5.2f}"
                f" {post[2]:6.2f} {overlap3:8d} {first_adm:14.3f} {first_post:14.3f}"
            )


if __name__ == "__main__":
    run()
