#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_112_operator_split_probe import lk_matrix, sigma_packet  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402


def run(tol=1e-10):
    print("E72.154 CPM kernel distance probe")
    print(" lam   L roots  rankM  nullDim  maxDistToKer  L*dist  minNonzeroSV  maxSV")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40), (18, 44)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        mask = (np.abs(d) <= 8.0).astype(float)
        lk = lk_matrix(d, k)
        op = bq.T @ (mask[:, None] * lk)
        u, svals, vh = svd(op, full_matrices=True)
        rank = int(np.sum(svals > tol))
        row_basis = vh[:rank, :]
        max_dist = 0.0
        for tau in roots[:6]:
            y = sigma_packet(L, d, tau)
            dist = norm(row_basis @ y) / max(norm(y), 1e-30)
            max_dist = max(max_dist, dist)
        min_sv = svals[rank - 1] if rank > 0 else 0.0
        print(
            f"{lam:4.0f} {L:5.2f} {len(roots):5d} {rank:6d} "
            f"{op.shape[1]-rank:7d} {max_dist:12.3e} {L*max_dist:8.3e} "
            f"{min_sv:12.3e} {svals[0]:6.3f}"
        )


if __name__ == "__main__":
    run()
