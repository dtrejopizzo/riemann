#!/usr/bin/env python3
import sys
import math
import cmath
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_055_far3_nodewise_verifier import setup_full, finite_roots_signed, hermite_kernel_bound, cauchy_real  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402


def selected_rows(lam, n_modes, sigma, tau, m, ncrit):
    d, L, xi = setup_full(lam, n_modes)
    roots = finite_roots_signed(d, xi, hmax=max(GAMMAS[:ncrit]) + 10.0)
    a = sigma + 1j * tau
    rows = []
    for gamma in GAMMAS[:ncrit]:
        t = -gamma
        geom = hermite_kernel_bound(a, 1j * gamma, m)
        mesh = abs(1.0 - cmath.exp(1j * gamma * L))
        expf = math.exp(sigma * L)
        pref = expf * geom * mesh
        cx = abs(cauchy_real(t, d, xi))
        dist = float(np.min(np.abs(t - roots))) if len(roots) else 1.0
        q = cx / max(dist, 1e-300)
        rows.append(
            {
                "gamma": gamma,
                "geom": geom,
                "mesh": mesh,
                "expf": expf,
                "pref": pref,
                "cx": cx,
                "dist": dist,
                "q": q,
                "term": pref * cx,
                "far": pref * dist,
            }
        )
    rows.sort(reverse=True, key=lambda row: row["far"])
    return L, rows[:3]


def run():
    print("E73.102 FAR3 tradeoff probe")
    print("Decomposes each selected main row into prefactor, Cauchy, divisor distance, and quotient.")
    print(" lam     L tau  gamma   geomB  meshB  prefB     cB  distB     qB  termB")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28), (28, 32)]:
        for sigma, tau, m in [(0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            L, rows = selected_rows(lam, n_modes, sigma, tau, m, 12)
            for row in rows:
                print(
                    f"{lam:4d} {L:7.3f} {tau:7.2f} {row['gamma']:6.2f}"
                    f" {bexp(row['geom'], L):7.3f} {bexp(row['mesh'], L):6.3f}"
                    f" {bexp(row['pref'], L):7.3f} {bexp(row['cx'], L):7.3f}"
                    f" {bexp(row['dist'], L):7.3f} {bexp(row['q'], L):7.3f}"
                    f" {bexp(row['term'], L):7.3f}"
                )


if __name__ == "__main__":
    run()
