#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402
from E73_148_signed_rowspace_probe import best_by_signed_margin  # noqa: E402
from E73_069_exact_far3_row_probe import setup_exact  # noqa: E402


def spectral_cutoff(row, e, xi, L, eps_power=8):
    vals, vecs = eigh(e)
    overlaps = np.abs(vecs.conj().T @ xi)
    null_j = int(np.argmax(overlaps))

    # Row-action convention: the row acts as row @ vector.
    coeff = row @ vecs
    alpha = coeff[null_j]

    eps = L ** (-eps_power)
    av = np.abs(vals)
    good = (av > eps)
    near = (av > 0.0) & (av <= eps)
    good[null_j] = False
    near[null_j] = False

    y_coeff = np.zeros_like(coeff)
    y_coeff[good] = coeff[good] / vals[good]
    y = y_coeff @ vecs.conj().T
    beta = coeff[near] @ vecs[:, near].conj().T if np.any(near) else np.zeros_like(row)
    recon = y @ e + alpha * xi.conj() + beta
    err = norm(recon - row)

    mid = (av > eps) & (av <= L ** -1)
    mid[null_j] = False
    bulk = av > L ** -1
    bulk[null_j] = False

    return {
        "alpha": alpha,
        "row_norm": norm(row),
        "y_norm": norm(y),
        "beta_norm": norm(beta),
        "good_norm": norm(coeff[good]),
        "near_norm": norm(coeff[near]),
        "mid_norm": norm(coeff[mid]),
        "bulk_norm": norm(coeff[bulk]),
        "recon_err": err,
        "near_count": int(np.sum(near)),
        "good_count": int(np.sum(good)),
    }


def run():
    print("E73.152 spectral-cutoff forced row certificate")
    print("Uses row-action coeffs c_a=row@v_a; alpha equals row@xi.")
    print("eps=L^-8.  Need alphaB<=-17 for SFRL-CUT_17.")
    print(
        " lam     L gamma row  alphaB   rowB  betaB     yB  nearB   midB  bulkB  errB nNear status"
    )
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        d, L, xi, e = setup_exact(lam, n_modes)
        del d
        for gamma in GAMMAS[:3]:
            _, _, _, frows, _, _ = best_by_signed_margin(lam, n_modes, gamma)
            for j, row in enumerate(frows):
                cert = spectral_cutoff(row, e, xi, L)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:3d}"
                    f" {bexp(abs(cert['alpha']), L):7.3f}"
                    f" {bexp(cert['row_norm'], L):6.3f}"
                    f" {bexp(cert['beta_norm'], L):6.3f}"
                    f" {bexp(cert['y_norm'], L):6.3f}"
                    f" {bexp(cert['near_norm'], L):6.3f}"
                    f" {bexp(cert['mid_norm'], L):6.3f}"
                    f" {bexp(cert['bulk_norm'], L):6.3f}"
                    f" {bexp(cert['recon_err'], L):6.3f}"
                    f" {cert['near_count']:5d}"
                    f" {'PASS' if abs(cert['alpha']) <= L**-17 else 'FAIL'}"
                )


if __name__ == "__main__":
    run()
