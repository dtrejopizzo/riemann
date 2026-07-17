#!/usr/bin/env python3
import sys
import cmath
import math
import numpy as np
import mpmath as mp
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


def cauchy_mp(t, d, xi):
    tt = mp.mpf(float(t))
    return abs(mp.fsum(mp.mpf(float(w)) / (tt - mp.mpf(float(p))) for p, w in zip(d, xi)))


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


def bexp(value, L):
    value = float(value)
    if value <= 0:
        return float("-inf")
    return math.log(value) / math.log(L)


def rows(lam, n_modes, sigma, tau, m, ncrit):
    d, L, xi = setup_full(lam, n_modes)
    roots = finite_roots_signed(d, xi, hmax=max(GAMMAS[:ncrit]) + 10.0)
    a = sigma + 1j * tau
    out = []
    for gamma in GAMMAS[:ncrit]:
        t = -gamma
        geom = hermite_kernel_bound(a, 1j * gamma, m)
        mesh = abs(1.0 - cmath.exp(1j * gamma * L))
        pref = math.exp(sigma * L) * geom * mesh
        cval = float(cauchy_mp(t, d, xi))
        far = float(np.min(np.abs(t - roots))) if len(roots) else 1.0
        out.append({"gamma": gamma, "pref": pref, "cval": cval, "term": pref * cval, "far_score": pref * far})
    out.sort(reverse=True, key=lambda row: row["far_score"])
    return L, out


def run():
    mp.mp.dps = 80
    print("E73.059 FAR3 factor exponent probe")
    print("Reports prefactor and Cauchy exponents for the FAR3 main nodes.")
    print(" lam     L tau   gamma     prefB        cB     termB       pref       Cx       term")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28)]:
        for sigma, tau, m in [(0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            L, rr = rows(lam, n_modes, sigma, tau, m, 12)
            for row in rr[:3]:
                print(
                    f"{lam:4d} {L:7.3f} {tau:7.2f} {row['gamma']:7.2f}"
                    f" {bexp(row['pref'], L):9.3f} {bexp(row['cval'], L):9.3f}"
                    f" {bexp(row['term'], L):9.3f} {row['pref']:10.3e}"
                    f" {row['cval']:9.3e} {row['term']:10.3e}"
                )


if __name__ == "__main__":
    run()
