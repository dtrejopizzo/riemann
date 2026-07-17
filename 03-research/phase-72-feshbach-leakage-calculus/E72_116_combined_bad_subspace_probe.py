#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, qr, solve, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_112_operator_split_probe import (  # noqa: E402
    cumulative_center_matrix,
    lk_matrix,
    sigma_packet,
    weighted_even_matrix,
)


def orthonormal_columns(cols, tol=1e-12):
    if not cols:
        return np.zeros((0, 0), dtype=complex)
    mat = np.column_stack(cols)
    q, r = qr(mat)
    keep = np.abs(np.diag(r)) > tol
    return q[:, keep]


def run(qbad=3):
    print(f"E72.116 combined bad-subspace probe q={qbad}")
    print(
        " lam   N roots dimB  maxProjRatio  maxMassRatio  "
        "maxTopEnergy  tailBound"
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
        bad = orthonormal_columns(cols)
        dimb = bad.shape[1]

        max_proj_ratio = 0.0
        max_mass_ratio = 0.0
        max_top_energy = 0.0
        max_tail = 0.0
        sig_tail = svals[qbad] if qbad < len(svals) else 0.0
        for tau in roots[:6]:
            y = sigma_packet(L, d, tau)
            yn = norm(y)
            coeff_bad = np.conj(bad).T @ y if dimb else np.zeros(0)
            proj_ratio = norm(coeff_bad) / max(yn, 1e-30)
            mass = mrow @ y
            mass_ratio = abs(mass) / max(norm(mrow) * yn, 1e-30)
            coeff_svd = vh @ y
            top_energy = float(np.sum((svals[:qbad] * np.abs(coeff_svd[:qbad])) ** 2))
            tail_bound = (sig_tail * yn) ** 2
            max_proj_ratio = max(max_proj_ratio, proj_ratio)
            max_mass_ratio = max(max_mass_ratio, mass_ratio)
            max_top_energy = max(max_top_energy, top_energy)
            max_tail = max(max_tail, tail_bound)
        print(
            f"{lam:4.0f} {n_modes:3d} {len(roots):5d} {dimb:4d} "
            f"{max_proj_ratio:12.3e} {max_mass_ratio:13.3e} "
            f"{max_top_energy:12.3e} {max_tail:10.3e}"
        )


if __name__ == "__main__":
    run()
