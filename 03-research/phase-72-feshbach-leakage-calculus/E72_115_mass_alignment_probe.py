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


def run():
    print("E72.115 mass alignment probe")
    print(" lam   N roots  max||Y||   ||m||    maxProd   max|mass|  maxRatio")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        mask = (np.abs(d) <= 8.0).astype(float)
        w = weighted_even_matrix(idx, mask)
        lk = lk_matrix(d, k)
        factor = 2.0 / (L * np.sqrt(np.exp(L)))
        qshort = bq @ solve(c_actual, bq.T)
        mrow = np.ones(w.shape[0], dtype=complex) @ w @ (mask[:, None] * qshort) @ (
            mask[:, None] * (factor * lk)
        )
        mnorm = norm(mrow)
        max_y = 0.0
        max_prod = 0.0
        max_mass = 0.0
        max_ratio = 0.0
        for tau in roots[:6]:
            y = sigma_packet(L, d, tau)
            mass = mrow @ y
            prod = mnorm * norm(y)
            max_y = max(max_y, norm(y))
            max_prod = max(max_prod, prod)
            max_mass = max(max_mass, abs(mass))
            max_ratio = max(max_ratio, abs(mass) / max(prod, 1e-30))
        print(
            f"{lam:4.0f} {n_modes:3d} {len(roots):5d} "
            f"{max_y:9.3e} {mnorm:8.2e} {max_prod:9.3e} "
            f"{max_mass:10.3e} {max_ratio:8.2e}"
        )


if __name__ == "__main__":
    run()
