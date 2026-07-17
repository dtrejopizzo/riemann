#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_112_operator_split_probe import lk_matrix, sigma_packet  # noqa: E402


def max_kernel_distance(L, d, row_basis, taus):
    out = 0.0
    for tau in taus:
        y = sigma_packet(L, d, tau)
        out = max(out, norm(row_basis @ y) / max(norm(y), 1e-30))
    return out


def run():
    print("E72.155 KERN-ORTH root-specificity probe")
    print(" lam   L  act# mod#  L*actDist  L*modelDist  L*gridDist  act/grid")
    for lam, n_modes in [(8, 24), (10, 28), (12, 32), (14, 36), (16, 40), (18, 44)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots_actual = finite_roots(xi, d, hmax=6.0)
        roots_model = finite_roots(k, d, hmax=6.0)
        if len(roots_actual) == 0:
            continue
        mask = (np.abs(d) <= 8.0).astype(float)
        op = bq.T @ (mask[:, None] * lk_matrix(d, k))
        _, svals, vh = svd(op, full_matrices=True)
        rank = int(np.sum(svals > 1e-10))
        row_basis = vh[:rank, :]
        grid = np.linspace(0.55, 5.95, min(6, max(3, len(roots_actual))))
        act = max_kernel_distance(L, d, row_basis, roots_actual[:6])
        mod = max_kernel_distance(L, d, row_basis, roots_model[:6]) if len(roots_model) else np.nan
        grd = max_kernel_distance(L, d, row_basis, grid)
        print(
            f"{lam:4.0f} {L:5.2f} {len(roots_actual):5d} {len(roots_model):4d} "
            f"{L*act:10.3e} {L*mod:12.3e} {L*grd:11.3e} {act/max(grd,1e-30):9.3e}"
        )


if __name__ == "__main__":
    run()
