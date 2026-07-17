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


def rows(lam, n_modes, sigma, tau, m, ncrit):
    d, L, xi = setup_full(lam, n_modes)
    roots = finite_roots_signed(d, xi, hmax=max(GAMMAS[:ncrit]) + 10.0)
    a = sigma + 1j * tau
    out = []
    for gamma in GAMMAS[:ncrit]:
        t = -gamma
        geom = hermite_kernel_bound(a, 1j * gamma, m)
        mesh = abs(1.0 - cmath.exp(1j * gamma * L))
        w = math.exp(sigma * L) * geom * mesh
        c = abs(cauchy_real(t, d, xi))
        r = float(np.min(np.abs(t - roots))) if len(roots) else 1.0
        f = w * r
        q = c / max(r, 1e-300)
        out.append({"gamma": gamma, "T": w * c, "F": f, "Q": q})
    out.sort(reverse=True, key=lambda row: row["F"])
    return L, out


def run():
    print("E73.053 FAR quotient tail probe")
    print("Uses T_k=F_k Q_k with Q_k=|C_x|/dist(-gamma,Div(P_x)).")
    print(" lam     L sigma     tau nK        WCS     tail3    sumFtail  maxQtail  qBoundTail/tail  maxQmain")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28)]:
        for ncrit in [6, 8, 10, 12]:
            for sigma, tau, m in [(0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
                L, rr = rows(lam, n_modes, sigma, tau, m, ncrit)
                total = sum(row["T"] for row in rr)
                main = rr[:3]
                tail = rr[3:]
                tail_t = sum(row["T"] for row in tail)
                tail_f = sum(row["F"] for row in tail)
                max_q_tail = max([row["Q"] for row in tail], default=0.0)
                max_q_main = max([row["Q"] for row in main], default=0.0)
                q_bound = tail_f * max_q_tail
                print(
                    f"{lam:4d} {L:7.3f} {sigma:5.2f} {tau:7.2f} {ncrit:2d}"
                    f" {total:10.3e} {tail_t:10.3e} {tail_f:10.3e}"
                    f" {max_q_tail:10.3e} {q_bound/max(tail_t, 1e-300):15.3e}"
                    f" {max_q_main:10.3e}"
                )


if __name__ == "__main__":
    run()
