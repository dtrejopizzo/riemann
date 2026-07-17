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


def run(qbad=3):
    print(f"E72.118 BNORM scalar probe q={qbad}")
    print(" lam   N roots  max||m||||Y||  max s1||Y||  max sq1||Y||")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        mask = (np.abs(d) <= 8.0).astype(float)
        w = weighted_even_matrix(idx, mask)
        tcent = cumulative_center_matrix(w.shape[0])
        lk = lk_matrix(d, k)
        factor = 2.0 / (L * np.sqrt(np.exp(L)))
        qshort = bq @ solve(c_actual, bq.T)
        rmat = tcent @ w @ (mask[:, None] * qshort) @ (mask[:, None] * (factor * lk))
        svals = svd(rmat, compute_uv=False)
        s1 = svals[0] if len(svals) else 0.0
        sq1 = svals[qbad] if qbad < len(svals) else 0.0
        mrow = np.ones(w.shape[0], dtype=complex) @ w @ (mask[:, None] * qshort) @ (
            mask[:, None] * (factor * lk)
        )
        mn = norm(mrow)
        max_m = 0.0
        max_s1 = 0.0
        max_sq1 = 0.0
        for tau in roots[:6]:
            y = sigma_packet(L, d, tau)
            yn = norm(y)
            max_m = max(max_m, mn * yn)
            max_s1 = max(max_s1, s1 * yn)
            max_sq1 = max(max_sq1, sq1 * yn)
        print(
            f"{lam:4.0f} {n_modes:3d} {len(roots):5d} "
            f"{max_m:14.3e} {max_s1:12.3e} {max_sq1:13.3e}"
        )


if __name__ == "__main__":
    run()
