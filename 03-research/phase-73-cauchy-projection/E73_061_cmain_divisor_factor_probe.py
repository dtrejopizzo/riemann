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


def numerator_denominator_mp(t, d, xi):
    tt = mp.mpf(float(t))
    den = mp.fprod(tt - mp.mpf(float(p)) for p in d)
    num = mp.mpf("0")
    for pole, weight in zip(d, xi):
        pp = mp.mpf(float(pole))
        ww = mp.mpf(float(weight))
        num += ww * mp.fprod(tt - mp.mpf(float(other)) for other in d if other != pole)
    return abs(num), abs(den), abs(num / den)


def bexp(value, L):
    value = mp.mpf(value)
    if value <= 0:
        return float("-inf")
    return float(mp.log(value) / mp.log(L))


def far3_rows(lam, n_modes, sigma, tau, m, ncrit):
    d, L, xi = setup_full(lam, n_modes)
    roots = finite_roots_signed(d, xi, hmax=max(GAMMAS[:ncrit]) + 10.0)
    a = sigma + 1j * tau
    rows = []
    for gamma in GAMMAS[:ncrit]:
        t = -gamma
        pref = math.exp(sigma * L) * hermite_kernel_bound(a, 1j * gamma, m) * abs(1.0 - cmath.exp(1j * gamma * L))
        far = float(np.min(np.abs(t - roots))) if len(roots) else 1.0
        num, den, cval = numerator_denominator_mp(t, d, xi)
        rows.append({"gamma": gamma, "pref": pref, "far_score": pref * far, "num": num, "den": den, "cval": cval})
    rows.sort(reverse=True, key=lambda row: row["far_score"])
    return L, rows[:3]


def run():
    mp.mp.dps = 100
    print("E73.061 CMAIN divisor-factor probe")
    print("Splits C_x=P_x/D_x into numerator and denominator exponents on FAR3 nodes.")
    print(" lam     L tau   gamma      numB      denB        cB        |P|        |D|       |C|")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28)]:
        for sigma, tau, m in [(0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            L, rows = far3_rows(lam, n_modes, sigma, tau, m, 12)
            for row in rows:
                print(
                    f"{lam:4d} {L:7.3f} {tau:7.2f} {row['gamma']:7.2f}"
                    f" {bexp(row['num'], L):9.3f} {bexp(row['den'], L):9.3f}"
                    f" {bexp(row['cval'], L):9.3f} {float(row['num']):10.3e}"
                    f" {float(row['den']):10.3e} {float(row['cval']):9.3e}"
                )


if __name__ == "__main__":
    run()
