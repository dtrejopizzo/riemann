#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_112_operator_split_probe import lk_matrix, sigma_packet  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402


def run():
    print("E72.153 CPM quadratic certificate probe")
    print(" lam   L roots  maxQ  L^2maxQ  max||MY||  max||Y||  ||M||")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40), (18, 44)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        mask = (np.abs(d) <= 8.0).astype(float)
        lk = lk_matrix(d, k)
        op = bq.T @ (mask[:, None] * lk)
        opn = svd(op, compute_uv=False)[0]
        max_q = 0.0
        max_my = 0.0
        max_y = 0.0
        for tau in roots[:6]:
            y = sigma_packet(L, d, tau)
            my = op @ y
            q = (norm(my) ** 2) / max((opn * norm(y)) ** 2, 1e-30)
            max_q = max(max_q, q)
            max_my = max(max_my, norm(my))
            max_y = max(max_y, norm(y))
        print(
            f"{lam:4.0f} {L:5.2f} {len(roots):5d} "
            f"{max_q:7.3e} {L*L*max_q:9.3e} {max_my:9.3e} "
            f"{max_y:9.3e} {opn:6.3f}"
        )


if __name__ == "__main__":
    run()
