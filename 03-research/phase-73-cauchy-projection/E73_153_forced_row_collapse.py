#!/usr/bin/env python3
import itertools
import sys
import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_069_exact_far3_row_probe import setup_exact  # noqa: E402
from E73_077_pair_coefficient_budget_probe import coeffs  # noqa: E402
from E73_148_signed_rowspace_probe import pair_row, forced_rows  # noqa: E402


def coeff_matrix(zs, w, L):
    return np.array([coeffs(z, w, L) for z in zs], dtype=complex)


def collapse_error(d, L, gamma, z_im_1, z_im_2, sigma=0.20):
    idx = np.rint(d * L / (2.0 * np.pi)).astype(int)
    w = -1j * gamma
    z1 = sigma + 1j * z_im_1
    z2 = sigma + 1j * z_im_2
    mat = coeff_matrix([z1, z2], w, L)
    rows = [
        pair_row(z1, w, idx, d, L, "signed"),
        pair_row(z2, w, idx, d, L, "signed"),
    ]
    decoded = forced_rows(mat, rows)
    q_w = 1.0 / (w + 1j * d)
    q_mw = 1.0 / (-w + 1j * d)
    err0 = norm(decoded[0] - q_w) / max(norm(q_w), 1e-300)
    err1 = norm(decoded[1] - q_mw) / max(norm(q_mw), 1e-300)
    row_id = norm(np.vstack(rows) - mat @ np.vstack([q_w, q_mw])) / max(norm(np.vstack(rows)), 1e-300)
    return L, np.linalg.cond(mat), row_id, err0, err1


def run():
    print("E73.153 forced row collapse verifier")
    print("Checks M^-1[p_infty(z1),p_infty(z2)] = [1/(w+id), 1/(-w+id)] coordinatewise.")
    print(" lam     L gamma      z1      z2      cond       rowId       err0       err1")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        d, L, xi, _ = setup_exact(lam, n_modes)
        del xi
        for gamma in GAMMAS[:3]:
            candidates = GAMMAS[:6]
            # Use several row pairs, including non-optimized choices, because
            # the collapse should be purely algebraic whenever M is invertible.
            for z_im_1, z_im_2 in list(itertools.combinations(candidates, 2))[:3]:
                L, cond, row_id, err0, err1 = collapse_error(d, L, gamma, z_im_1, z_im_2)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                    f" {z_im_1:7.2f} {z_im_2:7.2f}"
                    f" {cond:9.2e} {row_id:10.2e} {err0:10.2e} {err1:10.2e}"
                )


if __name__ == "__main__":
    run()
