#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, qr

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_112_operator_split_probe import sigma_packet  # noqa: E402
from E72_117_bad_subspace_gram_probe import bad_columns  # noqa: E402


def run(qbad=3):
    print(f"E72.123 S-FIN scale split probe q={qbad}")
    print(" lam   L roots  Y/(sqrtx L)  PB/sqrtx  L*PB/Y  maxProjRatio")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        sqrtx = np.sqrt(np.exp(L))
        cols = bad_columns(L, idx, d, k, bq, c_actual, qbad=qbad)
        q, r = qr(cols)
        keep = np.abs(np.diag(r)) > 1e-12
        q = q[:, keep]
        max_y_scaled = 0.0
        max_pb_scaled = 0.0
        max_lratio = 0.0
        max_ratio = 0.0
        for tau in roots[:6]:
            y = sigma_packet(L, d, tau)
            yn = norm(y)
            pb = norm(np.conj(q).T @ y)
            ratio = pb / max(yn, 1e-30)
            max_y_scaled = max(max_y_scaled, yn / (sqrtx * L))
            max_pb_scaled = max(max_pb_scaled, pb / sqrtx)
            max_lratio = max(max_lratio, L * ratio)
            max_ratio = max(max_ratio, ratio)
        print(
            f"{lam:4.0f} {L:5.2f} {len(roots):5d} "
            f"{max_y_scaled:12.3e} {max_pb_scaled:9.3e} "
            f"{max_lratio:8.3e} {max_ratio:12.3e}"
        )


if __name__ == "__main__":
    run()
