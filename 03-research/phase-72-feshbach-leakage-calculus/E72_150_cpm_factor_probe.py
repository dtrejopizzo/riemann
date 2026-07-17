#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_112_operator_split_probe import lk_matrix, sigma_packet  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402


def run():
    print("E72.150 cpm factor probe")
    print(
        " lam   L roots  max||Y||/(sqrtxL)  ||BPHLK||  "
        "factor*op*sqrtxL  max||cpm||"
    )
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40), (18, 44)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        x = np.exp(L)
        sqrtx = np.sqrt(x)
        mask = (np.abs(d) <= 8.0).astype(float)
        lk = lk_matrix(d, k)
        op = bq.T @ (mask[:, None] * lk)
        opn = svd(op, compute_uv=False)[0]
        factor = 2.0 / (L * sqrtx)
        max_y_scaled = 0.0
        max_cpm = 0.0
        for tau in roots[:6]:
            y = sigma_packet(L, d, tau)
            max_y_scaled = max(max_y_scaled, norm(y) / (sqrtx * L))
            max_cpm = max(max_cpm, norm(factor * (op @ y)))
        print(
            f"{lam:4.0f} {L:5.2f} {len(roots):5d} "
            f"{max_y_scaled:18.3e} {opn:10.3e} "
            f"{factor*opn*sqrtx*L:17.3e} {max_cpm:11.3e}"
        )


if __name__ == "__main__":
    run()
