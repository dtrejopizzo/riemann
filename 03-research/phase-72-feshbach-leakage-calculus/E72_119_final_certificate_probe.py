#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, solve, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_112_operator_split_probe import (  # noqa: E402
    cumulative_center_matrix,
    lk_matrix,
    sigma_packet,
    weighted_even_matrix,
)
from E72_117_bad_subspace_gram_probe import (  # noqa: E402
    bad_columns,
    determinant_saturation,
)
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402


def ccgd_value(d, bq, ce, s, hcut):
    a = bq.T @ (s / (s * s - d * d))
    y = solve(ce, a)
    g = bq @ y
    mask_tail = (np.abs(d) > hcut).astype(float)
    total = max(norm(g) ** 2, 1e-30)
    ccgd = float(np.sum(mask_tail * np.abs(g) ** 2) / total)
    graph = float(np.sum((d * d) * np.abs(g) ** 2) / total)
    return ccgd, graph


def bnorm_values(L, idx, d, k, bq, ce, roots, hcut, qbad):
    mask = (np.abs(d) <= hcut).astype(float)
    w = weighted_even_matrix(idx, mask)
    tcent = cumulative_center_matrix(w.shape[0])
    lk = lk_matrix(d, k)
    factor = 2.0 / (L * np.sqrt(np.exp(L)))
    qshort = bq @ solve(ce, bq.T)
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
    return max_m, max_s1, max_sq1


def min_gram_saturation(L, idx, d, k, bq, ce, roots, qbad):
    cols = bad_columns(L, idx, d, k, bq, ce, qbad=qbad)
    min_sat = 1.0
    max_proj = 0.0
    for tau in roots[:6]:
        y = sigma_packet(L, d, tau)
        sat, det_proj = determinant_saturation(cols, y)
        min_sat = min(min_sat, sat)
        max_proj = max(max_proj, det_proj)
    return min_sat, max_proj


def run(qbad=3, hcut=8.0, s=5 + 0.2j):
    print(f"E72.119 final finite certificate probe q={qbad}, H={hcut:g}, s={s.real:g}+{s.imag:g}i")
    print(
        " lam   N roots    CCGD     GraphN    MNorm     S1Norm    SqNorm   "
        "GBORTHsat  Bproj"
    )
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36)]:
        idx, L, d, xi, k, bq, ce, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        ccgd, graph = ccgd_value(d, bq, ce, s, hcut)
        graphn = graph / (1.0 + abs(s) ** 2)
        mn, s1n, sqn = bnorm_values(L, idx, d, k, bq, ce, roots, hcut, qbad)
        sat, bproj = min_gram_saturation(L, idx, d, k, bq, ce, roots, qbad)
        print(
            f"{lam:4.0f} {n_modes:3d} {len(roots):5d} "
            f"{ccgd:8.2e} {graphn:8.2e} {mn:9.2e} {s1n:9.2e} {sqn:9.2e} "
            f"{sat:10.5f} {bproj:7.2e}"
        )


if __name__ == "__main__":
    run()
