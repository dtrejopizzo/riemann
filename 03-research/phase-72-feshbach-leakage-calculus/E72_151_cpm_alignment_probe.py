#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_112_operator_split_probe import lk_matrix, sigma_packet  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402


def run():
    print("E72.151 cpm alignment probe")
    print(" lam   L roots  maxAlign  L*align  topEnergy  tail3Bound  max||cpm||")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40), (18, 44)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        mask = (np.abs(d) <= 8.0).astype(float)
        lk = lk_matrix(d, k)
        op = bq.T @ (mask[:, None] * lk)
        u, svals, vh = svd(op, full_matrices=False)
        factor = 2.0 / (L * np.sqrt(np.exp(L)))
        max_align = 0.0
        max_lalign = 0.0
        max_top = 0.0
        max_tail = 0.0
        max_cpm = 0.0
        for tau in roots[:6]:
            y = sigma_packet(L, d, tau)
            oy = op @ y
            align = norm(oy) / max(svals[0] * norm(y), 1e-30)
            coeffs = vh @ y
            top = norm(svals[:3] * coeffs[:3])
            tail = svals[3] * norm(y) if len(svals) > 3 else 0.0
            max_align = max(max_align, align)
            max_lalign = max(max_lalign, L * align)
            max_top = max(max_top, top / max(svals[0] * norm(y), 1e-30))
            max_tail = max(max_tail, tail / max(svals[0] * norm(y), 1e-30))
            max_cpm = max(max_cpm, factor * norm(oy))
        print(
            f"{lam:4.0f} {L:5.2f} {len(roots):5d} "
            f"{max_align:9.3e} {max_lalign:8.3e} "
            f"{max_top:9.3e} {max_tail:10.3e} {max_cpm:10.3e}"
        )


if __name__ == "__main__":
    run()
