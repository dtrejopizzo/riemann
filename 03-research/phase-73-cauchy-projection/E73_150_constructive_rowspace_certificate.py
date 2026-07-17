#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402
from E73_148_signed_rowspace_probe import best_by_signed_margin  # noqa: E402
from E73_069_exact_far3_row_probe import setup_exact  # noqa: E402


def pinv_on_complement(e, xi):
    vals, vecs = eigh(e)
    null_j = int(np.argmax(np.abs(vecs.conj().T @ xi)))
    inv_vals = np.zeros_like(vals)
    for j, val in enumerate(vals):
        if j != null_j:
            inv_vals[j] = 1.0 / val
    return (vecs * inv_vals) @ vecs.conj().T


def cert_row(row, e, xi, ep):
    alpha = row @ xi
    y = row @ ep
    recon = y @ e + alpha * xi.conj()
    err = norm(row - recon)
    return alpha, y, err


def roughness(y):
    if len(y) < 3:
        return 0.0, 0.0
    dy = np.diff(y)
    ddy = np.diff(dy)
    return norm(dy) / max(norm(y), 1e-300), norm(ddy) / max(norm(y), 1e-300)


def run():
    print("E73.150 constructive rowspace certificate")
    print("Constructs r=yE+alpha xi* with y=rE^+ for forced signed rows.")
    print("alphaB=log_L|alpha|; yB=log_L||y||; errB=log_L||r-yE-alpha xi*||.")
    print(" lam     L gamma row  alphaB      yB    errB     d1B     d2B status")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        d, L, xi, e = setup_exact(lam, n_modes)
        ep = pinv_on_complement(e, xi)
        for gamma in GAMMAS[:3]:
            _, _, _, frows, _, _ = best_by_signed_margin(lam, n_modes, gamma)
            for j, row in enumerate(frows):
                alpha, y, err = cert_row(row, e, xi, ep)
                d1, d2 = roughness(y)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:3d}"
                    f" {bexp(abs(alpha), L):8.3f} {bexp(norm(y), L):7.3f}"
                    f" {bexp(err, L):7.3f} {bexp(d1, L):7.3f}"
                    f" {bexp(d2, L):7.3f} {'PASS' if abs(alpha) <= L**-17 else 'FAIL'}"
                )


if __name__ == "__main__":
    run()
