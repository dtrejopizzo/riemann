#!/usr/bin/env python3
import sys
import math
import cmath
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_065_rowspace_cmain_probe import hermite_kernel_bound, bexp  # noqa: E402
from E73_069_exact_far3_row_probe import setup_exact, finite_roots  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def bezout_rows(lam, n_modes, sigma, tau, m, ncrit):
    d, L, xi, e = setup_exact(lam, n_modes)
    roots = finite_roots(d, xi, hmax=max(GAMMAS[:ncrit]) + 10.0)
    a = sigma + 1j * tau
    evals, evecs = eigh(e)
    inv = np.zeros_like(evals)
    inv[1:] = 1.0 / evals[1:]
    ep = (evecs * inv) @ evecs.T
    rows = []
    for gamma in GAMMAS[:ncrit]:
        t = -gamma
        pref = math.exp(sigma * L) * hermite_kernel_bound(a, 1j * gamma, m) * abs(1.0 - cmath.exp(1j * gamma * L))
        far = float(np.min(np.abs(t - roots))) if len(roots) else 1.0
        krow = 1.0 / (t - d)
        r = krow @ ep
        recon = r @ e
        resid = norm(krow - recon)
        row_norm = norm(krow)
        signed = abs(np.dot(krow, xi))
        rows.append(
            {
                "gamma": gamma,
                "far_score": pref * far,
                "pref": pref,
                "signed": signed,
                "row_norm": row_norm,
                "r_norm": norm(r),
                "resid": resid,
                "weighted": pref * resid,
            }
        )
    rows.sort(reverse=True, key=lambda row: row["far_score"])
    return L, rows[:3]


def run():
    print("E73.067 row Bezout probe")
    print("r_t is the minimum-norm least-squares row with r_t E closest to k_t.")
    print(" lam     L tau   gamma    rB residB weightB signedB rowNormB")
    for lam, n_modes in [(16, 20), (18, 22), (20, 24), (24, 28)]:
        for sigma, tau, m in [(0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            L, rows = bezout_rows(lam, n_modes, sigma, tau, m, 12)
            for row in rows:
                print(
                    f"{lam:4d} {L:7.3f} {tau:7.2f} {row['gamma']:7.2f}"
                    f" {bexp(row['r_norm'], L):7.3f} {bexp(row['resid'], L):7.3f}"
                    f" {bexp(row['weighted'], L):7.3f} {bexp(row['signed'], L):7.3f}"
                    f" {bexp(row['row_norm'], L):8.3f}"
                )


if __name__ == "__main__":
    run()
