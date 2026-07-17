#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, qr, slogdet, solve, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_112_operator_split_probe import (  # noqa: E402
    cumulative_center_matrix,
    lk_matrix,
    sigma_packet,
    weighted_even_matrix,
)


def bad_columns(L, idx, d, k, bq, c_actual, qbad=3):
    mask = (np.abs(d) <= 8.0).astype(float)
    w = weighted_even_matrix(idx, mask)
    tcent = cumulative_center_matrix(w.shape[0])
    lk = lk_matrix(d, k)
    factor = 2.0 / (L * np.sqrt(np.exp(L)))
    qshort = bq @ solve(c_actual, bq.T)
    rmat = tcent @ w @ (mask[:, None] * qshort) @ (mask[:, None] * (factor * lk))
    _, svals, vh = svd(rmat, full_matrices=False)
    mrow = np.ones(w.shape[0], dtype=complex) @ w @ (mask[:, None] * qshort) @ (
        mask[:, None] * (factor * lk)
    )
    cols = []
    if norm(mrow) > 1e-14:
        cols.append(np.conj(mrow) / norm(mrow))
    for i in range(min(qbad, len(svals))):
        cols.append(np.conj(vh[i, :]))
    return np.column_stack(cols)


def projection_ratio_qr(cols, y):
    q, r = qr(cols)
    keep = np.abs(np.diag(r)) > 1e-12
    q = q[:, keep]
    return norm(np.conj(q).T @ y) / max(norm(y), 1e-30)


def projection_ratio_gram(cols, y):
    g = np.conj(cols).T @ cols
    gy = np.conj(cols).T @ y
    yn = np.vdot(y, y).real
    proj2 = np.vdot(gy, solve(g, gy)).real
    ratio2 = max(proj2 / max(yn, 1e-30), 0.0)
    return np.sqrt(ratio2)


def determinant_saturation(cols, y):
    g = np.conj(cols).T @ cols
    gy = np.conj(cols).T @ y
    yn = np.vdot(y, y)
    aug = np.block([[g, gy[:, None]], [np.conj(gy)[None, :], np.array([[yn]])]])
    sign_g, log_g = slogdet(g)
    sign_aug, log_aug = slogdet(aug)
    if sign_g == 0 or sign_aug == 0:
        return np.nan
    # dist^2/||y||^2 = det(aug)/(det(g)*||y||^2)
    sat = np.exp(log_aug - log_g - np.log(max(yn.real, 1e-300)))
    proj_ratio2 = max(1.0 - sat.real, 0.0)
    return sat.real, np.sqrt(proj_ratio2)


def run(qbad=3):
    print(f"E72.117 bad-subspace Gram determinant probe q={qbad}")
    print(" lam   N roots  maxQRproj  maxGramproj  maxDetProj  minSat")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        cols = bad_columns(L, idx, d, k, bq, c_actual, qbad=qbad)
        max_qr = 0.0
        max_gram = 0.0
        max_det = 0.0
        min_sat = 1.0
        for tau in roots[:6]:
            y = sigma_packet(L, d, tau)
            qr_ratio = projection_ratio_qr(cols, y)
            gram_ratio = projection_ratio_gram(cols, y)
            sat, det_ratio = determinant_saturation(cols, y)
            max_qr = max(max_qr, qr_ratio)
            max_gram = max(max_gram, gram_ratio)
            max_det = max(max_det, det_ratio)
            min_sat = min(min_sat, sat)
        print(
            f"{lam:4.0f} {n_modes:3d} {len(roots):5d} "
            f"{max_qr:10.3e} {max_gram:12.3e} {max_det:11.3e} {min_sat:8.5f}"
        )


if __name__ == "__main__":
    run()
