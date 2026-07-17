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


def run():
    print("E72.114 SVD alignment probe")
    print(
        " lam   N roots    smax    stableRank  maxFlux  "
        "maxRatio  maxTop1Frac  maxTop3Frac"
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
        u, svals, vh = svd(rmat, full_matrices=False)
        smax = svals[0] if len(svals) else 0.0
        stable_rank = float(np.sum(svals * svals) / max(smax * smax, 1e-30))

        max_flux = 0.0
        max_ratio = 0.0
        max_top1 = 0.0
        max_top3 = 0.0
        for tau in roots[:6]:
            y = sigma_packet(L, d, tau)
            coeff = vh @ y
            contrib = (svals * np.abs(coeff)) ** 2
            total = float(np.sum(contrib))
            flux = np.sqrt(max(total, 0.0))
            denom = max(smax * norm(y), 1e-30)
            max_flux = max(max_flux, flux)
            max_ratio = max(max_ratio, flux / denom)
            if total > 1e-30:
                max_top1 = max(max_top1, float(contrib[0] / total))
                max_top3 = max(max_top3, float(np.sum(contrib[:3]) / total))
        print(
            f"{lam:4.0f} {n_modes:3d} {len(roots):5d} "
            f"{smax:8.2e} {stable_rank:11.3e} {max_flux:8.2e} "
            f"{max_ratio:8.2e} {max_top1:12.3e} {max_top3:12.3e}"
        )


if __name__ == "__main__":
    run()
