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


def terms_for_case(lam, n_modes, sigma, tau, m, ncrit):
    d, L, xi = setup_full(lam, n_modes)
    a = sigma + 1j * tau
    terms = []
    for gamma in GAMMAS[:ncrit]:
        geom = hermite_kernel_bound(a, 1j * gamma, m)
        mesh = abs(1.0 - cmath.exp(1j * gamma * L))
        cval = abs(cauchy_real(-gamma, d, xi))
        term = math.exp(sigma * L) * geom * mesh * cval
        terms.append((term, gamma, geom, mesh, cval))
    terms.sort(reverse=True, key=lambda x: x[0])
    return L, terms


def run():
    print("E73.044 dominant-node split probe")
    print("Measures how many critical nodes dominate WCS.")
    print(" lam     L sigma     tau  m      WCS   top1  top2  top3  topGamma1  mesh1     C1")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (18, 22), (20, 24), (24, 28)]:
        for sigma, tau, m in [(0.05, GAMMAS[0], 2), (0.10, GAMMAS[0], 2), (0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            L, terms = terms_for_case(lam, n_modes, sigma, tau, m, 6)
            total = sum(t[0] for t in terms)
            top_fracs = [sum(t[0] for t in terms[:r]) / max(total, 1e-300) for r in [1, 2, 3]]
            first = terms[0]
            print(
                f"{lam:4d} {L:7.3f} {sigma:5.2f} {tau:7.2f} {m:2d}"
                f" {total:9.3e} {top_fracs[0]:6.2f} {top_fracs[1]:5.2f} {top_fracs[2]:5.2f}"
                f" {first[1]:10.3f} {first[3]:8.2e} {first[4]:8.2e}"
            )


if __name__ == "__main__":
    run()
