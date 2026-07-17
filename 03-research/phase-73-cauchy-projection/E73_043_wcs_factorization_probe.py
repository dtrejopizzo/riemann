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


def wcs_vectors(lam, n_modes, sigma, tau, m, ncrit):
    d, L, xi = setup_full(lam, n_modes)
    a = sigma + 1j * tau
    weights = []
    data = []
    for gamma in GAMMAS[:ncrit]:
        k = 1j * gamma
        geom = hermite_kernel_bound(a, k, m)
        mesh = abs(1.0 - cmath.exp(1j * gamma * L))
        cval = abs(cauchy_real(-gamma, d, xi))
        weights.append(math.exp(sigma * L) * geom * mesh)
        data.append(cval)
    return L, np.array(weights), np.array(data)


def summarize(lam, n_modes, sigma, tau, m, ncrit):
    L, w, d = wcs_vectors(lam, n_modes, sigma, tau, m, ncrit)
    actual = float(np.dot(w, d))
    maxd_sumw = float(np.max(d) * np.sum(w))
    maxw_sumd = float(np.max(w) * np.sum(d))
    cs = float(np.linalg.norm(w) * np.linalg.norm(d))
    l2d_l1w = float(np.sum(w) * np.linalg.norm(d) / math.sqrt(len(d)))
    concentration = float(np.max(w * d) / max(actual, 1e-300))
    corr = float(np.corrcoef(np.log(w + 1e-300), np.log(d + 1e-300))[0, 1]) if len(d) > 1 else 0.0
    return {
        "lam": lam,
        "L": L,
        "sigma": sigma,
        "tau": tau,
        "m": m,
        "actual": actual,
        "maxd_sumw": maxd_sumw,
        "maxw_sumd": maxw_sumd,
        "cs": cs,
        "l2d_l1w": l2d_l1w,
        "concentration": concentration,
        "corr": corr,
        "sumw": float(np.sum(w)),
        "maxd": float(np.max(d)),
    }


def run():
    print("E73.043 WCS factorization probe")
    print("Compares direct WCS with separated product bounds.")
    print(
        " lam     L sigma     tau  m      WCS    maxDsumW  r1"
        "    maxWsumD  r2        CS  rCS  conc  corr"
    )
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (18, 22), (20, 24), (24, 28)]:
        for sigma, tau, m in [(0.05, GAMMAS[0], 2), (0.10, GAMMAS[0], 2), (0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            row = summarize(lam, n_modes, sigma, tau, m, 6)
            print(
                f"{row['lam']:4d} {row['L']:7.3f} {row['sigma']:5.2f} {row['tau']:7.2f}"
                f" {row['m']:2d} {row['actual']:9.3e}"
                f" {row['maxd_sumw']:11.3e} {row['maxd_sumw']/max(row['actual'], 1e-300):5.1f}"
                f" {row['maxw_sumd']:11.3e} {row['maxw_sumd']/max(row['actual'], 1e-300):5.1f}"
                f" {row['cs']:9.3e} {row['cs']/max(row['actual'], 1e-300):5.1f}"
                f" {row['concentration']:5.2f} {row['corr']:5.2f}"
            )


if __name__ == "__main__":
    run()
