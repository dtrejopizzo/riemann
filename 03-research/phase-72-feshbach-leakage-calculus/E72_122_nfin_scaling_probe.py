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
    print(f"E72.122 N-FIN scaling probe q={qbad}")
    print(
        " lam   L roots  max||Y||  Y/sqrtx  ||m||sqrtx  "
        "s1sqrtx  sq1sqrtx  maxM  maxS1  maxSq"
    )
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        mask = (np.abs(d) <= 8.0).astype(float)
        w = weighted_even_matrix(idx, mask)
        tcent = cumulative_center_matrix(w.shape[0])
        lk = lk_matrix(d, k)
        sqrtx = np.sqrt(np.exp(L))
        factor = 2.0 / (L * sqrtx)
        qshort = bq @ solve(c_actual, bq.T)
        rmat = tcent @ w @ (mask[:, None] * qshort) @ (mask[:, None] * (factor * lk))
        svals = svd(rmat, compute_uv=False)
        s1 = svals[0] if len(svals) else 0.0
        sq1 = svals[qbad] if qbad < len(svals) else 0.0
        mrow = np.ones(w.shape[0], dtype=complex) @ w @ (mask[:, None] * qshort) @ (
            mask[:, None] * (factor * lk)
        )
        mn = norm(mrow)
        max_y = 0.0
        max_m = 0.0
        max_s1 = 0.0
        max_sq1 = 0.0
        for tau in roots[:6]:
            yn = norm(sigma_packet(L, d, tau))
            max_y = max(max_y, yn)
            max_m = max(max_m, mn * yn)
            max_s1 = max(max_s1, s1 * yn)
            max_sq1 = max(max_sq1, sq1 * yn)
        print(
            f"{lam:4.0f} {L:5.2f} {len(roots):5d} "
            f"{max_y:9.2e} {max_y/sqrtx:8.2e} "
            f"{mn*sqrtx:10.2e} {s1*sqrtx:8.2e} {sq1*sqrtx:9.2e} "
            f"{max_m:6.2e} {max_s1:6.2e} {max_sq1:6.2e}"
        )


if __name__ == "__main__":
    run()
