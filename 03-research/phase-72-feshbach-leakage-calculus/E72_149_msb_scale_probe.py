#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_112_operator_split_probe import lk_matrix, sigma_packet, weighted_even_matrix  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402


def run():
    print("E72.149 MSB scale probe")
    print(
        " lam   L roots  ||b||  b/sqrtL  max||cpm||  cpm*sqrtL  "
        "cpm*L  product"
    )
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40), (18, 44)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        mask = (np.abs(d) <= 8.0).astype(float)
        w = weighted_even_matrix(idx, mask)
        mass_full = mask * (w.T @ np.ones(w.shape[0], dtype=complex))
        b = bq.T @ mass_full
        lk = lk_matrix(d, k)
        factor = 2.0 / (L * np.sqrt(np.exp(L)))
        max_cpm = 0.0
        for tau in roots[:6]:
            y = sigma_packet(L, d, tau)
            zpm = factor * (lk @ y)
            cpm = bq.T @ (mask * zpm)
            max_cpm = max(max_cpm, norm(cpm))
        bn = norm(b)
        print(
            f"{lam:4.0f} {L:5.2f} {len(roots):5d} "
            f"{bn:6.3f} {bn/np.sqrt(L):8.3f} "
            f"{max_cpm:10.3e} {max_cpm*np.sqrt(L):10.3e} "
            f"{max_cpm*L:7.3e} {bn*max_cpm:8.3e}"
        )


if __name__ == "__main__":
    run()
