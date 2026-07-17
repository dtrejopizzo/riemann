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
    return mp.fsum(mp.mpf(float(w)) / (tt - mp.mpf(float(p))) for p, w in zip(d, xi))


def rational_cauchy_mp(t, d, xi):
    tt = mp.mpf(float(t))
    den = mp.fprod(tt - mp.mpf(float(p)) for p in d)
    num = mp.mpf("0")
    for pole, weight in zip(d, xi):
        pp = mp.mpf(float(pole))
        ww = mp.mpf(float(weight))
        num += ww * mp.fprod(tt - mp.mpf(float(other)) for other in d if other != pole)
    return num / den


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


def certificate_rows(lam, n_modes, sigma, tau, m, ncrit):
    d, L, xi = setup_full(lam, n_modes)
    roots = finite_roots_signed(d, xi, hmax=max(GAMMAS[:ncrit]) + 10.0)
    a = sigma + 1j * tau
    rows = []
    for j, gamma in enumerate(GAMMAS[:ncrit]):
        t = -gamma
        geom = hermite_kernel_bound(a, 1j * gamma, m)
        mesh = abs(1.0 - cmath.exp(1j * gamma * L))
        prefactor = math.exp(sigma * L) * geom * mesh
        c_direct = abs(cauchy_mp(t, d, xi))
        c_rational = abs(rational_cauchy_mp(t, d, xi))
        rel = abs(c_direct - c_rational) / max(c_direct, mp.mpf("1e-80"))
        far = float(np.min(np.abs(t - roots))) if len(roots) else 1.0
        rows.append(
            {
                "j": j,
                "gamma": gamma,
                "far_score": prefactor * far,
                "term": float(prefactor * c_rational),
                "rel": float(rel),
            }
        )
    selected = sorted(rows, reverse=True, key=lambda row: row["far_score"])[:3]
    ids = {row["j"] for row in selected}
    for row in rows:
        row["part"] = "main" if row["j"] in ids else "tail"
    return L, rows


def run():
    mp.mp.dps = 100
    print("E73.055 FAR3 nodewise rational verifier")
    print("Verifies T_k via finite rational C_x=P_x/D_x and FAR3 selection.")
    print(" lam     L sigma     tau nK    mainSum    tailSum     total    maxRelRat  mainGammas")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28)]:
        for sigma, tau, m in [(0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            L, rows = certificate_rows(lam, n_modes, sigma, tau, m, 12)
            main = sum(row["term"] for row in rows if row["part"] == "main")
            tail = sum(row["term"] for row in rows if row["part"] == "tail")
            total = main + tail
            max_rel = max(row["rel"] for row in rows)
            main_gammas = ",".join(f"{row['gamma']:.1f}" for row in rows if row["part"] == "main")
            print(
                f"{lam:4d} {L:7.3f} {sigma:5.2f} {tau:7.2f} {12:2d}"
                f" {main:10.3e} {tail:10.3e} {total:9.3e}"
                f" {max_rel:12.3e} {main_gammas}"
            )


if __name__ == "__main__":
    run()
