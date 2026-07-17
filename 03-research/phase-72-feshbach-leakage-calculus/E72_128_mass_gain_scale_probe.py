#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_112_operator_split_probe import (  # noqa: E402
    lk_matrix,
    sigma_packet,
    weighted_even_matrix,
)


def mass_row(L, idx, d, k, bq, c_actual):
    mask = (np.abs(d) <= 8.0).astype(float)
    w = weighted_even_matrix(idx, mask)
    lk = lk_matrix(d, k)
    factor = 2.0 / (L * np.sqrt(np.exp(L)))
    qshort = bq @ solve(c_actual, bq.T)
    return np.ones(w.shape[0], dtype=complex) @ w @ (mask[:, None] * qshort) @ (
        mask[:, None] * (factor * lk)
    )


def run():
    print("E72.128 mass gain scale probe")
    print(
        " lam   L roots  max|mass|   L*mass   L^2*mass  "
        "mass/(||m||||Y||)  ||m||sqrtxL"
    )
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        mrow = mass_row(L, idx, d, k, bq, c_actual)
        mnorm = norm(mrow)
        max_mass = 0.0
        max_ratio = 0.0
        for tau in roots[:6]:
            y = sigma_packet(L, d, tau)
            mass = abs(mrow @ y)
            max_mass = max(max_mass, mass)
            max_ratio = max(max_ratio, mass / max(mnorm * norm(y), 1e-30))
        scale = mnorm * np.sqrt(np.exp(L)) * L
        print(
            f"{lam:4.0f} {L:5.2f} {len(roots):5d} "
            f"{max_mass:10.3e} {L*max_mass:8.3e} {L*L*max_mass:10.3e} "
            f"{max_ratio:17.3e} {scale:12.3e}"
        )


if __name__ == "__main__":
    run()
