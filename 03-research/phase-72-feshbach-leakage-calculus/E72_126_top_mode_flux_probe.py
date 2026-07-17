#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, solve, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_112_operator_split_probe import (  # noqa: E402
    cumulative_center_matrix,
    lk_matrix,
    sigma_packet,
    weighted_even_matrix,
)


def rmat_for(L, idx, d, k, bq, c_actual):
    mask = (np.abs(d) <= 8.0).astype(float)
    w = weighted_even_matrix(idx, mask)
    tcent = cumulative_center_matrix(w.shape[0])
    lk = lk_matrix(d, k)
    factor = 2.0 / (L * np.sqrt(np.exp(L)))
    qshort = bq @ solve(c_actual, bq.T)
    return tcent @ w @ (mask[:, None] * qshort) @ (mask[:, None] * (factor * lk))


def run(qbad=3):
    print(f"E72.126 top-mode flux probe q={qbad}")
    print(
        " lam   L roots  max|c_top|/sqrtx  max|s c|  max L|s c|  "
        "max s1sqrtxL  max tailFlux"
    )
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        sqrtx = np.sqrt(np.exp(L))
        rmat = rmat_for(L, idx, d, k, bq, c_actual)
        _, svals, vh = svd(rmat, full_matrices=False)
        max_ctop = 0.0
        max_sctop = 0.0
        max_lsctop = 0.0
        max_tail = 0.0
        for tau in roots[:6]:
            y = sigma_packet(L, d, tau)
            coeffs = vh @ y
            top_flux = svals[:qbad] * coeffs[:qbad]
            tail_flux = svals[qbad:] * coeffs[qbad:]
            max_ctop = max(max_ctop, norm(coeffs[:qbad]) / sqrtx)
            max_sctop = max(max_sctop, norm(top_flux))
            max_lsctop = max(max_lsctop, L * norm(top_flux))
            max_tail = max(max_tail, norm(tail_flux))
        print(
            f"{lam:4.0f} {L:5.2f} {len(roots):5d} "
            f"{max_ctop:16.3e} {max_sctop:10.3e} {max_lsctop:11.3e} "
            f"{svals[0]*sqrtx*L:13.3e} {max_tail:12.3e}"
        )


if __name__ == "__main__":
    run()
